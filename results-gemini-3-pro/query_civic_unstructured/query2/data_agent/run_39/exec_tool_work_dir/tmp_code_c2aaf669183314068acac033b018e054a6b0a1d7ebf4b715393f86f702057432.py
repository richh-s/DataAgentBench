code = """import json
import pandas as pd
import re

# Load Funding Data
with open('var_function-call-9204094371275024079', 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
with open('var_function-call-15109130543557145196', 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']
    if not text:
        continue
    
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    # Identify project blocks
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check if line is a project title
        # Heuristic: Line i is title if line i+1 (skipping empty) starts with (cid:190) or "Updates:"
        is_title = False
        
        # Look ahead limited lines
        dist = 0
        for j in range(i+1, len(lines)):
            next_l = lines[j].strip()
            if not next_l:
                continue
            
            if next_l.startswith('(cid:190)') or next_l.startswith('Updates:') or 'Updates:' in next_l:
                is_title = True
            
            # If we found a non-empty line and it wasn't the updates marker, then this line i probably isn't a title
            # Unless the marker is further down? Based on sample, it's immediate.
            # Sample:
            # "Project Name"
            # ""
            # "(cid:190) Updates:"
            break 
        
        if is_title:
            # Save previous
            if current_project:
                # Analyze previous block
                block_text = "\n".join(current_block).lower()
                p_name = current_project.strip()
                
                is_park = 'park' in p_name.lower() or 'park' in block_text
                is_completed_2022 = False
                
                # Check for completion in 2022
                # Look for "construction was completed" and "2022"
                if 'construction was completed' in block_text and '2022' in block_text:
                    is_completed_2022 = True
                
                if is_park and is_completed_2022:
                    completed_park_projects_2022.add(p_name)
            
            current_project = stripped
            current_block = []
        else:
            if current_project:
                current_block.append(stripped)

    # Process last block
    if current_project:
        block_text = "\n".join(current_block).lower()
        p_name = current_project.strip()
        
        is_park = 'park' in p_name.lower() or 'park' in block_text
        is_completed_2022 = False
        
        if 'construction was completed' in block_text and '2022' in block_text:
            is_completed_2022 = True
        
        if is_park and is_completed_2022:
            completed_park_projects_2022.add(p_name)

print("identified_projects:", list(completed_park_projects_2022))

total_funding = 0
matched_funding_records = []

for index, row in funding_df.iterrows():
    f_name = row['Project_Name']
    
    # Clean name
    # Remove (Suffix)
    cleaned_name = re.sub(r'\s*\(.*?\)$', '', f_name).strip()
    
    # Check if cleaned name is in our set
    # We might need fuzzy matching or exact.
    # The set has names extracted from docs.
    # Let's check for exact match first.
    
    match = False
    if cleaned_name in completed_park_projects_2022:
        match = True
    else:
        # Try case insensitive
        for p in completed_park_projects_2022:
            if cleaned_name.lower() == p.lower():
                match = True
                break
    
    if match:
        total_funding += int(row['Amount'])
        matched_funding_records.append(f_name)

print("matched_records:", matched_funding_records)
print("__RESULT__:")
print(total_funding)"""

env_args = {'var_function-call-9204094371275024079': 'file_storage/function-call-9204094371275024079.json', 'var_function-call-9204094371275022852': 'file_storage/function-call-9204094371275022852.json', 'var_function-call-15109130543557145196': 'file_storage/function-call-15109130543557145196.json'}

exec(code, env_args)
