# AI Resume Tailoring Tool

An AI-powered tool that analyzes a resume against a job description,
identifies skill gaps, computes semantic similarity, and generates a
tailored resume aligned with the role.

The application uses LLMs for structured information extraction and
rewriting, along with semantic embeddings to evaluate skill alignment
between resumes and job descriptions.

The interface is built with **Streamlit**, allowing users to upload a
resume, paste a job description, and receive a structured analysis along
with an AI‑tailored version of the resume.

------------------------------------------------------------------------

# Live Application

The deployed application can be accessed here:

https://resume-tailor-ai-tool.streamlit.app/

------------------------------------------------------------------------

# Project Structure

    ai-resume-tailor/
    │
    ├── app.py
    │
    ├── utils/
    │   ├── parser.py
    │   ├── jd_analyzer.py
    │   ├── resume_analyzer.py
    │   ├── matcher.py
    │   ├── skill_gap.py
    │   ├── tailor.py
    │   └── llm.py
    │
    ├── requirements.txt
    └── README.md

-----------------------------------------------------------------------

**File roles**

  `app.py`: Streamlit interface

  `parser.py`: Extracts text from PDF resumes

  `jd_analyzer.py`: Extracts structured information from job descriptions

  `resume_analyzer.py`: Extracts structured information from resumes

  `matcher.py`: Computes semantic similarity score

  `skill_gap.py`: Identifies matched and missing skills

  `tailor.py`: Generates tailored resume output

  `llm.py`: LLM interface (Gemini)

------------------------------------------------------------------------

# Architecture

The tool follows a modular pipeline separating extraction, analysis, and
generation.

    Resume PDF
         ↓
    parser.py
         ↓
    resume_analyzer.py
         ↓
    jd_analyzer.py
         ↓
    matcher.py        → Similarity Score
         ↓
    skill_gap.py      → Matched / Missing Skills
         ↓
    tailor.py         → Resume Rewriting
         ↓
    Streamlit UI

------------------------------------------------------------------------

# Tech Stack

**Frontend / Interface** - Streamlit

**AI / LLM** - Gemini API

**NLP & Semantic Matching** - Sentence Transformers - MiniLM embeddings

**Supporting Libraries** - Scikit-learn - PDFPlumber - Python Dotenv

------------------------------------------------------------------------

# Installation

## 1. Clone the repository

``` bash
git clone https://github.com/sjha132000/ai-resume-tailor.git
cd ai-resume-tailor
```

------------------------------------------------------------------------

## 2. Create a virtual environment

``` bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

``` bash
.venv\Scripts\activate
```

------------------------------------------------------------------------

## 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 4. Environment setup

### Gemini

Create a `.env` file in the root directory and add API key:

``` bash
GEMINI_API_KEY=your_api_key_here
```

------------------------------------------------------------------------

## 5. Run the application

``` bash
streamlit run app.py
```

The application will launch locally at:

    http://localhost:8501
