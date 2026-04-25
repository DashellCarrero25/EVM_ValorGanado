import { of, throwError } from 'rxjs';

import { ActividadesDashboardComponent } from './actividades-dashboard.component';
import { ProyectosService, ResumenProyectoEVM } from './proyectos.service';

describe('ActividadesDashboardComponent', () => {
  it('debe cargar el primer proyecto y su resumen al iniciar', () => {
    const resumenMock: ResumenProyectoEVM = {
      proyecto_id: 1,
      proyecto_nombre: 'Proyecto A',
      total_actividades: 2,
      indicadores: {
        pv: 100,
        ev: 90,
        ac: 80,
        cv: 10,
        sv: -10,
        cpi: 1.125,
        spi: 0.9,
        eac: 88.89,
        vac: 11.11,
        interpretacion: {
          cpi_estado: 'Bajo presupuesto (óptimo)',
          spi_estado: 'Atrasado (riesgo)'
        }
      }
    };

    const proyectosService = jasmine.createSpyObj<ProyectosService>('ProyectosService', ['getProyectos', 'getResumenEvm']);
    proyectosService.getProyectos.and.returnValue(of([{ id: 1, nombre: 'Proyecto A' }]));
    proyectosService.getResumenEvm.and.returnValue(of(resumenMock));

    const component = new ActividadesDashboardComponent(proyectosService);
    component.ngOnInit();

    expect(component.proyectoSeleccionadoId).toBe(1);
    expect(proyectosService.getResumenEvm).toHaveBeenCalledWith(1);
    expect(component.resumenProyecto?.proyecto_id).toBe(1);
    expect(component.resumenError).toBeNull();
  });

  it('debe manejar error al cargar resumen', () => {
    const proyectosService = jasmine.createSpyObj<ProyectosService>('ProyectosService', ['getProyectos', 'getResumenEvm']);
    proyectosService.getProyectos.and.returnValue(of([{ id: 2, nombre: 'Proyecto B' }]));
    proyectosService.getResumenEvm.and.returnValue(throwError(() => new Error('boom')));

    const component = new ActividadesDashboardComponent(proyectosService);
    component.ngOnInit();

    expect(component.resumenProyecto).toBeNull();
    expect(component.resumenError).toBe('Error al cargar el resumen EVM del proyecto');
  });
});
