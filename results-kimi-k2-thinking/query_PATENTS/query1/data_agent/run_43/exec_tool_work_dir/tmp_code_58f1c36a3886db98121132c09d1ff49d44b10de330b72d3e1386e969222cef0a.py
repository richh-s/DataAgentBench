code = """import json

# Get the file path from the storage
file_path = locals()['var_functions.execute_python:30']

# Read the data from the file
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract the CPC codes
cpc_codes = data['cpc_codes_level5_best_2022']

# Format output as plain text with one code per line
output = '\n'.join(cpc_codes)

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'total_records': 5, 'years_range': [2020, 2021], 'unique_cpc_groups': 18, 'sample_data_points': [[2021, {'C01B': 6, 'H01M': 25, 'C01G': 3, 'C01P': 3, 'Y02E': 1, 'B29C': 4, 'C08J': 7, 'B32B': 44, 'C09D': 1, 'B29L': 2, 'C08G': 5, 'B29K': 4, 'H01H': 11}], [2020, {'F16H': 22, 'A61K': 4, 'C12N': 12, 'A01K': 3, 'A61P': 1}]]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'total_records': '277813'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:24': {'years_analyzed': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 'total_level5_codes_recent': 141687, 'codes_best_2022': 17241}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json'}

exec(code, env_args)
