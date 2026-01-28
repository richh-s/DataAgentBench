code = """import json

funding_path = var_functions.query_db:68
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

# Get projects with funding > 50000
funding_names = [rec['Project_Name'] for rec in funding if int(rec['Amount']) > 50000]

# Extract capital design projects
design_projects = []
for rec in civic:
    if 'text' in rec:
        txt = rec['text']
        if 'Capital' in txt and 'Design' in txt:
            lines = txt.split('\n')
            for line in lines:
                line_clean = line.strip()
                if line_clean and len(line_clean) < 80:
                    lower = line_clean.lower()
                    if 'update' not in lower and 'schedule' not in lower:
                        if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower:
                            design_projects.append(line_clean)

# Deduplicate and count matches
seen = set()
unique_design = []
for p in design_projects:
    if p not in seen:
        seen.add(p)
        unique_design.append(p)

matched = 0
for dp in unique_design:
    dp_norm = ''.join(c for c in dp.lower() if c.isalnum())
    if dp_norm:
        for fp in funding_names:
            fp_norm = ''.join(c for c in fp.lower() if c.isalnum())
            if dp_norm in fp_norm or fp_norm in dp_norm:
                matched += 1
                break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
