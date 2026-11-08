from chatbot import SupportChatbot
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup


def test_stock_lookup_uses_tool():
    bot = SupportChatbot(
        "Sunny",
        "Be friendly.",
        OrderLookup({"A100": "shipped"}),
        model=MockModel(),
        stock_tool=StockLookup({"rain jacket": 12}),
    )
    assert bot.respond("Is the rain jacket in stock?") == (
        "We have 12 of the rain jacket in stock."
    )
