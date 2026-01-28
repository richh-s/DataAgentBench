code = """import json
import re

# Read funding data from the file
funding_file = var_functions.query_db:8
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data from the file
civic_file = var_functions.query_db:10
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

print(f'Loaded {len(funding_data)} funding records')
print(f'Loaded {len(civic_docs_data)} civic documents')

# Create a list of project names from funding data for quick lookup
funding_project_names = [item['Project_Name'] for item in funding_data]

# Debug: Show first few project names
print('Sample funding project names:', funding_project_names[:5])

# Find projects by searching for exact matches in the text
matched_projects = []

for funding_name in funding_project_names:
    # Search for this exact name in all civic documents
    for doc in civic_docs_data:
        if funding_name in doc.get('text', ''):
            # Try to determine type and status from context
            text = doc.get('text', '')
            
            # Check if it's in design section
            design_section_start = text.find('Capital Improvement Projects (Design)')
            construction_section_start = text.find('Capital Improvement Projects (Construction)')
            not_started_section_start = text.find('Capital Improvement Projects (Not Started)')
            
            project_pos = text.find(funding_name)
            
            if design_section_start < project_pos and (construction_section_start == -1 or project_pos < construction_section_start) and (not_started_section_start == -1 or project_pos < not_started_section_start):
                # Project is in design section
                if any(keyword in funding_name.lower() for keyword in ['(fema', '(caljpia', '(caloes']):
                    project_type = 'disaster'
                else:
                    project_type = 'capital'
                
                # Get the amount for this project
                amount = next((item['Amount'] for item in funding_data if item['Project_Name'] == funding_name), '0')
                
                matched_projects.append({
                    'Project_Name': funding_name,
                    'type': project_type,
                    'status': 'design',
                    'amount': amount
                })

# Remove duplicates from matched_projects
seen = set()
final_matched = []
for proj in matched_projects:
    if proj['Project_Name'] not in seen:
        final_matched.append(proj)
        seen.add(proj['Project_Name'])

print(f'Found {len(final_matched)} total capital/disaster projects with design status and funding > $50k')

# Count only capital projects (not disaster)
capital_design_count = sum(1 for proj in final_matched if proj['type'] == 'capital')

print('Capital projects with design status and funding > $50k:', capital_design_count)

# Show the capital projects found
capital_projects = [proj for proj in final_matched if proj['type'] == 'capital']
print('Capital projects found:', capital_projects)

result = {
    'count': capital_design_count,
    'projects': capital_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
