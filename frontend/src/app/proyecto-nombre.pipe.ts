import { Pipe, PipeTransform } from '@angular/core';
import { Proyecto } from './proyectos.service';

@Pipe({
  name: 'proyectoNombre',
  standalone: true
})
export class ProyectoNombrePipe implements PipeTransform {
  transform(proyectoId: number, proyectos: Proyecto[]): string {
    const proyecto = proyectos.find(p => p.id === proyectoId);
    return proyecto ? proyecto.nombre : '';
  }
}
