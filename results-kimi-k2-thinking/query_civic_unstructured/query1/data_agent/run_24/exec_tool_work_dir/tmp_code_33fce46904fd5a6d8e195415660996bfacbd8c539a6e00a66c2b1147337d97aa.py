code = """import json

# Load data from files
funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_docs = json.load(f)

# Step 1: Get all funding records with amount > $50,000
funding_over_50k = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        funding_over_50k.append(record)

# Step 2: Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split to get design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        # Extract non-empty lines that are not markers
        for line in design_section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and len(line) > 5:
                    design_capital_projects.append(line)

# Remove duplicates
design_capital_projects = list(set(design_capital_projects))

# Step 3: Count matches between design projects and high funding
matched_count = 0

for design_proj in design_capital_projects:
    for funding_rec in funding_over_50k:
        funding_name = funding_rec['Project_Name']
        if design_proj == funding_name or funding_name.startswith(design_proj + ' '):
            matched_count += 1
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
