# ai-agent

An AI research agent that answers your question. It searches the web (DuckDuckGo) and Wikipedia, writes a short report, and saves it to `research_output.txt`.

Technology used: Python, LangChain, and free LLMs from OpenRouter or Groq

## Requirements

- Python 3.10 or newer
- A free API key from [OpenRouter](https://openrouter.ai) (recommended) or [Groq](https://console.groq.com)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/stevenlu0830/ai-agent.git
   cd ai-agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate it with `.venv\Scripts\activate` instead.

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Get a free API key (no credit card needed):
   - **OpenRouter:** sign up at [openrouter.ai](https://openrouter.ai), then create a key at [openrouter.ai/keys](https://openrouter.ai/keys). It starts with `sk-or-v1-`.
   - **Groq:** create a key at [console.groq.com/keys](https://console.groq.com/keys). It starts with `gsk_`.

5. Create a file named `.env` in the project folder and add your key:

   ```bash
   echo 'OPENROUTER_API_KEY="sk-or-v1-your-key-here"' > .env
   ```

   If you use Groq instead, write `GROQ_API_KEY="gsk_your-key-here"` to `.env`. When both keys are set, OpenRouter is used. Git ignores `.env`, so your key stays out of the repository.

   Optional settings for `.env`:

   | Variable | Default | What it does |
   |---|---|---|
   | `OPENROUTER_MODEL` | `openrouter/free` | Model to use on OpenRouter. The default picks a free model that supports tool calling. |
   | `GROQ_MODEL` | `openai/gpt-oss-120b` | Model to use on Groq. |

## Usage

Activate the virtual environment (once per new terminal) and run the agent:

```bash
source .venv/bin/activate
python main.py
```

Type your question when prompted:

```
Enter your research query: What does a human cell consist of?
```

The agent prints each tool it uses, then the final report. Each run's question and report are added to the end of `research_output.txt`, which is created automatically. Git ignores this file.

## Free tier limits

OpenRouter's free models allow 20 requests per minute and 50 per day, or 1,000 per day after a one-time purchase of $10 of credits. One question usually takes 3–5 requests.

## Troubleshooting

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | Activate the virtual environment and run `pip install -r requirements.txt`. |
| `No API key found` | Create `.env` with your key (setup step 5) and save the file. |
| `404 ... No endpoints found matching your data policy` (OpenRouter) | Allow free models at [openrouter.ai/settings/privacy](https://openrouter.ai/settings/privacy). |
| `403 Forbidden` (Groq) | Groq isn't available on your network or in your region. Use OpenRouter instead. |
| `429` | You hit a rate limit. Wait a minute, or until the next day if you used up the daily limit. |
