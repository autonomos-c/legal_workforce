# Configuración de GitHub Codespaces

## Problema de Persistencia

Los Codespaces son entornos de desarrollo efímeros, lo que significa que:
1. El sistema de archivos se reinicia con cada recreación
2. Las variables de entorno no persisten
3. Las dependencias necesitan reinstalarse
4. La configuración de MCP servers se pierde

## Solución: Codespace Secrets

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

## Proceso de Desarrollo

1. Primera vez:
   a. Configurar Codespace Secrets en GitHub
   b. Crear nuevo codespace desde main
   c. El sistema se configurará automáticamente

2. En cada sesión:
   - Los secrets estarán disponibles como variables de entorno
   - pip install -r requirements.txt instalará dependencias
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
   - Verificar que las extensiones están instaladas
   - Reinstalar dependencias si es necesario:
     ```bash
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
