code = """import json

# Load the UNIV CALIFORNIA patents data
california_patents_path = locals()['var_functions.query_db:4']
if isinstance(california_patents_path, str):
    with open(california_patents_path, 'r') as f:
        california_patents = json.load(f)
else:
    california_patents = california_patents_path

# Extract publication numbers and CPC codes from UNIV CALIFORNIA patents
publication_numbers = []
for patent in california_patents:
    patents_info = patent['Patents_info']
    # Extract publication number
    if 'pub. number' in patents_info:
        start = patents_info.find('pub. number') + len('pub. number')
        pub_num = patents_info[start:].strip().split()[0]
        publication_numbers.append(pub_num)
    elif 'publication number' in patents_info:
        start = patents_info.find('publication number') + len('publication number')
        pub_num = patents_info[start:].strip().split()[0]
        publication_numbers.append(pub_num)

print(f"Found {len(publication_numbers)} UNIV CALIFORNIA publication numbers")
print("Sample:", publication_numbers[:10])

# Extract CPC codes from the first few patents
all_cpc_codes = []
for patent in california_patents:
    cpc_data = json.loads(patent['cpc'])
    codes = [item['code'] for item in cpc_data]
    all_cpc_codes.extend(codes)

unique_cpc = list(set(all_cpc_codes))
print(f"\nFound {len(unique_cpc)} unique CPC codes")
print("Sample CPC codes:", unique_cpc[:10])

# Format data as JSON serializable
result_data = {
    'publication_numbers': publication_numbers,
    'cpc_codes': unique_cpc
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
