code = """import json
import pandas as pd

# Keys
key_funding = locals()['var_function-call-10032448971430008742']
key_docs = locals()['var_function-call-17801199440429665660']

# Load data
with open(key_funding, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(int)

# Funding lookup
funding_lookup = {}
for _, row in df_funding.iterrows():
    funding_lookup[row['Project_Name']] = row['Amount']

valid_projects = set(funding_lookup.keys())

with open(key_docs, 'r') as f:
    civic_docs = json.load(f)

disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey']

matched_records = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    
    # Identify project indices
    project_indices = []
    for idx, line in enumerate(lines):
        clean = line.strip()
        if clean in valid_projects:
            project_indices.append((idx, clean))
            
    # Process blocks
    for i in range(len(project_indices)):
        start_idx, p_name = project_indices[i]
        # Determine end index
        if i + 1 < len(project_indices):
            end_idx = project_indices[i+1][0]
        else:
            end_idx = len(lines)
            
        block_lines = lines[start_idx:end_idx]
        block_text = " ".join(block_lines).lower()
        
        # Check start date
        start_2022 = False
        # Keywords
        if 'begin construction' in block_text or 'start date' in block_text or 'st:' in block_text:
            # Check line by line for 2022 near keyword
            for bl in block_lines:
                bl_lower = bl.lower()
                if ('begin construction' in bl_lower or 'start date' in bl_lower or 'st:' in bl_lower):
                    if '2022' in bl_lower:
                        start_2022 = True
                        break
        
        if not start_2022:
            continue
            
        # Check disaster
        is_disaster = False
        if any(k in p_name for k in disaster_keywords):
            is_disaster = True
        elif any(k.lower() in block_text for k in disaster_keywords):
            is_disaster = True
            
        if is_disaster:
            # Try to map to specific funding record
            best_match = p_name
            potential_suffixes = [' (FEMA Project)', ' (CalOES Project)', ' (CalJPIA Project)', ' (FEMA/CalOES Project)']
            for suffix in potential_suffixes:
                candidate = p_name + suffix
                if candidate in funding_lookup:
                    best_match = candidate
                    break
            
            matched_records.append(best_match)

unique_projects = list(set(matched_records))
total = sum(funding_lookup[p] for p in unique_projects)

print("__RESULT__:")
print(json.dumps({
    "projects": unique_projects,
    "total_funding": total
}))"""

env_args = {'var_function-call-10032448971430008742': 'file_storage/function-call-10032448971430008742.json', 'var_function-call-17801199440429665660': 'file_storage/function-call-17801199440429665660.json'}

exec(code, env_args)
