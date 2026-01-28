code = """import json
import pandas as pd

funding_path = locals()['var_function-call-14443830636332700640']
docs_path = locals()['var_function-call-14443830636332701107']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(float)

def get_base_name(name):
    # Remove suffix starting with space+parenthesis
    if '(' in name:
        parts = name.split('(')
        # Check if last part ends with )
        if parts[-1].strip().endswith(')'):
            # Join all except last
            return "(".join(parts[:-1]).strip()
    return name.strip()

project_map = {}
for _, row in df_funding.iterrows():
    full_name = row['Project_Name']
    base_name = get_base_name(full_name)
    if base_name not in project_map:
        project_map[base_name] = []
    project_map[base_name].append(row)

base_project_names = set(project_map.keys())
all_project_names = set(df_funding['Project_Name'].tolist())

extracted_projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        is_new_project = False
        matched_name = None
        
        if line in base_project_names:
            is_new_project = True
            matched_name = line
        elif line in all_project_names:
            is_new_project = True
            matched_name = get_base_name(line)
        
        if is_new_project:
            if current_project:
                extracted_projects.append({
                    "name": current_project,
                    "block": current_block
                })
            current_project = matched_name
            current_block = []
        else:
            if current_project:
                current_block.append(line)
    
    if current_project:
        extracted_projects.append({
            "name": current_project,
            "block": current_block
        })

projects_started_2022 = []

for p in extracted_projects:
    name = p['name']
    block_lines = p['block']
    
    start_year = None
    
    # Check lines for start info
    for line in block_lines:
        lower_line = line.lower()
        # Look for start/begin/advertise
        if "begin construction" in lower_line or "advertise" in lower_line or "start" in lower_line:
            # Check for 2022
            if "2022" in line:
                start_year = "2022"
                break
    
    # Identify if disaster
    is_disaster = False
    
    # Text keywords
    block_text = " ".join(block_lines)
    keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Fire", "Disaster", "Emergency"]
    for k in keywords:
        if k in block_text:
            is_disaster = True
            break
            
    # Funding name check
    if not is_disaster:
        recs = project_map.get(name, [])
        for r in recs:
            fname = r['Project_Name']
            if "FEMA" in fname or "CalOES" in fname or "CalJPIA" in fname:
                is_disaster = True
                break
    
    if start_year == "2022" and is_disaster:
        projects_started_2022.append(name)

unique_names = set(projects_started_2022)
total_amount = 0.0
for name in unique_names:
    recs = project_map.get(name, [])
    for r in recs:
        total_amount += r['Amount']

print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "projects": list(unique_names)}))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)
