code = """import json
import re

# Load the data files
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Extract capital projects with design status from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Design' in text:
        # Find capital improvement design section
        start = text.find('Capital Improvement Projects (Design)')
        if start > -1:
            # Get section until next major heading
            subsection = text[start:start+2000]
            lines = subsection.split('\n')
            for line in lines:
                stripped = line.strip()
                if stripped and len(stripped) > 10 and 'Project' in stripped and 'fema' not in stripped.lower():
                    design_projects.add(stripped)

# Count funded projects > 50000
count = 0
funded_names = set()

for record in funding_data:
    amount = int(record['Amount'])
    project_name = record['Project_Name']
    
    if amount > 50000:
        # Match base name without suffix
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
        if base_name in design_projects:
            funded_names.add(base_name)

count = len(funded_names)

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
