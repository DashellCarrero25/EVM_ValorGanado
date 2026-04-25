import { Component, Input, OnChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChartConfiguration, ChartType } from 'chart.js';
import { NgChartsModule } from 'ng2-charts';
import { Actividad } from '../actividades.service';

@Component({
  selector: 'app-evm-chart',
  standalone: true,
  imports: [CommonModule, NgChartsModule],
  template: `
    <div class="evm-chart-title-bar">
      <h3 class="evm-chart-title">Gráfica comparativa PV, EV y AC</h3>
    </div>
    <div class="evm-chart-container">
      <canvas baseChart
        [data]="chartData"
        [options]="chartOptions"
        [type]="chartType">
      </canvas>
    </div>
  `,
  styleUrl: './evm-chart.component.scss'
})
export class EvmChartComponent implements OnChanges {
  @Input() actividades: Actividad[] = [];

  chartType: ChartType = 'bar';
  chartData: ChartConfiguration['data'] = { labels: [], datasets: [] };
  chartOptions: ChartConfiguration['options'] = {
    responsive: true,
    plugins: {
      legend: { display: true },
      title: { display: false }
    }
  };

  ngOnChanges(): void {
    this.updateChart();
  }

  updateChart() {
    if (!this.actividades?.length) {
      this.chartData = { labels: [], datasets: [] };
      return;
    }
    this.chartData = {
      labels: this.actividades.map(a => a.nombre),
      datasets: [
        {
          label: 'PV',
          data: this.actividades.map(a => a.evm.pv),
          backgroundColor: 'rgba(54, 162, 235, 0.7)'
        },
        {
          label: 'EV',
          data: this.actividades.map(a => a.evm.ev),
          backgroundColor: 'rgba(75, 192, 192, 0.7)'
        },
        {
          label: 'AC',
          data: this.actividades.map(a => a.evm.ac),
          backgroundColor: 'rgba(255, 99, 132, 0.7)'
        }
      ]
    };
  }
}
