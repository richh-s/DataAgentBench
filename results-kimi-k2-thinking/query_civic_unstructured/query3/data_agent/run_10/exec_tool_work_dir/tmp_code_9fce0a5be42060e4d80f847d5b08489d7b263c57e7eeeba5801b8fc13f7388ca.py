code = """import json

# Check available variables
all_vars = list(locals().keys())
funding_var = next((v for v in all_vars if 'query_db:0' in v), None)
civic_var = next((v for v in all_vars if 'query_db:4' in v), None)

print('Funding var:', funding_var)
print('Civic var:', civic_var)

# Get the data
funding_info = locals()[funding_var]
civic_info = locals()[civic_var]

print('Funding info type:', type(funding_info))
print('Civic info type:', type(civic_info))

# If they are strings (file paths), load the JSON
if isinstance(funding_info, str):
    with open(funding_info) as f:
        funding_data = json.load(f)
else:
    funding_data = funding_info

if isinstance(civic_info, str):
    with open(civic_info) as f:
        civic_data = json.load(f)
else:
    civic_data = civic_info

print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_data))

# Find emergency/FEMA projects in funding data
matches = []
for record in funding_data:
    name_lower = record['Project_Name'].lower()
    if 'emergency' in name_lower or 'fema' in name_lower:
        matches.append(record)

print('Direct matches:', len(matches))
for m in matches[:5]:
    print(f"  {m['Project_Name']} - {m['Funding_Source']} - ${m['Amount']}")

result = json.dumps(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
