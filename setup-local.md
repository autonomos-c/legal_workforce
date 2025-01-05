# Configuración Local del Proyecto

## Preparación Inicial

1. Crea un archivo .env en la raíz del proyecto:
```bash
cp .env.example .env
```

2. Edita el archivo .env y agrega tus API keys:
- GROQ_API_KEY: Obtén tu key en https://console.groq.com
- BRAVE_API_KEY: Obtén tu key en https://brave.com/search/api/

## Crear Nuevo Codespace

1. En GitHub:
   - Code > Codespaces > Create codespace
   - Selecciona:
     * Branch: main
     * Machine type: 4-core

2. El sistema automáticamente:
   - Configurará el entorno básico
   - Instalará dependencias
   - Mantendrá el MCP memory server

## Verificar la Configuración

Para verificar que todo está configurado:

```python
# En una terminal de Python
from src.groq_integration import GroqIntegration
groq = GroqIntegration()
# Si no hay errores, la configuración es correcta
```

## Solución de Problemas

Si encuentras errores:

1. Verifica el archivo .env:
```bash
cat .env  # Debería mostrar tus API keys
```

2. Verifica las variables de entorno:
```bash
echo $GROQ_API_KEY  # Debería mostrar tu key
```

3. Si es necesario, reinstala las dependencias:
```bash
pip install -r requirements.txt
