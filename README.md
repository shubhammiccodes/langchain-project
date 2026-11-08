# LangChain Project

A hands-on LangChain learning repository covering model integration, streaming, batching, tools, messages, and agents. The examples are provided as Jupyter notebooks in [`langchain-code-directory/`](./langchain-code-directory/).

## Requirements

- Python 3.14 or newer
- An API key for the cloud provider used by an example, or a local [Ollama](https://ollama.com/) installation
- [uv](https://docs.astral.sh/uv/) recommended, although `pip` can also be used

## Setup

Clone the repository and create an environment:

```bash
git clone https://github.com/shubhammiccodes/langchain-project.git
cd langchain-project
uv sync
```

Activate the environment if you want to run commands manually:

```bash
source .venv/bin/activate
```

Alternatively, install the declared dependencies with pip:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install ipykernel
```

## Configure environment variables

Create a `.env` file in the repository root. Add only the credentials required by the notebook you are running:

```dotenv
# Google Gemini examples
GOOGLE_API_KEY=your-google-api-key

# Groq examples
GROQ_API_KEY=your-groq-api-key

# Optional defaults used by config.py
MODEL_PROVIDER=ollama
MODEL=llama3.2:3b
```

`.env` is ignored by Git. Never commit API keys or other secrets.

For Ollama examples, install and start Ollama separately, then download the model configured in `.env`:

```bash
ollama pull llama3.2:3b
```

If you select another local model, set its name in `MODEL` before starting the notebook.

## Run the notebooks

Start Jupyter from the project root:

```bash
uv run jupyter lab
```

Open the notebooks in this order:

| Notebook | Topics |
| --- | --- |
| [`1-langchaindemo-intro.ipynb`](./langchain-code-directory/1-langchaindemo-intro.ipynb) | LangChain introduction and agent basics |
| [`2-llm-integration.ipynb`](./langchain-code-directory/2-llm-integration.ipynb) | Connecting LangChain to language models |
| [`3-streaming-&-batch.ipynb`](./langchain-code-directory/3-streaming-%26-batch.ipynb) | Streaming responses and batch requests |
| [`4-tools.ipynb`](./langchain-code-directory/4-tools.ipynb) | Defining and using tools |
| [`5-messages.ipynb`](./langchain-code-directory/5-messages.ipynb) | LangChain message types and conversations |

Select the project’s Python environment as the notebook kernel. Run cells from top to bottom and make sure the relevant provider credentials or local model are available first.

## Command-line entry point

The package currently exposes a small example command:

```bash
uv run langchain-project
```

It prints a greeting. The main learning examples currently live in the notebooks rather than in the command-line package.

## Project layout

```text
.
├── config.py                       # Loads .env and model defaults
├── langchain-code-directory/       # Learning notebooks
├── src/langchain_project/          # Python package
├── pyproject.toml                  # Project metadata and dependencies
├── requirements.txt                # pip dependency list
└── uv.lock                         # Locked uv dependency versions
```

## Troubleshooting

- **Missing API key:** confirm the variable name matches the provider and restart the notebook kernel after changing `.env`.
- **Ollama connection error:** make sure the Ollama application/service is running and that the configured model has been pulled.
- **Import errors:** run `uv sync` or reinstall the dependencies inside the active virtual environment.

## License

No license has been specified for this repository yet.
