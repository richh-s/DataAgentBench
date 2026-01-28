code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:40']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Simple approach - count funded projects > 50000
count_50k = sum(1 for rec in funding_data if int(rec['Amount']) > 50000)

# Get design project names from civic docs (simplified)
design_names = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Design' in text:
        idx = text.find('Capital Improvement Projects (Design)')
        if idx > -1:
            snippet = text[idx:idx+2000]
            lines = snippet.split('\n')
            for line in lines:
                stripped = line.strip()
                if len(stripped) > 10 and 'Project' in stripped and 'fema' not in stripped.lower():
                    design_names.add(stripped)

# Simple matching
matches = 0
matched_set = set()

for rec in funding_data:
    amount = int(rec['Amount'])
    if amount > 50000:
        proj_name = rec['Project_Name']
        # Basic comparison
        base_proj = proj_name
        if '(' in proj_name:
            base_proj = proj_name.split('(')[0].strip()
        
        if base_proj in design_names:
            matched_set.add(base_proj)

result = {'count': len(matched_set)}

# Print in required format
result_str = json.dumps(result)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
