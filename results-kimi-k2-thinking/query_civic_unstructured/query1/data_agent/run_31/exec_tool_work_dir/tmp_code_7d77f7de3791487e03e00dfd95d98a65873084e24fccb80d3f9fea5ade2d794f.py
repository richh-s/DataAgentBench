code = """import json

funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding_data = json.load(f)

with open(civic_path) as f:
    civic_docs = json.load(f)

funding_projects = []
for rec in funding_data:
    if int(rec['Amount']) > 50000:
        funding_projects.append(rec['Project_Name'])

design_projects = []

for doc in civic_docs:
    if 'text' in doc and isinstance(doc['text'], str):
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(') and len(line) < 80:
                    lower_line = line.lower()
                    # Skip metadata
                    if 'update' not in lower_line and 'schedule' not in lower_line:
                        # Check for project keywords
                        for keyword in ['road', 'avenue', 'drive', 'park', 'canyon', 'beach', 'storm', 'bridge', 'project']:
                            if keyword in lower_line:
                                design_projects.append(line)
                                break

# Remove duplicates
unique_design = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        seen.add(proj)
        unique_design.append(proj)

# Match projects
match_count = 0
for proj in unique_design:
    proj_norm = proj.lower().replace(' ', '')
    proj_norm = ''.join(c for c in proj_norm if c.isalnum())
    
    for fund_proj in funding_projects:
        fund_norm = fund_proj.lower().replace(' ', '')
        fund_norm = ''.join(c for c in fund_norm if c.isalnum())
        
        if proj_norm in fund_norm or fund_norm in proj_norm:
            match_count += 1
            break

result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
