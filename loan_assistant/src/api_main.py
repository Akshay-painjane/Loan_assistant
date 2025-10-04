from fastapi import FastAPI
from ingestion import read_interest_excel, read_loan_pdf, read_terms_pdf
from qa import answer_query
import os
from logger import logger

app = FastAPI()

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

loan_pdf_path = os.path.join(PROJECT_ROOT, "docs", "loan_application.pdf")
interest_xlsx_path = os.path.join(PROJECT_ROOT, "docs", "interest_rates.xlsx")
terms_pdf_path = os.path.join(PROJECT_ROOT, "docs", "terms_conditions.pdf")

loan_data = read_loan_pdf(loan_pdf_path)
interest_df = read_interest_excel(interest_xlsx_path)
terms_text = read_terms_pdf(terms_pdf_path)

@app.get("/query")
def ask(query: str):
    answer = answer_query(query, loan_data, interest_df, terms_text)
  
    logger.info(f"QUERY: {query}")
    logger.info(f"RESPONSE: {answer}")
    
    return {"answer": answer}