code = """import json
import sqlite3
import pandas as pd
import re

# Load Funding Data
funding_path = locals()['var_function-call-12717263916929775114']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load Civic Docs
civic_path = locals()['var_function-call-12717263916929775677']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = "\n".join([d['text'] for d in civic_docs])

# Define keywords
keywords = ['emergency', 'fema', 'disaster', 'fire']

# Function to extract projects from text
def extract_projects(text):
    lines = text.split('\n')
    projects = []
    
    # section headers
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    
    section_map = {
        "Design": "design",
        "Construction": "construction",
        "Not Started": "not started"
    }
    
    # Identify project blocks:
    project_indices = []
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "(cid:190) Project Description:" in line:
            # Find name (previous non-empty line)
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                name = lines[j].strip()
                project_indices.append({'name': name, 'start_line': j, 'marker_line': i})
    
    # Sort
    project_indices.sort(key=lambda x: x['start_line'])
    
    # Iterate through projects
    for k in range(len(project_indices)):
        p = project_indices[k]
        start = p['start_line']
        end = project_indices[k+1]['start_line'] if k < len(project_indices) - 1 else len(lines)
        
        block_lines = lines[start:end]
        block_text = "\n".join(block_lines)
        
        projects.append({
            'name': p['name'],
            'block': block_text,
            'status_context': 'unknown',
            'line_idx': start
        })

    # Iterate lines to assign status
    current_status = "unknown"
    p_idx = 0
    
    for i, line in enumerate(lines):
        lower_line = line.lower()
        if "capital improvement projects (design)" in lower_line:
            current_status = "design"
        elif "capital improvement projects (construction)" in lower_line:
            current_status = "construction"
        elif "capital improvement projects (not started)" in lower_line:
            current_status = "not started"
            
        if p_idx < len(projects) and projects[p_idx]['line_idx'] == i:
            projects[p_idx]['status_context'] = current_status
            p_idx += 1
            
    return projects

extracted_projects = extract_projects(full_text)

# Match with Funding and Filter
results = []

# Prepare funding df
# Use regex to clean name: remove (...) content
df_funding['Project_Name_Clean'] = df_funding['Project_Name'].astype(str).str.replace(r'\s*\(.*?\)\s*', '', regex=True).str.strip().str.lower()

for p in extracted_projects:
    p_name = p['name']
    p_text = p['block'].lower()
    p_status = p['status_context']
    
    # Refine status based on text content
    if "construction was completed" in p_text:
        p_status = "completed"
    
    # Determine relevance (Topic)
    is_related = False
    for kw in keywords:
        if kw in p_name.lower() or kw in p_text:
            is_related = True
            break
            
    # Normalize name for matching
    p_name_clean = re.sub(r'\s*\(.*?\)\s*', '', p_name).strip().lower()
    
    # Find matching funding records
    # 1. Exact clean match
    matches = df_funding[df_funding['Project_Name_Clean'] == p_name_clean]
    
    # 2. If no match, try substring match (one way)
    if matches.empty:
         matches = df_funding[df_funding['Project_Name_Clean'].str.contains(re.escape(p_name_clean), case=False) | 
                              df_funding['Project_Name_Clean'].apply(lambda x: p_name_clean in x)]
    
    funding_records = matches.to_dict('records')
    
    # Check if funding name makes it related
    if not is_related and funding_records:
        for rec in funding_records:
            if any(kw in rec['Project_Name'].lower() for kw in keywords):
                is_related = True
                break
                
    if is_related and funding_records:
        # Use a set to avoid duplicates if multiple matches return same project (unlikely but possible)
        seen_ids = set()
        for rec in funding_records:
            if rec['Funding_ID'] not in seen_ids:
                results.append({
                    "Project_Name": rec['Project_Name'],
                    "Funding_Source": rec['Funding_Source'],
                    "Amount": rec['Amount'],
                    "Status": p_status
                })
                seen_ids.add(rec['Funding_ID'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7885629070765766098': ['civic_docs'], 'var_function-call-7885629070765766627': ['Funding'], 'var_function-call-7885629070765767156': 'file_storage/function-call-7885629070765767156.json', 'var_function-call-7885629070765767685': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12717263916929775114': 'file_storage/function-call-12717263916929775114.json', 'var_function-call-12717263916929775677': 'file_storage/function-call-12717263916929775677.json'}

exec(code, env_args)
