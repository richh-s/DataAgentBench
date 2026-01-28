code = """import json
import re

# Load funding data (projects > $50,000)
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Create a dictionary mapping lowercased project names to funding amounts
funded_amounts = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip().lower()
    funded_amounts[proj_name] = int(record['Amount'])

# Load civic documents data
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status from civic documents
design_capital_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        # Find where design section ends
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start > 0:
            design_section = text[design_start:construction_start]
        else:
            design_section = text[design_start:]
        
        # Extract project names from design section
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty lines and control text
            if len(line) > 5 and not line.startswith('(') and not line.startswith('▪') \
               and 'Capital Improvement Projects' not in line and 'Updates:' not in line \
               and 'Project Schedule:' not in line and 'Estimated Schedule:' not in line \
               and 'Project Description:' not in line and 'Page' not in line \
               and 'RECOMMENDED ACTION:' not in line and 'DISCUSSION:' not in line:
                # Check if next few lines contain project metadata
                context = '\n'.join(lines[i+1:i+4])
                if 'Updates:' in context or 'Project Schedule:' in context or 'Estimated Schedule:' in context:
                    design_capital_projects.append(line)

# Count projects with funding > $50,000
count_over_50000 = 0
matched_projects = []

for project in design_capital_projects:
    proj_lower = project.lower()
    
    # Direct match
    if proj_lower in funded_amounts and funded_amounts[proj_lower] > 50000:
        count_over_50000 += 1
        matched_projects.append({'name': project, 'funding': funded_amounts[proj_lower]})
    else:
        # Check for partial matches
        for funded_name, amount in funded_amounts.items():
            if amount > 50000 and (proj_lower in funded_name or funded_name in proj_lower):
                count_over_50000 += 1
                matched_projects.append({'name': project, 'funded_as': funded_name, 'funding': amount})
                break

print('__RESULT__:')
print(json.dumps({
    'design_capital_projects': len(design_capital_projects),
    'count_over_50000': count_over_50000
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
