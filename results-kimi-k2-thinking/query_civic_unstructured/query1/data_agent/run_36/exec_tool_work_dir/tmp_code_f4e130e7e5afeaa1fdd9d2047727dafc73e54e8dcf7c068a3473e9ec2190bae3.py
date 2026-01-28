code = """import json

# Load funding data > $50,000
f_file = var_functions.query_db:44
with open(f_file) as f:
    funding_records = json.load(f)

# Load civic documents
c_file = var_functions.query_db:28 
with open(c_file) as f:
    civic_docs = json.load(f)

# Extract capital design projects from civic documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_section = ''
    lines = text.split('\n')
    in_design = False
    
    for line in lines:
        lower_line = line.lower().strip()
        if 'capital improvement projects (design)' in lower_line:
            in_design = True
            continue
        if in_design:
            if any(marker in lower_line for marker in ['projects (construction)', 'disaster recovery projects', 'projects (not started)']):
                break
            if len(line.strip()) > 8 and not any(exclude in lower_line for exclude in ['updates:', 'project schedule', 'subject:', 'cid:']):
                project_name = line.strip().lstrip('0123456789.-• ')
                if len(project_name) > 8 and ' ' in project_name:
                    design_projects.append(project_name)

# Filter funding > $50,000
high_funding = [f for f in funding_records if int(f.get('Amount', 0)) > 50000]

# Match projects by name
matches = set()
for design in design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        # Check if names match or are similar
        if (design_lower == fund_name or 
            design_lower in fund_name or 
            fund_name in design_lower or
            any(word in fund_name for word in design_lower.split()[:3] if len(word) > 4)):
            matches.add(design)
            break

result = {'count': len(matches), 'projects': list(matches)[:10]}
print('___RESULT:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
