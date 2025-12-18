import requests
import sys
import threading
import time

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"

spinner_running = False

def spinner():
    """Display a simple spinner while waiting for response."""
    while spinner_running:
        for cursor in '|/-\\':
            print(f'\rThinking... {cursor}', end='', flush=True)
            time.sleep(0.1)

def generate_response(prompt):
    global spinner_running
    spinner_running = True

    # Start spinner thread
    spin_thread = threading.Thread(target=spinner)
    spin_thread.start()

    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False  # Full response returned at once
        }

        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        data = {"response": None}
        print(f"\nError connecting to Ollama: {e}")
        print("Make sure Ollama is running and the model is available.")
    except Exception as e:
        data = {"response": None}
        print(f"\nUnexpected error: {e}")
    finally:
        spinner_running = False
        spin_thread.join()

    print("\r", end='')  # Clear spinner line
    print("\nLlama says:\n")
    print(data.get("response", "No response returned."))

if __name__ == "__main__":
    print("Welcome to Llama CLI! Type 'exit' to quit.")
    while True:
        user_prompt = input("\nYou: ")
        if user_prompt.lower() in ['exit', 'quit']:
            print("Exiting Llama CLI. Goodbye!")
            break
        if user_prompt.strip() == '':
            continue
        generate_response(user_prompt)
