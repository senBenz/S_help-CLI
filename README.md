# S_Help CLI

**S_Help CLI** is an interactive command-line tool that allows you to chat with a locally running Llama AI model. It provides a fast and simple way to send prompts to the model and receive intelligent responses directly in your terminal.

---

## Features

- 💬 **Fully interactive chat** with your AI model
- ⏳ **"Thinking…" spinner animation** while the AI generates a response
- 🖥️ **Runs locally** using the Llama 3 model via Ollama
- 🚀 **Easy to invoke** from any terminal after installation
- 📦 **Minimal dependencies**: Python 3 and the `requests` library

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Requirements](#requirements)
- [Example Session](#example-session)
- [Development](#development)
- [Workflow Overview](#workflow-overview)
- [License](#license)

---

## Installation

### 1. Clone or navigate to your project folder

```bash
git clone https://github.com/senBenz/S_help-CLI
cd S_help-CLI
```

### 2. Ensure Python 3 is installed

```bash
python3 --version
```

If Python 3 is not installed, download it from [python.org](https://www.python.org/downloads/).

### 3. Install required dependencies

```bash
pip install requests
```

### 4. Make the script executable

```bash
chmod +x S_Help
```

### 5. (Optional) Move to a system PATH directory for global access

To run `S_Help` from anywhere in your terminal:

```bash
sudo mv S_Help /usr/local/bin/
```

Now you can invoke the CLI from any directory by simply typing `S_Help`.

---

## Usage

### Running the CLI

```bash
S_Help
```

### Interactive Chat

Once you run the command, you'll see:

```
Welcome to S_Help CLI! Type 'exit' to quit.

You: 
```

- **Type your prompt** and press Enter
- The CLI displays a **"Thinking…" spinner** while the AI processes your request
- Once ready, the **AI's response** appears
- Continue chatting or type `exit` or `quit` to close the CLI

### Example

```
You: Tell me a joke!
Thinking… /
Llama says:
Why did the computer go to the doctor? Because it caught a virus!

You: Explain recursion in simple words.
Thinking… -
Llama says:
Recursion is when a function calls itself to solve a problem in smaller steps. 
It's like looking into a mirror that reflects another mirror.

You: exit
Exiting S_Help CLI. Goodbye!
```

---

## Configuration

You can customize the CLI by editing the script:

### Change the AI Model

Modify the model name in the script:

```python
MODEL_NAME = "llama3:latest"  # Change to your preferred model
```

### Change the API Endpoint

If your Ollama instance runs on a different host or port:

```python
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"  # Update as needed
```

---

## Requirements

- **Python 3.7+**
- **`requests` library** (`pip install requests`)
- **Ollama CLI** installed and running
- **Llama 3 model** pulled locally via Ollama

### Installing Ollama and Pulling the Model

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the Llama 3 model:

```bash
ollama pull llama3
```

3. Verify Ollama is running:

```bash
ollama list
```

---

## Example Session

```bash
$ S_Help
Welcome to S_Help CLI! Type 'exit' to quit.

You: What is artificial intelligence?
Thinking… |
Llama says:
Artificial intelligence (AI) is the simulation of human intelligence in machines 
that are programmed to think and learn like humans. It involves creating systems 
that can perform tasks requiring human-like reasoning, problem-solving, and decision-making.

You: Give me a python code example
Thinking… \
Llama says:
Here's a simple Python function to calculate factorial:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

You: exit
Exiting S_Help CLI. Goodbye!
```

---

## Development

### Creating a Development Copy

To safely test changes without affecting the main CLI:

```bash
cp S_Help S_Help_dev
chmod +x S_Help_dev
./S_Help_dev
```

### Project Structure

```
S_help-CLI/
├── S_Help          # Main executable script
├── README.md       # Documentation
└── LICENSE         # MIT License
```

---

## Workflow Overview

```
┌─────────────────────────────────────────────┐
│ User opens terminal and runs: S_Help        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ CLI displays welcome message                │
│ "Welcome to S_Help CLI! Type 'exit' to quit"│
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ User enters prompt                          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ CLI shows "Thinking…" spinner               │
│ Sends prompt to Ollama API                  │
│ (http://localhost:11434/api/generate)       │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ Llama 3 model processes prompt              │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ CLI stops spinner and displays response     │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ User can:                                   │
│ • Enter another prompt                      │
│ • Type 'exit' to quit                       │
└─────────────────────────────────────────────┘
```

---

## Troubleshooting

### Common Issues

**1. "Connection refused" error**
- Ensure Ollama is running: `ollama serve`
- Check if the model is pulled: `ollama list`

**2. "Module not found" error**
- Install requests: `pip install requests`

**3. CLI not found after moving to /usr/local/bin/**
- Verify PATH includes `/usr/local/bin`: `echo $PATH`
- Try using the full path: `/usr/local/bin/S_Help`

**4. Permission denied**
- Make the script executable: `chmod +x S_Help`

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** - you are free to use, modify, and distribute this software.

---

## Author

Created by [senBenz](https://github.com/senBenz) @SAAD AAQIL 

---

## Acknowledgments

- Built with [Ollama](https://ollama.ai)
- Powered by [Llama 3](https://ai.meta.com/llama/)
- Python `requests` library

---

