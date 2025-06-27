from transformers import pipeline

# Load the text-generation pipeline using a local Hugging Face model
pipe = pipeline("text-generation", model="openai-community/gpt2")

def generate_text(prompt, max_tokens=50, temperature=0.5):
    try:
        output = pipe(prompt, max_new_tokens=max_tokens, do_sample=True, temperature=temperature)
        return output[0]["generated_text"]
    except Exception as e:
        return f"Error: {e}"

# Simple interactive loop
if __name__ == "__main__":
    print("Welcome to the GPT-2 Text Generator!")
    while True:
        prompt = input("\nEnter a prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        elif not prompt.strip():
            print("Prompt cannot be empty.")
        else:
            response = generate_text(prompt)
            print("\nGenerated Text:\n", response)
