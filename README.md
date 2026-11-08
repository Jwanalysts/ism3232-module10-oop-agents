# Week 11 — Local AI Model

This project upgrades my Week 10 customer support chatbot and JW Analysts business assistant with a local AI model using Ollama.

## Mini-Project Reflection

My JW Analysts assistant successfully answers questions about website development pricing using the service lookup tool. The AI model can also handle general customer conversations, but questions about services not covered by the instructions may need to be referred to a human representative. In my store chatbot experiment, the model incorrectly agreed that the store closed at 11 PM, even though its instructions said 7 PM. This showed me that AI-generated answers are not always reliable, even when the model has clear instructions. I kept service prices, order statuses, stock quantities, and human handoffs in Python code because those details must remain accurate. The model handles general conversation, while Python rules and tools control important business information.

## Running the Projects

Install dependencies:

    pip install -r requirements.txt

Run the support chatbot:

    python main.py

Run the JW Analysts assistant:

    python my_main.py

Run tests:

    pytest -v
