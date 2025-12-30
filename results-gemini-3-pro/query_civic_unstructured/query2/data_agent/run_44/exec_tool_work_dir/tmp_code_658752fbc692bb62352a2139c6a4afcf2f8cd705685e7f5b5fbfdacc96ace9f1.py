code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-2604806260123295524'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2604806260123292981'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

projects = []
for doc in civic_docs:
    text = doc['text']
    # Look for lines that look like headers followed by Updates
    # We use a pattern that finds a line (the title) followed by a line containing 'Updates:'
    # The (cid:190) is usually before Updates
    pattern = re.compile(r'\n([^\n]+)\n.*Updates:')
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        if i < len(matches) - 1:
            end = matches[i+1].start()
        else:
            end = len(text)
        content = text[start:end]
        projects.append({'name': name, 'text': content})

completed_parks = []
for p in projects:
    name = p['name']
    text = p['text'].lower()
    full_text = (name + " " + p['text']).lower()
    
    # Check topic
    is_park = 'park' in full_text and 'parking' not in full_text
    if 'playground' in full_text:
        is_park = True
    
    # Check completed 2022
    is_comp_2022 = False
    lines = text.split('\n')
    for line in lines:
        if 'completed' in line and '2022' in line:
            # check for design
            if 'design' in line and 'construction' not in line:
                continue
            is_comp_2022 = True
            break
            
    if is_park and is_comp_2022:
        completed_parks.append(name)

completed_parks = list(set(completed_parks))
print(f"DEBUG: Projects found: {completed_parks}")

total = 0
found_projects = []
for name in completed_parks:
    # Exact match or strip
    # Also clean up potential special chars in name extracted
    clean_name = name.strip()
    match = funding_df[funding_df['Project_Name'].str.strip() == clean_name]
    if not match.empty:
        total += match['Amount'].sum()
        found_projects.append(clean_name)
    else:
        # Try simple fuzzy: if clean_name is in Project_Name
        # or Project_Name in clean_name
        # Be careful of partial matches
        print(f"DEBUG: No exact funding for {clean_name}")

print("__RESULT__:")
print(json.dumps({"total_funding": int(total), "projects": found_projects}))"""

env_args = {'var_function-call-2604806260123295524': 'file_storage/function-call-2604806260123295524.json', 'var_function-call-2604806260123292981': 'file_storage/function-call-2604806260123292981.json'}

exec(code, env_args)
