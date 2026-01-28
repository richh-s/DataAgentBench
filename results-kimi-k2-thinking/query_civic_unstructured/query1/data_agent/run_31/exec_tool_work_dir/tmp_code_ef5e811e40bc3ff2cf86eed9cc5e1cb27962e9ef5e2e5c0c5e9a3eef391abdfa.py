code = """import json

# Read funding data
f_funding = var_functions.query_db:2
f_civic = var_functions.query_db:5

with open(f_funding) as f:
    funding = json.load(f)

with open(f_civic) as f:
    civic = json.load(f)

# Projects with funding > 50000
funding_names = []
for rec in funding:
    if int(rec['Amount']) > 50000:
        funding_names.append(rec['Project_Name'])

# Extract capital design projects from civic docs
project_candidates = []

for doc in civic:
    if 'text' in doc:
        text = str(doc['text'])
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and 8 < len(line) < 60:
                    lower_line = line.lower()
                    if 'update' not in lower_line and 'schedule' not in lower_line:
                        keywords = ['road', 'park', 'canyon', 'storm', 'bridge']
                        for kw in keywords:
                            if kw in lower_line:
                                project_candidates.append(line)
                                break

# Remove duplicates
unique_projects = []
added = set()
for proj in project_candidates:
    if proj not in added:
        added.add(proj)
        unique_projects.append(proj)

# Count matches
match_count = 0
for proj in unique_projects:
    proj_norm = proj.lower().replace(' ', '')
    proj_norm = ''.join([c for c in proj_norm if c.isalnum()])
    
    for fund_name in funding_names:
        fund_norm = fund_name.lower().replace(' ', '')
        fund_norm = ''.join([c for c in fund_norm if c.isalnum()])
        
        if proj_norm in fund_norm or fund_norm in proj_norm:
            match_count += 1
            break

result = json.dumps({'count': match_count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs']}

exec(code, env_args)
