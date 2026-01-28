code = """import json

# Load UNIV CALIFORNIA patents
univ_california_file = var_functions.query_db:20
with open(univ_california_file, 'r') as f:
    univ_california_patents = json.load(f)

# Count patents and extract basic info
total_univ_patents = len(univ_california_patents)

# Extract publication numbers using simpler method
pub_numbers = []
for patent in univ_california_patents:
    info = patent['Patents_info']
    if 'US-' in info:
        start = info.find('US-')
        end = info.find(' ', start)
        if end == -1:
            end = info.find('.', start)
        if end == -1:
            end = len(info)
        pub_numbers.append(info[start:end])

print('__RESULT__:')
print(json.dumps({
    'total_univ_california_patents': total_univ_patents,
    'sample_pub_numbers': pub_numbers[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.query_db:0', 'var_functions.query_db:2'], 'current_dir': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}]}

exec(code, env_args)
