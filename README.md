# AI Text Summarizer

A Python project that uses **OpenAI GPT** to summarize long text into concise summaries.  
Ideal for quickly understanding articles, notes, or any long paragraphs.

---

## Features

- 🎨 **Modern Web Interface** - Beautiful, responsive UI built with Flask
- 🤖 **AI-Powered** - Uses OpenAI GPT for intelligent summarization
- 📏 **Adjustable Length** - Choose between short, medium, or long summaries
- 📊 **Statistics** - See character count and reduction percentage
- 📋 **Copy to Clipboard** - Easy one-click copy functionality
- 💻 **CLI Support** - Command-line interface still available via `main.py`

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ankitmodanwall/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

---

## Usage

### Web Interface (Recommended)

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and navigate to:

```
http://localhost:5000
```

3. Enter your text, choose summary length, and click "Summarize Text"!

### Command Line Interface

Run the CLI version:

```bash
python main.py
```

Follow the prompts to enter text and choose summary length.

---

## Project Structure

```
ai-text-summarizer/
├── app.py                 # Flask web application
├── main.py               # CLI version
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .env.example         # Example environment file
├── templates/
│   └── index.html       # Web interface HTML
└── static/
    ├── style.css        # Styling
    └── script.js        # Frontend JavaScript
```

---

## Technologies Used

- **Python 3.x**
- **OpenAI API** - GPT models for text summarization
- **Flask** - Web framework
- **HTML/CSS/JavaScript** - Frontend interface
- **python-dotenv** - Environment variable management

---

## Summary Length Options

- **Short**: 1-2 sentences - Quick overview
- **Medium**: 3-4 sentences - Balanced summary (default)
- **Long**: 6-8 sentences - Detailed summary

---

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## License

See [LICENSE.md](LICENSE.md) for details.

---

## Troubleshooting

**Issue**: "OpenAI API key not configured"
- Make sure you created a `.env` file with your API key

**Issue**: "Module not found"
- Run `pip install -r requirements.txt` to install dependencies

**Issue**: Port 5000 already in use
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

---

Built with ❤️ using OpenAI GPT
