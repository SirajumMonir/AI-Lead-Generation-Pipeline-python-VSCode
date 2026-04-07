🚀 AI Automation & ETL Data Pipeline

An end-to-end automated lead generation system featuring a dual-architecture approach. This project demonstrates both a No-Code AI Agent workflow (n8n) and a Custom Python ETL script to extract, process, and store business data using Large Language Models and Search APIs.

🧠 Project Architecture

This project is divided into two distinct pipelines to showcase versatility in automation:

1. The Autonomous AI Agent (n8n)

A cloud-based AI workflow that acts as an autonomous assistant.

Trigger: Telegram Bot (User inputs a target business).

Brain: Groq / Llama 3 (AI Agent makes routing and extraction decisions).

Tools: SerpAPI (for live web search).

Database: Google Sheets (Connected via Google Cloud Service Account).

Engineering Highlights: * Bypassed native n8n schema validation bugs by decoupling the Google Sheets node and parsing raw AI outputs using custom JavaScript expressions (JSON.parse($json.output)).

Implemented conditional IF nodes to handle AI hallucinations gracefully without crashing the pipeline.

2. Python Batch-Processing ETL Pipeline (Local)

A secure, local Python script designed for bulk data extraction.

Input: Reads target businesses from an input_leads.csv file using pandas.

Processing: Iterates through the list, dynamically generating search queries and interacting with the SerpAPI via the requests library.

Error Handling: Utilizes robust try...except blocks to handle missing JSON keys and nested API data structures smoothly.

Output: Appends cleaned and formatted data into a local leads_database.csv file.

🛠️ Tech Stack & Tools Used

Automation: n8n, Telegram API

Language: Python 3.11

Libraries: requests, pandas, python-dotenv, time, os

APIs: Google Sheets API, SerpAPI

LLM: Meta Llama 3 (via Groq)

💻 Local Installation (Python Pipeline)

Clone the repository:

git clone [https://github.com/your-username/ai-lead-generation-pipeline.git](https://github.com/your-username/ai-lead-generation-pipeline.git)


Create and activate a virtual environment:

python -m venv ai_env
ai_env\Scripts\activate


Install required dependencies:

pip install requests pandas python-dotenv


Create a .env file in the root directory and add your API key:

SERPAPI_KEY=your_api_key_here


Run the script:

python main.py


🎯 Key Competencies Demonstrated

Workflow Automation & API Integration

Edge-case handling in AI tool calls

Data extraction, transformation, and loading (ETL)

Secure environment variable management

Developed as part of my journey to master AI Automation and Backend Engineering.
