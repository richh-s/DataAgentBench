code = """import json

# Read the funding data file path and load it
funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Read the civic documents file path and load it
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
high_funding_projects = [r for r in funding_records if int(r['Amount']) > 50000]
high_funding_names = set(r['Project_Name'] for r in high_funding_projects)

# Extract capital projects with design status
design_capital_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Split by the design header and get the content
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_content = parts[1]
            # Split lines and extract project names (non-empty lines that don't start with certain markers)
            for line in design_content.split('\n'):
                line = line.strip()
                if line and not line.startswith('Capital Improvement Projects') and not line.startswith('(') and len(line) > 5:
                    # Additional filters to avoid headers/metadata
                    if not line.startswith('To:') and not line.startswith('From:') and not line.startswith('Date') and not line.startswith('Subject'):
                        design_capital_names.append(line)

# Remove duplicates
design_capital_names = list(set(design_capital_names))

# Count matches where project name appears in funding data
match_count = 0
matched_names = []

for design_name in design_capital_names:
    for funding_record in high_funding_projects:
        funding_name = funding_record['Project_Name']
        # Check for exact match or funding name starting with design name (for suffixes)
        if design_name == funding_name or funding_name.startswith(design_name + ' '):
            match_count += 1
            matched_names.append(design_name)
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
