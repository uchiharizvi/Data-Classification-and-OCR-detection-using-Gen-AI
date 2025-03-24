import PyPDF2
import os
import logging

logger = logging.getLogger("attachements")

def extract_attachments(uploaded_file):
    extracted_texts = ""
    if uploaded_file.name.__contains__(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            text += page_obj.extract_text()
    else:
        text = None
        
    if text is not None:
        logger.info("Attachment Parsed succesfully")
        extracted_texts = text
    return extracted_texts