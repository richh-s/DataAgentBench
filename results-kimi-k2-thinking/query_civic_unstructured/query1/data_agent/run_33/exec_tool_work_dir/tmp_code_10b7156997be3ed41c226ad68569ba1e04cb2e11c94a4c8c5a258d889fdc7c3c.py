code = """import json

# Load the funding data
funding_file = var_functions.query_db:8
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic documents
civic_file = var_functions.query_db:10
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Extract project names from funding data
project_names = [item['Project_Name'] for item in funding_data]

print('Total projects with >$50k funding:', len(project_names))

# Simple approach: look for projects mentioned in design sections
design_projects = set()

# Process each civic document
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find design sections
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start >= 0:
        # Get the design section text
        design_section_end = construction_start if construction_start >= 0 else len(text)
        design_section = text[design_start:design_section_end]
        
        # Check which projects appear in this section
        for proj_name in project_names:
            if proj_name in design_section:
                design_projects.add(proj_name)

# Remove disaster projects (only keep capital projects)
capital_design_projects = []
for proj in design_projects:
    if '(FEMA' not in proj and '(CalJPIA' not in proj and '(CalOES' not in proj:
        capital_design_projects.append(proj)

print('Capital projects with status=design and funding>$50k:', len(capital_design_projects))
print('Sample projects:', capital_design_projects[:5])

result = {'count': len(capital_design_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
