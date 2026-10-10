from langchain.chat_models import init_chat_model

llm= init_chat_model(
    model="ollama:gemma3:4b",
    temperature = 1.0
)

print("Welcome to Cue chat")
question = input("Ask your question: ")
response = llm.invoke( "You :" + question)  #LLM Call.....
print(f"Response: {response.text}")