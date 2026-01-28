code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:70']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Total funding records:', len(funding_data))
print('Sample records:', funding_data[:3])

# Load civic docs data
civic_file = locals()['var_functions.query_db:54']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Total civic documents:', len(civic_data))

# Build funding lookup mapping
funding_lookup = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[project_name] = amount
    
    # Also store base name without suffixes
    base_name = project_name.split(' (')[0]
    if base_name not in funding_lookup:
        funding_lookup[base_name] = amount

print('Funding lookup size:', len(funding_lookup))
print('Sample lookup entries:', list(funding_lookup.items())[:5])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:66': [{'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}], 'var_functions.list_db:68': ['civic_docs'], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
