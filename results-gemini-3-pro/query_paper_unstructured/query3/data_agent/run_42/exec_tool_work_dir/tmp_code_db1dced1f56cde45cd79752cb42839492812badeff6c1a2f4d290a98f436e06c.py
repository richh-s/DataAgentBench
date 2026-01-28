code = """import json
import re

file_path = locals()['var_function-call-2666164887420722559']
with open(file_path, 'r') as f:
    papers = json.load(f)

relevant_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for "empirical"
    if 'empirical' not in text.lower():
        continue

    # Extract Year
    # Look for 4 digit year in first 2000 characters
    header = text[:2000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    pub_year = 0
    if years:
        # Convert to ints and filter reasonable range (e.g. 2000-2025)
        valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
        if valid_years:
            # Usually the first one is the publication year (e.g. in header or copyright)
            # However, sometimes previous years are cited. 
            # Often the publication year is the one that appears with the venue or copyright.
            # I'll take the mode or the first one? Let's take the first valid one found.
            pub_year = valid_years[0]
    
    # Alternative: check for 'YY pattern if 4-digit not found or to confirm?
    # Actually, 4-digit is more reliable if present.
    
    if pub_year > 2016:
        relevant_titles.append(title)

print("__RESULT__:")
print(json.dumps(relevant_titles))"""

env_args = {'var_function-call-12623071366451944695': 'file_storage/function-call-12623071366451944695.json', 'var_function-call-15611850361610481914': 'file_storage/function-call-15611850361610481914.json', 'var_function-call-2666164887420722559': 'file_storage/function-call-2666164887420722559.json'}

exec(code, env_args)
