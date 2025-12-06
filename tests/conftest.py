import pytest
from unittest.mock import MagicMock
import sys

@pytest.fixture
def mock_openai_chatcompletion(monkeypatch):
    mock_create = MagicMock()
    mock_acreate = MagicMock()
    
    # Setup default return value structure
    mock_response = {
        "choices": [
            {
                "message": {
                    "content": "Mocked response",
                    "role": "assistant",
                    "function_call": None,
                }
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        "model": "gpt-3.5-turbo",
        "object": "chat.completion",
        "created": 1234567890,
        "id": "chatcmpl-123"
    }
    
    mock_create.return_value = mock_response
    
    # Async mock needs to be an awaitable
    async def async_return(*args, **kwargs):
        return mock_response
    mock_acreate.side_effect = async_return

    monkeypatch.setattr("autogen.oai.ChatCompletion.create", mock_create)
    monkeypatch.setattr("autogen.oai.ChatCompletion.acreate", mock_acreate)
    
    return mock_create, mock_acreate
