# Guía de usuario de DigitalForensicKit

Esta guía describe el uso de la herramienta DigitalForensicKit en escenarios prácticos de análisis forense digital.

## Requisitos previos

- Python 3.9 o superior
- Instalar dependencias con `pip install -r requirements.txt`
- Privilegios de administrador para análisis de memoria/disco

## Análisis de memoria

```sh
dfk-cli memory --analyze --input mi_volcado.raw --profile Win10x64 --case "CasoMalware2025"
```

## Análisis de disco

```sh
dfk-cli disk --inspect --input mi_imagen.dd --case "CasoDisco2025"
```

## Análisis de red

```sh
dfk-cli network --analyze --input mi_captura.pcap --case "CasoRed2025"
```

## Análisis de logs

```sh
dfk-cli logs --parse --input syslog.log apache.log --case "CasoLogs2025"
```

## Generación de informe

```sh
dfk-cli report --generate --case "CasoMalware2025" --author "Perito Forense"
```

## Notas de seguridad

- Trabaje siempre sobre copias de evidencia.
- Verifique la integridad de los archivos analizados.
- Consulte la documentación técnica (`docs/api_reference.md`) para detalles avanzados.

## Interfaz web

Inicie con:

```sh
python -m ui.web
```

Acceda a `http://localhost:5000` y siga el asistente.