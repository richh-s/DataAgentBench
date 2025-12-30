code = """import json
import pandas as pd
import re

# Load inputs
with open(locals()['var_function-call-7811788439429183235'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-3690034761458033571'], 'r') as f:
    civic_docs = json.load(f)

def normalize(text):
    # simple normalization
    return " ".join(text.split()).strip()

funding_names = set(funding_df['Project_Name'].apply(normalize).tolist())

extracted = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    curr_proj = None
    curr_dates = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        norm_line = normalize(line)
        is_new = False
        
        # Check against funding names
        if norm_line in funding_names:
            is_new = True
        else:
            # Check context
            if i + 1 < len(lines):
                nxt = lines[i+1]
                if "Updates:" in nxt or "Project Description:" in nxt:
                    if "Agenda Item" not in line and len(line) > 5:
                        is_new = True
                        # Clean artifacts like (cid:190) which are bullet points often
                        # We will just take the string as is for now, normalization handles spaces
                        pass

        if is_new:
            if curr_proj:
                extracted.append({'name': curr_proj, 'dates': curr_dates})
            curr_proj = norm_line
            curr_dates = []
        elif curr_proj:
            if "Begin" in line or "Start" in line:
                curr_dates.append(line)

    if curr_proj:
        extracted.append({'name': curr_proj, 'dates': curr_dates})

# Filter
qualifying = set()
disaster_keys = ["FEMA", "CalOES", "CalJPIA"]

for p in extracted:
    name = p['name']
    # Type check
    is_disaster = False
    for k in disaster_keys:
        if k in name:
            is_disaster = True
            break
    
    if is_disaster:
        # Date check
        for d in p['dates']:
            if "2022" in d:
                qualifying.add(name)

total = 0
for name in qualifying:
    # Find amount
    row = funding_df[funding_df['Project_Name'].apply(normalize) == name]
    if not row.empty:
        total += int(row.iloc[0]['Amount'])

print("__RESULT__:")
print(json.dumps({"total": total, "projects": list(qualifying)}))"""

env_args = {'var_function-call-7811788439429183235': 'file_storage/function-call-7811788439429183235.json', 'var_function-call-3690034761458033571': 'file_storage/function-call-3690034761458033571.json'}

exec(code, env_args)
