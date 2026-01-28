code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-11119621278912765381'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10468269192346586678'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    clean_lines = [l.strip() for l in lines]
    
    # Identify indices of lines containing "Updates:"
    # Also handle the (cid:190) marker if present
    update_indices = []
    for i, line in enumerate(clean_lines):
        if "Updates:" in line:
            update_indices.append(i)
            
    for k, idx in enumerate(update_indices):
        # Name is the previous non-empty line
        name_idx = idx - 1
        while name_idx >= 0 and clean_lines[name_idx] == "":
            name_idx -= 1
            
        if name_idx < 0:
            continue
            
        project_name = clean_lines[name_idx]
        
        # End of block is the start of the next project (next name_idx)
        # Or end of text
        if k + 1 < len(update_indices):
            next_idx = update_indices[k+1]
            next_name_idx = next_idx - 1
            while next_name_idx >= 0 and clean_lines[next_name_idx] == "":
                next_name_idx -= 1
            block_end = next_name_idx
        else:
            block_end = len(clean_lines)
            
        block_lines = clean_lines[name_idx:block_end]
        block_text = " ".join(block_lines)
        
        extracted_projects.append({"name": project_name, "text": block_text})

matched_names = set()

for proj in extracted_projects:
    text_lower = proj['text'].lower()
    name_lower = proj['name'].lower()
    
    # Topic Check
    if "park" not in name_lower and "park" not in text_lower:
        continue
        
    # Status/Date Check
    # Must be completed in 2022
    # Check for "completed" and "2022"
    if "completed" in text_lower and "2022" in text_lower:
        # Check context
        # 1. "Construction was completed ... 2022"
        # 2. "Completed ... 2022"
        # We want to avoid "Complete Design: 2022"
        
        # Regex to find "completed" not preceded by "design" (roughly)
        # Or simpler: if "construction" appears in the same text block, it's likely a construction project.
        # If "design" appears, we must be careful.
        
        # Let's check for specific positive phrases
        if "construction was completed" in text_lower:
            # Check if 2022 is in the text
            if "2022" in text_lower:
                matched_names.add(proj['name'])
        elif "notice of completion" in text_lower and "2022" in text_lower:
             matched_names.add(proj['name'])
        elif "project is complete" in text_lower and "2022" in text_lower:
             matched_names.add(proj['name'])
        else:
            # Fallback: check proximity
            # If "completed" and "2022" are within X characters
            # And "design" is NOT within that window
            pass

# Normalize names
matched_names_list = list(matched_names)
matched_names_norm = [n.strip() for n in matched_names_list]

# Filter funding
# Exact match might fail due to "Project" suffix or similar.
# The prompt says: "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
# So exact match (trimmed) is expected.
funding_matched = df_funding[df_funding['Project_Name'].str.strip().isin(matched_names_norm)]

total_amount = pd.to_numeric(funding_matched['Amount']).sum()

print("__RESULT__:")
print(json.dumps({
    "matched_projects": matched_names_norm,
    "funding_rows": funding_matched.to_dict(orient='records'),
    "total_funding": int(total_amount)
}))"""

env_args = {'var_function-call-5712816459567478650': ['civic_docs'], 'var_function-call-5712816459567478655': ['Funding'], 'var_function-call-13090257420212352430': 'file_storage/function-call-13090257420212352430.json', 'var_function-call-13090257420212352471': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11119621278912765381': 'file_storage/function-call-11119621278912765381.json', 'var_function-call-10468269192346586678': 'file_storage/function-call-10468269192346586678.json'}

exec(code, env_args)
