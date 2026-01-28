code = """import json

# Read the UNIV CALIFORNIA patents data from the file
with open('var_functions.query_db:8', 'r') as f:
    uc_patents = json.load(f)

# Also read the sample CPC data
with open('var_functions.query_db:14', 'r') as f:
    uc_patents_sample = json.load(f)

print(f"Total UNIV CALIFORNIA patents: {len(uc_patents)}")
print(f"Sample patents with CPC: {len(uc_patents_sample)}")

# Extract publication numbers from UNIV CALIFORNIA patents
uc_pub_numbers = []
for patent in uc_patents[:100]:  # Process first 100 to see pattern
    patents_info = patent['Patents_info']
    # Extract publication number using regex
    import re
    match = re.search(r'pub\. number ([^\.]+)', patents_info)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.append(pub_num)

print(f"Sample extracted publication numbers: {uc_pub_numbers[:10]}")

print('__RESULT__:')
print(json.dumps({
    "total_uc_patents": len(uc_patents),
    "sample_pub_numbers": uc_pub_numbers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
