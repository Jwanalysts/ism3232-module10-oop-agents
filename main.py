
from order_tool import OrderLookup
from chatbot import SupportChatbot


def main():
    orders = {
        "A100": "shipped",
        "A101": "processing",
        "A102": "delivered"
    }

    order_tool = OrderLookup(orders)

    bot = SupportChatbot(
        "Sunny",
        "You are a friendly customer support assistant.",
        order_tool
    )

    messages = [
        "hello",
        "Where is order A100?",
        "Where is order A101?",
        "Where is my order?",
        "Please change my shipping address",
        "What is the weather today?"
    ]

    for message in messages:
        print(f"Customer: {message}")
        print(f"Sunny: {bot.respond(message)}")
        print()

    print(f"Total messages in history: {len(bot.history)}")


if __name__ == "__main__":
    main()
