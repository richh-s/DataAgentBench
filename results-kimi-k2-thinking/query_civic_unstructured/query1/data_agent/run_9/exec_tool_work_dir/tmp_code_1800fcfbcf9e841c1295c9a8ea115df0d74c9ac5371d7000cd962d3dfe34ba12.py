code = """import json, re

# Load data
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:8']

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    docs = json.load(f)

# Build high funding set (>50k)
high_funding = {}
for rec in funding:
    amount = int(rec['Amount'])
    if amount > 50000:
        high_funding[rec['Project_Name'].lower()] = amount

# Extract capital design projects
design_projects = []

for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in txt:
        continue
    
    # Get design section
    parts = txt.split('Capital Improvement Projects (Design)')
    if len(parts) < 2:
        continue
    
    section = parts[1]
    # Truncate at next major heading
    end_headings = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']
    for heading in end_headings:
        if heading in section:
            section = section.split(heading)[0]
    
    # Parse project names
    for line in section.splitlines():
        line = line.strip()
        if len(line) < 8:
            continue
        
        # Filter out non-project lines
        if any(x in line for x in ['Updates', 'Schedule', 'Page', 'Agenda Item', '(cid:', '•', '◆']):
            continue
        
        # Check if it looks like a project name
        if line[0].isupper() and not line.isupper():
            clean_line = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', line)
            if len(clean_line) > 10:
                design_projects.append(clean_line)

# Deduplicate
duplicates_removed = []
seen = set()
for proj in design_projects:
    if proj.lower() not in seen:
        duplicates_removed.append(proj)
        seen.add(proj.lower())

# Count matches
matches = 0
matched_set = set()
for proj in duplicates_removed:
    if proj.lower() in high_funding and proj not in matched_set:
        matches += 1
        matched_set.add(proj)

# Output just the count
print('__RESULT__:')
print(str(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
