import ollama
import csv

def add_to_csv(filename, row, new=False):
    mode = 'w' if new else 'a+'
    with (open(filename, mode=mode, newline='') as file):
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row)


models = ["gemma3:1b", "llama3.2:latest"]
prompt = "Explain what artificial intelligence is in three simple sentences."

add_to_csv("results.csv", ["Model", "Prompt", "Response"], new=True)

for model in models:
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    print(model)
    print(response['message']['content'])

    add_to_csv("results.csv", [model, prompt, response['message']['content']])
