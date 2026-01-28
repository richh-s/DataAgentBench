code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic docs
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# High funding projects
high_funding = set()
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding.add(item['Project_Name'])

print('High funding projects:', len(high_funding))

# Extract design capital projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_part = parts[1].split('Capital Improvement Projects (Construction)')[0]
            lines = design_part.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 15 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line:
                    clean = re.sub(r'^(cid:\d+)\s*', '', line)
                    if len(clean) > 15:
                        design_projects.add(clean)

print('Design projects:', len(design_projects))

# Find matches
matches = design_projects.intersection(high_funding)
print('Matches:', len(matches))

result = {
    'high_funding': len(high_funding),
    'design_projects': len(design_projects),
    'matching_count': len(matches),
    'matching_projects': sorted(list(matches))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
