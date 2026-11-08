# Week 11 — Local AI Model

This project upgrades my Week 10 customer support chatbot and JW Analysts business assistant with a local AI model using Ollama.

## Mini-Project Reflection

The model successfully answered a question about shipping time using the facts provided in its instructions. It correctly refused to invent an answer about gift wrapping because that information was not provided. However, during testing, the model incorrectly agreed that the store closed at 11 PM even though its instructions stated 7 PM. I decided to keep service prices, order statuses, stock quantities, and human handoffs in Python code because those details must remain accurate and should not depend on generated responses. The model handles general conversation while the code controls important business information.

## Running the Projects

Install dependencies:

    pip install -r requirements.txt

Run the support chatbot:

    python main.py

Run the JW Analysts assistant:

    python my_main.py

Run tests:

    pytest -v
