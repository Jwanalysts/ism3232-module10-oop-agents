from chatbot import SupportChatbot
from mock_model import MockModel
from order_tool import OrderLookup


class FailingModel:
    def reply(self, instructions, history):
        return None


class RecordingModel:
    def __init__(self):
        self.received_history = None

    def reply(self, instructions, history):
        self.received_history = list(history)
        return "This is a model response."


def make_bot(model):
    return SupportChatbot(
        "Sunny",
        "You are Sunny, a support assistant.",
        OrderLookup({"A100": "shipped"}),
        model=model,
    )


def test_mock_model_greeting():
    bot = make_bot(MockModel())
    assert bot.respond("hello") == "Hello! How can I help you today?"


def test_model_receives_history():
    model = RecordingModel()
    bot = make_bot(model)
    assert bot.respond("How are you?") == "This is a model response."
    assert model.received_history[-1]["content"] == "How are you?"


def test_model_failure_fallback():
    bot = make_bot(FailingModel())
    assert "can't answer" in bot.respond("What is the weather?").lower()


def test_order_rule_overrides_model():
    bot = make_bot(FailingModel())
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_human_handoff_overrides_model():
    bot = make_bot(FailingModel())
    assert "human agent" in bot.respond("Change my address").lower()
