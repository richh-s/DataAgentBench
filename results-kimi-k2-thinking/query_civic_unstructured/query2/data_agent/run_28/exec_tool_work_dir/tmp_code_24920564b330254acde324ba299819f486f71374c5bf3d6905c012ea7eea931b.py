code = """import json
import re

funding_recs = var_functions.query_db:8

print(len(funding_recs))

park_funding = []
for rec in funding_recs:
    pname = str(rec.get('Project_Name', '')).lower()
    if 'park' in pname:
        park_funding.append({
            'name': rec.get('Project_Name'),
            'amount': int(rec.get('Amount', 0))
        })

print(len(park_funding))

for p in park_funding[:10]:
    print(p)

total = sum(p['amount'] for p in park_funding)
print('total:', total)

result = {'park_projects': park_funding, 'total_all_years': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
