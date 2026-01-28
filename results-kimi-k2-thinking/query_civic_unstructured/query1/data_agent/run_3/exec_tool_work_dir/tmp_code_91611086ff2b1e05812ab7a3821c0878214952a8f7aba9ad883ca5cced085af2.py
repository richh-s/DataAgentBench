code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find capital design projects
capital_design = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for the design section header
    if 'Capital Improvement Projects (Design)' in text:
        # Extract project names until we hit the next section
        pattern = r'Capital Improvement Projects \(Design\)(.+?)Capital Improvement Projects \(Construction\)'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            section = match.group(1)
            # Find lines that look like project names
            for line in section.split('\n'):
                clean = line.strip()
                if clean and len(clean) > 8 and 'Project' in clean and 'fema' not in clean.lower():
                    capital_design.add(clean)

# Match with funding > 50000
matched = set()
for record in funding_data:
    if int(record['Amount']) > 50000:
        proj = record['Project_Name']
        base = re.sub(r'\s*\([^)]*\)$', '', proj)
        if base in capital_design:
            matched.add(base)

result = {'count': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
