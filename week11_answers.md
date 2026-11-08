# Week 11 — Talking to a Local Model

## Exercise 1 — What Is a Language Model?

A language model predicts and generates text based on patterns it learned during training. It is not a database, so it can sometimes make up information that sounds correct. We should use code and tools for important facts instead of trusting every model response.

## Exercise 3 — Conversation History

A model does not automatically remember previous conversations. Our Python program stores messages in a history list and sends that history back to the model. This allows the model to understand earlier messages and respond with context.

## Exercise 4 — Using a Model in a Chatbot

MockModel and OllamaModel both use a reply method, so the chatbot can work with either model. MockModel helps us test without running Ollama. OllamaModel connects to a real local AI model. If Ollama fails, the chatbot returns a safe fallback response instead of crashing.
