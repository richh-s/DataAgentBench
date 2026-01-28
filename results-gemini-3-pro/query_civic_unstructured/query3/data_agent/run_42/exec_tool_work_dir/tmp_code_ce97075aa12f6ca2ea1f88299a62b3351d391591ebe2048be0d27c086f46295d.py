code = """import json
import pandas as pd
import re
import os

# Access file paths
funding_file_path = locals()['var_function-call-15139260812561284578']
civic_docs_file_path = locals()['var_function-call-12991954254927401902']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([d['text'] for d in civic_docs])

def normalize_name(name):
    # Regex: space, open paren, any char non-greedy, close paren
    # Using double backslashes for safety
    name = re.sub("\\s*\\(.*?\\)", "", name)
    return name.strip().lower()

funding_df['normalized_name'] = funding_df['Project_Name'].apply(normalize_name)

lines = full_text.split('\n')
current_status = 'unknown'
project_blocks = []
current_project = None
current_block = []

known_names = set(funding_df['normalized_name'].tolist())

# Regex for headers: Capital Improvement Projects (Status)
# pattern: Capital Improvement Projects \((.*?)\)
header_pattern = "Capital Improvement Projects \\((.*?)\\)"
header_re = re.compile(header_pattern, re.IGNORECASE)

for line in lines:
    line_stripped = line.strip()
    if not line_stripped:
        continue
    
    header_match = header_re.search(line_stripped)
    if header_match:
        current_status = header_match.group(1).lower()
        if current_project:
            project_blocks.append({
                "name": current_project,
                "status": block_status,
                "text": "\n".join(current_block)
            })
            current_project = None
            current_block = []
        continue
    
    norm_line = normalize_name(line_stripped)
    # Check if line matches a project name
    if norm_line in known_names and len(norm_line) > 5:
        if current_project:
            project_blocks.append({
                "name": current_project,
                "status": block_status,
                "text": "\n".join(current_block)
            })
        
        current_project = line_stripped
        block_status = current_status
        current_block = []
    else:
        if current_project:
            current_block.append(line_stripped)

if current_project:
    project_blocks.append({
        "name": current_project,
        "status": block_status,
        "text": "\n".join(current_block)
    })

results = []
found_projects = set()

for block in project_blocks:
    norm_name = normalize_name(block['name'])
    matches = funding_df[funding_df['normalized_name'] == norm_name]
    
    for idx, row in matches.iterrows():
        funding_name = row['Project_Name']
        text_lower = block['text'].lower()
        
        is_relevant = False
        if "fema" in funding_name.lower() or "emergency" in funding_name.lower():
            is_relevant = True
        
        if "fema" in text_lower or "emergency" in text_lower:
            is_relevant = True
            
        if is_relevant:
            status = block['status']
            if "completed" in text_lower and "construction was completed" in text_lower:
                status = "completed"
            elif "construction" in status and "under construction" in text_lower:
                status = "construction"
            elif "design" in status:
                status = "design"
            
            # Map 'construction' to 'design' if needed? 
            # Prompt: "Projects have three statuses: 'design', 'completed', and 'not started'".
            # If status is construction, maybe mapped to 'design' (in progress)?
            # Or maybe I should return 'construction' and let user decide.
            # But the prompt says "Projects have three statuses...". This implies the answer should use these terms.
            # "Construction" is definitely NOT "not started". It is NOT "completed".
            # "Design" description says "(in planning/design phase)". Construction is BEYOND design.
            # Maybe the data has "active" or "construction" but the prompt simplifies?
            # I will output "construction" if that's what headers say. 
            # Actually, "Capital Improvement Projects (Construction)" header exists.
            # The prompt might be slightly off or I should map.
            # Let's check "Latigo Canyon Road Retaining Wall Repair Project". Status: Design (header). Text: "Awaiting final FEMA/CalOES approval".
            # "Malibu Road Slope Repairs". Status: Construction (header).
            # I will keep "construction" as it is accurate to the document.
            
            res_entry = {
                "Project_Name": funding_name,
                "Funding_Source": row['Funding_Source'],
                "Amount": row['Amount'],
                "Status": status
            }
            results.append(res_entry)
            found_projects.add(funding_name)

# Add missing FEMA/Emergency projects from Funding
for idx, row in funding_df.iterrows():
    funding_name = row['Project_Name']
    if funding_name not in found_projects:
        if "fema" in funding_name.lower() or "emergency" in funding_name.lower():
            results.append({
                "Project_Name": funding_name,
                "Funding_Source": row['Funding_Source'],
                "Amount": row['Amount'],
                "Status": "Unknown"
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7580785904433881642': ['Funding'], 'var_function-call-7580785904433881717': ['civic_docs'], 'var_function-call-15139260812561284578': 'file_storage/function-call-15139260812561284578.json', 'var_function-call-15139260812561285023': 'file_storage/function-call-15139260812561285023.json', 'var_function-call-12991954254927401902': 'file_storage/function-call-12991954254927401902.json'}

exec(code, env_args)
