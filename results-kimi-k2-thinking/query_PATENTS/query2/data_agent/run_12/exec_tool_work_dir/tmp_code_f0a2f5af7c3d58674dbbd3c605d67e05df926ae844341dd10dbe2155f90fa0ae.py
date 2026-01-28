code = """import json
import re
from collections import defaultdict

# Load data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Total German patents loaded:', len(german_patents))

# Filter for second half 2019 and count CPC level 4 codes
second_half_months = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']
cpc_counts = defaultdict(int)
valid_patents = 0

for rec in german_patents:
    grant_date = rec.get('grant_date','')
    if '2019' in grant_date and any(month in grant_date for month in second_half_months):
        valid_patents += 1
        # Parse CPC codes
        try:
            cpc_list = json.loads(rec.get('cpc','[]'))
            codes = set()
            for item in cpc_list:
                code = item.get('code','')
                if len(code) >= 4:
                    codes.add(code[:4])
            for cpc in codes:
                cpc_counts[cpc] += 1
        except:
            continue

print('Patents in second half 2019:', valid_patents)
print('Unique CPC level 4 codes:', len(cpc_counts))

# Show top codes
sorted_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)
print('\nTop CPC codes:')
for cpc, count in sorted_cpc[:10]:
    print(cpc, ':', count)

print('\n__RESULT__:')
print(json.dumps({'total_codes': len(cpc_counts), 'top_codes': sorted_cpc[:10]}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
