code = """import json
import pandas as pd
import re

# Load Funding Data
funding_path = locals()['var_function-call-9396770381544518491']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load Civic Docs
docs_path = locals()['var_function-call-9396770381544517930']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

extracted_projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_text = ""
    
    for i, line in enumerate(lines):
        sline = line.strip()
        
        # Detect start of a project section via "Updates:"
        if "Updates:" in sline and "Public Works" not in sline and "Agenda" not in sline:
            # Look backwards for the title
            # Title is likely the line before, skipping empty lines
            title = None
            j = i - 1
            while j >= 0:
                prev = lines[j].strip()
                if prev and "Page " not in prev and "Agenda" not in prev:
                    title = prev
                    break
                j -= 1
            
            if title:
                # Save previous project
                if current_project:
                    extracted_projects.append({
                        "name": current_project,
                        "text": current_text
                    })
                
                current_project = title
                current_text = sline + "\n" # start collecting text
        
        elif current_project:
            current_text += sline + "\n"

    # Save last project
    if current_project:
        extracted_projects.append({
            "name": current_project,
            "text": current_text
        })

# Analyze extracted projects
results = []
for p in extracted_projects:
    name = p['name']
    text = p['text']
    
    # Check for disaster keywords in Name (suffixes)
    # Hint: "Disaster project names often include suffixes like '(FEMA Project)', '(CalJPIA Project)', or '(CalOES Project)'."
    is_disaster_name = False
    if "FEMA" in name or "CalOES" in name or "CalJPIA" in name or "Disaster" in name:
        is_disaster_name = True
        
    # Check for start date in 2022
    # Patterns: "Begin Construction: <...2022...>", "Advertise: <...2022...>"
    started_2022 = False
    
    # Regex search for dates associated with start keywords
    # We look for "Begin Construction: ... 2022" or "Advertise: ... 2022"
    # Or "Start Date: ... 2022"
    
    # Normalize text for easier search
    # Replace (cid:131) with nothing?
    
    # Search for "Begin Construction" line
    begin_match = re.search(r'Begin Construction\s*:?[\s\S]{0,20}(202[0-9])', text, re.IGNORECASE)
    if begin_match:
        year = begin_match.group(1)
        if year == '2022':
            started_2022 = True
            
    # Search for "Advertise" line
    if not started_2022:
        adv_match = re.search(r'Advertise\s*:?[\s\S]{0,20}(202[0-9])', text, re.IGNORECASE)
        if adv_match:
            year = adv_match.group(1)
            if year == '2022':
                started_2022 = True

    results.append({
        "extracted_name": name,
        "is_disaster_name": is_disaster_name,
        "started_2022": started_2022,
        "full_text_start": text[:100]
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json'}

exec(code, env_args)
