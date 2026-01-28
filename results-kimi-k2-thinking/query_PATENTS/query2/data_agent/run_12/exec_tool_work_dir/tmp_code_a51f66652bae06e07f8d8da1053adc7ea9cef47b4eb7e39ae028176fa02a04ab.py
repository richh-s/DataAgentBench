code = """import json
import re
from collections import defaultdict, OrderedDict
import math

# Load German patent data
result_value = locals()['var_functions.query_db:48']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        patents = json.load(f)
else:
    patents = result_value

print('Total German patents from 2019:', len(patents))

# Function to check if date is in second half 2019
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
        codes = defaultdict(int)  # code: count in this patent
        for item in cpc_list:
            code = item.get('code', '')
            if len(code) >= 4:
                level4 = code[:4]
                codes[level4] += 1
        return list(codes.keys())
    except:
        return []

# Function to extract year
def extract_year(date_str):
    match = re.search(r'(\d{4})', date_str)
    return int(match.group(1)) if match else None

# Build historical data for EMA calculation
print('Building historical patent counts by CPC and year...')
cpc_yearly_counts = defaultdict(lambda: defaultdict(int))
extended_cpc_codes = set()

# First, collect all patents from the database to build history
# For now, use the 2019 data we have and create mock historical data to demonstrate
# In real scenario, we would query all years

# Process our 2019 German patents
second_half_2019_patents = []
for rec in patents:
    if is_second_half_2019(rec.get('grant_date', '')):
        second_half_2019_patents.append(rec)
        cpc_codes = get_cpc_level4(rec.get('cpc', '[]'))
        for cpc in cpc_codes:
            cpc_yearly_counts[cpc][2019] += 1
            extended_cpc_codes.add(cpc)

print('German patents in second half 2019:', len(second_half_2019_patents))
print('Unique CPC level 4 codes found:', len(extended_cpc_codes))

# Query for historical data - we need to get German patents from earlier years
# For demonstration, let's check what years we have in our data
years_in_data = defaultdict(int)
for rec in patents:
    year = extract_year(rec.get('grant_date', ''))
    if year:
        years_in_data[year] += 1

print('Years found in German patent data:', dict(years_in_data))

# Get the CPC codes with highest counts in second half 2019
cpc_2019_counts = defaultdict(int)
for rec in second_half_2019_patents:
    cpc_codes = get_cpc_level4(rec.get('cpc', '[]'))
    for cpc in cpc_codes:
        cpc_2019_counts[cpc] += 1

top_cpcs = sorted(cpc_2019_counts.items(), key=lambda x: x[1], reverse=True)[:20]
print('\nTop CPC level 4 codes by count in second half 2019:')
for cpc, count in top_cpcs:
    print(f"{cpc}: {count} patents")

print('\n__RESULT__:')
print(json.dumps({
    'second_half_2019_patents': len(second_half_2019_patents),
    'total_cpc_codes': len(extended_cpc_codes),
    'top_cpcs': top_cpcs
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': [{'total': '216'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
