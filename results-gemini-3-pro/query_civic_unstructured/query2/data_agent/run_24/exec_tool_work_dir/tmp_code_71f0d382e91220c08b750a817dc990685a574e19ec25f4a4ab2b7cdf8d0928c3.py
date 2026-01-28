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
    lines = text.splitlines()
    lines = [l.strip() for l in lines if l.strip()]
    
    for i, line in enumerate(lines):
        if "Updates:" in line:
            if i > 0:
                proj_name = lines[i-1]
                # Take next 20 lines
                chunk = " ".join(lines[i:i+20])
                extracted_projects.append({
                    "Project_Name": proj_name,
                    "text_chunk": chunk
                })

matched_records = []
for p in extracted_projects:
    name = p['Project_Name']
    chunk = p['text_chunk'].lower()
    full_str = (name + " " + chunk).lower()
    
    if "park" in full_str:
        # Check completion in 2022
        # Look for "completed" or "complete construction" near "2022"
        # Using a simple check first
        if "2022" in chunk:
            match1 = re.search(r'completed.{0,50}2022', chunk)
            match2 = re.search(r'complete construction.{0,50}2022', chunk)
            if match1 or match2:
                matched_records.append(p)

total = 0
projects_found = []

if matched_records:
    df_match = pd.DataFrame(matched_records)
    df_match['join_key'] = df_match['Project_Name'].apply(lambda x: x.lower().strip())
    funding_df['join_key'] = funding_df['Project_Name'].apply(lambda x: x.lower().strip())
    
    merged = pd.merge(df_match, funding_df, on='join_key', how='inner')
    # Deduplicate in case we parsed the same project multiple times from different docs or sections
    merged = merged.drop_duplicates(subset=['Project_Name_y'])
    
    total = merged['Amount'].sum()
    projects_found = merged['Project_Name_y'].tolist()

print("__RESULT__:")
print(json.dumps({"total": total, "projects": projects_found}))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json'}

exec(code, env_args)
