code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10835669272488718990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10835669272488721645'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

extracted_projects = []

headers_list = ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for doc in civic_docs:
    text = doc['text']
    segments = re.split(r'\(cid:190\)\s*Updates:', text)
    
    for i in range(1, len(segments)):
        prev_segment = segments[i-1].strip()
        prev_lines = [line.strip() for line in prev_segment.split('\n') if line.strip()]
        
        if not prev_lines:
            continue
            
        candidate_name = prev_lines[-1]
        
        if candidate_name in headers_list and len(prev_lines) > 1:
            candidate_name = prev_lines[-2]
            
        body = segments[i]
        
        # Extract Start Date
        st = None
        st_match = re.search(r'Begin [Cc]onstruction:\s*([A-Za-z0-9\s]+)', body)
        if st_match:
            st = st_match.group(1).split('\n')[0].strip()
            
        # Check type/topic
        is_disaster = False
        name_lower = candidate_name.lower()
        body_lower = body.lower()
        
        if "fema" in name_lower or "caloes" in name_lower or "disaster" in name_lower:
            is_disaster = True
        elif "fema" in body_lower or "caloes" in body_lower or "disaster" in body_lower or "woolsey" in body_lower:
            is_disaster = True
            
        extracted_projects.append({
            "name": candidate_name,
            "st": st,
            "is_disaster": is_disaster
        })

target_projects = []
for p in extracted_projects:
    if p['st'] and '2022' in p['st'] and p['is_disaster']:
        target_projects.append(p)

matched_funding = []
total_amount = 0

for p in target_projects:
    p_name = p['name']
    
    # Matching logic:
    # 1. Exact match
    # 2. Starts with p_name
    
    matches = df_funding[df_funding['Project_Name'] == p_name]
    if matches.empty:
        # Escape regex characters in p_name just in case
        safe_p_name = re.escape(p_name)
        matches = df_funding[df_funding['Project_Name'].str.contains(safe_p_name, case=False, na=False)]
    
    if not matches.empty:
        for _, row in matches.iterrows():
            # Avoid duplicate counting if same funding record matched multiple times (unlikely with this loop but good to be safe)
            # Actually, if the text has "Project A" and "Project A (Phase 2)", and we match "Project A", we might get both?
            # But here `p` is distinct project entries from text.
            # We should probably track Funding_ID to avoid duplicates if multiple text entries map to same funding?
            # But the text likely lists unique projects.
            
            matched_funding.append({
                "Project_Name": row['Project_Name'],
                "Amount": row['Amount'],
                "Funding_ID": row['Funding_ID']
            })

# Remove duplicate funding IDs
unique_funding = {f['Funding_ID']: f for f in matched_funding}.values()
total_amount = sum(item['Amount'] for item in unique_funding)

print("__RESULT__:")
print(json.dumps({"projects": list(unique_funding), "total_amount": total_amount, "debug_targets": target_projects}, indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json'}

exec(code, env_args)
