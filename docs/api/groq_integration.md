# Groq Integration API

## Configuración

La API key de Groq se configura automáticamente a través del devcontainer. No es necesario configurar manualmente variables de entorno.

## Clase GroqIntegration

```python
class GroqIntegration:
    """Clase principal para integración con Groq API"""
```

### Métodos

#### `__init__()`

```python
def __init__(self):
    """
    Inicializa la conexión con Groq API
    La API key se obtiene automáticamente del entorno configurado
    """
```

#### `get_chat_completion()`

```python
def get_chat_completion(
    messages: List[Dict[str, str]],
    model: str = "llama-3.1-8b-instant",
    temperature: float = 0.7
) -> str:
    """
    Obtiene una respuesta del modelo de lenguaje
    
    Args:
        messages: Lista de mensajes en formato OpenAI
        model: Modelo a utilizar (default: llama-3.1-8b-instant)
        temperature: Creatividad de la respuesta (0.0 - 1.0)
        
    Returns:
        Respuesta generada por el modelo
        
    Raises:
        ValueError: Si no se encuentra la API key en el entorno
        Exception: Errores de conexión con la API
    """
```

## Ejemplo de Uso

```python
from src.groq_integration import GroqIntegration

# El devcontainer ya tiene configurada la API key
groq = GroqIntegration()

# Ejemplo de uso con el agente legal
response = groq.get_chat_completion([
    {
        "role": "system",
        "content": "Eres un asistente legal especializado."
    },
    {
        "role": "user",
        "content": "¿Cuáles son los elementos básicos de un contrato?"
    }
])
print(response)
```

## Desarrollo

### Testing

Las pruebas se ejecutan automáticamente en el CI:
```bash
pytest tests/test_groq_integration.py
```

### Configuración Local

Si desarrollas fuera del devcontainer:
1. Copia .env.example a .env
2. Agrega tu GROQ_API_KEY
3. El contenedor cargará la variable automáticamente

### Mejores Prácticas

1. Usar el devcontainer para desarrollo
2. Las API keys se manejan automáticamente
3. Mantener los tests actualizados
4. Documentar cambios en la API
