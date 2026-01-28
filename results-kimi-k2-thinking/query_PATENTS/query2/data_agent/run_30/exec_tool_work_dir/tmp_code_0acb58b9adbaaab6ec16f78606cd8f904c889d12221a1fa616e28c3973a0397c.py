code = """import json
import re
from datetime import datetime

# Fix the variable name
result_file = var_functions.query_db:2

with open(result_file, 'r') as f:
    patents_data = json.load(f)

print('Total patents records:', len(patents_data))

# Filter for second half of 2019 (July-December) for Germany
filtered_patents = []
months_h2_2019 = ['July', 'August', 'September', 'October', 'November', 'December']

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    if 'DE' not in patents_info:
        continue
    
    grant_date = patent.get('grant_date', '')
    if '2019' not in grant_date:
        continue
    
    has_month_h2 = any(month in grant_date for month in months_h2_2019)
    if not has_month_h2:
        continue
        
    filtered_patents.append(patent)

print('German patents granted in second half of 2019:', len(filtered_patents))

# Extract CPC codes at level 4
cpc_level4_data = []

for patent in filtered_patents:
    cpc_field = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_field)
    except:
        continue
        
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
            
        parts = code.split('/')
        if len(parts) >= 1:
            main_group = parts[0]
            if len(main_group) >= 4:
                level4_code = main_group[:4]
                cpc_level4_data.append({
                    'cpc_code': level4_code,
                    'full_code': code,
                    'patent_info': patent['Patents_info'],
                    'grant_date': patent['grant_date']
                })

print('CPC level 4 entries extracted:', len(cpc_level4_data))

unique_cpc_codes = list(set(item['cpc_code'] for item in cpc_level4_data))
print('Unique CPC level 4 codes:', len(unique_cpc_codes))
print('Sample codes:', unique_cpc_codes[:10])

result = {
    'filtered_patents_count': len(filtered_patents),
    'cpc_level4_entries': cpc_level4_data,
    'unique_cpc_codes': unique_cpc_codes
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
