import { Component, OnChanges, OnInit, Output, EventEmitter, Input, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActividadesService, Actividad } from '../actividades.service';
import { ProyectosService, Proyecto } from '../proyectos.service';
import { ProyectoNombrePipe } from '../proyecto-nombre.pipe';
import { MatTableModule } from '@angular/material/table';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-actividades-table',
  standalone: true,
  imports: [CommonModule, MatTableModule, MatProgressSpinnerModule, MatCardModule, MatFormFieldModule, MatInputModule, FormsModule, ProyectoNombrePipe, MatIconModule, MatButtonModule],
  templateUrl: './actividades-table.component.html',
  styleUrl: './actividades-table.component.scss'
})
export class ActividadesTableComponent implements OnInit, OnChanges {
  @Input() proyectoId: number | null = null;
  @Output() editar = new EventEmitter<Actividad>();
  @Output() actividadesChange = new EventEmitter<Actividad[]>();

  actividadPendienteEliminar: Actividad | null = null;

  editarActividad(actividad: Actividad): void {
    this.editar.emit(actividad);
  }

  solicitarEliminarActividad(actividad: Actividad): void {
    this.actividadPendienteEliminar = actividad;
    this.error = null;
  }

  cancelarEliminacion(): void {
    this.actividadPendienteEliminar = null;
  }

  confirmarEliminacion(): void {
    if (!this.actividadPendienteEliminar) {
      return;
    }

    this.actividadesService.eliminarActividad(this.actividadPendienteEliminar.id).subscribe({
      next: () => {
        this.actividadPendienteEliminar = null;
        this.cargarActividades();
      },
      error: () => {
        this.error = 'Error al eliminar la actividad';
      }
    });
  }
  actividades: Actividad[] = [];
  actividadesFiltradas: Actividad[] = [];
  proyectos: Proyecto[] = [];
  loading = false;
  error: string | null = null;
  filtroProyecto = '';

  constructor(
    private readonly actividadesService: ActividadesService,
    private readonly proyectosService: ProyectosService
  ) {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['proyectoId'] && !changes['proyectoId'].firstChange) {
      this.filtrar();
    }
  }

  ngOnInit(): void {
    this.cargarProyectos();
    this.cargarActividades();
  }

  cargarProyectos(): void {
    this.proyectosService.getProyectos().subscribe({
      next: (proyectos) => {
        this.proyectos = proyectos;
        this.filtrar();
      },
      error: () => this.proyectos = []
    });
  }

  cargarActividades(): void {
    this.loading = true;
    this.error = null;
    this.actividadesService.getActividades().subscribe({
      next: (data) => {
        this.actividades = data;
        this.filtrar();
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Error al cargar actividades';
        this.loading = false;
      }
    });
  }

  filtrar(): void {
    const filtro = this.filtroProyecto.trim().toLowerCase();
    this.actividadesFiltradas = this.actividades.filter(act => {
      const coincideProyectoSeleccionado = this.proyectoId == null || act.proyecto_id === this.proyectoId;
      const nombreProyecto = this.proyectos.find(p => p.id === act.proyecto_id)?.nombre?.toLowerCase() || '';
      const coincideFiltro = !filtro || nombreProyecto.includes(filtro);
      return coincideProyectoSeleccionado && coincideFiltro;
    });
    this.actividadesChange.emit(this.actividadesFiltradas);
  }
}
