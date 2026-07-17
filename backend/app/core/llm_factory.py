from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from app.core.config import settings


def create_llm(
    provider: str | None = None,
    model: str | None = None,
    temperature: float = 0,
):

    provider = (
        provider
        or settings.default_llm_provider
    )

    model = (
        model
        or settings.default_llm_model
    )

    if provider == "google":

        return ChatGoogleGenerativeAI(

            model=model,

            google_api_key=
                settings.google_api_key,

            temperature=temperature,
        )

    raise ValueError(
        f"Unsupported provider: {provider}"
    )