from ingestion import read_interest_excel, read_loan_pdf, read_terms_pdf
from qa import answer_query
import os

from logger import logger

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

loan_pdf_path = os.path.join(PROJECT_ROOT, "docs", "loan_application.pdf")
interest_xlsx_path = os.path.join(PROJECT_ROOT, "docs", "interest_rates.xlsx")
terms_pdf_path = os.path.join(PROJECT_ROOT, "docs", "terms_conditions.pdf")

loan_data = read_loan_pdf(loan_pdf_path)
interest_df = read_interest_excel(interest_xlsx_path)
terms_text = read_terms_pdf(terms_pdf_path)

print("Loan Assistant Ready (type 'exit' to quit)")

while True:
    q = input("Q: ")
    if q.lower() in ["exit", "quit"]:
        break

    ans = answer_query(q, loan_data, interest_df, terms_text)
    print("A:", ans)

    logger.info(f"QUERY: {q}")
    logger.info(f"RESPONSE: {ans}")
