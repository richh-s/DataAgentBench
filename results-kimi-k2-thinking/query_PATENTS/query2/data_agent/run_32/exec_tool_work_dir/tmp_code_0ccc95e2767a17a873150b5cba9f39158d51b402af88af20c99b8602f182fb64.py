code = """import json
import pandas as pd
import re
from datetime import datetime

# Helper function to extract CPC level 4 codes
def get_cpc_level_4(code):
    """Extract CPC code up to level 4 (e.g., A61K31 from A61K31/00)"""
    if not code:
        return None
    # Split by / and take the main part before /
    main_part = code.split('/')[0]
    # Remove any non-alphanumeric characters from the end
    clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
    return clean_part

# Helper function to parse flexible date formats
def parse_date(date_str):
    """Parse various date formats from natural language"""
    if not date_str or pd.isna(date_str):
        return None
    
    date_str = str(date_str).lower().strip()
    
    # Remove ordinal suffixes like 'th', 'st', 'nd', 'rd'
    date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
    date_str = re.sub(r'(\d+)\s*(st|nd|rd|th)', r'\1', date_str)
    
    # Common patterns to try
    patterns = [
        (r'([a-z]+)\s+(\d+),\s+(\d{4})', '%B %d, %Y'),  # March 15, 2020
        (r'([a-z]+)\s+(\d+)\s+(\d{4})', '%B %d %Y'),  # March 15 2020
        (r'(\d+)\s+([a-z]+)\s+(\d{4})', '%d %B %Y'),  # 15 March 2020
        (r'(\d{4})\s+([a-z]+)\s+(\d+)', '%Y %B %d'),  # 2020 March 15
        (r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', '%Y-%m-%d'),  # 2020-03-15
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', '%m/%d/%Y'),  # 03/15/2020
    ]
    
    for pattern, fmt in patterns:
        match = re.search(pattern, date_str)
        if match:
            try:
                extracted_date = match.group(0)
                return datetime.strptime(extracted_date, fmt)
            except:
                continue
    
    # Try parsing just year
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        try:
            year = int(year_match.group(1))
            if 1900 <= year <= 2100:
                return datetime(year, 1, 1)
        except:
            pass
    
    return None

# Check the structure of the data
print('__RESULT__:')
print(json.dumps("Date parsing and CPC level 4 extraction functions ready"))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
