code = """import json
import re

# Access the German patents data
results_key = 'var_functions.query_db:28'
german_patents_data = locals().get(results_key)

# Load the data from file if it's a path
if isinstance(german_patents_data, str) and german_patents_data.endswith('.json'):
    with open(german_patents_data, 'r') as f:
        results = json.load(f)
else:
    results = german_patents_data

print(f'Loaded {len(results)} records')

# Function to parse grant date and check if it's second half 2019
def is_second_half_2019(date_str):
    if not date_str:
        return False
    
    date_str = str(date_str).lower()
    
    # Check for 2019
    if '2019' not in date_str:
        return False
    
    # Check for second half months
    second_half_months = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    for month in second_half_months:
        if month in date_str:
            return True
    
    return False

# Function to extract CPC level 4 code
def extract_cpc_level_4(cpc_code):
    if not cpc_code:
        return None
    try:
        main_part = str(cpc_code).split('/')[0]
        clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
        return clean_part
    except:
        return None

# Process patents
cpc_counts = {}
total_processed = 0

for patent in results:
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    if not is_second_half_2019(grant_date):
        continue
    
    try:
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
            
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code')
            if cpc_code:
                level_4 = extract_cpc_level_4(cpc_code)
                if level_4:
                    cpc_counts[level_4] = cpc_counts.get(level_4, 0) + 1
                    total_processed += 1
    except:
        continue

print(f'Processed {total_processed} CPC entries')
print(f'Found {len(cpc_counts)} unique CPC Level 4 codes')

# Show top CPC codes
top_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:20]
print('Top CPC Level 4 codes:')
for cpc, count in top_cpc:
    print(f'  {cpc}: {count}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Date parsing and CPC level 4 extraction functions ready', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'total_records': '11735'}]}

exec(code, env_args)
