import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActividadesTableComponent } from './actividades-table/actividades-table.component';
import { ActividadFormComponent } from './actividad-form/actividad-form.component';
import { MatCardModule } from '@angular/material/card';
import { EvmChartComponent } from './evm-chart/evm-chart.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { ProyectosService, Proyecto, ResumenProyectoEVM } from './proyectos.service';

@Component({
  selector: 'app-actividades-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    ActividadesTableComponent,
    ActividadFormComponent,
    MatCardModule,
    EvmChartComponent,
    MatFormFieldModule,
    MatSelectModule,
    MatProgressSpinnerModule,
  ],
  templateUrl: './actividades-dashboard.component.html',
  styleUrl: './actividades-dashboard.component.scss'
})
export class ActividadesDashboardComponent implements OnInit {
  actividadEditar: any = null;
  highlightForm = false;
  proyectos: Proyecto[] = [];
  proyectoSeleccionadoId: number | null = null;
  resumenProyecto: ResumenProyectoEVM | null = null;
  resumenLoading = false;
  resumenError: string | null = null;
    onEditarActividad(actividad: any) {
      this.actividadEditar = actividad;
      this.highlightForm = true;
      setTimeout(() => {
        const formEl = document.querySelector('.actividad-form');
        if (formEl) {
          formEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        setTimeout(() => {
          this.highlightForm = false;
        }, 1200);
      }, 100);
    }

    onEdicionFinalizada() {
      this.actividadEditar = null;
      this.tabla?.cargarActividades();
    }
  @ViewChild(ActividadesTableComponent) tabla?: ActividadesTableComponent;
  actividades: any[] = [];

  constructor(private readonly proyectosService: ProyectosService) {}

  ngOnInit(): void {
    this.proyectosService.getProyectos().subscribe({
      next: (proyectos) => {
        this.proyectos = proyectos;
        if (proyectos.length > 0) {
          this.proyectoSeleccionadoId = proyectos[0].id;
          this.cargarResumenProyecto();
        }
      },
      error: () => {
        this.proyectos = [];
        this.resumenError = 'Error al cargar proyectos';
      }
    });
  }

  onActividadCreada() {
    this.tabla?.cargarActividades();
    this.cargarResumenProyecto();
  }

  // Recibe las actividades desde la tabla
  onActividadesChange(actividades: any[]) {
    this.actividades = actividades;
  }

  onProyectoSeleccionado(): void {
    this.cargarResumenProyecto();
  }

  cargarResumenProyecto(): void {
    if (this.proyectoSeleccionadoId == null) {
      this.resumenProyecto = null;
      this.resumenError = null;
      return;
    }

    this.resumenLoading = true;
    this.resumenError = null;
    this.proyectosService.getResumenEvm(this.proyectoSeleccionadoId).subscribe({
      next: (resumen) => {
        this.resumenProyecto = resumen;
        this.resumenLoading = false;
      },
      error: () => {
        this.resumenProyecto = null;
        this.resumenLoading = false;
        this.resumenError = 'Error al cargar el resumen EVM del proyecto';
      }
    });
  }
}
