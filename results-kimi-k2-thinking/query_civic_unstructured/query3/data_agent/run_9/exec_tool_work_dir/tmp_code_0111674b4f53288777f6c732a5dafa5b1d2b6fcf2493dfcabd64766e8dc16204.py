code = """import json, re, os

# Load funding data
funding_file = open('results/query_db_6.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Find FEMA/emergency projects
results = []
for rec in funding_data:
    pname = rec['Project_Name'].upper()
    if 'FEMA' in pname or 'EMERGENCY' in pname:
        results.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

print('FOUND', len(results), 'FEMA/EMERGENCY PROJECTS')
for i, r in enumerate(results[:10]):
    print(i, r['Project_Name'])

# Save results
output = json.dumps(results, indent=2)
print(output[:500])

__RESULT__ = output"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
