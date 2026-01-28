code = """# Load data from files
civic_docs = []
import json
with open('var_functions.query_db_36') as f:
    civic_docs = json.load(f)

funding_data = []
with open('var_functions.query_db_8') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        for line in text.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line) < 120:
                bad_words = ['updates', 'schedule', 'description', 'page', 'agenda']
                if not any(w in line.lower() for w in bad_words):
                    if line not in park_projects:
                        park_projects.append(line)

# Match funding
total = 0
for p in park_projects:
    pl = p.lower()
    for f in funding_data:
        if f['Project_Name'].lower() == pl:
            total += int(f['Amount'])

print('__RESULT__:')
print({"total_funding": total, "projects": len(park_projects), "project_list": park_projects})"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
