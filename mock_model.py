class MockModel:
    """A fake AI model for testing."""

    def reply(self, instructions, history):
        last_message = history[-1]["content"].lower()

        if "hello" in last_message:
            return "Hello! How can I help you today?"

        return "I'm not sure how to help with that. I can check an order or stock."
