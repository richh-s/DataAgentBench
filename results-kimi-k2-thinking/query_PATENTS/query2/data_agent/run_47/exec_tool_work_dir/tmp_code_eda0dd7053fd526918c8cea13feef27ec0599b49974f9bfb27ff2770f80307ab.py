code = """import json

# Access the file path correctly
file_path = locals()['var_functions.query_db:20']

# Now load and process the data
with open(file_path, 'r') as f:
    patents_2019 = json.load(f)

# Filter for second half of 2019 (July - December)
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
filtered_patents = []

for patent in patents_2019:
    grant_date = patent.get('grant_date', '')
    if any(month in grant_date for month in second_half_months):
        filtered_patents.append(patent)

result = {
    'total_2019_patents': len(patents_2019),
    'second_half_patents': len(filtered_patents),
    'sample': filtered_patents[0] if filtered_patents else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
