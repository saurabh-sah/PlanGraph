from app.core.llm_factory import (
    create_llm
)


llm = create_llm()

response = llm.invoke(
    "Hello"
)

print(response.content)