code = """import json, re

# Load data
with open(locals()['var_functions.query_db:2'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:8'], 'r') as f:
    civic_docs = json.load(f)

# Filter high funding projects
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]
print(f'High funding projects: {len(high_funding)}')

# Build funding lookup
funding_lookup = {}
for f in high_funding:
    funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])

# Extract capital design projects
capital_design = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Get design section
        section = text.split('Capital Improvement Projects (Design)')[1]
        # Remove subsequent sections
        for heading in ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']:
            if heading in section:
                section = section.split(heading)[0]
                break
        
        # Extract lines that look like project names
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and len(line) < 100 and line[0].isupper():
                # Skip non-project lines
                skip = ['Project Schedule', 'Updates', 'Complete Design', 'Advertise', 'Begin Construction', 'Page', 'Agenda Item', '(cid:', '•']
                if not any(s in line for s in skip):
                    capital_design.append(line)

print(f'Design projects found: {len(capital_design)}')

# Match projects
matches = []
seen = set()
for proj in capital_design:
    proj_key = proj.lower()
    if proj_key in funding_lookup and proj not in seen:
        matches.append({'name': proj, 'amount': funding_lookup[proj_key]})
        seen.add(proj)

print(f'Matches found: {len(matches)}')

# Return count
result = len(matches)
print('__RESULT__:')
print(json.dumps({'count': result, 'matches': matches[:5]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
