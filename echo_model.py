class EchoModel:
    """Repeat the last customer message."""

    def reply(self, instructions, history):
        return "You said: " + history[-1]["content"]
