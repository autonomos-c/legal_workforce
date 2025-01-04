# Configuración de GitHub Codespace

## Eliminar Codespace Actual

1. En VSCode, ir a Remote Explorer
2. Click derecho en el Codespace actual
3. Seleccionar "Delete"

## Crear Nuevo Codespace

1. Click en "New codespace"
2. Seleccionar:
   - Repository: autonomos-c/c_assistant
   - Branch: main
   - Region: Elegir la más cercana
   - Machine type: 4-core, 8GB RAM
   - Configuración: Usar devcontainer.json

## Verificar Recursos

Una vez creado, verificar:
- 4 CPUs disponibles
- 8GB RAM
- 32GB almacenamiento
- Extensiones instaladas automáticamente
- MCP servers configurados

## Notas
- El nuevo Codespace usará la configuración del devcontainer que acabamos de commitear
- Se instalarán automáticamente todas las dependencias
- Las extensiones de VSCode se configurarán según lo especificado
