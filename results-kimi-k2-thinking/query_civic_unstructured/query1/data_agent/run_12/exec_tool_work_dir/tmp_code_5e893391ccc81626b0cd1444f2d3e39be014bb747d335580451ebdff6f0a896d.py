code = """import json

# Get the file paths
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:1']

# Read funding data
f = open(funding_path)
funding_data = json.load(f)
f.close()

# Read civic data
c = open(civic_path)
civic_data = json.load(c)
c.close()

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    amt = int(item['Amount'])
    if amt > 50000:
        funding_lookup[item['Project_Name']] = amt

# Find capital design projects
projects = set()

for doc in civic_data:
    txt = doc.get('text', '')
    if not txt:
        continue
    
    # Find design section
    marker = 'Capital Improvement Projects (Design)'
    if marker not in txt:
        continue
    
    start = txt.index(marker) + len(marker)
    section = txt[start:]
    
    # Find section end
    construction_marker = 'Capital Improvement Projects (Construction)'
    not_started_marker = 'Capital Improvement Projects (Not Started)'
    disaster_marker = 'Disaster Recovery Projects'
    
    ends = []
    for m in [construction_marker, not_started_marker, disaster_marker]:
        pos = section.find(m)
        if pos > 0:
            ends.append(pos)
    
    if ends:
        end = min(ends)
        section = section[:end]
    
    # Extract project names
    for line in section.split('\n'):
        line = line.strip()
        if len(line) < 5:
            continue
        if line.startswith('(') or line.startswith('-') or line.startswith('•'):
            continue
        
        # Skip metadata
        if 'Updates' in line or 'Schedule' in line:
            continue
        if 'Complete Design' in line or 'Advertise' in line:
            continue
        if 'Begin Construction' in line:
            continue
        if 'Capital Improvement' in line:
            continue
        if 'Project Description' in line:
            continue
        
        # Check if funded
        if line in funding_lookup:
            projects.add(line)

result = {
    'count': len(projects),
    'projects': sorted(list(projects))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:24': {'funding_records': 276, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}}}

exec(code, env_args)
