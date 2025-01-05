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

### Usando GitHub Codespaces (Recomendado)

1. Configurar Secrets:
   - En GitHub: Settings > Secrets and variables > Codespaces
   - Agregar GROQ_API_KEY y BRAVE_API_KEY
   - Ver docs/codespace_setup.md para más detalles

2. Crear Codespace:
   - Ir al repositorio en GitHub
   - Click en "Code" > "Open with Codespaces"
   - Seleccionar configuración (4 cores)

3. El sistema usará:
   - Secrets como variables de entorno
   - pip para gestión de dependencias
   - Extensiones de VSCode necesarias

### Usando VSCode Local

1. Configurar entorno:
   - Copiar .env.example a .env
   - Agregar API keys al .env
   - Instalar Python 3.11+

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

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
