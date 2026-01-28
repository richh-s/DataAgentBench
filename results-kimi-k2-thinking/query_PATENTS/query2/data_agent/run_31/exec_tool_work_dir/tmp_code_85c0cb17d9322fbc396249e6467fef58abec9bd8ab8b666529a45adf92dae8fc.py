code = """import json

# Load the German patents data from the file
result_file = locals()['var_functions.query_db:8']
with open(result_file, 'r') as f:
    german_patents = json.load(f)

print(f"Total German patents in H2 2019: {len(german_patents)}")

# Extract patent info, CPC codes, and grant dates
extracted_data = []
for patent in german_patents:
    try:
        cpc_list = json.loads(patent['cpc'])
        cpc_codes = [cpc['code'] for cpc in cpc_list]
        
        extracted_data.append({
            'patent_info': patent['Patents_info'],
            'cpc_codes': cpc_codes,
            'grant_date': patent['grant_date']
        })
    except Exception as e:
        continue

print(f"Successfully processed patents: {len(extracted_data)}")
print(f"Sample patent data: {extracted_data[0] if extracted_data else 'No data'}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
