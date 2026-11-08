class BusinessAssistant:
    """A mock assistant for JW Analysts."""

    def __init__(self, name, service_tool, model=None):
        self.name = name
        self.service_tool = service_tool
        self.model = model
        self.instructions = (
            "You are the JW Analysts assistant. Answer briefly. "
            "Website development starts at $500. "
            "Social media management starts at $300. "
            "Only use these facts or verified service information. "
            "If you do not know, say so and refer the customer to our team."
        )
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if "payment" in text or "refund" in text:
            return "A human representative must handle that request."

        service = self.service_tool.find_service(user_message)

        if service is not None:
            price = self.service_tool.find_price(service)
            return f"Our {service} service starts at ${price}."

        if self.model is not None:
            reply = self.model.reply(self.instructions, self.history)
            if reply is None:
                return "Sorry, I can't answer that right now. Please contact our team."
            return reply

        if "hello" in text:
            return f"Hello! I'm {self.name}, your JW Analysts assistant."

        return "I can help with service information. Please contact our team for other requests."
