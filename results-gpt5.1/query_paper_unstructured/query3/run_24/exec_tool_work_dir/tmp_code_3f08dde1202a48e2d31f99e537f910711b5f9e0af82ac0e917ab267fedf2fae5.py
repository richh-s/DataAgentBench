code = """import re, json, pandas as pd
from datetime import datetime

# Load full mongo and citations results
with open(var_call_olLcGzpHLt5tCj2TGPDJyEMn, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_NdiSsuuSfkiGchj4B88O5KCF, 'r') as f:
    citation_records = json.load(f)

# Helper to extract year from text
year_pattern = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text)]
    # year_pattern.findall with groups returns tuples; handle that

# fix: recompile and use finditer"""

env_args = {'var_call_olLcGzpHLt5tCj2TGPDJyEMn': 'file_storage/call_olLcGzpHLt5tCj2TGPDJyEMn.json', 'var_call_NdiSsuuSfkiGchj4B88O5KCF': 'file_storage/call_NdiSsuuSfkiGchj4B88O5KCF.json'}

exec(code, env_args)
