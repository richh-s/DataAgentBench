code = """import json

docs = json.load(open(locals()['var_functions.query_db:8']))
funding = json.load(open(locals()['var_functions.query_db:6']))

# Simple approach: find park project names in funding data that were reported completed in 2022
park_projects_in_funding = []
for r in funding:
    pn = r['Project_Name']
    if 'park' in pn.lower():
        park_projects_in_funding.append(pn)

# Look for these projects in civic docs with 2022 completion
completed_2022_names = []
for doc in docs:
    txt = doc.get('text','')
    for proj_name in park_projects_in_funding:
        if proj_name in txt and '2022' in txt:
            # Check if completed in 2022
            if 'completed' in txt.lower():
                completed_2022_names.append(proj_name)

# Get unique list
completed_2022_names = list(set(completed_2022_names))

# Sum funding for these projects
total_fund = 0
for r in funding:
    if r['Project_Name'] in completed_2022_names:
        total_fund += int(r['Amount'])

result = {
    'completed_park_projects_2022': completed_2022_names,
    'total_funding': total_fund
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:26': {'potential_docs_with_2022_completion': 5, 'park_projects_in_funding': 20}}

exec(code, env_args)
