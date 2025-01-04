FROM mcr.microsoft.com/devcontainers/python:3.11

# Evitar prompts durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar Node.js y npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Configurar directorio de trabajo
WORKDIR /workspaces/legal_workforce

# Instalar dependencias de Python globalmente
RUN pip install --upgrade pip

# Cambiar al usuario no root
USER vscode
