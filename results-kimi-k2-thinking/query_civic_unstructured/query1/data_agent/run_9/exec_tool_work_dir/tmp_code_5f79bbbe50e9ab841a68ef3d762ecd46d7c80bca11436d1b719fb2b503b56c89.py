code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:50']
civic_file = locals()['var_functions.query_db:8']

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for projects > 50k
funding_lookup = {}
for rec in funding_records:
    name = rec['Project_Name'].lower().strip()
    funding_lookup[name] = int(rec['Amount'])
    # Also add base name without parenthetical
    base = re.sub(r'\s*\([^)]*\)$', '', name)
    if base != name:
        funding_lookup[base] = int(rec['Amount'])

# Extract capital design projects
design_proj = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        part = text.split('Capital Improvement Projects (Design)')[1]
        # Cut off at next section
        if 'Capital Improvement Projects (Construction)' in part:
            part = part.split('Capital Improvement Projects (Construction)')[0]
        
        for line in part.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                # Skip metadata lines
                if any(x in line for x in ['Updates:', 'Schedule:', 'Page ', 'Agenda Item', '(cid:', '•']):
                    continue
                if any(x in line for x in ['Complete Design', 'Advertise:', 'Construction:']):
                    continue
                
                clean = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', line)
                if len(clean) > 10:
                    design_proj.append(clean.lower())

# Count matches with funding
count = 0
seen = set()
for proj in design_proj:
    if proj in funding_lookup and proj not in seen:
        count += 1
        seen.add(proj)

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
