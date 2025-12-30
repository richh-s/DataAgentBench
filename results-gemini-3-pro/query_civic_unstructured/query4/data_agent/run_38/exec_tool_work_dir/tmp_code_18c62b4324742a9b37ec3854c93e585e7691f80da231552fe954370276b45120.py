code = """import json
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-11668788458618260347']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
# Convert Amount to numeric
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

# Load civic docs
civic_path = locals()['var_function-call-11668788458618261250']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

def parse_date(date_str):
    if not date_str:
        return None
    date_str = date_str.lower().strip()
    
    # Check for "Spring 2022" directly
    if 'spring 2022' in date_str or 'spring, 2022' in date_str:
        return 'Spring 2022'
        
    # Check for year 2022 and months/seasons
    if '2022' in date_str:
        if 'spring' in date_str:
            return 'Spring 2022'
        # Months: March (03), April (04), May (05)
        if any(m in date_str for m in ['march', 'april', 'may']):
            return 'Spring 2022'
        
        # Regex for dates like 03/2022, 2022-03
        if re.search(r'(03|04|05)[/\-.]2022', date_str) or re.search(r'2022[/\-.](03|04|05)', date_str):
            return 'Spring 2022'
            
    return None

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify project indices
    project_indices = []
    for i, line in enumerate(lines):
        line_clean = line.strip()
        # Look for the Updates or Project Description marker
        # Using a looser check to avoid encoding issues with the bullet
        if "Updates:" in line_clean and len(line_clean) < 50: 
             # Check if previous line is a title
             j = i - 1
             while j >= 0 and not lines[j].strip():
                 j -= 1
             if j >= 0:
                 project_name = lines[j].strip()
                 project_indices.append((j, project_name))
        elif "Project Description:" in line_clean and len(line_clean) < 50:
             j = i - 1
             while j >= 0 and not lines[j].strip():
                 j -= 1
             if j >= 0:
                 project_name = lines[j].strip()
                 # Avoid duplicates if both Updates and Description appear
                 if not project_indices or project_indices[-1][1] != project_name:
                     project_indices.append((j, project_name))
    
    # Process each project block
    for k in range(len(project_indices)):
        start_idx, p_name = project_indices[k]
        if k < len(project_indices) - 1:
            end_idx = project_indices[k+1][0]
        else:
            end_idx = len(lines)
        
        block_text = "\n".join(lines[start_idx:end_idx])
        
        # Extract Begin Construction date
        match = re.search(r'Begin [Cc]onstruction:([^\n]*)', block_text)
        start_date = None
        if match:
            start_date = match.group(1).strip()
        
        parsed_st = parse_date(start_date)
        
        if parsed_st == 'Spring 2022':
            extracted_projects.append({
                'Project_Name': p_name,
                'st': parsed_st,
                'raw_st': start_date
            })

# Join with funding
df_extracted = pd.DataFrame(extracted_projects)

if not df_extracted.empty:
    merged = pd.merge(df_funding, df_extracted, on='Project_Name', how='inner')
    count = len(merged)
    total_funding = int(merged['Amount'].sum())
    
    print("__RESULT__:")
    print(json.dumps({
        "count": count,
        "total_funding": total_funding,
        "projects": merged[['Project_Name', 'raw_st', 'Amount']].to_dict(orient='records')
    }))
else:
    print("__RESULT__:")
    print(json.dumps({
        "count": 0,
        "total_funding": 0,
        "projects": []
    }))"""

env_args = {'var_function-call-5073457582333833681': ['civic_docs'], 'var_function-call-5073457582333837024': ['Funding'], 'var_function-call-11668788458618260347': 'file_storage/function-call-11668788458618260347.json', 'var_function-call-11668788458618261250': 'file_storage/function-call-11668788458618261250.json'}

exec(code, env_args)
