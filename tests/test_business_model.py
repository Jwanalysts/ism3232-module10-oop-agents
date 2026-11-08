from business_assistant import BusinessAssistant
from mock_model import MockModel
from service_tool import ServiceLookup


class SilentModel:
    def reply(self, instructions, history):
        return None


def make_bot(model):
    return BusinessAssistant(
        "JW Assistant",
        ServiceLookup({"website development": 500}),
        model=model,
    )


def test_business_model_greeting():
    assert make_bot(MockModel()).respond("hello") == (
        "Hello! How can I help you today?"
    )


def test_business_model_failure():
    assert "can't answer" in make_bot(SilentModel()).respond("hello")


def test_business_tool_still_works():
    assert "500" in make_bot(SilentModel()).respond("How much is website development?")


def test_business_handoff_still_works():
    assert "human" in make_bot(SilentModel()).respond("I want a refund").lower()
