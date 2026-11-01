
from service_tool import ServiceLookup
from business_assistant import BusinessAssistant


def make_bot():
    services = {
        "website development": 500,
        "social media management": 300,
        "business consulting": 200
    }
    tool = ServiceLookup(services)
    return BusinessAssistant("JW Assistant", tool)


def test_service_lookup():
    tool = ServiceLookup({"website development": 500})
    assert tool.find_price("website development") == 500


def test_unknown_service():
    tool = ServiceLookup({"website development": 500})
    assert tool.find_price("accounting") is None


def test_service_case_insensitive():
    bot = make_bot()
    assert "$500" in bot.respond("WEBSITE DEVELOPMENT")


def test_business_greeting():
    bot = make_bot()
    assert "JW Assistant" in bot.respond("hello")


def test_business_human_handoff():
    bot = make_bot()
    assert "human" in bot.respond("I need a refund")


def test_business_unknown_request():
    bot = make_bot()
    assert "contact our team" in bot.respond("Can you do my taxes?")


def test_business_history():
    bot = make_bot()
    bot.respond("hello")

    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_business_separate_histories():
    bot1 = make_bot()
    bot2 = make_bot()

    bot1.respond("hello")

    assert len(bot1.history) == 2
    assert len(bot2.history) == 0
