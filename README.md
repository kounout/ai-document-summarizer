# AI Document Summarizer

An interactive web application built with Python and Streamlit that uses Google Gemini to generate concise summaries from raw text or uploaded PDF documents.

## Why I Built This
Reading through long papers, articles, or reports can be time-consuming. I built this app to quickly distill documents into clear summaries while maintaining a clean, distraction-free user interface. It handles both direct text inputs and multi-page PDFs, with a built-in download feature for saving generated summaries.

## Core Features
- **Dual Input Options:** Summarize text pasted directly into the browser or process uploaded `.pdf` files.
- **PDF Parsing:** Automatically extracts text from uploaded PDF documents page-by-page.
- **Instant Export:** Allows users to download generated summaries directly as a text file.
- **Secure API Integration:** Manages API credentials using environment variables to keep keys safe.

## Tech Stack
- **Interface:** [Streamlit](https://streamlit.io/)
- **AI/LLM:** Google Gemini API (`google-genai` SDK)
- **PDF Extraction:** `pypdf`
- **Environment Management:** `python-dotenv`

## Getting Started

### Prerequisites
- Python 3.9+ installed on your system.
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kounout/ai-document-summarizer.git
   cd ai-document-summarizer
