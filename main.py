import os
import openai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("❌ Error: Missing API key! Set OPENAI_API_KEY in your .env file.")
    exit()

def summarize_text(text):
    """Summarizes input text using OpenAI GPT model"""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize this text in 3-4 sentences:\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error during summarization: {e}"

def main():
    print("=== 🧠 AI Text Summarizer ===")
    while True:
        text = input("\nEnter text to summarize (or type 'exit' to quit):\n")
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break
        summary = summarize_text(text)
        print("\n--- ✨ Summary ---")
        print(summary)

if __name__ == "__main__":
    main()
