# Arquitectura de DigitalForensicKit

![Diagrama de arquitectura](architecture.png)

## Componentes principales

- **core/**: Modelado de evidencia, cadena de custodia, generación de informes.
- **modules/**: Módulos de análisis (memoria, disco, red, logs).
- **ui/**: CLI y web.
- **utils/**: Utilidades y funciones auxiliares.

## Flujo de análisis típico

1. **Ingesta de evidencia**: El usuario carga archivos (memoria, disco, logs, pcap).
2. **Análisis modular**: Cada módulo procesa su evidencia y extrae hallazgos.
3. **Correlación y reporte**: Los resultados se integran en un informe profesional.
4. **Exportación y custodia**: Se exportan IOCs, gráficos y reporte con hashes/timestamps.

## Extensibilidad

- Módulos y plugins pueden añadirse en `modules/`.
- Soporte para formatos y análisis personalizados.

---