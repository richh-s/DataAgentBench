code = """import json, re

# Load data
f_file = locals()['var_functions.query_db:2']
c_file = locals()['var_functions.query_db:8']

with open(f_file, 'r') as f:
    funding_data = json.load(f)
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for >50k
high_funding = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.append(f['Project_Name'].lower())
funding_set = set(high_funding)

# Extract design projects
design_proj_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        if 'Capital Improvement Projects (Construction)' in section:
            section = section.split('Capital Improvement Projects (Construction)')[0]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                skip = ['Updates', 'Schedule', 'Design', 'Advertise', 'Construction', 'Page ', 'Agenda Item', '(cid:']
                if not any(s in line for s in skip):
                    design_proj_names.append(line)

# Deduplicate
unique_names = []
unique_set = set()
for name in design_proj_names:
    lower_name = name.lower()
    if lower_name not in unique_set:
        unique_names.append(name)
        unique_set.add(lower_name)

# Count matches
matched = 0
seen = set()
for name in unique_names:
    if name.lower() in funding_set and name not in seen:
        matched += 1
        seen.add(name)

print('__RESULT__:')
print(matched)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
