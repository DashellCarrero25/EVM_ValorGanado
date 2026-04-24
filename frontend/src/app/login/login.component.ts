import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { HttpClient, HttpErrorResponse, HttpClientModule } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  loginForm: FormGroup;
  loading = false;
  error: string | null = null;

  constructor(private fb: FormBuilder, private http: HttpClient, private router: Router) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
  }

  submit(): void {
    this.error = null;
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched();
      return;
    }
    this.loading = true;
    this.http.post<any>('/api/login', this.loginForm.value, { observe: 'response' }).subscribe({
      next: (response) => {
        console.log('Login status:', response.status); // Mostrar 200 en éxito
        const res = response.body;
        localStorage.setItem('access_token', res.access_token);
        this.router.navigate(['/']);
      },
      error: (err: HttpErrorResponse) => {
        console.log('Login error status:', err.status); // Mostrar código de error
        if (err.status === 401) {
          this.error = 'Usuario o contraseña incorrectos';
        } else {
          this.error = 'Error inesperado. Intenta de nuevo.';
        }
        this.loading = false;
      },
      complete: () => {
        this.loading = false;
      }
    });
  }

  get correo() { return this.loginForm.get('email'); }
  get password() { return this.loginForm.get('password'); }
}
