# Configuración de Entorno Local

## 1. Preparación Inicial

### Clonar Repositorio
```bash
git clone https://github.com/autonomos-c/legal_workforce.git
cd legal_workforce
```

### Crear Entorno Virtual
```bash
# Crear venv en directorio del proyecto
python -m venv venv

# Activar venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### Configurar Variables de Entorno
```bash
# Copiar template
cp .env.example .env

# Editar .env con las API keys:
GROQ_API_KEY=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
BRAVE_API_KEY=BSANOhifT5Rcp-VCYTXGhxyZyny__Lm
```

## 2. Instalación de Dependencias

### Python
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### Node.js (para MCP servers)
```bash
# Instalar paquetes MCP globalmente
npm install -g @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
```

## 3. Configuración de VSCode

### Extensiones Necesarias
- Python (ms-python.python)
- Pylance (ms-python.vscode-pylance)
- Claude Dev (saoudrizwan.claude-dev)
- Black Formatter (ms-python.black-formatter)
- isort (ms-python.isort)

### Configuración de MCP
Ubicación: ~/.vscode/settings.json
```json
{
  "claude-dev.mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "${env:BRAVE_API_KEY}"
      }
    }
  }
}
```

## 4. Flujo de Trabajo Git

### Actualizar Repositorio
```bash
# Antes de empezar a trabajar
git pull origin main

# Crear rama para nuevas características
git checkout -b feature/nombre-caracteristica
```

### Subir Cambios
```bash
# Verificar cambios
git status

# Agregar cambios
git add .

# Crear commit
git commit -m "tipo: descripción del cambio"

# Subir cambios
git push origin feature/nombre-caracteristica
```

### Tipos de Commit
- feat: Nueva característica
- fix: Corrección de bug
- docs: Cambios en documentación
- style: Cambios de formato
- refactor: Refactorización de código
- test: Agregar o modificar tests
- chore: Tareas de mantenimiento

## 5. Verificación

### Probar Integración
```python
# En terminal Python
from src.groq_integration import GroqIntegration
groq = GroqIntegration()
```

### Ejecutar Tests
```bash
pytest tests/
```

## 6. Mantenimiento

### Actualizar Dependencias
```bash
# Actualizar todo
pip install -r requirements.txt --upgrade

# Actualizar paquete específico
pip install --upgrade nombre-paquete
```

### Limpiar Entorno
```bash
# Desactivar venv
deactivate

# Eliminar archivos compilados
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
```

## Notas Importantes

1. Siempre trabajar con el entorno virtual activado
2. Mantener .env fuera del control de versiones
3. Hacer commits frecuentes y descriptivos
4. Actualizar documentación cuando sea necesario
5. Ejecutar tests antes de subir cambios
