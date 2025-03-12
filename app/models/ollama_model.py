from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from app.configs.config import LOCAL_OLLAMA_MODEL_URL,MODEL_NAME

ollama_provider = OpenAIProvider(
    base_url=LOCAL_OLLAMA_MODEL_URL
)

ollama_model = OpenAIModel(
    model_name=MODEL_NAME,
    provider=ollama_provider
)
