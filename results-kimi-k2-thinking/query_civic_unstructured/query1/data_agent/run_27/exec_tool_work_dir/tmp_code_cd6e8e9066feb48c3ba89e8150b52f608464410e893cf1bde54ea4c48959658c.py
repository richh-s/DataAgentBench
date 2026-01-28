code = """import json

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

# First, just extract all project names from design section
project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1]
            # Find lines that are not empty and don't contain certain patterns
            for line in design_section.split('\n'):
                line = line.strip()
                if line and not line.startswith('Page') and not line.startswith('(') and 'Updates' not in line and 'Schedule' not in line and ':' not in line:
                    project_names.append(line)

# Now check funding for each project
funding_threshold = 50000
capital_design_projects = []

for pname in project_names:
    # Check if it's a capital project (not disaster)
    is_disaster = any(marker in pname for marker in ['(FEMA', '(CalOES', '(CalJPIA'])
    if not is_disaster:
        # Check funding
        for fund in funding_data:
            if fund.get('Project_Name') == pname:
                amount = int(fund.get('Amount', 0))
                if amount > funding_threshold:
                    capital_design_projects.append({
                        'name': pname,
                        'amount': amount
                    })
                break

count = len(capital_design_projects)

result = {
    'count': count,
    'projects': capital_design_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
