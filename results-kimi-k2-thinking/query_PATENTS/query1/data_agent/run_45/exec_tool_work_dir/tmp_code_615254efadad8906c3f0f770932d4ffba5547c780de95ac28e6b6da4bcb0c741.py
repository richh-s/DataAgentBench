code = """import json
import re
from collections import defaultdict

# Read the CPC publication data
with open('/tmp/tmp_result_6.json', 'r') as f:
    publications = json.load(f)

# Extract CPC codes and years
cpc_year_counts = defaultdict(lambda: defaultdict(int))

for pub in publications:
    cpc_data = pub['cpc']
    year = pub['year']
    
    if cpc_data and year:
        try:
            cpc_list = json.loads(cpc_data)
            
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if code:
                    group_code = code.split('/')[0]
                    if len(group_code) >= 4:
                        cpc_year_counts[group_code][year] += 1
        except:
            continue

# Get all unique years and sort them
all_years = set()
for cpc_code in cpc_year_counts:
    all_years.update(cpc_year_counts[cpc_code].keys())

sorted_years = sorted(list(all_years))
print('__RESULT__:')
print(json.dumps({
    'available_years': sorted_years,
    'total_cpc_groups': len(cpc_year_counts)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
