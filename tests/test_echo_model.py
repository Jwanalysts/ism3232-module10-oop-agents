from chatbot import SupportChatbot
from echo_model import EchoModel
from order_tool import OrderLookup


def test_echo_model():
    bot = SupportChatbot(
        "Sunny",
        "Be friendly.",
        OrderLookup({"A100": "shipped"}),
        model=EchoModel(),
    )
    assert bot.respond("good morning") == "You said: good morning"
