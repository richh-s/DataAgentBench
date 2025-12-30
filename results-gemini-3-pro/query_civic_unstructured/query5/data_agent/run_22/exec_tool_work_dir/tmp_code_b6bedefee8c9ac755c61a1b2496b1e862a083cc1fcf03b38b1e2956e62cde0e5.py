code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-4053517290050769829'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
project_names = set(funding_df['Project_Name'].unique())

# Load civic docs
with open(locals()['var_function-call-4397325354611622354'], 'r') as f:
    docs = json.load(f)

# Helper to normalize strings for comparison
def normalize(s):
    return s.strip().lower()

normalized_projects = {normalize(p): p for p in project_names}

extracted_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_type = None
    current_project = None
    current_project_data = {}
    
    # We will buffer lines to process a project block
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Detect Section Headers
        lower_line = line_stripped.lower()
        if "capital improvement projects" in lower_line:
            current_type = "capital"
        elif "disaster recovery projects" in lower_line:
            current_type = "disaster"
        
        # Check if line is a project name
        # We check if the line (normalized) is in our project list
        norm_line = normalize(line_stripped)
        
        # Heuristic: Project names in text might be substrings or exact matches
        # The prompt says they match.
        if norm_line in normalized_projects:
            # Save previous project
            if current_project:
                extracted_projects.append(current_project_data)
            
            current_project = normalized_projects[norm_line]
            current_project_data = {
                'Project_Name': current_project,
                'type': current_type, # Inherit from section
                'text_block': ""
            }
            # Also check if name implies disaster
            if "(fema" in lower_line or "(caloes" in lower_line or "disaster" in lower_line:
                current_project_data['type'] = "disaster"
                
        elif current_project:
            current_project_data['text_block'] += line + "\n"

    # Append last project
    if current_project:
        extracted_projects.append(current_project_data)

# Now process the text blocks to find start dates
final_projects = []
for p in extracted_projects:
    text = p['text_block']
    st = None
    
    # Regex for start date
    # Patterns: "Begin Construction: <Date>", "Construction began: <Date>", "Advertise: <Date>"
    # We want "started in 2022".
    
    # Pattern 1: Begin Construction: [Month Year] or [Season Year]
    match = re.search(r"Begin Construction:\s*([A-Za-z0-9\s]+)", text, re.IGNORECASE)
    if match:
        st = match.group(1).strip()
    
    if not st:
        match = re.search(r"Construction began:?\s*([A-Za-z0-9\s,]+)", text, re.IGNORECASE)
        if match:
            st = match.group(1).strip()

    if not st:
        # Check for "Construction was completed..." implies it started before. 
        # But we specifically need "started in 2022".
        # If it says "Updates: Construction began in January 2022", that works.
        match = re.search(r"Construction.*began.*in\s*([A-Za-z0-9\s,]+)", text, re.IGNORECASE)
        if match:
            st = match.group(1).strip()

    p['st'] = st
    final_projects.append(p)

df_extracted = pd.DataFrame(final_projects)

# Filter for Disaster projects
# Type can be "disaster" from section or name
# Also check if Project Name contains FEMA/CalOES/Disaster
def is_disaster(row):
    if row['type'] == 'disaster':
        return True
    name = row['Project_Name'].lower()
    if 'fema' in name or 'caloes' in name or 'disaster' in name:
        return True
    return False

df_extracted['is_disaster'] = df_extracted.apply(is_disaster, axis=1)

# Filter for Start Date in 2022
def started_in_2022(st):
    if not st:
        return False
    return "2022" in st

df_extracted['started_2022'] = df_extracted['st'].apply(started_in_2022)

# Join with funding
merged = pd.merge(df_extracted, funding_df, on='Project_Name', how='inner')

# Filter
target_projects = merged[merged['is_disaster'] & merged['started_2022']]

# Calculate total funding
# Note: There might be duplicate entries if a project appears in multiple docs.
# We should probably deduplicate by Project_Name.
target_projects = target_projects.drop_duplicates(subset=['Project_Name'])

total_funding = target_projects['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "projects": target_projects[['Project_Name', 'st', 'Amount']].to_dict(orient='records'),
    "debug_extracted_count": len(df_extracted),
    "debug_target_count": len(target_projects)
}))"""

env_args = {'var_function-call-4053517290050769829': 'file_storage/function-call-4053517290050769829.json', 'var_function-call-4397325354611622354': 'file_storage/function-call-4397325354611622354.json'}

exec(code, env_args)
