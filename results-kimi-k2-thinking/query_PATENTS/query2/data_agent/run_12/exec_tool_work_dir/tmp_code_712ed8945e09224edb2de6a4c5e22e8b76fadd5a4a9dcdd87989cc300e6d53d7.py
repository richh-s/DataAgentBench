code = """import json
import re
from collections import defaultdict

# Load German patent data from query
result_value = locals()['var_functions.query_db:48']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        patents = json.load(f)
else:
    patents = result_value

print('Loaded', len(patents), 'German patents from 2019')

# Check second half of 2019
second_half_months = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']
second_half_patents = []

for rec in patents:
    grant_date = rec.get('grant_date', '')
    if '2019' in grant_date and any(m in grant_date for m in second_half_months):
        second_half_patents.append(rec)

print('Patents in second half 2019:', len(second_half_patents))

# Extract CPC level 4 codes
cpc_counts = defaultdict(int)
for rec in second_half_patents:
    try:
        cpc_list = json.loads(rec.get('cpc', '[]'))
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                codes.add(code[:4])
        for cpc in codes:
            cpc_counts[cpc] += 1
    except:
        continue

print('Unique CPC level 4 codes:', len(cpc_counts))

# Show top 10
top_cpcs = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print('\nTop CPC codes:')
for cpc, count in top_cpcs:
    print(cpc + ': ' + str(count))

print('\n__RESULT__:')
result = {'total_cpc': len(cpc_counts), 'top_cpcs': top_cpcs}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': [{'total': '216'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
