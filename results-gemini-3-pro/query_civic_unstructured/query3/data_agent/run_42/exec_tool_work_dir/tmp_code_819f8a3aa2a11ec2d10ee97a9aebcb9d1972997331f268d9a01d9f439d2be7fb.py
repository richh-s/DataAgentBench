code = """import json
import pandas as pd
import re

# Access file paths
funding_file_path = locals()['var_function-call-15139260812561284578']
civic_docs_file_path = locals()['var_function-call-12991954254927401902']

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

with open(civic_docs_file_path, 'r') as f:
    civic_docs = json.load(f)

# Collect lines
lines = []
for d in civic_docs:
    lines.extend(d['text'].split('\n'))

def normalize_name(name):
    # Regex to remove parens content
    # pattern: space* ( .*? )
    pattern = r'\s*\(.*?\)'
    return re.sub(pattern, '', name).strip().lower()

funding_df['normalized_name'] = funding_df['Project_Name'].apply(normalize_name)

project_blocks = []
current_project = None
current_status = 'unknown'
current_block = []
block_status = 'unknown'

known_names = set(funding_df['normalized_name'].tolist())

# Regex for header: Capital Improvement Projects (Status)
# pattern: Capital Improvement Projects \((.*?)\)
header_pattern = r'Capital Improvement Projects \((.*?)\)'

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Check header
    header_match = re.search(header_pattern, line, re.IGNORECASE)
    if header_match:
        current_status = header_match.group(1).lower()
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status,
                'text': ' '.join(current_block)
            })
            current_project = None
            current_block = []
        continue

    norm_line = normalize_name(line)
    if norm_line in known_names and len(norm_line) > 5:
        if current_project:
            project_blocks.append({
                'name': current_project,
                'status': block_status,
                'text': ' '.join(current_block)
            })
        current_project = line
        block_status = current_status
        current_block = []
    else:
        if current_project:
            current_block.append(line)

if current_project:
    project_blocks.append({
        'name': current_project,
        'status': block_status,
        'text': ' '.join(current_block)
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
        if 'fema' in funding_name.lower() or 'emergency' in funding_name.lower():
            is_relevant = True
        if 'fema' in text_lower or 'emergency' in text_lower:
            is_relevant = True
            
        if is_relevant:
            status = block['status']
            if 'completed' in text_lower and 'construction was completed' in text_lower:
                status = 'completed'
            elif 'construction' in status and 'under construction' in text_lower:
                status = 'construction'
            elif 'design' in status:
                status = 'design'
                
            res_entry = {
                'Project_Name': funding_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': status
            }
            results.append(res_entry)
            found_projects.add(funding_name)

# Missing ones
for idx, row in funding_df.iterrows():
    funding_name = row['Project_Name']
    if funding_name not in found_projects:
        if 'fema' in funding_name.lower() or 'emergency' in funding_name.lower():
            results.append({
                'Project_Name': funding_name,
                'Funding_Source': row['Funding_Source'],
                'Amount': row['Amount'],
                'Status': 'not started' # Assumption if not found in design/construction logs? Or 'Unknown'. Prompt says "not started" is a status.
            })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-7580785904433881642': ['Funding'], 'var_function-call-7580785904433881717': ['civic_docs'], 'var_function-call-15139260812561284578': 'file_storage/function-call-15139260812561284578.json', 'var_function-call-15139260812561285023': 'file_storage/function-call-15139260812561285023.json', 'var_function-call-12991954254927401902': 'file_storage/function-call-12991954254927401902.json'}

exec(code, env_args)
