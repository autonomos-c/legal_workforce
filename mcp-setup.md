# Configuración de MCP Servers

## Requisitos Previos

1. VSCode instalado
2. Extensión Claude instalada
3. Node.js y npm instalados (para los servidores npm)
4. Python 3.x y pip instalados (para los servidores Python)

## Configuración a través de VSCode

### 1. Configuración de MCP Servers

1. Abrir VSCode Settings (Ctrl+,)
2. Buscar "Claude MCP"
3. Configurar los servidores a través de la interfaz:

- **filesystem**: Acceso al sistema de archivos
- **memory**: Sistema de memoria persistente
- **brave-search**: Búsqueda web (requiere API key)
- **fetch**: Obtención de recursos web
- **git**: Integración con git

### 2. Configuración de API Keys

1. En VSCode Settings, expandir la configuración de Claude
2. Agregar las API keys necesarias de forma segura:
   - Brave API Key para búsqueda web
   - Otras API keys según necesidad

### 3. Estructura de Directorios

```
/home/cdm/Documents/Cline/MCP/
├── venv/                    # Entorno virtual de Python
└── node_modules/           # Módulos de Node.js
```

## Instalación de Dependencias

### Python

```bash
mkdir -p /home/cdm/Documents/Cline/MCP
cd /home/cdm/Documents/Cline/MCP
python3 -m venv venv
source venv/bin/activate
pip install mcp-server-git mcp-server-fetch
```

### Node.js

```bash
cd /home/cdm/Documents/Cline/MCP
npm install @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
```

## Verificación

1. Abrir VSCode
2. Verificar que los MCP servers aparecen en la configuración
3. Probar cada servidor:
   - memory: Debería mantener contexto entre conversaciones
   - brave-search: Debería poder realizar búsquedas web
   - git: Debería poder interactuar con repositorios
   - fetch: Debería poder obtener recursos web

## Solución de Problemas

1. Si los MCP servers no responden:
   - Verificar que las dependencias están instaladas
   - Comprobar que las API keys están configuradas correctamente
   - Revisar los logs de VSCode

2. Si hay problemas de permisos:
   - Verificar permisos de los directorios
   - Asegurar que los scripts Python son ejecutables

## Mejores Prácticas

1. Seguridad:
   - Usar la interfaz de VSCode para API keys
   - No almacenar claves en archivos de texto
   - Rotar claves periódicamente

2. Mantenimiento:
   - Actualizar dependencias regularmente
   - Mantener VSCode y extensiones actualizados
   - Documentar cambios en la configuración

3. Backup:
   - Exportar configuración de VSCode periódicamente
   - Mantener registro de API keys en un gestor de contraseñas
   - Documentar proceso de recuperación
