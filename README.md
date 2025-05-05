# DigitalForensicKit

**DigitalForensicKit** es una herramienta modular y extensible de análisis forense digital dirigida a investigadores y profesionales de la seguridad informática. Permite examinar y correlacionar evidencias digitales de memoria, discos, registros y tráfico de red bajo un enfoque profesional orientado a la generación de informes válidos en contextos empresariales y legales.

---

## Características principales

- **Análisis de memoria RAM**: Detección de procesos, IOCs, malware y conexiones activas (basado en Volatility3).
- **Inspección forense de discos**: Soporte para NTFS, FAT, ext, HFS+, recuperación de archivos, análisis de metadatos y artefactos.
- **Análisis de red**: Procesamiento de PCAP, reconstrucción de sesiones, extracción de archivos y detección de conexiones maliciosas.
- **Análisis de logs**: Parsing, correlación y visualización de eventos de logs heterogéneos.
- **Generación de informes**: Exportación multi-formato (PDF, HTML, JSON), integración de evidencias, gráficos y IOCs.
- **Integridad y cadena de custodia**: Hashes, timestamping y registro detallado de acciones.
- **Extensible y seguro**: Arquitectura modular y defensiva, fácil de ampliar y auditar.

---

## Estructura del proyecto

```
DigitalForensicKit/
├── core/              # Componentes centrales del sistema
├── modules/           # Módulos de análisis específicos
├── ui/                # Interfaces de usuario (CLI y web)
├── utils/             # Utilidades y funciones auxiliares
├── tests/             # Tests unitarios y de integración
├── docs/              # Documentación completa
├── examples/          # Ejemplos prácticos y notebooks
├── requirements.txt   # Dependencias
├── setup.py           # Instalador del paquete
├── LICENSE            # Licencia GNU GPL v3
└── README.md          # Este archivo
```

---

## Instalación

### Requisitos

- Python 3.9+
- Dependencias listadas en `requirements.txt`
- Para ciertas funcionalidades: Volatility3, Sleuthkit, pytsk, pyshark, scapy
- Compatible con Linux, Windows y macOS

### Instalar dependencias

```sh
pip install -r requirements.txt
```

### Instalación como paquete

```sh
python setup.py install
```

---

## Uso rápido (CLI)

```sh
dfk-cli --help
```

Ejemplo de análisis de memoria:

```sh
dfk-cli memory analyze --input examples/memdump.raw --profile Win10x64
```

Ejemplo de generación de informe:

```sh
dfk-cli report generate --case "Malware Investigation" --output /tmp/informe.pdf
```

---

## Documentación

- [Guía de usuario](docs/user_guide.md)
- [Documentación técnica de la API](docs/api_reference.md)
- [Ejemplos y casos prácticos](examples/)
- [Diagrama de arquitectura](docs/architecture.md)

---

## Contribución y soporte

Las contribuciones son bienvenidas. Por favor revisa [CONTRIBUTING.md](docs/CONTRIBUTING.md) y abre issues o pull requests para mejoras o reportes de bugs.

---

## Licencia

Proyecto distribuido bajo GNU General Public License v3.0 (ver LICENSE).