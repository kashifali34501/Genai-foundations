from langchain.chat_models import init_chat_model

llm= init_chat_model(
    model="ollama:gemma3:4b",
    temperature = 1.0
)

history = [
    {"role": "system",
    "content": "You are a helpful assistant."}
]

print("Welcome to Cue chat")
while True:
    question = input("Ask your question: ")
    if not question:
        continue
    if question.lower() in {"exit", "quit", "bye"}:
        print("Exiting the chat. Goodbye!")
        break
    history.append({"role": "user", "content": question})
    response = llm.invoke(history)# LLM Call.....
    history.append({"role": "assistant", "content": response.text})
    print(f"Bot: {response.text}")

