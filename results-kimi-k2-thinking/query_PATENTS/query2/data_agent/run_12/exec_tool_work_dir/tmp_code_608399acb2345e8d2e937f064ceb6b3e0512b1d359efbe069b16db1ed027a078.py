code = """import json
import re
from collections import defaultdict

# Load German patent data from file
result_path = locals()['var_functions.query_db:48']
if isinstance(result_path, str) and result_path.endswith('.json'):
    with open(result_path, 'r') as f:
        patents = json.load(f)
else:
    patents = result_path

print('Loaded patents:', len(patents))

# Filter for second half 2019
second_half = ['July','August','September','October','November','December','Jul','Aug','Sep','Oct','Nov','Dec']
second_half_patents = []

for p in patents:
    gd = p.get('grant_date', '')
    if '2019' in gd and any(m in gd for m in second_half):
        second_half_patents.append(p)

print('Second half 2019 patents:', len(second_half_patents))

# Extract CPC level 4 codes and count
cpc_counts = defaultdict(int)
all_cpc_codes = set()

for p in second_half_patents:
    try:
        cpc_list = json.loads(p.get('cpc', '[]'))
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                codes.add(code[:4])
        for cpc in codes:
            cpc_counts[cpc] += 1
            all_cpc_codes.add(cpc)
    except:
        pass

print('Unique CPC level 4 codes:', len(all_cpc_codes))

# Get top CPC codes
top_cpcs = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)[:15]
print('Top 15 CPC codes by count:')
for cpc, cnt in top_cpcs:
    print(f"  {cpc}: {cnt}")

# Store results for next steps
result_data = {
    'cpc_codes': list(all_cpc_codes),
    'top_cpcs': top_cpcs,
    'counts': dict(cpc_counts)
}

print()
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': [{'total': '216'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:56': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}]}

exec(code, env_args)
