import { SimpleChange } from '@angular/core';
import { of } from 'rxjs';

import { ActividadesTableComponent } from './actividades-table.component';
import { ActividadesService } from '../actividades.service';
import { ProyectosService } from '../proyectos.service';

describe('ActividadesTableComponent', () => {
  let component: ActividadesTableComponent;
  let actividadesService: jasmine.SpyObj<ActividadesService>;
  let proyectosService: jasmine.SpyObj<ProyectosService>;

  beforeEach(() => {
    actividadesService = jasmine.createSpyObj<ActividadesService>('ActividadesService', ['getActividades', 'eliminarActividad']);
    proyectosService = jasmine.createSpyObj<ProyectosService>('ProyectosService', ['getProyectos']);

    actividadesService.getActividades.and.returnValue(of([]));
    actividadesService.eliminarActividad.and.returnValue(of(void 0));
    proyectosService.getProyectos.and.returnValue(of([]));

    component = new ActividadesTableComponent(actividadesService, proyectosService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('debe filtrar actividades por proyecto seleccionado y nombre', () => {
    component.proyectos = [
      { id: 1, nombre: 'Proyecto Alfa' },
      { id: 2, nombre: 'Proyecto Beta' },
    ];
    component.actividades = [
      { id: 11, proyecto_id: 1, nombre: 'A1', bac: 100, avance_planificado: 10, avance_real: 10, ac: 10, evm: {} as any },
      { id: 12, proyecto_id: 2, nombre: 'B1', bac: 100, avance_planificado: 10, avance_real: 10, ac: 10, evm: {} as any },
    ] as any;
    component.proyectoId = 1;
    component.filtroProyecto = 'alfa';

    const emitSpy = spyOn(component.actividadesChange, 'emit');
    component.filtrar();

    expect(component.actividadesFiltradas.length).toBe(1);
    expect(component.actividadesFiltradas[0].id).toBe(11);
    expect(emitSpy).toHaveBeenCalledWith(component.actividadesFiltradas);
  });

  it('debe refiltrar cuando cambia proyectoId en ngOnChanges', () => {
    const filtrarSpy = spyOn(component, 'filtrar');

    component.ngOnChanges({
      proyectoId: new SimpleChange(1, 2, false)
    });

    expect(filtrarSpy).toHaveBeenCalled();
  });
});
