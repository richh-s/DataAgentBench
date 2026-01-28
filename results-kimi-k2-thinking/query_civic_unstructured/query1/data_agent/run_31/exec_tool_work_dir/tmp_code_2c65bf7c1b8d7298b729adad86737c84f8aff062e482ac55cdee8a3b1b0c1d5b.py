code = """import json

# Load the data files
with open(var_functions.query_db:68) as f:
    funding_records = json.load(f)

with open(var_functions.query_db:5) as f:
    civic_docs = json.load(f)

# Filter for funding > 50000
high_funding = []
for rec in funding_records:
    amount = int(rec['Amount'])
    if amount > 50000:
        high_funding.append(rec)

# Extract capital design projects from civic docs
design_names = []

for doc in civic_docs:
    if 'text' in doc and doc['text']:
        text = doc['text']
        if 'Capital Improvement Projects' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                # Find likely project names (not metadata)
                if line and len(line) < 80 and line[0].isalpha():
                    lower = line.lower()
                    if 'update' not in lower and 'schedule' not in lower and 'action' not in lower:
                        if 'road' in lower or 'park' in lower or 'canyon' in lower or 'storm' in lower or 'bridge' in lower:
                            design_names.append(line)

# Remove duplicates
seen = set()
unique_design = []
for name in design_names:
    if name not in seen:
        seen.add(name)
        unique_design.append(name)

# Count matches
matches = 0
for design in unique_design:
    design_clean = ''.join(c for c in design.lower() if c.isalnum())
    for fund_rec in high_funding:
        fund_clean = ''.join(c for c in fund_rec['Project_Name'].lower() if c.isalnum())
        if design_clean in fund_clean or fund_clean in design_clean:
            if len(design_clean) > 5:
                matches += 1
                break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
