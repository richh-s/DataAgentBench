code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12716671968640832607'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-12716671968640831510'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}
text = civic_docs[0]['text']

# Regex pattern
# We are looking for: Newline -> Project Name -> Newline -> (cid:190) -> Header
pattern = r"\n([^\n]+)\s*\n\s*(?:\(cid:190\)|\u00be)\s*(?:Updates|Project Description|Project Updates)"

matches = list(re.finditer(pattern, text, re.MULTILINE))

projects = []
for i, match in enumerate(matches):
    project_name = match.group(1).strip()
    start_idx = match.end()
    if i + 1 < len(matches):
        end_idx = matches[i+1].start()
    else:
        end_idx = len(text)
    
    project_text = text[start_idx:end_idx]
    projects.append({'name': project_name, 'text': project_text})

# Keywords
keywords = ['park', 'playground']

target_projects = []
total_funding = 0

for p in projects:
    name = p['name']
    details = p['text']
    
    # Check if park related
    if not any(k in name.lower() for k in keywords):
        continue
        
    # Check for completion in 2022
    # Pattern: "completed" ... "2022"
    # We look for "completed" followed by date like "Month 2022"
    
    # Check if 2022 appears after completed
    # This regex looks for 'completed' then within 50 chars a year.
    comp_match = re.search(r"completed.{0,50}?(\d{4})", details, re.IGNORECASE | re.DOTALL)
    
    if comp_match:
        year = comp_match.group(1)
        if year == '2022':
            amount = funding_map.get(name, 0)
            target_projects.append({'name': name, 'amount': amount})
            total_funding += amount

print("__RESULT__:")
print(json.dumps({'target_projects': target_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json'}

exec(code, env_args)
