code = """import json

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded funding records:', len(funding_records))
print('Loaded civic documents:', len(civic_docs))

design_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    if 'capital improvement' in lower_text and 'design' in lower_text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) >= 10:
                lower_line = line.lower()
                # Skip administrative content
                admin_terms = ['updates:', 'schedule:', 'staff', 'city council', 'consultant', 'discussion:', 'page', 'complete design', 'advertise:', 'construction']
                is_admin = False
                for term in admin_terms:
                    if term in lower_line:
                        is_admin = True
                        break
                if is_admin:
                    continue
                
                # Look for project names with infrastructure keywords
                keywords = ['road', 'avenue', 'drive', 'park', 'drain', 'bridge', 'walkway', 'sewer', 'traffic', 'signal', 'median', 'crosswalk', 'improvements', 'repairs']
                for keyword in keywords:
                    if keyword in lower_line:
                        design_names.append(line)
                        break

# Remove duplicates
design_names = list(set(design_names))
print('Design project candidates:', len(design_names))

# Count matches with funding > 50000
match_count = 0
for project in design_names:
    proj_lower = project.lower()
    for fund in funding_records:
        amount = int(fund['Amount'])
        if amount > 50000:
            fund_lower = fund['Project_Name'].lower()
            # Check for matching names
            if proj_lower == fund_lower or proj_lower in fund_lower or fund_lower in proj_lower:
                match_count += 1
                break

print('Final count:', match_count)
print('__RESULT__:')
print(json.dumps({'count': match_count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
