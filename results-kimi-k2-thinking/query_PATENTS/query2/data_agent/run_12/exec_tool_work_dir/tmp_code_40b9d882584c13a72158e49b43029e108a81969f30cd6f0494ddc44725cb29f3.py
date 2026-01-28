code = """import json
import re
from collections import defaultdict

# Load the German patent data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Total German patents: ' + str(len(german_patents)))

# Check data structure
if len(german_patents) > 0:
    first = german_patents[0]
    print('Sample grant date: ' + first['grant_date'])
    print('Sample CPC (first 200 chars): ' + str(first['cpc'])[:200])

# Function to check if date is in second half of 2019
def is_second_half_2019(date_str):
    # Check if it's 2019
    if '2019' not in date_str:
        return False
    
    # Check for months July-December
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month in second_half_months:
        if month in date_str:
            return True
    return False

# Function to extract level 4 CPC codes
import json as js

def get_cpc_level4(cpc_str):
    try:
        cpc_list = js.loads(cpc_str)
        codes = []
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                codes.append(code[:4])
        return list(set(codes))
    except:
        return []

# Count patents by CPC level 4 code
print('\nFiltering for second half of 2019...')
cpc_counts = defaultdict(int)
valid_patents = 0

for rec in german_patents:
    grant_date = rec['grant_date']
    if is_second_half_2019(grant_date):
        valid_patents += 1
        cpc_codes = get_cpc_level4(rec['cpc'])
        for cpc in cpc_codes:
            cpc_counts[cpc] += 1

print('Patents in second half 2019: ' + str(valid_patents))
print('Unique CPC level 4 codes: ' + str(len(cpc_counts)))

# Show top CPC codes
sorted_cpc = sorted(cpc_counts.items(), key=lambda x: x[1], reverse=True)
print('\nTop 10 CPC level 4 codes:')
for cpc, count in sorted_cpc[:10]:
    print(cpc + ': ' + str(count))

print('__RESULT__:')
print(str(len(cpc_counts)))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
