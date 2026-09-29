# 🔍 Intelligent Code Reviewer & Explainer

An AI-powered application that reviews source code, finds bugs, explains the code, suggests improvements, and generates optimized code.

Built with **Python, Streamlit, and Google Gemini** as part of my **Generative AI Internship at Decode Labs**.

## ✨ Features

* Upload Python, JavaScript, or Java files
* Detect programming language
* Explain code in plain English
* Identify bugs and issues
* Suggest improvements
* Generate optimized code
* Display results with syntax highlighting
* Validate invalid and empty files

## 🏗️ Architecture

```text
User
  ↓
Streamlit UI
  ↓
File Validation & Parsing
  ↓
AI Reviewer
  ↓
Google Gemini
  ↓
Structured JSON Response
  ↓
Review Results
```

## 🔄 Workflow

```text
Upload Code
     ↓
Validate File
     ↓
Detect Language
     ↓
Send Code to Gemini
     ↓
Analyze Code
     ↓
Return Structured Results
     ↓
Display Review
```

The AI provides four main results:

1. **Code Explanation**
2. **Bugs and Issues**
3. **Suggested Improvements**
4. **Optimized Code**

## 📂 Project Structure

```text
Intelligent-Code-Reviewer/
│
├── app.py
├── ai_reviewer.py
├── prompts.py
├── parser.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ Technologies

* Python
* Streamlit
* Google Gemini
* Google GenAI SDK
* python-dotenv
* JSON

## 🚀 Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Intelligent-Code-Reviewer
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 🙏 Acknowledgment

This project was developed as part of my **Generative AI Internship at Decode Labs**.

Thank you to **Decode Labs** for providing this opportunity to gain practical experience in Generative AI and AI-powered application development.

## 👨‍💻 Author

**Abdisalam Ahmed Ali**

Generative AI Intern — Decode Labs
