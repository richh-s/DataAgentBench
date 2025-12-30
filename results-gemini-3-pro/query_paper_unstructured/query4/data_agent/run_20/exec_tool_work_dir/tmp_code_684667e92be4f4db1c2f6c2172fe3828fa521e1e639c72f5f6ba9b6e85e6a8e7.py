code = """import json
import re

# Load the result from the previous tool call
file_path = locals()['var_function-call-5659440359998634894']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for 2016 in the first 1000 characters
    # We look for "2016" or "'16" which might appear in conference headers
    # Example: "CHI '16", "Ubicomp '16", "Copyright 2016"
    
    header = text[:1000]
    
    # Simple check for 2016
    if '2016' in header:
        titles_2016.append(title)
        continue
        
    # Check for '16 with conference names (common venues from description)
    # Venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
    venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
    found_venue_year = False
    for v in venues:
        if f"{v} '16" in header or f"{v} 2016" in header or f"{v}'16" in header:
            found_venue_year = True
            break
    
    if found_venue_year:
        titles_2016.append(title)

print(f"__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-7797754870209307186': 'file_storage/function-call-7797754870209307186.json', 'var_function-call-5659440359998634894': 'file_storage/function-call-5659440359998634894.json'}

exec(code, env_args)
