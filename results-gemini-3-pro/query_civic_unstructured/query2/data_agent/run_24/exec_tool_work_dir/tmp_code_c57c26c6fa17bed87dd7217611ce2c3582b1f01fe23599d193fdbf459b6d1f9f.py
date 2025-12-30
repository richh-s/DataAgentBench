code = """import json
import re
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-10729501578572278771']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load civic docs
docs_path = locals()['var_function-call-14279954887626903002']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by lines
    lines = text.split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    
    # Identify projects
    for i, line in enumerate(lines):
        # Look for the Updates line
        if "Updates:" in line:
            # The line before is likely the project name
            if i > 0:
                proj_name = lines[i-1]
                
                # Extract the chunk of text for this project
                # From current line until the next project header (heuristic)
                # Or just take the next 20 lines
                chunk = " ".join(lines[i:i+20])
                
                extracted_projects.append({
                    "Project_Name": proj_name,
                    "text_chunk": chunk
                })

# Filter
matched_records = []
for p in extracted_projects:
    name = p['Project_Name']
    chunk = p['text_chunk'].lower()
    full_str = (name + " " + chunk).lower()
    
    # Check if park related
    if "park" in full_str:
        # Check if completed in 2022
        # We look for "completed" and "2022" in the chunk
        if "completed" in chunk:
            # Check date
            # simple check: is 2022 in the chunk near completed?
            # actually, let's just check if "completed" and "2022" are both present
            # and verify it's not "complete design 2022" or "start 2022"
            
            # The pattern in the text is:
            # "(cid:190) Updates: Construction was completed November 2022"
            # or "Complete Construction: November 2022"
            
            # We want 'completed' status in 2022.
            # So we check for "completed <...date...>" or "complete construction <...date...>"
            
            if "2022" in chunk:
                # Be more specific to avoid false positives
                # Check for "completed" ... "2022"
                # or "complete construction" ... "2022"
                
                # Check 1: "completed" followed by "2022" within 50 chars
                # Check 2: "complete construction" followed by "2022" within 50 chars
                
                match1 = re.search(r'completed.{0,50}2022', chunk)
                match2 = re.search(r'complete construction.{0,50}2022', chunk)
                
                if match1 or match2:
                    matched_records.append(p)

# Merge
if matched_records:
    df_match = pd.DataFrame(matched_records)
    # Normalize
    df_match['join_key'] = df_match['Project_Name'].apply(lambda x: x.lower().strip())
    funding_df['join_key'] = funding_df['Project_Name'].apply(lambda x: x.lower().strip())
    
    merged = pd.merge(df_match, funding_df, on='join_key', how='inner')
    
    # Deduplicate by project name if necessary (in case of multiple updates for same project)
    # Funding table has unique Project_Name? The description says "unique identifier for the funding record", but Project_Name might repeat?
    # Let's assume one funding record per project for now or sum if multiple.
    # Actually, looking at funding data, "Bluffs Park Shade Structure" appears once with 21000.
    
    # Remove duplicates if any (same project extracted multiple times)
    merged = merged.drop_duplicates(subset=['Project_Name_x'])
    
    total = merged['Amount'].sum()
    projects_found = merged['Project_Name_x'].tolist()
else:
    total = 0
    projects_found = []

print("__RESULT__:")
print(json.dumps({"total": total, "projects": projects_found}))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json'}

exec(code, env_args)
