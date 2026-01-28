code = """import json
import re

var_civic_docs = locals()['var_functions.query_db:2']
if isinstance(var_civic_docs, str):
    with open(var_civic_docs, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_civic_docs

var_funding = locals()['var_functions.query_db:6']
if isinstance(var_funding, str):
    with open(var_funding, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_funding

# Create a mapping of project names to funding amounts > 50000
funding_map = {}
for fund in funding_data:
    amount = int(fund.get('Amount', 0))
    if amount > 50000:
        funding_map[fund.get('Project_Name')] = amount

projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the design section
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1]
            # Split into potential project blocks
            blocks = design_section.split('\n\n')
            
            for block in blocks:
                lines = block.split('\n')
                for line in lines:
                    line = line.strip()
                    # Skip empty lines and clear indicators of non-project names
                    if not line:
                        continue
                    if line.startswith('Page') or line.startswith('(') or 'Updates' in line or 'Schedule' in line:
                        continue
                    if ':' in line and len(line) < 50:
                        continue
                    # If line starts with alphanumeric and is reasonably long, it's likely a project name
                    if line[0].isalnum() and len(line) > 10:
                        project_name = line
                        # Check if this project has funding > 50000
                        if project_name in funding_map:
                            amount = funding_map[project_name]
                            proj_type = 'disaster' if any(x in project_name for x in ['(FEMA', '(CalOES', '(CalJPIA']) else 'capital'
                            projects.append({
                                'Project_Name': project_name,
                                'Type': proj_type,
                                'Status': 'design',
                                'Amount': amount
                            })
                        break

capital_design_count = len([p for p in projects if p['Type'] == 'capital'])

print('__RESULT__:')
print(json.dumps(capital_design_count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
