import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { LoginComponent } from './login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { Router } from '@angular/router';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;
  let httpMock: HttpTestingController;
  let routerSpy: jasmine.SpyObj<Router>;

  beforeEach(waitForAsync(() => {
    routerSpy = jasmine.createSpyObj('Router', ['navigate']);
    TestBed.configureTestingModule({
      declarations: [LoginComponent],
      imports: [ReactiveFormsModule, HttpClientTestingModule],
      providers: [
        { provide: Router, useValue: routerSpy }
      ]
    }).compileComponents();
  }));


  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    httpMock = TestBed.inject(HttpTestingController);
    localStorage.clear();
    fixture.detectChanges();
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show validation errors if form is invalid', () => {
    component.loginForm.setValue({ correo: '', password: '' });
    component.submit();
    fixture.detectChanges();
    expect(component.loginForm.invalid).toBeTrue();
  });

  it('should call backend and navigate on successful login', () => {
    // Asegura que el formulario sea válido
    component.loginForm.get('correo')?.setValue('test@example.com');
    component.loginForm.get('password')?.setValue('testpass123');
    expect(component.loginForm.valid).toBeTrue();
    component.submit();
    fixture.detectChanges();
    const req = httpMock.expectOne('/api/login');
    expect(req.request.method).toBe('POST');
    req.flush({ access_token: 'token', usuario: { id: 1, correo: 'test@example.com', nombre: 'Test' } });
    expect(localStorage.getItem('access_token')).toBe('token');
    expect(routerSpy.navigate).toHaveBeenCalledWith(['/']);
  });

  it('should show error on 401 response', () => {
    component.loginForm.get('correo')?.setValue('fail@example.com');
    component.loginForm.get('password')?.setValue('wrongpass');
    expect(component.loginForm.valid).toBeTrue();
    component.submit();
    fixture.detectChanges();
    const req = httpMock.expectOne('/api/login');
    req.flush({ detail: 'Usuario o contraseña incorrectos' }, { status: 401, statusText: 'Unauthorized' });
    expect(component.error).toBe('Usuario o contraseña incorrectos');
  });

  it('should show generic error on other errors', () => {
    component.loginForm.get('correo')?.setValue('fail@example.com');
    component.loginForm.get('password')?.setValue('wrongpass');
    expect(component.loginForm.valid).toBeTrue();
    component.submit();
    fixture.detectChanges();
    const req = httpMock.expectOne('/api/login');
    req.flush(null, { status: 500, statusText: 'Server Error' });
    expect(component.error).toBe('Error inesperado. Intenta de nuevo.');
  });
});
