code = """import json

with open(locals()['var_function-call-8970245157857899203'], 'r') as f:
    funding_data = json.load(f)

search_terms = ["Bluffs Park", "Point Dume"]
matches = []

for row in funding_data:
    name = row['Project_Name']
    for term in search_terms:
        if term.lower() in name.lower():
            matches.append(row)

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-8970245157857899516': 'file_storage/function-call-8970245157857899516.json', 'var_function-call-8970245157857899203': 'file_storage/function-call-8970245157857899203.json', 'var_function-call-9746508737672211819': {'total_funding': 21000.0, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000.0}]}}

exec(code, env_args)
