code = """import json

# Load data from file paths
funding_path = locals()['var_functions.query_db:40']
civic_path = locals()['var_functions.query_db:5']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_documents = json.load(f)

# Extract capital design projects from civic documents
design_project_names = set()

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Find the design section using simple string search
    design_header = 'Capital Improvement Projects (Design)'
    construction_header = 'Capital Improvement Projects (Construction)'
    
    if design_header in text:
        start = text.index(design_header)
        
        # Find end of section
        end = len(text)
        if construction_header in text[start:]:
            end = start + text[start:].index(construction_header)
        
        section = text[start:end]
        
        # Find project names (lines with 'Project' and reasonable length)
        for line in section.split('\n'):
            clean = line.strip()
            if clean and len(clean) > 10 and 'Project' in clean.lower():
                # Only add capital projects (not FEMA/disaster)
                if 'fema' not in clean.lower() and 'disaster' not in clean.lower():
                    design_project_names.add(clean)

# Match with funding data > $50,000
matched_projects = set()

for funding in funding_records:
    amount = int(funding['Amount'])
    if amount > 50000:
        project_name = funding['Project_Name']
        
        # Remove suffixes like (FEMA Project), (CalOES Project), etc.
        if '(' in project_name:
            base_name = project_name[:project_name.index('(')].strip()
        else:
            base_name = project_name
        
        if base_name in design_project_names:
            matched_projects.add(base_name)

# Result
count = len(matched_projects)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
