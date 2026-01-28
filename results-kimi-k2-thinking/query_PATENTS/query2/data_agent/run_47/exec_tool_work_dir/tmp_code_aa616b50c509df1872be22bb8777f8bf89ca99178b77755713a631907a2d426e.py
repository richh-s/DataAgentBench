code = """import json

# Read the query results
with open(var_functions.query_db:8, 'r') as f:
    patents_2019 = json.load(f)

# Filter for second half of 2019 (July - December)
second_half_months = ['July', 'August', 'September', 'October', 'November', 'December']
second_half_patents = []

for patent in patents_2019:
    grant_date = patent.get('grant_date', '')
    # Check if any month from second half appears in grant_date
    if any(month in grant_date for month in second_half_months):
        second_half_patents.append(patent)

print(f"Total patents from DE in 2019: {len(patents_2019)}")
print(f"Patents granted in second half of 2019: {len(second_half_patents)}")
print("\nSample patent:")
print(json.dumps(second_half_patents[:3], indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
