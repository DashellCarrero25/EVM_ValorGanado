
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


export interface IndicadoresEVM {
  pv: number;
  ev: number;
  ac: number;
  cv: number;
  sv: number;
  cpi: number;
  spi: number;
  eac: number;
  vac: number;
  interpretacion: {
    cpi_estado: string;
    spi_estado: string;
  };
}

export interface Actividad {
  id: number;
  proyecto_id: number;
  nombre: string;
  bac: number;
  avance_planificado: number;
  avance_real: number;
  ac: number;
  fecha_inicio?: string | null;
  fecha_fin?: string | null;
  evm: IndicadoresEVM;
}

export interface ActividadCreate {
  proyecto_id: number;
  nombre: string;
  bac: number;
  avance_planificado: number;
  avance_real: number;
  ac: number;
  fecha_inicio?: string | null;
  fecha_fin?: string | null;
}

export interface ActividadUpdate {
  nombre?: string;
  bac?: number;
  avance_planificado?: number;
  avance_real?: number;
  ac?: number;
  fecha_inicio?: string | null;
  fecha_fin?: string | null;
}

@Injectable({
  providedIn: 'root'
})
export class ActividadesService {
  private apiUrl = '/api/actividades';

  constructor(private http: HttpClient) { }

  getActividades(): Observable<Actividad[]> {
    return this.http.get<Actividad[]>(this.apiUrl);
  }

  getActividad(id: number): Observable<Actividad> {
    return this.http.get<Actividad>(`${this.apiUrl}/${id}`);
  }

  crearActividad(data: ActividadCreate): Observable<Actividad> {
    return this.http.post<Actividad>(this.apiUrl, data);
  }

  actualizarActividad(id: number, data: ActividadUpdate): Observable<Actividad> {
    return this.http.put<Actividad>(`${this.apiUrl}/${id}`, data);
  }

  eliminarActividad(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
