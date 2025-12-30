code = """import json
import re

# Load the papers
with open(locals()['var_function-call-3133197345042129806'], 'r') as f:
    papers = json.load(f)

target_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract year
    # Look for 2017, 2018, ..., 2025 in the first 1000 chars
    # We want papers published AFTER 2016, so >= 2017
    # Regex for 2017-2029
    # We should look for specific patterns to avoid random numbers
    # But usually year is distinct. 
    # Let's search for 201[7-9] or 202[0-9]
    
    # Limit search to first 2000 chars to be safe (headers)
    header_text = text[:2000]
    
    # Find all years
    years = re.findall(r'20(1[7-9]|2[0-9])', header_text)
    
    # If years found, we assume it meets the criteria if at least one valid year is found in the header
    # But wait, what if it cites a 2018 paper in the abstract?
    # Usually the publication year is early in the text.
    # Let's try to be more specific. 
    # "Conference 'YY" or "Year: 20YY" or "Copyright 20YY"
    # The sample has "UBICOMP '15, ... 2015"
    # Let's look for "201[7-9]" or "202[0-9]"
    # If found in the first 500 chars, it's likely the pub year.
    
    found_year = False
    
    # Check strict regex in first 500 chars
    matches = re.findall(r'\b(20(?:1[7-9]|2[0-9]))\b', text[:500])
    if matches:
        found_year = True
    else:
        # Try 'YY format? e.g. '17, '18. Risk of false positives.
        # Let's stick to 4 digits.
        pass
        
    # Check contribution
    # "empirical" in text
    is_empirical = 'empirical' in text.lower()
    
    if found_year and is_empirical:
        target_titles.append(title)

print("__RESULT__:")
print(json.dumps(target_titles))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json'}

exec(code, env_args)
