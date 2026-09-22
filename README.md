# Prompt Evaluator

A lightweight Streamlit application that helps users assess the quality of an AI prompt before using it in production. The app sends the prompt to a Gemini model, which evaluates it across key quality dimensions and returns actionable feedback.

## What the project does

Prompt Evaluator is a simple prompt-analysis tool for developers, prompt engineers, and AI teams who want a quick, structured review of a prompt. Instead of manually judging clarity, specificity, context, completeness, and expected output, the app does it automatically.

The workflow is intentionally simple:

1. A user enters a prompt in the Streamlit UI.
2. The backend builds a structured evaluation prompt.
3. A Gemini model scores the prompt and explains strengths, weaknesses, and improvements.
4. The app displays the evaluation result to the user.

## Why the project is useful

This project is useful for anyone iterating on AI prompts, especially when trying to improve reliability and output quality.

### Key features

- Prompt quality scoring from 1 to 10
- Evaluation across five criteria:
  - Clarity
  - Specificity
  - Context
  - Completeness
  - Expected Output
- Summary of strengths and weaknesses
- Suggestions for prompt improvement
- Generating an improved prompt version
- Easy-to-use web interface built with Streamlit

### Benefits

- Speeds up prompt iteration
- Improves consistency in prompt quality reviews
- Helps identify weak areas before a prompt is used in an LLM workflow
- Makes prompt evaluation more accessible to non-experts

## Project structure

```text
Prompt_Evaluator/
├── backend/
│   ├── evaluator.py
│   ├── gemini_client.py
│   ├── prompt_builder.py
│   └── test_builder.py
├── config/
│   └── setting.py
├── frontend/
│   └── app.py
├── requirements.txt
├── README.md
└── .env.example (if added locally)
```

### Main components

- `frontend/app.py` - Streamlit user interface
- `backend/evaluator.py` - top-level evaluation entry point
- `backend/prompt_builder.py` - builds the prompt sent to the model
- `backend/gemini_client.py` - calls the Google Gemini API
- `requirements.txt` - Python dependencies

## Getting started

### Prerequisites

- Python 3.10 or newer
- A Google AI API key with access to Gemini
- A local terminal or IDE with access to the project folder

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Prompt_Evaluator
```

### 2. Create and activate a virtual environment

On Windows (Command Prompt):

```bat
python -m venv myvenv
myvenv\Scripts\activate
```

On Windows (PowerShell):

```powershell
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Gemini API key

This project expects an environment variable named `GOOGLE_API_KEY`.

On Windows (Command Prompt):

```bat
set GOOGLE_API_KEY=your_api_key_here
```

On Windows (PowerShell):

```powershell
$env:GOOGLE_API_KEY = "your_api_key_here"
```

On macOS/Linux:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

You can also store it in a local `.env` file if desired, since the project loads environment values using `python-dotenv`.

### 5. Run the app

```bash
streamlit run frontend/app.py
```

Then open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## Example usage

Open the app, paste a prompt such as:

```text
Write a product launch email for a new fitness app targeted at busy professionals.
```

Then click the Evaluate Prompt button. The model returns a structured review with scores, strengths, weaknesses, suggestions, and an improved version of the prompt.

## How the app works

The backend does the following:

1. `build_evaluation_prompt()` creates a structured evaluation task.
2. `generate_response()` sends that prompt to Gemini using the Google GenAI client.
3. `evaluate_prompt()` orchestrates the full evaluation flow.

This means the frontend only needs to collect user input and display the result; the evaluation logic remains separated in the backend.

## Support and help

If you are stuck or need guidance:

- Check the project source files in this repository first.
- Review the setup steps in this README.
- Confirm that `GOOGLE_API_KEY` is set correctly before running the app.
- Open an issue in the repository if you hit a reproducible bug or want a feature request discussed.

## Contributing

Contributions are welcome. A typical contribution workflow is:

1. Fork or clone the project.
2. Create a feature branch.
3. Make focused changes with clear commit messages.
4. Run the relevant checks locally.
5. Open a pull request describing the change and its purpose.

When contributing, keep the scope narrow and make sure the README and setup instructions stay accurate.

## Maintainer information

This repository appears to be a small personal or prototype project, so no formal maintainer team is defined in the codebase. If you are using or extending the app, treat it as a collaborative project and keep updates clear and well-documented.

## License

No license file is included in the repository snapshot currently provided, so license terms should be confirmed before redistributing or publishing the project.
