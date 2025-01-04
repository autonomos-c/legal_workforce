# Configuración de MCP Servers

## Configuración Inicial

1. Clonar el repositorio
2. Ejecutar el script de instalación:
```bash
./setup-mcp.sh
```

## Configuración de Secrets

### Usando GitHub Actions (Recomendado)

1. En VSCode, ir a la pestaña GitHub Actions
2. Seleccionar "MCP Setup"
3. Hacer clic en "Run workflow"
4. Ingresar los secrets requeridos:
   - Brave Search API Key
   - (Otros secrets según se necesiten)

Los secrets se manejarán de forma segura a través de GitHub Actions y se configurarán automáticamente en el sistema.

## Estructura del Proyecto

```
/home/cdm/Documents/Cline/MCP/
├── venv/                    # Entorno virtual de Python
├── node_modules/           # Módulos de Node.js
└── .env                    # Variables de entorno (generado por GitHub Actions)
```

## Verificación

1. Verificar que los MCP servers están configurados:
   - memory: Sistema de memoria persistente
   - brave-search: Búsqueda web con API key configurada
   - git: Integración con git
   - fetch: Obtención de recursos web

2. Probar funcionalidad:
   - Realizar una búsqueda con brave-search
   - Verificar que el sistema de memoria funciona
   - Comprobar integración con git

## Solución de Problemas

1. Si los secrets no se configuran:
   - Verificar que el workflow de GitHub Actions se ejecutó correctamente
   - Revisar los logs del workflow
   - Asegurar que los secrets fueron ingresados correctamente

2. Si hay problemas de permisos:
   - Verificar permisos de los directorios
   - Asegurar que los scripts son ejecutables

## Mantenimiento

1. Actualización de secrets:
   - Ejecutar el workflow "MCP Setup" nuevamente
   - Ingresar los nuevos valores de los secrets

2. Actualización de dependencias:
```bash
pip install --upgrade mcp-server-git mcp-server-fetch
npm update @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
```

## Seguridad

- Los secrets se manejan de forma segura a través de GitHub Actions
- No se almacenan en archivos de texto plano
- Se pueden actualizar fácilmente cuando sea necesario
