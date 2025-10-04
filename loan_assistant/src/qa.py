from typing import Dict
from genai_fallback import genai_fallback
from logger import logger 

def answer_query(query: str, loan_data: Dict, interest_df, terms_text: str) -> str:
    """
    Answers user queries based on structured and unstructured data.
    Falls back to mock Generative AI if no match found.
    """
    q = query.lower()
    response = None

    if "loan amount" in q:
        response = f"Requested amount: {loan_data.get('Requested Loan Amount', 'Not available')}"
    elif "applicant name" in q:
        response = f"Applicant: {loan_data.get('Applicant Name', 'Not available')}"
    elif "tenure" in q:
        response = f"Tenure: {loan_data.get('Tenure (Years)', 'Not available')} years"

    elif "interest rate" in q:
        for _, row in interest_df.iterrows():
            tenure_str = str(row["Tenure (Years)"]).lower()
            if tenure_str in q:
                rate = row["Interest Rate (%)"]
                response = f"Interest rate for {row['Tenure (Years)']} years: {rate}%"
                break
        if response is None:
            response = "Interest rate information not found for the requested tenure."

    elif any(keyword in q for keyword in ["penalty", "delay", "repayment", "prepayment", "default"]):
        lower_terms = terms_text.lower()
        lines = [
            line
            for line in lower_terms.split("\n")
            if any(k in line for k in q.split())
        ]
        if lines:
            snippet = lines[0][:300]
            response = f"From Terms & Conditions:\n{snippet.strip()}"


    if response is None:
        response = genai_fallback(query)

    logger.info(f"QUERY: {query}")
    logger.info(f"RESPONSE: {response}")

    return response
