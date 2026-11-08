from ollama import ResponseError, chat


class OllamaModel:
    """A real AI model running locally through Ollama."""

    def __init__(self, model_name):
        self.model_name = model_name

    def reply(self, instructions, history):
        messages = [{"role": "system", "content": instructions}]
        messages = messages + history

        try:
            response = chat(model=self.model_name, messages=messages)
        except (ConnectionError, ResponseError):
            return None

        return response.message.content
