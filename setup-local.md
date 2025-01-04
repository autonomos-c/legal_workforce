# Configuración Local del Proyecto

## Usando Variables de Entorno (.env)

1. Crea un archivo .env en la raíz del proyecto:
```bash
cp .env.example .env
```

2. Edita el archivo .env y agrega tus API keys:
- GROQ_API_KEY: Obtén tu key en https://console.groq.com
- BRAVE_API_KEY: Obtén tu key en https://brave.com/search/api/

## Reconstruir el Codespace

1. Asegúrate de tener el archivo .env configurado
2. Elimina el codespace actual:
   - En VSCode: Remote Explorer > Click derecho > Delete
   - O en GitHub: Settings > Codespaces > Delete

3. Crea un nuevo codespace:
   - En GitHub: Code > Codespaces > Create codespace
   - Selecciona:
     * Branch: main
     * Machine type: 4-core

4. El sistema automáticamente:
   - Leerá las variables del .env
   - Instalará dependencias
   - Configurará el entorno

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

3. Reinicia el contenedor si es necesario:
   - Command Palette (Ctrl+Shift+P)
   - "Remote-Containers: Rebuild Container"
