
class BusinessAssistant:
    """A mock assistant for JW Analysts."""

    def __init__(self, name, service_tool):
        self.name = name
        self.service_tool = service_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({
            "role": "user",
            "content": user_message
        })

        reply = self.choose_reply(user_message)

        self.history.append({
            "role": "assistant",
            "content": reply
        })

        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if "payment" in text or "refund" in text:
            return "A human representative must handle that request."

        service = self.service_tool.find_service(user_message)

        if service is not None:
            price = self.service_tool.find_price(service)
            return f"Our {service} service starts at ${price}."

        if "hello" in text:
            return f"Hello! I'm {self.name}, your JW Analysts assistant."

        return "I can help with service information. Please contact our team for other requests."
