import pandas as pd
from PyPDF2 import PdfReader
from logger import logger  

def read_loan_pdf(path):
    try:
        logger.info(f"Reading Loan PDF: {path}")
        reader = PdfReader(path)
        first_page = reader.pages[0]
        text = first_page.extract_text()
        data = {}
        for line in text.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        logger.info(f"Successfully read Loan PDF: {path}")
        return data
    except Exception as e:
        logger.error(f"Failed to read Loan PDF: {path} | Error: {e}")
        raise

def read_interest_excel(path):
    try:
        logger.info(f"Reading Interest Excel: {path}")
        df = pd.read_excel(path)
        logger.info(f"Successfully read Interest Excel: {path}")
        return df
    except Exception as e:
        logger.error(f"Failed to read Interest Excel: {path} | Error: {e}")
        raise

def read_terms_pdf(path):
    try:
        logger.info(f"Reading Terms PDF: {path}")
        reader = PdfReader(path)
        all_text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                all_text.append(page_text)
        text = "\n".join(all_text)
        logger.info(f"Successfully read Terms PDF: {path}")
        return text
    except Exception as e:
        logger.error(f"Failed to read Terms PDF: {path} | Error: {e}")
        raise
