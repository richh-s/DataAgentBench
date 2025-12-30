code = """import json
import re

# Load data
with open(locals()['var_function-call-6964896026869671245'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-867828661549977430'], 'r') as f:
    funding_data = json.load(f)

newline_char = chr(10)
full_text = newline_char.join([doc['text'] for doc in civic_docs])
full_text_lower = full_text.lower()

def clean_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

funding_by_clean_name = {}
for entry in funding_data:
    raw_name = entry['Project_Name']
    amt = int(entry['Amount'])
    c_name = clean_name(raw_name)
    if c_name not in funding_by_clean_name:
        funding_by_clean_name[c_name] = {'amounts': [], 'raw_names': []}
    funding_by_clean_name[c_name]['amounts'].append(amt)
    funding_by_clean_name[c_name]['raw_names'].append(raw_name)

total_funding = 0
matched_projects = []

for c_name, data in funding_by_clean_name.items():
    if len(c_name) < 5: continue
    if "project_" in c_name.lower(): continue

    # Check for Park keyword in name
    # We want to match "park" but not "parking"
    # Regex for park as a word?
    # Or just simple exclusion.
    name_lower = c_name.lower()
    is_park_name = False
    if 'park' in name_lower and 'parking' not in name_lower:
        is_park_name = True
    
    start_search = 0
    found_valid = False
    
    while True:
        idx = full_text.find(c_name, start_search)
        if idx == -1:
            break
        
        # Found an occurrence
        context = full_text[idx:idx+800]
        context_lower = context.lower()
        
        # Determine if park related
        is_park = is_park_name
        if not is_park:
            # Check context for "park" word, avoiding "parking"
            # We can use regex \bpark\b or similar
            if re.search(r'\bpark\b', context_lower):
                is_park = True
        
        # Check Completed 2022
        # Look for "completed" ... "2022"
        is_completed_2022 = False
        if is_park:
            if 'completed' in context_lower and '2022' in context_lower:
                c_indices = [m.start() for m in re.finditer('completed', context_lower)]
                for ci in c_indices:
                    # check surrounding 100 chars (increased window slightly)
                    snippet = context_lower[max(0, ci-60):ci+60]
                    if '2022' in snippet:
                        is_completed_2022 = True
                        break
        
        if is_park and is_completed_2022:
            found_valid = True
            break
        
        start_search = idx + 1
    
    if found_valid:
        total = sum(data['amounts'])
        total_funding += total
        matched_projects.append({
            "name": c_name,
            "amount": total
        })

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-6964896026869671245': 'file_storage/function-call-6964896026869671245.json', 'var_function-call-16721484954554461294': ['Funding'], 'var_function-call-867828661549977430': 'file_storage/function-call-867828661549977430.json'}

exec(code, env_args)
