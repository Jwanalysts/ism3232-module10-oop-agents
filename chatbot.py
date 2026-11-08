class SupportChatbot:
    """A mock support chatbot using simple rules."""

    def __init__(self, name, instructions, order_tool, model=None, stock_tool=None):
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.model = model
        self.stock_tool = stock_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."

        if "stock" in text and self.stock_tool is not None:
            return self.stock_reply(user_message)
        if "in stock" in text and self.stock_tool is not None:
            return self.stock_reply(user_message)

        if "order" in text:
            return self.order_reply(user_message)

        if "hello" in text and self.model is None:
            return f"Hello! I'm {self.name}. I can check an order status for you."

        if self.model is not None:
            return self.model_reply()

        return "I'm not sure how to help with that. I can check an order status."

    def model_reply(self):
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

    def needs_human(self, text):
        return any(word in text for word in ["address", "payment", "card", "refund"])

    def order_reply(self, user_message):
        order_id = self.order_tool.find_order_id(user_message)

        if order_id is None:
            return "Which order? Please send an order ID like A100."

        status = self.order_tool.find_status(order_id)

        return f"Order {order_id} is {status}."

    def stock_reply(self, user_message):
        item = self.stock_tool.find_item(user_message)
        if item is None:
            return "Which item would you like me to check?"
        quantity = self.stock_tool.find_quantity(item)
        return f"We have {quantity} of the {item} in stock."
