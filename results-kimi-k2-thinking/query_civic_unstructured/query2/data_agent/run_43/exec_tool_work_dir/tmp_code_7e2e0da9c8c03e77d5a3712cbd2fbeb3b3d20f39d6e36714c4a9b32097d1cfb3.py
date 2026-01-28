code = """import json
import os

# Load files
fresult = var_functions.query_db:5
cresult = var_functions.query_db:6

funding_file = str(fresult)
civic_file = str(cresult)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Find park projects completed in 2022
park_2022_projects = []
funding_dict = {}

for record in funding_data:
    pname = record.get('Project_Name', '')
    if pname:
        funding_dict[pname] = record

# Check for park projects with 2022 completion
for doc in civic_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for completion indicators with 2022
    if 'completed' in text.lower() and '2022' in text:
        # Check each funding record for park name and completion
        for pname, record in funding_dict.items():
            if any(keyword in pname.lower() for keyword in ['park', 'playground']):
                if pname.lower() in text.lower():
                    park_2022_projects.append({
                        'Project_Name': pname,
                        'Funding_Source': record.get('Funding_Source'),
                        'Amount': int(record.get('Amount', 0))
                    })

# Remove duplicates
unique_projects = []
seen_names = set()
for p in park_2022_projects:
    if p['Project_Name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['Project_Name'])

# Calculate total funding
total = sum(p['Amount'] for p in unique_projects)

result = {
    'total_funding': total,
    'projects': unique_projects,
    'count': len(unique_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
