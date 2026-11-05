# Exploring Local LLMs

## Project description

In this project, we used Ollama to run three different language models locally on our computers. We gave all three models the same prompt and compared their answers and response times.

The prompt we used was:

> Explain what artificial intelligence is in three simple sentences.

## Models used

We tested the following models:

- **Gemma 3 (1B)** – `gemma3:1b`
- **Llama 3.2** – `llama3.2:latest`
- **Qwen 2.5** – `qwen2.5:latest`

## How to run the code

The following software is needed:

- Python
- [Ollama](https://ollama.com/)
- Python Ollama library

First, install Ollama and download the models using the following commands:

```bash
ollama pull gemma3:1b
ollama pull llama3.2
ollama pull qwen2.5
```

Install the Python library:

```bash
py -m pip install ollama
```

Make sure the models are installed and available by running:

```bash
ollama list
```

To run the program, open a terminal in the project folder and execute:

```bash
py main.py
```

The program sends the same prompt to each model, prints the responses and measures the response time. The results are automatically saved in `results.csv`.

## Results and observations

All three local models gave relevant explanations of artificial intelligence. However, their answers differed in length and detail.

Gemma 3 gave the shortest and simplest explanation. Llama 3.2 provided a more detailed answer, including examples of tasks AI can perform. Qwen 2.5 also gave a detailed explanation, mentioning examples such as speech recognition and language translation.

We also noticed that not all models followed the prompt in exactly the same way. The prompt requested three sentences, but Qwen 2.5 returned only two sentences.

To get another perspective, we also compared the answers with ChatGPT using the same prompt. ChatGPT provided a clear explanation and included examples of how AI is used in different areas, such as healthcare, education and software development. Its answer was more balanced in terms of explaining AI and giving practical examples.

Regarding response time, Gemma 3 was the fastest in our test, taking **7.53 seconds**. Llama 3.2 took **19.15 seconds**, while Qwen 2.5 took **19.05 seconds**.

These measurements were taken from one run, so response times may vary depending on the computer and whether a model needs to be loaded. We did not measure ChatGPT's response time under the same conditions because it runs through an online service rather than locally.

Overall, this project showed us how different language models can generate different answers to the same prompt. It also showed that local models can provide useful answers, while ChatGPT gave a more balanced response in our comparison.