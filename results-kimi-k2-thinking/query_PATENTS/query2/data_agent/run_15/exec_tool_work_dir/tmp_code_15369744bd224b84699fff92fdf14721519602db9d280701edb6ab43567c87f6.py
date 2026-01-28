code = """import json
import re

# Load the query result
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    patents_data = json.load(f)

print(f'Total patents retrieved: {len(patents_data)}')

# Inspect a few records to understand structure
for i, patent in enumerate(patents_data[:3]):
    print(f'\n=== Patent {i+1} ===')
    print(f'Patents_info: {patent["Patents_info"][:200]}...')
    print(f'grant_date: {patent["grant_date"]}')
    print(f'cpc codes: {patent["cpc"][:200] if len(patent["cpc"]) > 200 else patent["cpc"]}')

# Check for Germany patents
pattern = r'\bDE[-\d]'
german_patents = [p for p in patents_data if re.search(pattern, p['Patents_info'])]
print(f'\nPotential German patents found: {len(german_patents)}')

# Check structure of CPC codes
if patents_data:
    cpc_data = patents_data[0]['cpc']
    print(f'\nCPC field type: {type(cpc_data)}')
    if cpc_data.strip().startswith('['):
        try:
            cpc_list = json.loads(cpc_data)
            print(f'CPC codes extracted: {len(cpc_list)}')
            if cpc_list:
                print(f'First CPC: {cpc_list[0]}')
        except:
            print('Failed to parse CPC as JSON')
    __RESULT__:
    print(json.dumps({
        'total': len(patents_data),
        'german_count': len(german_patents),
        'cpc_parsable': True
    }))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
