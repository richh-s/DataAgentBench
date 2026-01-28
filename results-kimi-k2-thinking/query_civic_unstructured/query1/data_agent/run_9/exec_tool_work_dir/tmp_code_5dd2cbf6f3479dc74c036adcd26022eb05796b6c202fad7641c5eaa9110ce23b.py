code = """import json

# Get file paths
funding_file = str(locals()['var_functions.query_db:2'])
civic_file = str(locals()['var_functions.query_db:8'])

# Read funding data
funding_data = json.loads(open(funding_file, 'r').read())

# Read civic docs data
civic_docs = json.loads(open(civic_file, 'r').read())

# Filter funding > $50,000
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]

# Create lookup
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in high_funding}

# Extract capital design projects
capital_design = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        # Truncate at next major heading
        for heading in ['Capital Improvement Projects (Construction)', 'Disaster Recovery', 'Capital Improvement Projects (Not Started)']:
            if heading in section:
                section = section.split(heading)[0]
                break
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                if not any(x in line.lower() for x in ['updates', 'schedule', 'advertise', 'construction', 'page', 'agenda item']):
                    capital_design.append(line)

# Match and count
matches = []
seen = set()
for proj in capital_design:
    key = proj.lower()
    if key in funding_lookup and proj not in seen:
        matches.append(proj)
        seen.add(proj)

count = len(matches)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
