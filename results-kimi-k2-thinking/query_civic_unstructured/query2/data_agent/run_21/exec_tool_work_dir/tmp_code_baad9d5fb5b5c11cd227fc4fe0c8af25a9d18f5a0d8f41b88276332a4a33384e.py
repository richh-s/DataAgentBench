code = """import json

# Load funding data
f_path = locals()['var_functions.query_db:10']
with open(f_path, 'r') as f:
    funding = json.load(f)

# Load civic docs  
c_path = locals()['var_functions.query_db:11']
with open(c_path, 'r') as f:
    civic = json.load(f)

# Filter park projects from funding
park_funding = []
for item in funding:
    if 'park' in item['Project_Name'].lower():
        park_funding.append({
            'name': item['Project_Name'],
            'amount': int(item['Amount'])
        })

# Find park projects completed in 2022 from civic docs
completed_2022_projects = []

doc = civic[0]
text = doc.get('text', '')
lines = text.split('\n')

for i, line in enumerate(lines):
    line_lower = line.lower()
    if 'park' in line_lower and len(line.strip()) > 5:
        # Check nearby lines for 2022 completion
        for j in range(max(0, i-3), min(len(lines), i+4)):
            check_line = lines[j].lower()
            if '2022' in check_line and ('completed' in check_line or 'completion' in check_line):
                completed_2022_projects.append(line.strip())

# Match and sum funding
total_funding = 0
matched_projects = []

for fund_item in park_funding:
    for completed_proj in completed_2022_projects:
        fund_name = fund_item['name'].lower()
        proj_name = completed_proj.lower()
        if fund_name in proj_name or proj_name in fund_name:
            matched_projects.append(fund_item)
            total_funding += fund_item['amount']
            break

result = {
    'total_funding': total_funding,
    'matched_projects': len(matched_projects),
    'sample_matched': [p['name'] for p in matched_projects[:5]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
