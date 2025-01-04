#!/bin/bash

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Directorios
MCP_DIR="/home/cdm/Documents/Cline/MCP"
CONFIG_DIR="$HOME/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings"

echo -e "${YELLOW}Configurando MCP Servers...${NC}"

# Crear directorios necesarios
echo "Creando directorios..."
mkdir -p "$MCP_DIR"
mkdir -p "$CONFIG_DIR"

# Verificar Node.js y npm
if ! command -v node &> /dev/null || ! command -v npm &> /dev/null; then
    echo -e "${RED}Error: Node.js y npm son requeridos${NC}"
    exit 1
fi

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 es requerido${NC}"
    exit 1
fi

# Crear y activar entorno virtual
echo "Configurando entorno Python..."
cd "$MCP_DIR"
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
echo "Instalando dependencias Python..."
pip install mcp-server-git mcp-server-fetch

# Instalar dependencias npm
echo "Instalando dependencias npm..."
npm init -y
npm install @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search

# Solicitar Brave API Key si no existe
if [ ! -f "$MCP_DIR/.env" ]; then
    echo -e "${YELLOW}Ingrese su Brave API Key:${NC}"
    read -r brave_key
    echo "BRAVE_API_KEY=$brave_key" > "$MCP_DIR/.env"
    echo "MCP_DIR=$MCP_DIR" >> "$MCP_DIR/.env"
    echo "PROJECT_DIR=/home/cdm/legal_agent" >> "$MCP_DIR/.env"
fi

# Crear archivo de configuración MCP
echo "Configurando MCP settings..."
cat > "$CONFIG_DIR/cline_mcp_settings.json" << EOL
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
        "BRAVE_API_KEY": "\${BRAVE_API_KEY}"
      }
    },
    "fetch": {
      "command": "\${MCP_DIR}/venv/bin/python",
      "args": [
        "-m",
        "mcp_server_fetch"
      ]
    },
    "git": {
      "command": "\${MCP_DIR}/venv/bin/python",
      "args": [
        "-m",
        "mcp_server_git",
        "--repository",
        "\${PROJECT_DIR}"
      ]
    }
  }
}
EOL

# Crear backup de configuración
echo "Creando backup de configuración..."
cp "$CONFIG_DIR/cline_mcp_settings.json" "$MCP_DIR/mcp_settings_backup.json"

echo -e "${GREEN}Configuración de MCP completada${NC}"
echo -e "${YELLOW}Importante:${NC}"
echo "1. La configuración se ha guardado en: $CONFIG_DIR/cline_mcp_settings.json"
echo "2. Un backup se ha creado en: $MCP_DIR/mcp_settings_backup.json"
echo "3. Las variables de entorno están en: $MCP_DIR/.env"
echo -e "${YELLOW}Para activar el entorno en nuevas sesiones:${NC}"
echo "source $MCP_DIR/venv/bin/activate"
