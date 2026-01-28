code = """import json
with open(var_functions.query_db:0, 'r') as f:
    funding = json.load(f)
projects = ["2022 Morning View Resurfacing & Storm Drain Improvements", "PCH Median Improvements Project", "Westward Beach Road Drainage Improvements Project"]
matches = []
for p in projects:
    for f in funding:
        if f['Project_Name'] == p and int(f['Amount']) > 50000:
            matches.append(p)
print('__RESULT__:')
print(json.dumps({'count': len(matches), 'projects': matches}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs']}

exec(code, env_args)
