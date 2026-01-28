code = """import json

data_civic = json.load(open('var_functions.query_db_36'))
data_funding = json.load(open('var_functions.query_db_8'))

park_projects = []

for doc in data_civic:
    text = doc.get('text', '')
    # Check if document contains park and 2022 completion
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        # Extract project names containing Park
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) < 120:
                # Filter out metadata
                if 'updates' not in line.lower() and 'schedule' not in line.lower() and 'description' not in line.lower():
                    if line not in park_projects:
                        park_projects.append(line)

# Match with funding
total = 0
for project in park_projects:
    proj_lower = project.lower()
    for fund in data_funding:
        fund_name = fund['Project_Name'].lower()
        if proj_lower == fund_name:
            total += int(fund['Amount'])

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': len(park_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
