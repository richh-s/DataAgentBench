code = """import json, pandas as pd, re

# Load data
funding = var_functions.query_db_14
projects = var_functions.query_db_16

funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find Spring 2022 projects
found = []
for doc in projects:
    txt = doc.get('text', '')
    for m in re.finditer(r'Spring[^\n]{0,100}2022', txt, re.IGNORECASE):
        ctx = txt[max(0, m.start()-500):m.end()+200]
        for _, row in funding_df.iterrows():
            name = row['Project_Name']
            if name[:50] in ctx:
                found.append({'name': name, 'amount': row['Amount']})
                break

# Deduplicate
unique = {p['name']: p for p in found}
final = list(unique.values())

result = {
    'count': len(final),
    'funding': sum(p['amount'] for p in final),
    'projects': final
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
