code = """import json

# Access funding data that was queried
funding_data = var_functions.query_db:0
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

# Access civic docs data
civic_data = var_functions.query_db:2
if isinstance(civic_data, str):
    with open(civic_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic documents')

# Process documents to find capital design projects
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'capital improvement' in text and 'design' in text:
        full_text = doc.get('text', '')
        lines = full_text.split('\n')
        for line in lines:
            clean_line = line.strip()
            if len(clean_line) >= 10:
                lower_line = clean_line.lower()
                skip_words = ['updates', 'schedule', 'staff', 'city council', 'consultant', 'discussion', 'page ', 'complete design', 'advertise', 'construction']
                should_skip = False
                for word in skip_words:
                    if word in lower_line:
                        should_skip = True
                        break
                if should_skip:
                    continue
                project_words = ['road', 'avenue', 'drive', 'park', 'drain', 'bridge', 'walkway', 'sewer', 'traffic', 'signal']
                for word in project_words:
                    if word in lower_line:
                        design_projects.append(clean_line)
                        break

design_projects = list(set(design_projects))
print('Found', len(design_projects), 'potential design projects')

# Match with funding > 50000
matches = 0
for project in design_projects:
    project_lower = project.lower()
    for fund in funding_records:
        fund_amount = int(fund['Amount'])
        if fund_amount > 50000:
            fund_name_lower = fund['Project_Name'].lower()
            # Check for name match
            if project_lower == fund_name_lower or project_lower in fund_name_lower or fund_name_lower in project_lower:
                matches += 1
                break

print('Matches found:', matches)
output = {'count': matches}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
