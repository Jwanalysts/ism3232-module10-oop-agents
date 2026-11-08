from chatbot import SupportChatbot
from order_tool import OrderLookup


def make_bot():
    orders = {"A100": "shipped", "A101": "processing"}
    tool = OrderLookup(orders)
    return SupportChatbot("Sunny", "Be friendly.", tool)


def test_order_lookup():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A100") == "shipped"


def test_unknown_order():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A999") is None


def test_order_id_case_insensitive():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_order_id("Where is a100?") == "A100"


def test_chatbot_greeting():
    bot = make_bot()
    assert "Sunny" in bot.respond("hello")


def test_chatbot_order_status():
    bot = make_bot()
    assert "shipped" in bot.respond("Where is order A100?")


def test_chatbot_missing_order_id():
    bot = make_bot()
    assert "Which order?" in bot.respond("Where is my order?")


def test_chatbot_human_handoff():
    bot = make_bot()
    assert "human agent" in bot.respond("Change my address")


def test_chatbot_unknown_question():
    bot = make_bot()
    assert "not sure" in bot.respond("What is the weather?")


def test_chatbot_history():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_separate_chatbot_histories():
    bot1 = make_bot()
    bot2 = make_bot()
    bot1.respond("hello")

    assert len(bot1.history) == 2
    assert len(bot2.history) == 0
