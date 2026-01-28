code = """import json
import re
from datetime import datetime

# Read the file from previous query
file_path = locals()['var_functions.query_db:15']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Filter for German patents granted in second half of 2019
filtered_patents = []
th_2019_months = ['July', 'August', 'September', 'October', 'November', 'December']

for patent in patents_data:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    
    # Check if German
    if 'DE' not in patents_info:
        continue
    
    # Check if 2019
    if '2019' not in grant_date:
        continue
    
    # Check if second half
    is_second_half = any(month in grant_date for month in th_2019_months)
    if not is_second_half:
        continue
    
    filtered_patents.append(patent)

print('German patents in second half of 2019:', len(filtered_patents))

# Extract CPC codes at level 4 and filing years
cpc_data = []

for patent in filtered_patents:
    # Try to extract filing year from grant_date or parse date
    grant_date = patent.get('grant_date', '')
    
    cpc_field = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_field)
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        # Extract CPC level 4
        parts = code.split('/')
        if len(parts) >= 1:
            main_group = parts[0]
            # CPC level 4 format: first 4 characters after section
            if len(main_group) >= 4:
                level4_code = main_group[:4]
                cpc_data.append({
                    'cpc_code': level4_code,
                    'full_code': code,
                    'patent_info': patent['Patents_info'],
                    'grant_date': grant_date,
                    'year': 2019
                })

print('CPC level 4 entries:', len(cpc_data))

# Group by CPC code and count
from collections import Counter
cpc_counts = Counter([item['cpc_code'] for item in cpc_data])
print('Unique CPC codes:', len(cpc_counts))
print('Top 10 CPC codes:', cpc_counts.most_common(10))

# Save for next step
result = {
    'german_patents_2019_h2': len(filtered_patents),
    'cpc_entries': len(cpc_data),
    'unique_cpc_codes': len(cpc_counts),
    'cpc_code_list': list(cpc_counts.keys()),
    'top_cpc': cpc_counts.most_common(20)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'filtered_patents_count': 72, 'cpc_level4_entries': 878, 'unique_cpc_codes_count': 97, 'top_cpc_codes': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]], 'all_unique_cpc_codes': ['B29L', 'A61K', 'F23L', 'C04B', 'F21V', 'E01F', 'B64D', 'B60Y', 'B01L', 'Y02D', 'C22F', 'B29D', 'F23N', 'G06N', 'G01R', 'A61P', 'G01L', 'H01L', 'F24F', 'G01N', 'B60W', 'B81C', 'Y04S', 'G06E', 'A61C', 'G01J', 'H01H', 'B60R', 'Y02A', 'B41F', 'C09K', 'F02M', 'B23K', 'B30B', 'F02D', 'F24B', 'G06T', 'B81B', 'Y02T', 'F04B', 'B60S', 'G01B', 'B82Y', 'H02K', 'F41H', 'A61F', 'F23B', 'F42B', 'E21B', 'Y02W', 'G02B', 'B01J', 'H04N', 'F04C', 'F02N', 'G05D', 'Y02P', 'E05Y', 'A61M', 'G08C', 'G07C', 'E05F', 'F01C', 'B27L', 'C22C', 'B22F', 'A61G', 'Y02B', 'F17C', 'E05B', 'B02C', 'G08B', 'A24C', 'B62B', 'C23F', 'F16C', 'Y02E', 'Y10T', 'H04W', 'H04L', 'B60K', 'B29K', 'F04D', 'B29C', 'G06F', 'G01D', 'C07K', 'H01R', 'F16H', 'A43B', 'A61B', 'B66C', 'F16K', 'A47C', 'B63B', 'E02F', 'B60N']}, 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
