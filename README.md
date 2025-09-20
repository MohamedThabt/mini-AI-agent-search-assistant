# Mini AI Agent Search Assistant

A lightweight AI-powered research assistant that uses Google's Gemini AI model to search the web, query Wikipedia, and save research results to files. This tool helps you gather information on any topic quickly and efficiently.

## Features

- **Web Search**: Uses DuckDuckGo to search for recent information on any topic
- **Wikipedia Integration**: Fetches additional context from Wikipedia articles
- **AI-Powered Analysis**: Leverages Google Gemini 1.5 Flash for intelligent research synthesis
- **File Saving**: Automatically saves research results to `research_output.txt`
- **Interactive CLI**: Simple command-line interface for easy usage

## How It Works

1. You provide a research topic or question
2. The AI agent uses DuckDuckGo to search for recent information
3. Wikipedia is queried for additional context when needed
4. The AI synthesizes the information into a comprehensive response
5. Results can be automatically saved to a text file

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd ai_agent
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirments.txt
```

### Step 4: Set Up Environment Variables

1. Create a `.env` file in the project root:

```bash
touch .env
```

2. Add your Google Gemini API key to the `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

**To get a Gemini API key:**

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and paste it in your `.env` file

### Step 5: Run the Application

```bash
python main.py
```

## Usage

1. Run the application: `python main.py`
2. Enter your research question when prompted
3. The AI will search the web and Wikipedia for information
4. Review the comprehensive research results
5. Results are automatically saved to `research_output.txt`

### Example Usage

```
What can i help you research? What is Laravel framework?

Research Results:
Laravel is a free, open-source PHP web framework, created by Taylor Otwell and intended for the development of web applications following the model–view–controller (MVC) architectural pattern...
```

## Project Structure

```
ai_agent/
├── main.py              # Main application logic and agent setup
├── tools.py             # Custom tools for search, Wikipedia, and file saving
├── requirments.txt      # Python dependencies
├── research_output.txt  # Generated research results
├── .env                 # Environment variables (API keys)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Dependencies

- **langchain**: Framework for building AI applications
- **langchain-google-genai**: Google Gemini integration
- **langchain-community**: Community tools and utilities
- **duckduckgo-search**: Web search functionality
- **wikipedia**: Wikipedia API wrapper
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation and parsing

## Configuration

The application uses the following configuration:

- **AI Model**: Google Gemini 1.5 Flash
- **Temperature**: 0 (deterministic responses)
- **Max Iterations**: 5
- **Wikipedia Results**: Top 1 result, max 100 characters
- **Output File**: `research_output.txt`

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `GEMINI_API_KEY` is correctly set in the `.env` file
2. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirments.txt`
3. **Network Issues**: Check your internet connection for web search functionality

### Getting Help

If you encounter any issues:

1. Check that your virtual environment is activated
2. Verify all dependencies are installed
3. Ensure your API key is valid and has sufficient quota
4. Check the console output for detailed error messages

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
