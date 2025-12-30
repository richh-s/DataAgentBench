code = """import pandas as pd
import json

funding_path = locals()['var_function-call-16409169562152250528']
docs_path = locals()['var_function-call-16409169562152248833']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_df = funding_df[funding_df['Amount'] > 50000]

def is_disaster(name):
    keywords = ['(FEMA', '(CalOES', '(CalJPIA']
    for k in keywords:
        if k in name:
            return True
    return False

funding_df['is_disaster'] = funding_df['Project_Name'].apply(is_disaster)
capital_funding = funding_df[~funding_df['is_disaster']].copy()

design_projects = set()

for doc in docs_data:
    text = doc['text']
    lines = text.splitlines()
    in_design_section = False
    
    for i, line in enumerate(lines):
        clean_line = line.strip()
        
        if "Capital Improvement Projects (Design)" in clean_line:
            in_design_section = True
            continue
            
        if ("Capital Improvement Projects (Construction)" in clean_line or 
            "Capital Improvement Projects (Not Started)" in clean_line or 
            "Disaster Recovery Projects" in clean_line):
            in_design_section = False
            continue
        
        if in_design_section:
            if "Updates:" in clean_line:
                 k = i - 1
                 while k >= 0:
                     prev_line = lines[k].strip()
                     if not prev_line or "Page" in prev_line or "Agenda Item" in prev_line or prev_line.isdigit():
                         k -= 1
                         continue
                     if "Capital Improvement Projects (Design)" in prev_line:
                         break 
                     
                     design_projects.add(prev_line)
                     break

matched_projects = set()
doc_names = list(design_projects)

for idx, row in capital_funding.iterrows():
    f_name = row['Project_Name'].strip()
    fn_lower = f_name.lower()
    
    found = False
    for d_name in doc_names:
        d_name_clean = d_name.strip()
        dn_lower = d_name_clean.lower()
        
        if fn_lower == dn_lower or fn_lower in dn_lower or dn_lower in fn_lower:
            found = True
            break
            
    if found:
        matched_projects.add(f_name)

print("Extracted Design Projects:", doc_names)
print("Matches found:", len(matched_projects))
print("Matched Names:", list(matched_projects))

print("__RESULT__:")
print(json.dumps(len(matched_projects)))"""

env_args = {'var_function-call-16409169562152250528': 'file_storage/function-call-16409169562152250528.json', 'var_function-call-16409169562152248833': 'file_storage/function-call-16409169562152248833.json'}

exec(code, env_args)
