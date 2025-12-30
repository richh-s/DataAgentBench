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

headers_list = [
    "Capital Improvement Projects (Design)", 
    "Capital Improvement Projects (Construction)", 
    "Capital Improvement Projects (Not Started)", 
    "Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc['text']
    # Regex to split: find 'Updates:' preceded by the bullet char
    # We use . to match the bullet char to avoid encoding issues
    segments = re.split(r'.\s*Updates:', text)
    
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
        # Look for 'Begin Construction:'
        st_match = re.search(r'Begin Construction:\s*([A-Za-z0-9\s]+)', body)
        if st_match:
            st = st_match.group(1).split('\n')[0].strip()
        else:
             # Try finding date in 'Project Schedule' section generally?
             pass

        # Check type/topic
        is_disaster = False
        name_lower = candidate_name.lower()
        body_lower = body.lower()
        
        # Check explicit keywords
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
    # Check if started in 2022
    if p['st'] and '2022' in p['st'] and p['is_disaster']:
        target_projects.append(p)

matched_funding = []

for p in target_projects:
    p_name = p['name']
    
    # Match in funding DB
    # Filter by name
    matches = df_funding[df_funding['Project_Name'] == p_name]
    if matches.empty:
        # Partial match
        safe_p_name = re.escape(p_name)
        matches = df_funding[df_funding['Project_Name'].str.contains(safe_p_name, case=False, na=False)]
    
    if not matches.empty:
        for _, row in matches.iterrows():
            matched_funding.append({
                "Project_Name": row['Project_Name'],
                "Amount": row['Amount'],
                "Funding_ID": row['Funding_ID']
            })

# Unique funding IDs
unique_funding = {}
for item in matched_funding:
    unique_funding[item['Funding_ID']] = item

total_amount = sum(item['Amount'] for item in unique_funding.values())

print("__RESULT__:")
print(json.dumps({
    "projects": list(unique_funding.values()), 
    "total_amount": total_amount, 
    "debug_targets": target_projects
}, indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json'}

exec(code, env_args)
