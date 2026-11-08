from business_assistant import BusinessAssistant
from ollama_model import OllamaModel
from service_tool import ServiceLookup

SERVICES = {
    "website development": 500,
    "social media management": 300,
    "business consulting": 200,
}

bot = BusinessAssistant(
    "JW Assistant",
    ServiceLookup(SERVICES),
    model=OllamaModel("granite4.1:3b"),
)

if __name__ == "__main__":
    print("Type quit to stop.")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        print(f"Assistant: {bot.respond(message)}")
