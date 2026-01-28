code = """import json
import pandas as pd

# Read the publication data
pub_data_path = locals().get('var_functions.query_db:5')
if pub_data_path:
    with open(pub_data_path, 'r') as f:
        pub_data = json.load(f)
else:
    pub_data = locals().get('var_functions.query_db:5', [])

# Parse CPC codes and extract year from publication_date
cpc_year_data = []

for record in pub_data:
    cpc_json = record.get('cpc', '[]')
    pub_date = record.get('publication_date', '')
    
    try:
        cpc_list = json.loads(cpc_json) if isinstance(cpc_json, str) else cpc_json
    except:
        continue
    
    # Extract year from publication date
    if pub_date:
        parts = pub_date.split()[-1]
        try:
            year = int(parts)
        except:
            continue
        
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                cpc_code = cpc_item['code']
                cpc_year_data.append({
                    'cpc_code': cpc_code,
                    'year': year
                })

if cpc_year_data:
    print('__RESULT__:')
    print(json.dumps(cpc_year_data[:100] if len(cpc_year_data) > 100 else cpc_year_data))
else:
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
