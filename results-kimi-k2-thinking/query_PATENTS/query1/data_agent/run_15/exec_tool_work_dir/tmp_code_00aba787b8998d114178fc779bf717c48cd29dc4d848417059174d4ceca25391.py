code = """import json
import pandas as pd
import re

# Load the publication data from the stored variable
result_key = 'var_functions.query_db:6'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        publications = json.load(f)
else:
    publications = result_file

print(f"Total publications: {len(publications)}")

# Parse CPC codes and extract years
cpc_year_data = []

for pub in publications:
    cpc_str = pub.get('cpc', '')
    pub_date_str = pub.get('publication_date', '')
    
    if not cpc_str or not pub_date_str:
        continue
    
    # Extract year from publication date (format: "Aug 3rd, 2021")
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON string
    try:
        cpc_list = json.loads(cpc_str)
    except:
        # Try to evaluate as Python literal if JSON fails
        try:
            cpc_list = eval(cpc_str)
        except:
            continue
    
    if not isinstance(cpc_list, list):
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            code = cpc_item['code']
            # Store the full code and also extract group (first part before /)
            if '/' in code:
                group = code.split('/')[0]
            else:
                group = code
            
            cpc_year_data.append({
                'full_code': code,
                'group_code': group,
                'year': year,
                'inventive': cpc_item.get('inventive', False),
                'first': cpc_item.get('first', False)
            })

print(f"Total CPC entries: {len(cpc_year_data)}")
if cpc_year_data:
    print(f"Sample data: {cpc_year_data[:3]}")
    
    # Convert to DataFrame for easier processing
    df = pd.DataFrame(cpc_year_data)
    print(f"DataFrame shape: {df.shape}")
    print(f"Year range: {df['year'].min()} to {df['year'].max()}")
    print(f"Unique groups: {len(df['group_code'].unique())}")
else:
    print("No CPC data found")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
