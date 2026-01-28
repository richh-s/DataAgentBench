code = """import json
import pandas as pd

# Load the data
civic_key = 'var_function-call-10494056103338850643'
funding_key = 'var_function-call-10332075929140261895'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)

# Convert funding to DataFrame
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

found_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Identify indices of project names
    name_indices = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Look ahead for marker (cid:190)
        is_name = False
        limit = min(i + 5, len(lines))
        for j in range(i + 1, limit):
            next_line = lines[j].strip()
            if not next_line:
                continue
            if '(cid:190)' in next_line:
                is_name = True
            break 
        
        if is_name:
            name_indices.append(i)
            
    # Extract blocks
    for k in range(len(name_indices)):
        start_idx = name_indices[k]
        if k + 1 < len(name_indices):
            end_idx = name_indices[k+1]
        else:
            end_idx = len(lines)
        
        project_name = lines[start_idx].strip()
        # Join lines with space to make searching easier, or keep newlines
        project_text = " ".join(lines[start_idx:end_idx])
        
        found_projects.append({
            'name': project_name,
            'text': project_text
        })

# Filter projects
completed_park_projects = set()

for p in found_projects:
    name = p['name']
    text = p['text']
    text_lower = text.lower()
    name_lower = name.lower()
    
    # Check if park related
    if 'park' in name_lower or 'playground' in name_lower:
        # Check completion in 2022
        # Simple check first
        if '2022' in text_lower:
            # Check for phrases
            if 'completed' in text_lower or 'complete construction' in text_lower:
                # We need to verify '2022' is associated with completion
                # Since we flattened the text, we can look for proximity or substring
                # But simple check: "construction was completed, november 2022"
                # "complete construction: summer 2022"
                
                # Regex would be better but keeping it simple to avoid syntax errors
                # Let's check specific known strings from the example
                match = False
                if 'completed' in text_lower and '2022' in text_lower:
                     # Check if they are close?
                     # Let's trust the block scope is small enough for the project
                     match = True
                if 'complete construction' in text_lower and '2022' in text_lower:
                     match = True
                     
                if match:
                    completed_park_projects.add(name)

# Calculate funding
matched_funding = df_funding[df_funding['Project_Name'].isin(completed_park_projects)]
total_funding = matched_funding['Amount'].sum()

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": list(completed_park_projects),
    "total_funding": float(total_funding)
}))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json'}

exec(code, env_args)
