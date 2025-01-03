import pytest
from src.groq_integration import GroqIntegration

class TestGroqIntegration:
    def test_initialization(self):
        # Prueba de inicialización básica
        with pytest.raises(ValueError):
            groq = GroqIntegration()  # Debería fallar sin API_KEY
            
    def test_get_chat_completion(self, monkeypatch):
        # Mock de la API para pruebas
        def mock_chat_completion(*args, **kwargs):
            class MockResponse:
                def __init__(self):
                    self.choices = [type('obj', (object,), {'message': type('obj', (object,), {'content': 'Mock response'})})]
            
            return MockResponse()

        monkeypatch.setenv('GROQ_API_KEY', 'test_key')
        monkeypatch.setattr('groq.Groq.chat.completions.create', mock_chat_completion)
        
        groq = GroqIntegration()
        response = groq.get_chat_completion([{"role": "user", "content": "test"}])
        
        assert response == "Mock response"
