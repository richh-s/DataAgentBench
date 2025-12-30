code = """import json
import re

# Load the file from the previous query_db result
file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

valid_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # remove .txt
    
    # Extract year from first 1000 chars
    # Strategy: find all 4-digit years 20xx.
    # We are looking for publication year > 2016.
    # Usually appears as "CHI 2017", "Copyright 2018", etc.
    # We take the set of years found in the header and see if any is > 2016.
    # But we need the *publication* year.
    # If the text has "2015" and "2018", which is it?
    # Usually the later one in the header is the copyright/pub year.
    # Or the one associated with the conference.
    
    header = text[:500]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    # Convert to ints
    years = [int(y) for y in years if 2000 <= int(y) <= 2025]
    
    if not years:
        continue
        
    # Heuristic: The publication year is likely the max year found in the header 
    # (e.g. "Copyright 2018", "CHI 2018")
    # unless it's a reference to a past paper?
    # In headers, references are rare.
    pub_year = max(years)
    
    if pub_year > 2016:
        valid_titles.append(title)

print("__RESULT__:")
print(json.dumps(valid_titles))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json'}

exec(code, env_args)
