from pydantic import BaseModel


class LLMConfig(BaseModel):

    provider: str = "google"

    model: str = "gemini-2.5-flash"

    temperature: float = 0

    streaming: bool = False