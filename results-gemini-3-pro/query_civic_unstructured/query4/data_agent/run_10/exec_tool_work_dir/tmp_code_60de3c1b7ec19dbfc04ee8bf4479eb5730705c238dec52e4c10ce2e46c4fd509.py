code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function_call_10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function_call_10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects = []

def is_spring_2022(date_str):
    if not date_str:
        return False
    d = date_str.lower().strip()
    # Explicit Spring 2022
    if 'spring 2022' in d or 'spring, 2022' in d:
        return True
    # Months in 2022
    if '2022' in d:
        if 'march' in d or 'april' in d or 'may' in d:
            return True
        # Numeric
        if re.search(r'(03|3|04|4|05|5)[/-]2022', d): return True
        if re.search(r'2022[/-](03|3|04|4|05|5)', d): return True
    return False

# Iterate docs
for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    extracted_projects = {}
    current_proj_name = None
    current_proj_lines = []
    
    # Ignore list broken into multiple lines to avoid length issues
    ignores = [
        "Page ", "Agenda Item", "Public Works", "Commission", 
        "Date prepared", "Meeting date", "Subject:", 
        "RECOMMENDED ACTION:", "DISCUSSION:", "Capital Improvement Projects"
    ]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check potential name
        is_name = True
        if line.startswith('('): is_name = False
        for ig in ignores:
            if ig in line:
                is_name = False
                break
        
        if is_name:
            # Look ahead for bullet
            found_bullet = False
            for k in range(1, 5):
                if i + k < len(lines):
                    nl = lines[i+k]
                    # Check for bullet (cid:190)
                    if nl.startswith('(') and 'cid' in nl and '190' in nl:
                        found_bullet = True
                        break
            
            if found_bullet:
                if current_proj_name:
                    extracted_projects[current_proj_name] = "\n".join(current_proj_lines)
                current_proj_name = line
                current_proj_lines = []
                i += 1
                continue
        
        if current_proj_name:
            current_proj_lines.append(line)
        i += 1
    
    if current_proj_name:
        extracted_projects[current_proj_name] = "\n".join(current_proj_lines)
    
    # Process extracted projects
    for proj, content in extracted_projects.items():
        content_lower = content.lower()
        
        # Parse schedule lines
        # Lines often: "(cid:131) Key: Value"
        # We look for lines containing ':'
        
        candidate_found = False
        
        # Split content into lines
        c_lines = content.split('\n')
        for cline in c_lines:
            if ':' in cline:
                parts = cline.split(':', 1)
                k = parts[0].lower()
                v = parts[1].strip()
                
                # Check for Start indicators
                if 'advertise' in k or 'begin construction' in k or 'start' in k:
                    if is_spring_2022(v):
                        projects.append({
                            'Project_Name': proj,
                            'Start_Date': v,
                            'Source': k
                        })
                        candidate_found = True
                        break
        
        if not candidate_found:
            # Maybe the date is just in the text?
            pass

# Deduplicate
df_res = pd.DataFrame(projects)
if not df_res.empty:
    df_res = df_res.drop_duplicates(subset=['Project_Name'])

def normalize(n):
    return n.lower().strip() if n else ""

# Join
matched_projects = []
if not df_res.empty:
    df_res['join_key'] = df_res['Project_Name'].apply(normalize)
    df_funding['join_key'] = df_funding['Project_Name'].apply(normalize)
    
    merged = pd.merge(df_res, df_funding, on='join_key', how='inner')
    
    print("__RESULT__:")
    print(json.dumps({
        "count": len(merged),
        "total_funding": merged['Amount'].sum(),
        "projects": merged['Project_Name_x'].tolist(),
        "unmerged": df_res[~df_res['join_key'].isin(df_funding['join_key'])]['Project_Name'].tolist()
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"count": 0, "total_funding": 0}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json'}

exec(code, env_args)
