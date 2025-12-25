code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_qJ4F1Jo8Bq14y29orQRQkrqg, 'r') as f:
    books = json.load(f)
with open(var_call_1EiTdmJPTfEaWlGLXmAFNYD8, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Extract publication year from details text using regex for a 4-digit year between 1800-2099
# Heuristics: look for patterns like 'on <Month> <day>, <year>' or ', <year>' after 'published' / 'edition' / 'released'

year_pattern = re.compile(r'(18|19|20)\d{2}')

def extract_year(details):
    if not isinstance(details, str):
        return None
    years = [int(y) for y in year_pattern.findall(details) if isinstance(y, str)]
    # year_pattern with groups returns tuples; adjust:"""

env_args = {'var_call_qJ4F1Jo8Bq14y29orQRQkrqg': 'file_storage/call_qJ4F1Jo8Bq14y29orQRQkrqg.json', 'var_call_RLFj9UEJnUcn9qFYtMEQTzax': ['books_info'], 'var_call_59tfr1G4noKhzllw786wceGj': ['review'], 'var_call_1EiTdmJPTfEaWlGLXmAFNYD8': 'file_storage/call_1EiTdmJPTfEaWlGLXmAFNYD8.json'}

exec(code, env_args)
