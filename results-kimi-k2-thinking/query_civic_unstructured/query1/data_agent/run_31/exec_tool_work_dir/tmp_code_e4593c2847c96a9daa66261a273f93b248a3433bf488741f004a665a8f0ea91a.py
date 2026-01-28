code = """import json

funding_file = var_functions.query_db:68
civic_file = var_functions.query_db:5

with open(funding_file) as f:
    funding_data = json.load(f)

with open(civic_file) as f:
    civic_data = json.load(f)

# Count funding projects over 50000
funding_count = 0
funding_names = []

for rec in funding_data:
    if int(rec['Amount']) > 50000:
        funding_count += 1
        funding_names.append(rec['Project_Name'])

# Extract project names from civic docs
design_lines = []

for doc in civic_data:
    if 'text' in doc:
        text = str(doc['text'])
        if 'Capital' in text and 'Design' in text:
            for line in text.split('\n'):
                line = line.strip()
                if line and len(line) < 80 and len(line) > 5:
                    lower = line.lower()
                    if 'updates' not in lower and 'schedule' not in lower:
                        if 'road' in lower or 'park' in lower or 'canyon' in lower:
                            design_lines.append(line)

# Remove duplicates
unique_design = list(dict.fromkeys(design_lines))

# Match projects
matched = 0
for design in unique_design:
    d_clean = design.lower().replace(' ', '').replace('(', '').replace(')', '')
    d_clean = ''.join(c for c in d_clean if c.isalnum())
    
    for fund in funding_names:
        f_clean = fund.lower().replace(' ', '').replace('(', '').replace(')', '')
        f_clean = ''.join(c for c in f_clean if c.isalnum())
        
        if d_clean in f_clean or f_clean in d_clean:
            if len(d_clean) > 8:
                matched += 1
                break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
