code = """import json
import pandas as pd

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Mongo docs count:', len(mongo_docs))
print('Funding records count:', len(funding_records))

# Check structure
if mongo_docs:
    print('First mongo doc keys:', list(mongo_docs[0].keys()))
if funding_records:
    print('First funding record:', funding_records[0])

# Find projects with emergency or fema in name from funding data
df_funding = pd.DataFrame(funding_records)
mask = df_funding['Project_Name'].str.contains('emergency|fema', case=False, na=False)
emergency_fema_projects = df_funding[mask]

print('Emergency/FEMA projects in funding:', len(emergency_fema_projects))

result = emergency_fema_projects.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
