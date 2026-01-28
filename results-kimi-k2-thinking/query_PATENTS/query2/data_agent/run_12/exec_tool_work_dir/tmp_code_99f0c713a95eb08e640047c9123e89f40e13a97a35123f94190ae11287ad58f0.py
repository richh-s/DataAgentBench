code = """import json
import re
from collections import defaultdict

# Load the data
result_value = locals()['var_functions.query_db:30']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        german_patents = json.load(f)
else:
    german_patents = result_value

print('Loaded ' + str(len(german_patents)) + ' German-related patents')

# Function to extract year from grant_date
def extract_year(date_str):
    match = re.search(r'(\d{4})', date_str)
    if match:
        return int(match.group(1))
    return None

# Function to filter second half of 2019
def is_second_half_2019(date_str):
    if '2019' not in date_str:
        return False
    second_half = ['July','August','September','October','November','December',
                   'Jul','Aug','Sep','Oct','Nov','Dec']
    return any(month in date_str for month in second_half)

# Function to extract level 4 CPC codes
def get_cpc_level4(cpc_str):
    try:
        cpc_list = json.loads(cpc_str)
        codes = set()
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                codes.add(code[:4])
        return list(codes)
    except:
        return []

# Build year-by-year counts for each CPC level 4 code
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))

print('Processing patents...')
for rec in german_patents:
    grant_date = rec.get('grant_date', '')
    year = extract_year(grant_date)
    if year and year >= 2010:  # Consider data from 2010 onwards
        cpc_codes = get_cpc_level4(rec.get('cpc', '[]'))
        for cpc in cpc_codes:
            cpc_yearly_counts[cpc][year] += 1

# Check which CPC codes have data in second half 2019
print('\nChecking second half 2019 patents:')
second_half_cpcs = set()
for rec in german_patents:
    if is_second_half_2019(rec.get('grant_date', '')):
        cpc_codes = get_cpc_level4(rec.get('cpc', '[]'))
        for cpc in cpc_codes:
            second_half_cpcs.add(cpc)

print('Unique CPC codes in second half 2019: ' + str(len(second_half_cpcs)))

# Show CPC codes with highest counts in 2019
cpc_2019_counts = {}
for cpc in cpc_yearly_counts:
    cpc_2019_counts[cpc] = cpc_yearly_counts[cpc].get(2019, 0)

sorted_2019 = sorted(cpc_2019_counts.items(), key=lambda x: x[1], reverse=True)
print('\nTop CPC codes by 2019 count:')
for cpc, count in sorted_2019[:10]:
    print(cpc + ': ' + str(count))

print('\n__RESULT__:')
import json as js
result_data = {
    'total_cpc_codes': len(cpc_yearly_counts),
    'second_half_2019_codes': len(second_half_cpcs),
    'top_2019_cpcs': sorted_2019[:10],
    'year_range': list(range(min([y for c in cpc_yearly_counts.values() for y in c.keys()]), 
                           max([y for c in cpc_yearly_counts.values() for y in c.keys()]) + 1)) if cpc_yearly_counts else []
}
print(js.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
