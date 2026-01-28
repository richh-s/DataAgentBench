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
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
            
        # Check if line is a project title
        is_title = False
        
        # Look ahead
        for j in range(i+1, min(i+5, len(lines))):
            next_l = lines[j].strip()
            if not next_l:
                continue
            
            if '(cid:190)' in next_l or 'Updates:' in next_l:
                is_title = True
            break 
        
        if is_title:
            if current_project:
                block_text = '\n'.join(current_block).lower()
                p_name = current_project.strip()
                
                is_park = 'park' in p_name.lower() or 'park' in block_text
                
                is_completed_2022 = False
                if 'construction was completed' in block_text and '2022' in block_text:
                    is_completed_2022 = True
                
                if is_park and is_completed_2022:
                    completed_park_projects_2022.add(p_name)
            
            current_project = stripped
            current_block = []
        else:
            if current_project:
                current_block.append(stripped)

    # Last block
    if current_project:
        block_text = '\n'.join(current_block).lower()
        p_name = current_project.strip()
        
        is_park = 'park' in p_name.lower() or 'park' in block_text
        
        is_completed_2022 = False
        if 'construction was completed' in block_text and '2022' in block_text:
            is_completed_2022 = True
        
        if is_park and is_completed_2022:
            completed_park_projects_2022.add(p_name)

print('identified_projects:', list(completed_park_projects_2022))

total_funding = 0
matched_records = []

for index, row in funding_df.iterrows():
    f_name = row['Project_Name']
    
    # Clean name
    cleaned_name = re.sub(r'\s*\(.*?\)$', '', f_name).strip()
    
    match = False
    if cleaned_name in completed_park_projects_2022:
        match = True
    else:
        for p in completed_park_projects_2022:
            if cleaned_name.lower() == p.lower():
                match = True
                break
    
    if match:
        total_funding += int(row['Amount'])
        matched_records.append(f_name)

print('matched_records:', matched_records)
print('__RESULT__:')
print(total_funding)"""

env_args = {'var_function-call-9204094371275024079': 'file_storage/function-call-9204094371275024079.json', 'var_function-call-9204094371275022852': 'file_storage/function-call-9204094371275022852.json', 'var_function-call-15109130543557145196': 'file_storage/function-call-15109130543557145196.json'}

exec(code, env_args)
