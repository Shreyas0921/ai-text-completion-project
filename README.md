# GPT-2 Text Generator (Hugging Face Local Model)

This is a simple Python application that uses the Hugging Face `transformers` library to load a local GPT-2 model (`openai-community/gpt2`) and generate text based on user-provided prompts. The app runs in the terminal and returns AI-generated responses using configurable generation settings.

---

## ✨ Features

- Uses a local Hugging Face GPT-2 model (no API key required)
- Real-time prompt-based text generation
- Adjustable `temperature` and `max_tokens` parameters
- Interactive command-line interface
- Includes basic input validation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gpt2-text-generator.git
cd gpt2-text-generator
```

### 2. Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install transformers
```

> Note: The first time you run the script, the `openai-community/gpt2` model will automatically download from Hugging Face.

---

## 🚀 Usage

To run the app:

```bash
python app.py
```

### Example Session:
```text
Welcome to the GPT-2 Text Generator!

Enter a prompt (or type 'exit' to quit): The future of AI is
Generated Text:
The future of AI is rapidly evolving, and it has the potential to...
```

To exit the application, type:
```
exit
```

---

## 🔧 Default Configuration

- **Model:** `openai-community/gpt2`
- **Max Tokens:** 50
- **Temperature:** 0.5  
  (Higher values = more randomness; lower = more focused/predictable)

These can be adjusted in the `generate_text()` function inside `app.py`.

---

## 📋 Dependencies

- `transformers` – Hugging Face library for accessing pretrained models

Install via:

```bash
pip install transformers
```

---

.
