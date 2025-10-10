import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: Missing API key! Set OPENAI_API_KEY in your .env file.")
    exit()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def summarize_text(text):
    """Summarizes input text using GPT-5"""
    response = client.responses.create(
        model="gpt-5",
        input=f"Summarize this text in 3-4 sentences:\n{text}"
    )
    return response.output_text

def main():
    print("=== AI Text Summarizer ===")
    while True:
        text = input("\nEnter text to summarize (or 'exit' to quit):\n")
        if text.lower() == "exit":
            print("Goodbye!")
            break
        summary = summarize_text(text)
        print("\n--- Summary ---")
        print(summary)

if __name__ == "__main__":
    main()
