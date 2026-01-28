code = """import json

# Get file paths
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:8']

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Filter funding > $50k
high_funding = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.append(f)

# Build lookup
funding_lookup = {}
for h in high_funding:
    funding_lookup[h['Project_Name'].lower()] = int(h['Amount'])

print('Funding lookup size:', len(funding_lookup))

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        
        # Truncate at next section
        for heading in ['Capital Improvement Projects (Construction)', 'Disaster Recovery', 'Capital Improvement Projects (Not Started)']:
            if heading in section:
                section = section.split(heading)[0]
                break
        
        # Find lines that start with capital letters and look like project names
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                checks = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Construction', 'Page ', 'Agenda Item', '(cid:']
                skip = any(c in line for c in checks)
                if not skip:
                    design_projects.append(line)

print('Design projects found:', len(design_projects))

# Match
matched = []
seen = set()
for proj in design_projects:
    if proj.lower() in funding_lookup and proj not in seen:
        matched.append(proj)
        seen.add(proj)

print('Final matches:', len(matched))

result = len(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
