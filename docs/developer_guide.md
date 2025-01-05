# Developer Guide

## Estructura del Proyecto

```
legal_agent/
├── src/               # Código fuente principal
├── tests/             # Pruebas unitarias
├── docs/              # Documentación
└── mkdocs.yml         # Configuración de documentación
```

## Configuración del Entorno

### Desarrollo Local (Recomendado)

Ver [Guía de Configuración Local](local_setup.md) para instrucciones detalladas sobre:
- Configuración inicial
- Instalación de dependencias
- Configuración de VSCode y MCP
- Flujo de trabajo con Git
- Mantenimiento del entorno

### Usando GitHub Codespaces (Alternativo)

Para desarrollo en la nube, ver [Configuración de Codespaces](codespace_setup.md).

Nota: El desarrollo local es recomendado por:
- Mejor rendimiento
- Control total del entorno
- Sin limitaciones de recursos
- Desarrollo más fluido

## Desarrollo

### MCP Servers

Los MCP servers proporcionan funcionalidades adicionales:
- memory: Mantiene el historial y estado
- brave-search: Búsqueda web (requiere BRAVE_API_KEY)

### Pruebas

Ejecutar pruebas localmente:
```bash
pytest --cov=src --cov-report=term-missing
```

### Linting y Formateo

Herramientas de desarrollo:
- black: Formateo de Python
- isort: Organización de imports
- flake8: Linting
- mypy: Verificación de tipos

## Contribución

1. Crear nueva rama:
```bash
git checkout -b feature/nueva-funcionalidad
```

2. Desarrollar:
   - Instalar dependencias con pip
   - Ejecutar pruebas localmente
   - Seguir guías de estilo de código

3. Crear pull request:
   - Describir cambios claramente
   - Asegurar que las pruebas pasen
   - Mantener el código limpio y documentado
