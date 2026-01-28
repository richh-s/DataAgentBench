code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-4053517290050769829'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
project_names = set(funding_df['Project_Name'].unique())

# Load civic docs
with open(locals()['var_function-call-4397325354611622354'], 'r') as f:
    docs = json.load(f)

def normalize(s):
    return s.strip().lower()

normalized_projects = {normalize(p): p for p in project_names}

extracted_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_type = "capital" # Default
    current_project = None
    current_project_data = {}
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        lower_line = line_stripped.lower()
        if "capital improvement projects" in lower_line:
            current_type = "capital"
        elif "disaster recovery projects" in lower_line:
            current_type = "disaster"
        
        norm_line = normalize(line_stripped)
        
        if norm_line in normalized_projects:
            if current_project:
                extracted_projects.append(current_project_data)
            
            current_project = normalized_projects[norm_line]
            current_project_data = {
                'Project_Name': current_project,
                'type': current_type,
                'text_block': ""
            }
            # Check for inline disaster markers
            if "(fema" in lower_line or "(caloes" in lower_line or "disaster" in lower_line:
                current_project_data['type'] = "disaster"
                
        elif current_project:
            current_project_data['text_block'] += line + "\n"

    if current_project:
        extracted_projects.append(current_project_data)

# Process Dates
final_projects = []
for p in extracted_projects:
    text = p['text_block']
    st = None
    
    # Regex with double backslashes for JSON safety
    # "Begin Construction: ..."
    match = re.search(r"Begin Construction:?\s*([A-Za-z0-9\s,]+)", text, re.IGNORECASE)
    if match:
        st = match.group(1).strip()
    
    if not st:
        match = re.search(r"Construction began:?\s*([A-Za-z0-9\s,]+)", text, re.IGNORECASE)
        if match:
            st = match.group(1).strip()
            
    p['st'] = st
    final_projects.append(p)

df_extracted = pd.DataFrame(final_projects)

# Define disaster filter
def is_disaster(row):
    if row['type'] == 'disaster':
        return True
    name = row['Project_Name'].lower()
    if 'fema' in name or 'caloes' in name:
        return True
    return False

if not df_extracted.empty:
    df_extracted['is_disaster'] = df_extracted.apply(is_disaster, axis=1)
    
    # Define start date filter
    def started_in_2022(st):
        if not st:
            return False
        return "2022" in st
    
    df_extracted['started_2022'] = df_extracted['st'].apply(started_in_2022)
    
    # Merge
    merged = pd.merge(df_extracted, funding_df, on='Project_Name', how='inner')
    
    # Filter
    target_projects = merged[merged['is_disaster'] & merged['started_2022']]
    
    # Deduplicate by Project_Name (take the one with positive amount, but amounts should be same)
    target_projects = target_projects.drop_duplicates(subset=['Project_Name'])
    
    total_funding = target_projects['Amount'].sum()
    
    result = {
        "total_funding": total_funding,
        "projects": target_projects[['Project_Name', 'st', 'Amount']].to_dict(orient='records')
    }
else:
    result = {"total_funding": 0, "projects": []}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4053517290050769829': 'file_storage/function-call-4053517290050769829.json', 'var_function-call-4397325354611622354': 'file_storage/function-call-4397325354611622354.json'}

exec(code, env_args)
