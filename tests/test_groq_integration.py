import pytest
from unittest.mock import patch, MagicMock
from src.groq_integration import GroqIntegration

class TestGroqIntegration:
    def test_initialization_without_key(self, monkeypatch):
        # Deshabilitar variable de entorno
        monkeypatch.delenv('GROQ_API_KEY', raising=False)
        
        # Prueba de inicialización sin API_KEY
        with pytest.raises(ValueError):
            GroqIntegration()

    def test_initialization_with_key(self):
        # Prueba de inicialización con API_KEY
        groq = GroqIntegration(api_key='test_key')
        assert groq is not None

    @patch('src.groq_integration.Groq')
    def test_get_chat_completion(self, mock_groq):
        # Configurar mock
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = 'Mock response'
        
        mock_client.chat.completions.create.return_value = mock_response
        mock_groq.return_value = mock_client

        # Instanciar y probar
        groq = GroqIntegration(api_key='test_key')
        response = groq.get_chat_completion([{"role": "user", "content": "test"}])
        
        assert response == "Mock response"
        mock_client.chat.completions.create.assert_called_once()
