code = """import json
import pandas as pd
import re

# Load paths
f_path = locals()['var_function-call-9396770381544518491']
d_path = locals()['var_function-call-9396770381544517930']

with open(f_path, 'r') as f:
    funding_list = json.load(f)

with open(d_path, 'r') as f:
    docs_list = json.load(f)

# Collect all project info
candidates = []

for doc in docs_list:
    text = doc['text']
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    lines = text.split('\n')
    
    current_name = ""
    current_chunk = ""
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        if "Updates:" in line:
            # The name is likely in the previous non-empty lines
            # Search backwards
            k = i - 1
            name_candidate = "Unknown"
            while k >= 0:
                prev = lines[k].strip()
                if prev and "Page" not in prev and "Agenda" not in prev and "Status Report" not in prev:
                    name_candidate = prev
                    break
                k -= 1
            
            # Now extract the block for this project
            # It starts from 'line' (Updates:) until the next project name?
            # Or usually until the next header?
            # We will read ahead until we hit a line that looks like a header (or next Updates)
            
            block_text = line + "\n"
            m = i + 1
            while m < len(lines):
                next_line = lines[m].strip()
                if "Updates:" in next_line: # Next project started
                     break
                block_text += next_line + "\n"
                m += 1
            
            candidates.append({
                "name": name_candidate,
                "text": block_text
            })

# Filter
final_matches = []
for c in candidates:
    name = c['name']
    text = c['text']
    
    # 1. Check Disaster Type
    # Priority: Name suffix in Funding data.
    # We will try to match this name to Funding data later.
    # But strictly based on extraction:
    is_disaster = False
    if "FEMA" in name or "CalOES" in name or "Disaster" in name:
        is_disaster = True
    
    # 2. Check Start Date 2022
    # Look for "Begin Construction...2022" or "Advertise...2022"
    started_2022 = False
    
    # Regex
    # Case insensitive
    # Allow some chars between keyword and date
    if re.search(r'Begin Construction.*?2022', text, re.IGNORECASE):
        started_2022 = True
    elif re.search(r'Advertise.*?2022', text, re.IGNORECASE):
        started_2022 = True
    
    final_matches.append({
        "extracted_name": name,
        "is_disaster": is_disaster,
        "started_2022": started_2022,
        "raw_snippet": text[:100]
    })

print("__RESULT__:")
print(json.dumps(final_matches))"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json'}

exec(code, env_args)
