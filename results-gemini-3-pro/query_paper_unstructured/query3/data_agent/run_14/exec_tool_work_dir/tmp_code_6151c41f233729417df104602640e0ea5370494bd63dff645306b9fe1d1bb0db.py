code = """import json
import re

# Load the documents
with open(locals()['var_function-call-9752705045220679725'], 'r') as f:
    docs = json.load(f)

valid_titles = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for year in first 3000 chars
    header_text = text[:3000]
    
    # Try to find specific patterns first
    # Pattern 1: Copyright 20XX
    copyright_match = re.search(r'Copyright\s+(?:©\s*)?(20\d{2})', header_text, re.IGNORECASE)
    # Pattern 2: Conference 'XX (where XX is 2 digits) -> 20XX
    conf_match = re.search(r"Conference\s+'(\d{2})", header_text, re.IGNORECASE)
    # Pattern 3: Simple 20XX
    year_matches = re.findall(r'\b(20\d{2})\b', header_text)
    
    year = None
    if copyright_match:
        year = int(copyright_match.group(1))
    elif conf_match:
        year = 2000 + int(conf_match.group(1))
    elif year_matches:
        # Take the first one that is reasonable (e.g. between 2000 and 2025)
        for y in year_matches:
            y_int = int(y)
            if 2000 <= y_int <= 2025:
                year = y_int
                break
    
    # Check Contribution
    # Check if 'empirical' is in text (case insensitive)
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        valid_titles.append(title)

print("__RESULT__:")
print(json.dumps(valid_titles))"""

env_args = {'var_function-call-17324318872041737699': 'file_storage/function-call-17324318872041737699.json', 'var_function-call-7414201362251444319': 'file_storage/function-call-7414201362251444319.json', 'var_function-call-9752705045220679725': 'file_storage/function-call-9752705045220679725.json'}

exec(code, env_args)
