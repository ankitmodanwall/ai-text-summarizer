import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def summarize_text(text, detail_level="medium"):
    """Summarizes input text using OpenAI GPT model with adjustable detail level"""
    
    if detail_level == "short":
        prompt = f"Summarize this text in 1-2 sentences:\n{text}"
    elif detail_level == "long":
        prompt = f"Summarize this text in 6-8 sentences:\n{text}"
    else:
        prompt = f"Summarize this text in 3-4 sentences:\n{text}"

    try:
        response = openai.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during summarization: {str(e)}"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    """API endpoint for text summarization"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        detail_level = data.get('detail_level', 'medium')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        if not openai.api_key:
            return jsonify({'error': 'OpenAI API key not configured'}), 500
        
        summary = summarize_text(text, detail_level)
        
        return jsonify({
            'success': True,
            'summary': summary,
            'original_length': len(text),
            'summary_length': len(summary)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not openai.api_key:
        print("❌ Warning: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
