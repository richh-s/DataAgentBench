code = """import json
import pandas as pd

civic_key = 'var_function-call-10494056103338850643'
funding_key = 'var_function-call-10332075929140261895'
marker = "(cid:190)"

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
# Clean Amount: remove '$', ',' if any (though sample showed ints in string '24000')
# The sample showed "Amount": "24000". So to_numeric is fine.
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)

found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    name_indices = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        is_name = False
        limit = min(i + 5, len(lines))
        for j in range(i + 1, limit):
            next_line = lines[j].strip()
            if not next_line:
                continue
            if marker in next_line:
                is_name = True
            break
        
        if is_name:
            name_indices.append(i)
            
    for k in range(len(name_indices)):
        start_idx = name_indices[k]
        if k + 1 < len(name_indices):
            end_idx = name_indices[k+1]
        else:
            end_idx = len(lines)
        
        project_name = lines[start_idx].strip()
        project_text = " ".join(lines[start_idx:end_idx])
        
        found_projects.append({
            "name": project_name,
            "text": project_text
        })

completed_park_projects = set()

for p in found_projects:
    name = p['name']
    text = p['text']
    text_lower = text.lower()
    name_lower = name.lower()
    
    if "park" in name_lower or "playground" in name_lower:
        # Check for completion in 2022
        # Use simple string check logic
        # Must have "2022"
        if "2022" in text_lower:
            # Must have "completed" or "complete construction"
            if "completed" in text_lower or "complete construction" in text_lower:
                completed_park_projects.add(name)

matched_funding = df_funding[df_funding['Project_Name'].isin(completed_park_projects)]
total_funding = matched_funding['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": float(total_funding)
}))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json'}

exec(code, env_args)
