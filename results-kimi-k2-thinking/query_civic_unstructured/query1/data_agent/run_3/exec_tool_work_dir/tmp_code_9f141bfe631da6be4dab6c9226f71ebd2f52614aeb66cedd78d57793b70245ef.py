code = """import json

# Load data from files
funding_path = locals()['var_functions.query_db:40']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_db = json.load(f)

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_db = json.load(f)

# Extract capital design project names from civic documents
design_project_list = []

for doc in civic_db:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    for line in lines:
        clean_line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
        elif 'Capital Improvement Projects (Construction)' in clean_line or 'Disaster Recovery' in clean_line:
            in_design_section = False
        elif in_design_section:
            if clean_line and len(clean_line) > 10 and 'Project' in clean_line:
                lower_line = clean_line.lower()
                if 'fema' not in lower_line and 'disaster' not in lower_line:
                    design_project_list.append(clean_line)

# Convert to set for uniqueness
design_set = set(design_project_list)

# Find matching funded projects > $50,000
matched_projects = []

for funding in funding_db:
    amount = int(funding['Amount'])
    if amount > 50000:
        full_name = funding['Project_Name']
        # Remove parenthetical suffix
        if '(' in full_name:
            base_name = full_name.split('(')[0].strip()
        else:
            base_name = full_name
        
        # Check if matches a design project
        if base_name in design_set:
            matched_projects.append(base_name)

# Count unique matches
result_count = len(set(matched_projects))

# Output result
print('__RESULT__:')
print(json.dumps({'count': result_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
