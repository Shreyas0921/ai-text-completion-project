# Generative AI Text Completion App (GPT-3.5)

This Python-based terminal application interacts with OpenAI’s GPT-3.5 model to generate text based on user input. It allows users to explore AI-generated completions using prompts of their choice, and supports multiple requests in a session. The app is useful for creative, educational, or experimental purposes.

## Features

- Real-time interaction with OpenAI’s GPT-3.5
- Handles multiple user prompts in one session
- Includes basic input validation (e.g., prevents empty prompts)
- Configurable temperature and max token settings
- Lightweight and easy to run locally

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/generative-ai-text-app.git
cd generative-ai-text-app
```

### 2. Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install openai python-dotenv
```

### 4. Add Your API Key

1. Create a `.env` file in the project directory.
2. Inside `.env`, add:

```
OPENAI_API_KEY=your-api-key-here
```

> 🔐 Keep this file private and never upload your API key to public repositories.

## Usage

To start the app:

```bash
python app.py
```

You will be prompted to enter a message. After submitting a prompt, the app will return a generated response from GPT-3.5.

To exit the app, type:

```
exit
```

## Example Prompts

Try any of these:

- `Hello`
- `Continue this story: Once upon a time...`
- `Explain photosynthesis to a 10-year-old.`
- `Write a haiku about the ocean.`
- `Tell me about the history of the English language.`

## Default Settings

- **Model**: `gpt-3.5-turbo`
- **Temperature**: `0.7`
- **Max Tokens**: `100`

You can change these defaults directly in the `generate_response()` function in `app.py`.

## Dependencies

- `openai`: Connects to the GPT-3.5 API
- `python-dotenv`: Loads environment variables from the `.env` file

Install both with:

```bash
pip install openai python-dotenv
```

## Limitations

- The model may generate off-topic, repetitive, or incorrect responses.
- Responses can reflect biases present in training data.
- Not suitable for critical use without human oversight.

