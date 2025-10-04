from logger import logger  
def genai_fallback(query, context=None):
    """
    Mock Generative AI fallback.
    Simulates an LLM-style friendly response.
    """
    response = (
        f"I couldn't find the exact answer in the documents. "
        f"However, based on general loan practices, {query.lower()} "
        f"typically depends on the lender's specific terms and policies."
    )
    

    logger.info(f"GENAI FALLBACK INVOKED")
    logger.info(f"QUERY: {query}")
    logger.info(f"CONTEXT: {context if context else 'None'}")
    logger.info(f"FALLBACK RESPONSE: {response}")
    
    return response
