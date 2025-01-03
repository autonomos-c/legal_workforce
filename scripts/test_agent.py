import sys
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(Path(__file__).parent.parent / '.env')

# Agregar directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from src.groq_integration import GroqIntegration

def main():
    # Cargar contexto legal
    context_path = Path(__file__).parent.parent / "context" / "legal_context.txt"
    with open(context_path, "r") as f:
        legal_context = f.read()

    # Crear instancia del agente
    groq = GroqIntegration()

    # Preparar mensaje inicial
    messages = [
        {"role": "system", "content": "Eres un asistente legal experto. Responde consultas basado en el contexto proporcionado."},
        {"role": "user", "content": legal_context},
        {"role": "user", "content": "Explica los requisitos para constituir una sociedad anónima en México"}
    ]

    # Obtener respuesta
    response = groq.get_chat_completion(messages)
    print("Respuesta del agente:")
    print(response)

if __name__ == "__main__":
    main()
