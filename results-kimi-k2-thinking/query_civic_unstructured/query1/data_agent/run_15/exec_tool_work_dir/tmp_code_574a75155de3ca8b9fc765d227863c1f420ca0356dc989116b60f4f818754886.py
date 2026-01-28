code = """import json
import re

# Load funding data
f_path = locals()['var_functions.query_db:38']
with open(f_path) as f:
    funding_data = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:40']
with open(c_path) as f:
    civic_docs = json.load(f)

# Step 1: Get projects with funding > 50000
high_funding = {}
for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        high_funding[rec['Project_Name']] = amount

print('High funding projects:', len(high_funding))

# Step 2: Extract design capital projects from documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            
            for line in section.split('\n'):
                line = line.strip()
                if line and len(line) > 15 and line[0] not in ['(', '-', '•']:
                    if 'Updates:' not in line and 'Schedule:' not in line:
                        clean = re.sub(r'^(cid:\d+)\s*', '', line)
                        if len(clean) > 15:
                            design_projects.append(clean)

print('Design projects:', len(design_projects))

# Step 3: Find matches
matches = []
for design_proj in design_projects:
    if design_proj in high_funding:
        matches.append(design_proj)

print('Matches:', len(matches))

result = {
    'high_funding_count': len(high_funding),
    'design_count': len(design_projects),
    'match_count': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
