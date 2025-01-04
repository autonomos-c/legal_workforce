FROM mcr.microsoft.com/devcontainers/python:3.11

# Evitar prompts durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js y npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# Crear y configurar el entorno virtual de Python
RUN python -m venv /workspace/venv
ENV PATH="/workspace/venv/bin:$PATH"

# Configurar directorio de trabajo
WORKDIR /workspace

# Instalar dependencias de Python globalmente
RUN pip install --upgrade pip \
    faiss-cpu \
    numpy \
    sentence-transformers \
    pytest \
    python-dotenv \
    loguru

# Crear directorio para MCP
RUN mkdir -p /workspace/Documents/Cline/MCP

# Cambiar al usuario no root
USER vscode
