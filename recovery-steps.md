# Pasos para Recuperar el Sistema

## 1. Configurar Secrets en GitHub

Antes de recrear el codespace, configurar los siguientes secrets en GitHub:

1. GROQ_API_KEY: Para la integración con Groq
2. BRAVE_API_KEY: Para el servidor MCP de búsqueda
3. CODECOV_TOKEN: Para reportes de cobertura

Para configurar los secrets:
1. Ir a Settings del repositorio
2. Seleccionar Secrets and variables > Actions
3. Agregar cada secret con New repository secret

## 2. Recrear el Codespace

1. Eliminar el codespace actual:
   - En GitHub: Settings > Codespaces > Eliminar el codespace actual
   - O en VSCode: Remote Explorer > Click derecho > Delete

2. Crear nuevo codespace:
   - En GitHub: Code > Codespaces > Create codespace
   - Seleccionar:
     * Branch: main
     * Region: La más cercana
     * Machine type: 4-core, 8GB RAM

## 3. Verificar la Configuración

El sistema usa:
- Python 3.11 con venv
- Node.js 18.x
- MCP servers configurados
- Extensiones de VSCode necesarias

La configuración está en:
- .devcontainer/devcontainer.json
- .devcontainer/Dockerfile

## 4. Post-Configuración

El sistema automáticamente:
1. Creará el entorno virtual
2. Instalará dependencias
3. Configurará los MCP servers
4. Instalará extensiones

## Solución de Problemas

Si hay problemas:
1. Verificar que los secrets están configurados
2. Confirmar que el devcontainer.json y Dockerfile están presentes
3. Revisar los logs del contenedor
4. Asegurarse que las extensiones están instaladas

## Estructura del Proyecto

```
/workspace/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── src/
│   └── groq_integration.py
├── tests/
└── requirements.txt
```

## Notas Importantes

- Los secrets son cruciales para el funcionamiento
- El sistema requiere 4 CPUs y 8GB RAM mínimo
- La configuración del devcontainer maneja la mayoría de la setup
- Los MCP servers se configuran automáticamente
