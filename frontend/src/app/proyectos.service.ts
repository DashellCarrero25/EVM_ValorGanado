import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { IndicadoresEVM } from './actividades.service';

export interface Proyecto {
  id: number;
  nombre: string;
  descripcion?: string;
  fecha_inicio?: string;
  fecha_fin?: string;
  usuario_responsable_id?: number;
}

export interface ResumenProyectoEVM {
  proyecto_id: number;
  proyecto_nombre: string;
  total_actividades: number;
  indicadores: IndicadoresEVM;
}

@Injectable({
  providedIn: 'root'
})
export class ProyectosService {
  private apiUrl = '/api/proyectos';

  constructor(private http: HttpClient) {}

  getProyectos(): Observable<Proyecto[]> {
    return this.http.get<Proyecto[]>(this.apiUrl);
  }

  getResumenEvm(proyectoId: number): Observable<ResumenProyectoEVM> {
    return this.http.get<ResumenProyectoEVM>(`${this.apiUrl}/${proyectoId}/resumen-evm`);
  }
}
