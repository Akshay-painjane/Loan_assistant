Conversational Loan Assistant

A Python + GenAI Prototype for Loan Query Automation

Overview

This project implements a Conversational Loan Assistant that can answer natural-language questions about personal loan applications by reading structured and unstructured data from multiple sources:

Loan Application (PDF) → Applicant details, amount, tenur
Interest Rates (Excel) → Product variants, tenure-based rate
Terms & Conditions (PDF) → Eligibility rules, penalties, repayment policies

If the answer isn’t found in the ingested documents, the assistant uses a Generative AI Fallback (simulated) to produce a relevant response.

Core Feature
Extract structured data from loan application PDFs
Parse interest rate tables from Excel
Read and index Terms & Conditions text
Answer user questions via CLI or REST API
Fallback to simulated GenAI for unmatched queries
Logging and health-check support
Containerized for easy deployment


Description:

cli_main.py → Command-line conversational interface

api_main.py → REST API (FastAPI)

genai_fallback.py → Mock Generative AI fallback logic

ingestion.py → Document ingestion & parsing (PDF/Excel)

qa.py → Query analysis and response logic

Setup Instructions
1️. Clone the Repository
git clone https://github.com/Akshay-painjane/Loan_assistant.git
cd conversational-loan-assistant

2️ .Create a Virtual Environment
python -m venv venv
venv\Scripts\activate        # (Windows)
# or
source venv/bin/activate     # (Mac/Linux)

3️. Install Dependencies
pip install -r requirements.txt

4️. Run the Application
CLI Mode
python src/cli_main.py

API Mode (if implemented)
uvicorn api_main:app --host 0.0.0.0 --port 8000


Docker

Build the Docker image:

1.Build Docker Image
docker build -t loan-assistant .

2️.Run the CLI inside Docker
docker run -it loan-assistant
-it → interactive terminal mode for CLI chat.

Example Queries
Query	Response
What is the requested loan amount?	Requested amount: ₹5,00,000
What is the interest rate for 5 years?	Interest rate for 5 years: 12.0%
What happens if EMI is delayed?	[Extracted from T&C PDF or fallback AI response]
