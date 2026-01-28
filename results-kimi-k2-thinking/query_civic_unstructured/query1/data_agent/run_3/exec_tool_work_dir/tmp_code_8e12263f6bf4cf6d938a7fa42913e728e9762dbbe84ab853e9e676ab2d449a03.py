code = """import json
import re

funding_data = json.load(open(locals()['var_functions.query_db:2']))
civic_docs = json.load(open(locals()['var_functions.query_db:5']))

# Find design stage capital projects from civic documents
capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for design section and extract project names
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section text
        start = text.index('Capital Improvement Projects (Design)')
        section = text[start:start+2000]
        # Extract lines that are likely project names
        lines = section.split('\n')
        for line in lines:
            clean = line.strip()
            if clean and len(clean) > 10 and 'Project' in clean:
                low = clean.lower()
                if 'fema' not in low and 'disaster' not in low:
                    capital_design_projects.add(clean)

# Count matches with funding > 50000
matches = set()
for record in funding_data:
    if int(record['Amount']) > 50000:
        full_name = record['Project_Name']
        base = full_name.split('(')[0].strip()
        if base in capital_design_projects:
            matches.add(base)

result = {'count': len(matches)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
