# Groq Integration API

## Clase GroqIntegration

```python
class GroqIntegration:
    """Clase principal para integración con Groq API"""
```

### Métodos

#### `__init__()`

```python
def __init__(self):
    """Inicializa la conexión con Groq API"""
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
        model: Modelo a utilizar
        temperature: Creatividad de la respuesta
        
    Returns:
        Respuesta generada por el modelo
    """
```

## Ejemplo de Uso

```python
from src.groq_integration import GroqIntegration

groq = GroqIntegration()
response = groq.get_chat_completion([
    {"role": "user", "content": "Explica la importancia de los modelos de lenguaje rápido"}
])
print(response)
```

## Manejo de Errores

La clase maneja los siguientes errores:

- `ValueError`: Cuando falta la API_KEY
- `Exception`: Errores de conexión con la API
