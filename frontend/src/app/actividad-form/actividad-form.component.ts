import { Component, Output, EventEmitter, OnInit, Input, SimpleChanges, OnChanges } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ActividadesService, ActividadCreate } from '../actividades.service';
import { ProyectosService, Proyecto } from '../proyectos.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSelectModule } from '@angular/material/select';

@Component({
  selector: 'app-actividad-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatButtonModule, MatProgressSpinnerModule, MatSelectModule],
  templateUrl: './actividad-form.component.html',
  styleUrl: './actividad-form.component.scss'
})
export class ActividadFormComponent implements OnInit, OnChanges {
  @Input() highlight = false;
  @Input() actividadEditar: any = null;
  @Output() edicionFinalizada = new EventEmitter<void>();
    ngOnChanges(changes: SimpleChanges): void {
      if (changes['actividadEditar'] && this.actividadEditar) {
        this.actividadForm.patchValue({
          ...this.actividadEditar,
          fecha_inicio: this.actividadEditar.fecha_inicio || '',
          fecha_fin: this.actividadEditar.fecha_fin || ''
        });
      }
    }
  @Output() actividadCreada = new EventEmitter<void>();

  actividadForm: FormGroup;
  loading = false;
  error: string | null = null;
  proyectos: Proyecto[] = [];

  constructor(
    private fb: FormBuilder,
    private actividadesService: ActividadesService,
    private proyectosService: ProyectosService
  ) {
    this.actividadForm = this.fb.group({
      proyecto_id: [null, Validators.required],
      nombre: ['', Validators.required],
      bac: [0, [Validators.required, Validators.min(0)]],
      avance_planificado: [0, [Validators.required, Validators.min(0), Validators.max(100)]],
      avance_real: [0, [Validators.required, Validators.min(0), Validators.max(100)]],
      ac: [0, [Validators.required, Validators.min(0)]],
      fecha_inicio: [''],
      fecha_fin: ['']
    });
  }

  ngOnInit(): void {
    this.proyectosService.getProyectos().subscribe({
      next: (proyectos) => this.proyectos = proyectos,
      error: () => this.proyectos = []
    });
  }

  limpiar(): void {
    this.actividadForm.reset();
  }

  submit(): void {
    this.error = null;
    if (this.actividadForm.invalid) {
      this.actividadForm.markAllAsTouched();
      return;
    }
    this.loading = true;
    const data = this.actividadForm.value;
    if (this.actividadEditar && this.actividadEditar.id) {
      // Modo edición
      this.actividadesService.actualizarActividad(this.actividadEditar.id, data).subscribe({
        next: () => {
          this.loading = false;
          this.actividadForm.reset();
          this.edicionFinalizada.emit();
        },
        error: () => {
          this.error = 'Error al actualizar actividad';
          this.loading = false;
        }
      });
    } else {
      // Modo creación
      this.actividadesService.crearActividad(data).subscribe({
        next: () => {
          this.loading = false;
          this.actividadForm.reset();
          this.actividadCreada.emit();
        },
        error: () => {
          this.error = 'Error al crear actividad';
          this.loading = false;
        }
      });
    }
  }
}
