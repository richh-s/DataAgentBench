code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:6']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:5']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Step 1: Filter funding for amount > 50000
funding_over_50k = []
for record in funding_records:
    if int(record['Amount']) > 50000:
        funding_over_50k.append(record)

# Step 2: Extract design capital projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split text and find design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        # Extract potential project names (lines that aren't metadata)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty or marker lines
            if line and not line.startswith('(') and not line.startswith('Capital'):
                # Avoid metadata headers
                if 'To:' not in line and 'From:' not in line and 'Date' not in line and 'Subject' not in line:
                    if len(line) > 5:
                        design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Step 3: Count matches
funding_names = set(r['Project_Name'] for r in funding_over_50k)
match_count = 0

for project in design_projects:
    for funding_name in funding_names:
        if project == funding_name or funding_name.startswith(project + ' '):
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
