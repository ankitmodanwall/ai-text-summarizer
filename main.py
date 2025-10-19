import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("❌ Error: Missing API key! Set OPENAI_API_KEY in your .env file.")
    exit()

def summarize_text(text, detail_level="medium"):
    """Summarizes input text using OpenAI GPT model with adjustable detail level"""
    
    # 👇 Customize prompt based on desired summary length
    if detail_level == "short":
        prompt = f"Summarize this text in 1-2 sentences:\n{text}"
    elif detail_level == "long":
        prompt = f"Summarize this text in 6-8 sentences:\n{text}"
    else:
        prompt = f"Summarize this text in 3-4 sentences:\n{text}"

    try:
        response = openai.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": prompt}
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

        # 👇 Ask user for summary detail level
        detail_level = input("Choose summary length (short / medium / long): ").strip().lower()
        if detail_level not in ["short", "medium", "long"]:
            print("Invalid choice. Using default: medium.")
            detail_level = "medium"

        summary = summarize_text(text, detail_level)
        print("\n--- ✨ Summary ---")
        print(summary)

if __name__ == "__main__":
    main()
``
