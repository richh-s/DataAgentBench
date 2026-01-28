code = """import json
import pandas as pd
import re
from datetime import datetime

# Helper function to extract CPC level 4 codes
def get_cpc_level_4(code):
    if not code:
        return None
    main_part = code.split('/')[0]
    clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
    return clean_part

# Helper function to parse flexible date formats
def parse_date(date_str):
    if not date_str or pd.isna(date_str):
        return None
    
    date_str = str(date_str).lower().strip()
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    date_str = re.sub(r'(\d+)\s*(st|nd|rd|th)', r'\1', date_str)
    
    patterns = [
        (r'([a-z]+)\s+(\d+),\s+(\d{4})', '%B %d, %Y'),
        (r'([a-z]+)\s+(\d+)\s+(\d{4})', '%B %d %Y'),
        (r'(\d+)\s+([a-z]+)\s+(\d{4})', '%d %B %Y'),
        (r'(\d{4})\s+([a-z]+)\s+(\d+)', '%Y %B %d'),
        (r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', '%Y-%m-%d'),
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', '%m/%d/%Y'),
    ]
    
    for pattern, fmt in patterns:
        match = re.search(pattern, date_str)
        if match:
            try:
                extracted_date = match.group(0)
                return datetime.strptime(extracted_date, fmt)
            except:
                continue
    
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        try:
            year = int(year_match.group(1))
            if 1900 <= year <= 2100:
                return datetime(year, 1, 1)
        except:
            pass
    
    return None

print('__RESULT__:')
print(json.dumps('Date parsing and CPC level 4 extraction functions ready'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
