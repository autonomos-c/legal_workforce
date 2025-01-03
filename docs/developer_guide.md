# Developer Guide

## Estructura del Proyecto

```
legal_agent/
├── src/               # Código fuente principal
├── tests/             # Pruebas unitarias
├── docs/              # Documentación
├── .github/           # Configuración de GitHub
├── .env               # Variables de entorno
├── requirements.txt   # Dependencias
└── mkdocs.yml         # Configuración de documentación
```

## Configuración del Entorno

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución de Pruebas

```bash
pytest --cov=src --cov-report=term-missing
```

## Contribución

1. Crear nueva rama:
```bash
git checkout -b feature/nueva-funcionalidad
```

2. Ejecutar linters:
```bash
black src tests
isort src tests
flake8 src tests
mypy src
```

3. Crear pull request siguiendo la plantilla
