code = """import json

# The query result is stored in a JSON file
result_file = var_functions.query_db:2

print('Result file path:', result_file)

# Read the data
with open(result_file, 'r') as f:
    data = json.load(f)

print(f'\nTotal records: {len(data)}')

# Show first few records to understand structure
for i in range(min(3, len(data))):
    print(f'\n--- Record {i+1} ---')
    print('Grant date:', data[i]['grant_date'])
    print('Patents_info:', data[i]['Patents_info'][:150])
    print('CPC codes:', data[i]['cpc'][:200])

# Check date format for second half of 2019
second_half_patterns = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
matched = []
for record in data[:10]:
    grant_date = record['grant_date']
    if any(month in grant_date for month in second_half_patterns):
        matched.append(grant_date)
        
print(f'\nSample second half 2019 dates ({len(matched)}):')
for date in matched[:5]:
    print('  ', date)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
