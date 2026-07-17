from app.core.llm_factory import (
    create_llm
)


class LLMService:

    def __init__(
        self,
        provider=None,
        model=None,
        temperature=0,
    ):

        self.llm = create_llm(
            provider=provider,
            model=model,
            temperature=temperature,
        )

    def invoke(
        self,
        messages,
    ):

        return self.llm.invoke(
            messages
        )