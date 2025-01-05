# Configuración de GitHub Codespaces

## Problema de Persistencia

Los Codespaces son entornos de desarrollo efímeros, lo que significa que:
1. El sistema de archivos se reinicia con cada recreación
2. Las variables de entorno no persisten
3. Las dependencias necesitan reinstalarse
4. La configuración de MCP servers se pierde

## Solución: Codespace Secrets y MCP

Para mantener la configuración entre sesiones:

1. Configurar Codespace Secrets:
   - En GitHub: Settings > Secrets and variables > Codespaces
   - Agregar los siguientes secrets:
     * GROQ_API_KEY
     * BRAVE_API_KEY

2. Estos secrets:
   - Se cargan automáticamente como variables de entorno
   - Están disponibles en cada nuevo codespace
   - Son seguros y encriptados
   - No se pierden al reiniciar

3. Configurar MCP Servers:
   - Ubicación: ~/.vscode-remote/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
   - Contenido necesario:
     ```json
     {
       "mcpServers": {
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
   - Esta configuración persiste entre sesiones

## Proceso de Desarrollo

1. Primera vez:
   a. Configurar Codespace Secrets en GitHub
   b. Verificar configuración de MCP servers
   c. Crear nuevo codespace desde main
   d. Instalar herramientas básicas:
      ```bash
      sudo apt-get update && sudo apt-get install -y python3-pip
      ```
   e. Instalar extensiones requeridas:
      ```bash
      code --install-extension ms-python.black-formatter
      code --install-extension ms-python.isort
      ```
   f. Instalar dependencias:
      ```bash
      pip install -r requirements.txt
      npm install -g @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
      ```

2. En cada sesión nueva:
   - Los secrets estarán disponibles como variables de entorno
   - Verificar que pip está instalado:
     ```bash
     which pip || sudo apt-get install -y python3-pip
     ```
   - Reinstalar dependencias si es necesario:
     ```bash
     pip install -r requirements.txt
     ```
   - Los MCP servers usarán las API keys de los secrets

3. Al reiniciar/recrear:
   - Los secrets se mantendrán
   - Solo necesitas reinstalar dependencias
   - No es necesario reconfigurar API keys

## Verificación

Para verificar la configuración:
```python
from src.groq_integration import GroqIntegration
groq = GroqIntegration()
```

Si no hay errores, los secrets están configurados correctamente.

## Solución de Problemas

1. Si las API keys no están disponibles:
   - Verificar Codespace Secrets en GitHub
   - Recrear el codespace si es necesario

2. Si los MCP servers no funcionan:
   - Verificar cline_mcp_settings.json
   - Asegurar que el contenido es correcto
   - Reinstalar extensiones si es necesario:
     ```bash
     code --install-extension saoudrizwan.claude-dev
     ```
   - Reinstalar dependencias:
     ```bash
     npm install -g @modelcontextprotocol/server-memory @modelcontextprotocol/server-brave-search
     pip install -r requirements.txt
     ```

3. Si el entorno no se configura:
   - Asegurarse de usar la rama main
   - Verificar que los secrets están configurados
   - Recrear el codespace desde cero

## Mejores Prácticas

1. Siempre usar Codespace Secrets para API keys
2. No depender de archivos .env locales
3. Mantener requirements.txt actualizado
4. Usar la rama main para nuevos codespaces

## Notas Importantes

- El archivo .env.example es solo una referencia
- No comprometer API keys en el código
- Los Codespace Secrets son la fuente única de verdad para las credenciales
- La recreación del codespace es segura con secrets configurados
