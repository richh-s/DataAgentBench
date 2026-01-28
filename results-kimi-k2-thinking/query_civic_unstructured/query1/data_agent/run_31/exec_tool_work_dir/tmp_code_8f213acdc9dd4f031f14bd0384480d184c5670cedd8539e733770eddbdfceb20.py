code = """import json

funding_path = var_functions.query_db:68
civic_path = var_functions.query_db:5

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    civic = json.load(f)

# Simple count
high_funding = [rec for rec in funding if int(rec['Amount']) > 50000]
design_projects_count = 0

for doc in civic:
    if 'text' in doc:
        txt = doc['text']
        if 'Capital' in txt and 'Design' in txt:
            lines = txt.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 5 and len(line) < 100:
                    lower = line.lower()
                    if 'road' in lower or 'park' in lower:
                        design_projects_count += 1

# Very basic matching
matched = 0
for fund in high_funding:
    fname = fund['Project_Name'].lower()
    # Check if any of the extracted lines match roughly
    # This is a simplified check
    if 'road' in fname or 'park' in fname or 'canyon' in fname:
        matched += 1

result = {'total_design_projects': design_projects_count, 'total_high_funding': len(high_funding), 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
