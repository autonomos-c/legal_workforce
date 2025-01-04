# Configuración del Entorno de Desarrollo con DevContainer

## Requisitos Previos

1. VSCode instalado
2. Extensión "Remote - Containers" en VSCode
3. Docker Desktop instalado y corriendo
4. GitHub Codespaces habilitado en tu cuenta

## Inicio Rápido

1. Clonar el repositorio
2. Abrir en VSCode
3. Cuando aparezca la notificación "Reopen in Container", hacer clic en "Reopen"
4. O usar Command Palette (Ctrl+Shift+P): "Remote-Containers: Reopen in Container"

## Recursos Asignados

- CPUs: 4 cores
- Memoria: 8GB
- Almacenamiento: 32GB

## Características Incluidas

### Lenguajes y Runtimes
- Python 3.11 con venv
- Node.js 18.x
- npm actualizado

### Herramientas de Desarrollo
- Git
- GitHub CLI
- VSCode Extensions:
  - Python
  - Pylance
  - GitHub Actions
  - Claude Dev
  - Black Formatter
  - isort

### MCP Servers Configurados
- filesystem: Acceso a archivos
- memory: Sistema de memoria persistente
- brave-search: Búsqueda web
- fetch: Obtención de recursos
- git: Integración con git

## Estructura de Directorios

```
/workspace/                  # Directorio raíz del proyecto
├── venv/                   # Entorno virtual de Python
└── Documents/Cline/MCP/    # Directorio MCP
```

## Variables de Entorno

- MCP_DIR: /workspace/Documents/Cline/MCP
- PROJECT_DIR: /workspace
- BRAVE_API_KEY: Configurado a través de GitHub Actions

## Formateo de Código

- Black para Python (automático al guardar)
- isort para organizar imports
- Configuración consistente para todo el equipo

## Solución de Problemas

1. Si el contenedor no inicia:
   - Verificar que Docker está corriendo
   - Revisar los logs de Docker
   - Verificar recursos disponibles

2. Si los MCP servers no funcionan:
   - Verificar que las extensiones están instaladas
   - Comprobar que las dependencias se instalaron
   - Revisar los logs de VSCode

3. Si hay problemas de permisos:
   - El contenedor usa el usuario 'vscode'
   - Los directorios principales están configurados con permisos correctos

## Mejores Prácticas

1. Siempre usar el contenedor para desarrollo
2. Mantener actualizado el Dockerfile y devcontainer.json
3. Documentar cambios en las dependencias
4. Usar GitHub Actions para secrets y configuración sensible

## Mantenimiento

1. Actualizar imagen:
   - Command Palette: "Remote-Containers: Rebuild Container"

2. Actualizar dependencias:
   - Modificar Dockerfile o requirements.txt
   - Reconstruir el contenedor

3. Backup:
   - Todo el código se guarda en el repositorio
   - La configuración está versionada
   - Los secrets se manejan via GitHub Actions
