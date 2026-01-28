code = """import json
import pandas as pd
import re

# Load
with open(locals()['var_function_call_10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function_call_10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects_found = []

for doc in civic_docs:
    # Use chr(10) for newline to avoid backslash issues
    lines = [l.strip() for l in doc['text'].split(chr(10)) if l.strip()]
    
    curr_proj = None
    curr_text = []
    
    for i, line in enumerate(lines):
        # Check for name
        is_name = False
        # Heuristic: line doesn't start with ( or bullet char, followed by bullet char line
        if not line.startswith('(') and "Page" not in line:
            # Check next few lines
            for k in range(1, 4):
                if i+k < len(lines):
                    nx = lines[i+k]
                    if nx.startswith('(') and 'cid' in nx:
                        is_name = True
                        break
        
        if is_name:
            if curr_proj:
                full_txt = " ".join(curr_text).lower()
                # Check criteria
                if 'spring 2022' in full_txt and ('advertise' in full_txt or 'construction' in full_txt):
                    projects_found.append(curr_proj)
            curr_proj = line
            curr_text = []
        else:
            if curr_proj:
                curr_text.append(line)
    
    if curr_proj:
        full_txt = " ".join(curr_text).lower()
        if 'spring 2022' in full_txt and ('advertise' in full_txt or 'construction' in full_txt):
            projects_found.append(curr_proj)

# Dedupe
projects_found = list(set(projects_found))

# Join
matched_count = 0
matched_funding = 0
matched_names = []

df_funding['norm'] = df_funding['Project_Name'].str.lower().str.strip()

for p in projects_found:
    p_norm = p.lower().strip()
    match = df_funding[df_funding['norm'] == p_norm]
    if not match.empty:
        matched_count += 1
        matched_funding += match['Amount'].sum()
        matched_names.append(p)

print("__RESULT__:")
print(json.dumps({"count": matched_count, "total_funding": matched_funding, "projects": matched_names}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json'}

exec(code, env_args)
