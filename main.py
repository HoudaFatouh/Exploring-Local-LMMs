import ollama
import csv
import time

def add_to_csv(filename, row, new=False):
    mode = 'w' if new else 'a+'
    with (open(filename, mode=mode, newline='') as file):
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)


models = ["gemma3:1b", "llama3.2:latest", "qwen2.5:latest"]
prompt = "Explain what artificial intelligence is in three simple sentences."

add_to_csv("results.csv", ["Model", "Prompt", "Response", "Response time (seconds)"], new=True)

for model in models:
    start = time.perf_counter()

    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

    end = time.perf_counter()
    elapsed_time = end - start

    print(model)
    print(response['message']['content'])
    print(f"Response time: {elapsed_time:.2f} seconds")

    add_to_csv("results.csv", [model, prompt, response['message']['content'], round(elapsed_time, 2)])