# Developer Guide

## Estructura del Proyecto

```
legal_agent/
├── .devcontainer/     # Configuración de desarrollo
├── src/               # Código fuente principal
├── tests/             # Pruebas unitarias
├── docs/              # Documentación
├── .github/           # Configuración de GitHub Actions
└── mkdocs.yml         # Configuración de documentación
```

## Configuración del Entorno

### Usando GitHub Codespaces (Recomendado)

1. Abrir en Codespaces:
   - Ir al repositorio en GitHub
   - Click en "Code" > "Open with Codespaces"
   - Seleccionar configuración (4 cores, 16GB RAM)

2. Todo se configura automáticamente:
   - Dependencias de Python
   - Herramientas de desarrollo
   - MCP servers
   - Extensiones de VSCode

### Usando VSCode Local

1. Abrir en VSCode:
   - VSCode detectará el devcontainer
   - Click en "Reopen in Container"

2. El contenedor se construirá automáticamente con:
   - Python 3.11
   - Todas las dependencias
   - Herramientas de desarrollo

## Desarrollo

### MCP Servers

Los MCP servers mantienen el contexto del desarrollo:
- memory: Mantiene el historial y estado del proyecto
- git: Integración con el repositorio
- brave-search: Búsqueda de documentación
- fetch: Obtención de recursos

### Pruebas

Las pruebas se ejecutan automáticamente en GitHub Actions:
```bash
pytest --cov=src --cov-report=term-missing
```

### Linting y Formateo

El código se formatea automáticamente al guardar:
- black: Formateo de Python
- isort: Organización de imports
- flake8: Linting
- mypy: Verificación de tipos

## CI/CD

GitHub Actions ejecuta automáticamente:
1. Pruebas unitarias
2. Cobertura de código
3. Linting y verificación de tipos
4. Construcción de documentación

## Contribución

1. Crear nueva rama:
```bash
git checkout -b feature/nueva-funcionalidad
```

2. Desarrollar con devcontainer:
   - El entorno está configurado automáticamente
   - Los linters se ejecutan al guardar
   - Las pruebas se pueden ejecutar localmente

3. Crear pull request:
   - GitHub Actions verificará todo automáticamente
   - La cobertura de código se reporta en Codecov
   - Los cambios deben pasar todas las verificaciones
