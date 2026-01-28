code = """import json
import pandas as pd
import re

with open(locals()['var_function_call_10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function_call_10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects = []
for doc in civic_docs:
    lines = [l.strip() for l in doc['text'].split('\n') if l.strip()]
    curr_name = None
    curr_buff = []
    
    # Identify project blocks
    # Look for lines followed by "(cid:190)" lines
    for i, line in enumerate(lines):
        # Heuristic for name
        is_name = False
        if not line.startswith('(') and len(line) < 100 and "Page" not in line and "Item" not in line:
            # Look ahead
            for k in range(1, 4):
                if i+k < len(lines) and lines[i+k].startswith('(') and 'cid' in lines[i+k] and '190' in lines[i+k]:
                    is_name = True
                    break
        
        if is_name:
            if curr_name:
                # Process previous
                full_text = " ".join(curr_buff).lower()
                # Check for Spring 2022 start
                # Look for "advertise: spring 2022" or "begin construction: spring 2022"
                # Simplify regex: (advertise|construction).*spring 2022
                if re.search(r'(advertise|construction|start).*spring 2022', full_text):
                    projects.append(curr_name)
                elif re.search(r'(advertise|construction|start).*spring, 2022', full_text):
                    projects.append(curr_name)
            
            curr_name = line
            curr_buff = []
        else:
            if curr_name:
                curr_buff.append(line)

    # Last project
    if curr_name:
        full_text = " ".join(curr_buff).lower()
        if re.search(r'(advertise|construction|start).*spring 2022', full_text):
            projects.append(curr_name)

# Dedupe
projects = list(set(projects))

# Join
matched = []
total = 0
df_funding['norm'] = df_funding['Project_Name'].str.lower().str.strip()

for p in projects:
    p_norm = p.lower().strip()
    match = df_funding[df_funding['norm'] == p_norm]
    if not match.empty:
        matched.append(p)
        total += match['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"count": len(matched), "total_funding": total, "projects": matched}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json'}

exec(code, env_args)
