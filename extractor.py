# extractor.py
import re

def extract_upi(text: str):
    return re.findall(r'[\w.\-]+@[\w]+', text)

def extract_bank_accounts(text: str):
    return re.findall(r'\b\d{9,18}\b', text)

def extract_links(text: str):
    return re.findall(r'https?://\S+', text)
