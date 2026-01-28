code = """import json

# Load funding data (file path stored in variable)
funding_path = var_functions.query_db:2
with open(funding_path) as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:5
with open(civic_path) as f:
    civic_records = json.load(f)

# Get funding amounts > 50000
large_funding = {}
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        large_funding[rec['Project_Name']] = amount

# Simple project name extraction from civic docs
possible_projects = []

for doc in civic_records:
    if isinstance(doc, dict) and 'text' in doc:
        text = doc['text']
        # Look for capital projects in design
        if 'Capital Improvement Projects (Design)' in text:
            # This is a status report with design projects
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Look for lines that are likely project names
                # Skip metadata lines
                if line and 8 < len(line) < 60 and not line.startswith('(') and ':' not in line:
                    lower = line.lower()
                    if 'update' not in lower and 'schedule' not in lower and 'action' not in lower:
                        if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                            possible_projects.append(line)

# Remove duplicates
unique_projects = list(set(possible_projects))

# Match projects
count = 0
matched_names = []

for proj in unique_projects:
    # Clean project name
    proj_clean = proj.lower().replace('(', '').replace(')', '')
    proj_clean = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in proj_clean)
    proj_clean = ' '.join(proj_clean.split())
    
    if not proj_clean:
        continue
        
    for fund_name in large_funding:
        # Clean funding name similarly
        fund_clean = fund_name.lower().replace('(', '').replace(')', '')
        fund_clean = ''.join(c if c.isalnum() or c == ' ' else ' ' for c in fund_clean)
        fund_clean = ' '.join(fund_clean.split())
        
        # Check for overlap
        if proj_clean in fund_clean or fund_clean in proj_clean:
            count += 1
            matched_names.append({'project': proj, 'funding': fund_name, 'amount': large_funding[fund_name]})
            break

result = {'count': count, 'matches': matched_names[:5]}  # Include sample matches
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
