# Configuración de MCP Servers

## Requisitos Previos

1. Node.js y npm instalados
2. Python 3.x y pip instalados
3. Entorno virtual de Python configurado

## Estructura de Directorios

```
/home/cdm/Documents/Cline/MCP/
├── venv/                    # Entorno virtual de Python
├── package.json            # Dependencias npm
└── .env                    # Variables de entorno (no versionado)
```

## Instalación

1. Crear y activar entorno virtual Python:
```bash
mkdir -p /home/cdm/Documents/Cline/MCP
cd /home/cdm/Documents/Cline/MCP
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias Python:
```bash
pip install mcp-server-git mcp-server-fetch
```

3. Instalar dependencias npm:
```bash
npm install @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
```

## Configuración

1. Crear archivo `.env`:
```env
BRAVE_API_KEY=your_api_key_here
```

2. Configurar MCP servers en VSCode:
Archivo: `~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/"
      ]
    },
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    },
    "fetch": {
      "command": "${MCP_DIR}/venv/bin/python",
      "args": [
        "-m",
        "mcp_server_fetch"
      ]
    },
    "git": {
      "command": "${MCP_DIR}/venv/bin/python",
      "args": [
        "-m",
        "mcp_server_git",
        "--repository",
        "${PROJECT_DIR}"
      ]
    }
  }
}
```

## Variables de Entorno

Crear archivo `.env` en el directorio raíz del proyecto:

```env
MCP_DIR=/home/cdm/Documents/Cline/MCP
PROJECT_DIR=/home/cdm/legal_agent
BRAVE_API_KEY=your_api_key_here
```

## Mantenimiento

1. Actualizar dependencias:
```bash
pip install --upgrade mcp-server-git mcp-server-fetch
npm update @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
```

2. Backup de configuración:
- Mantener copia de seguridad de `cline_mcp_settings.json`
- Documentar cualquier cambio en la configuración

## Solución de Problemas

1. Si los MCP servers no responden:
- Verificar que el entorno virtual está activado
- Confirmar que las variables de entorno están configuradas
- Revisar los logs de VSCode

2. Si hay problemas de permisos:
- Verificar permisos de los directorios
- Asegurar que los scripts Python son ejecutables

## Mejores Prácticas

1. Control de Versiones:
- Versionar los archivos de configuración template
- NO versionar archivos con información sensible (.env)
- Mantener documentación actualizada

2. Seguridad:
- Usar variables de entorno para claves API
- Rotar claves periódicamente
- Limitar permisos de acceso

3. Mantenimiento:
- Actualizar dependencias regularmente
- Mantener copias de seguridad de configuración
- Documentar cambios y problemas conocidos
