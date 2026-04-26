import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EvmChartComponent } from './evm-chart.component';
import { By } from '@angular/platform-browser';

describe('EvmChartComponent', () => {
  let component: EvmChartComponent;
  let fixture: ComponentFixture<EvmChartComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EvmChartComponent]
    }).compileComponents();
    fixture = TestBed.createComponent(EvmChartComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should render chart with correct labels and data', () => {
    component.actividades = [
      {
        id: 1,
        proyecto_id: 1,
        nombre: 'Act 1',
        bac: 100,
        avance_planificado: 50,
        avance_real: 40,
        ac: 60,
        fecha_inicio: '2024-04-01',
        fecha_fin: '2024-04-10',
        evm: { pv: 50, ev: 40, ac: 60, cv: -20, sv: -10, cpi: 0.67, spi: 0.8, eac: 120, vac: -20, interpretacion: { cpi_estado: 'Bajo presupuesto', spi_estado: 'Atrasado' } }
      },
      {
        id: 2,
        proyecto_id: 1,
        nombre: 'Act 2',
        bac: 200,
        avance_planificado: 80,
        avance_real: 90,
        ac: 100,
        fecha_inicio: '2024-04-05',
        fecha_fin: '2024-04-20',
        evm: { pv: 160, ev: 180, ac: 100, cv: 80, sv: 20, cpi: 1.8, spi: 1.125, eac: 111, vac: 89, interpretacion: { cpi_estado: 'Sobre presupuesto', spi_estado: 'Adelantado' } }
      }
    ];
    component.ngOnChanges();
    fixture.detectChanges();
    expect(component.chartData.labels).toEqual(['Act 1', 'Act 2']);
    expect(component.chartData.datasets[0].data).toEqual([50, 160]); // PV
    expect(component.chartData.datasets[1].data).toEqual([40, 180]); // EV
    expect(component.chartData.datasets[2].data).toEqual([60, 100]); // AC
  });

  it('should show empty chart if no actividades', () => {
    component.actividades = [];
    component.ngOnChanges();
    fixture.detectChanges();
    expect(component.chartData.labels).toEqual([]);
    expect(component.chartData.datasets.length).toBe(0);
  });
});
