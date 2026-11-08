from business_assistant import BusinessAssistant
from service_tool import ServiceLookup


def main():
    services = {
        "website development": 500,
        "social media management": 300,
        "business consulting": 200,
    }

    tool = ServiceLookup(services)
    bot = BusinessAssistant("JW Assistant", tool)

    messages = [
        "hello",
        "How much is website development?",
        "Tell me about social media management",
        "Do you offer business consulting?",
        "Can I request a refund?",
        "Can you help me with accounting?",
    ]

    for message in messages:
        print(f"Customer: {message}")
        print(f"Assistant: {bot.respond(message)}")
        print()

    print(f"Total messages in history: {len(bot.history)}")


if __name__ == "__main__":
    main()
