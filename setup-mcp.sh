#!/bin/bash

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Directorio base
MCP_DIR="/home/cdm/Documents/Cline/MCP"

echo -e "${YELLOW}Instalando dependencias de MCP Servers...${NC}"

# Crear directorio necesario
echo "Creando directorio..."
mkdir -p "$MCP_DIR"

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
cd "$MCP_DIR"
npm init -y
npm install @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search

echo -e "${GREEN}Instalación de dependencias completada${NC}"
echo -e "${YELLOW}Importante:${NC}"
echo "1. Las dependencias se han instalado en: $MCP_DIR"
echo "2. Para activar el entorno Python en nuevas sesiones:"
echo "   source $MCP_DIR/venv/bin/activate"
echo -e "${YELLOW}Siguiente paso:${NC}"
echo "Configurar los MCP servers a través de la interfaz de VSCode:"
echo "1. Abrir VSCode Settings (Ctrl+,)"
echo "2. Buscar 'Claude MCP'"
echo "3. Configurar los servidores y API keys necesarias"
