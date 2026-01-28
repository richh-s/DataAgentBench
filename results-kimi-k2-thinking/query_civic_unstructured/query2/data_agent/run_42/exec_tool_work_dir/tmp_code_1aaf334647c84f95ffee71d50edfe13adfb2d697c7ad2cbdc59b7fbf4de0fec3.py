code = """import json

# Read civic documents
civic_docs = json.load(open(locals()['var_functions.query_db:8']))

# Look for completed park projects in 2022
completed_park_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for 2022 completion with park context
    if '2022' in text and 'completed' in lower_text and 'park' in lower_text:
        completed_park_2022.append(doc)

# Read funding data  
funding_records = json.load(open(locals()['var_functions.query_db:6']))

# Filter for park projects
park_projects = [r for r in funding_records if 'park' in r['Project_Name'].lower()]

result = {
    'potential_docs_with_2022_completion': len(completed_park_2022),
    'park_projects_in_funding': len(park_projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
