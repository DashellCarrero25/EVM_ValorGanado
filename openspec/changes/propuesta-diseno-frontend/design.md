## Context

El frontend de la aplicación debe ser claro, accesible y visualmente coherente. Los usuarios necesitan identificar rápidamente el estado de sus proyectos y actividades, por lo que el contraste y la jerarquía visual son prioritarios. Se busca un diseño moderno, minimalista y funcional, adaptable a distintos dispositivos.

## Goals / Non-Goals

**Goals:**
- Definir una paleta de colores base y reglas de contraste para toda la interfaz.
- Garantizar accesibilidad visual (contraste AA/AAA, tipografía legible).
- Especificar estilos para headers, backgrounds, alertas y tipografía.
- Proveer ejemplos visuales y recomendaciones para componentes clave.

**Non-Goals:**
- No se abordarán temas de branding avanzado ni personalización por usuario en esta fase.
- No se implementarán dark/light modes automáticos inicialmente.

## Decisions

- Background principal: blanco (#FFFFFF) o gris claro (#F5F6FA) para máxima legibilidad.
- Headers: azul #3ECCF0 como color principal, permitiendo variantes más oscuras (#2CA3C7) para jerarquía.
- Tipografía: negra (#222) sobre fondos claros, blanca (#FFF) sobre headers o fondos oscuros, siempre asegurando contraste mínimo AA.
- Alertas: fondo rojo (#F44336), icono de alerta visible, texto blanco o negro según contraste óptimo.
- Uso de iconografía simple y colores de estado (verde para éxito, amarillo para advertencia, rojo para error).
- Botones y enlaces con suficiente contraste y feedback visual.

## Risks / Trade-offs

- [Riesgo] Falta de contraste en algunos dispositivos → Mitigación: pruebas de contraste y herramientas de accesibilidad.
- [Riesgo] Sobrecarga visual por exceso de color → Mitigación: priorizar fondos neutros y usar color solo para resaltar.

## Migration Plan

1. Definir variables de color y estilos globales en el proyecto Angular.
2. Aplicar lineamientos a componentes base (headers, tablas, alertas, botones).
3. Validar contraste y accesibilidad con herramientas automáticas y revisión manual.
4. Documentar ejemplos visuales y recomendaciones en Storybook o similar.

## Open Questions

- ¿Se requerirá soporte para dark mode en el futuro?
- ¿Qué nivel de personalización visual esperan los usuarios finales?