code = """import json

# Load the JSON data
civic_documents = locals()['var_functions.query_db:5']
funding_over_50k = locals()['var_functions.query_db:30']

# Handle if they are file paths
try:
    if isinstance(civic_documents, str):
        with open(civic_documents) as f:
            civic_documents = json.load(f)
    if isinstance(funding_over_50k, str):
        with open(funding_over_50k) as f:
            funding_over_50k = json.load(f)
except:
    pass

# Build funding dictionary
funded = {}
for record in funding_over_50k:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funded[name] = amount

# Find capital projects in design status
design_capital_projects = set()

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Look for Design section of Capital Improvement Projects
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        
        if end == -1:
            design_section = text[start:]
        else:
            design_section = text[start:end]
        
        # Check for project names in this section
        lines = design_section.split('\n')
        
        for line in lines:
            clean = line.strip()
            if clean in funded:
                # Check if disaster project (FEMA in name)
                if 'fema' not in clean.lower():
                    design_capital_projects.add(clean)

# Additional search for any capital projects mentioned as design
for project_name in funded:
    if project_name in design_capital_projects:
        continue
    
    # Skip disaster projects
    if 'fema' in project_name.lower():
        continue
    
    # Check if project appears in design context
    for doc in civic_documents:
        text = doc.get('text', '')
        if project_name in text:
            design_capital_projects.add(project_name)
            break

result = len(design_capital_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
