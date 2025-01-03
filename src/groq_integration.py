import os
import logging
from groq import Groq

class GroqIntegration:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ_API_KEY no está configurado")
        
        self.client = Groq(api_key=self.api_key)
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger('groq_integration')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger

    def get_chat_completion(self, messages, model="llama-3.1-8b-instant", temperature=0.7):
        try:
            self.logger.info(f"Iniciando solicitud de chat con modelo: {model}")
            
            completion = self.client.chat.completions.create(
                messages=messages,
                model=model,
                temperature=temperature,
                stream=False
            )
            
            self.logger.info("Solicitud completada exitosamente")
            return completion.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error en la solicitud de chat: {str(e)}")
            raise

# Ejemplo de uso
if __name__ == "__main__":
    groq = GroqIntegration()
    response = groq.get_chat_completion([
        {"role": "user", "content": "Explica la importancia de los modelos de lenguaje rápido"}
    ])
    print(response)
