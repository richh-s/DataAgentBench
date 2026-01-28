code = """import json
f_funding = var_functions.query_db:68
f_civic = var_functions.query_db:5

# Load the data files
with open(f_funding) as f:
    funding_records = json.load(f)

with open(f_civic) as f:
    civic_docs = json.load(f)

# Count funding projects with amount > 50000
count_funding = sum(1 for r in funding_records if int(r['Amount']) > 50000)

# Extract capital design projects from civic docs
design_project_lines = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 5 and len(line) < 100:
                line_lower = line.lower()
                # Check for infrastructure keywords and avoid metadata
                keywords = ['road', 'park', 'canyon', 'storm', 'beach', 'bridge', 'avenue']
                has_keyword = any(k in line_lower for k in keywords)
                not_metadata = 'update' not in line_lower and 'schedule' not in line_lower
                if has_keyword and not_metadata:
                    design_project_lines.append(line)

# Remove duplicates
unique_design = list(dict.fromkeys(design_project_lines))

# Match with funding projects
matched = 0
for design_proj in unique_design:
    dp_clean = ''.join(c for c in design_proj.lower() if c.isalnum())
    for fund_rec in funding_records:
        if int(fund_rec['Amount']) > 50000:
            fp_clean = ''.join(c for c in fund_rec['Project_Name'].lower() if c.isalnum())
            if dp_clean in fp_clean or fp_clean in dp_clean:
                if len(dp_clean) > 8:  # Filter out short matches
                    matched += 1
                    break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
