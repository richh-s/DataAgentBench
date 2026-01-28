code = """# Simplest approach - just return the raw codes
file_key = 'var_functions.execute_python:26'
file_path = locals()[file_key]
import json
with open(file_path, 'r') as f:
    full_result = json.load(f)

# Get just the list
codes = full_result.get('cpc_codes_best_year_2022', [])

# Print each code on a new line
for code in codes:
    print(code)

# Print result marker
print('__RESULT__:')
print('Done')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}, 'var_functions.list_db:12': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_cpc_codes': 128707, 'sample_processed': 5000, 'years_range': '2010 to 2024', 'codes_with_best_year_2022': [], 'best_codes_2022_details': []}, 'var_functions.execute_python:22': {'total_unique_codes': 0, 'frequent_codes_analyzed': 0, 'top_codes': []}, 'var_functions.execute_python:24': {'total_cpc_codes_tracked': 102927, 'top_codes_analyzed': 2000, 'best_ema_codes_by_year': {'2018': {'cpc_code': 'Y02E60/10', 'ema': 269.0, 'count': 269}, '2019': {'cpc_code': 'A61P35/00', 'ema': 257.8, 'count': 241}, '2020': {'cpc_code': 'A61P35/00', 'ema': 270.64, 'count': 322}, '2021': {'cpc_code': 'Y02E60/10', 'ema': 298.84800000000007, 'count': 428}, '2022': {'cpc_code': 'A61P35/00', 'ema': 333.56960000000004, 'count': 473}, '2023': {'cpc_code': 'Y02E60/10', 'ema': 351.02272000000005, 'count': 466}, '2024': {'cpc_code': 'Y02E60/10', 'ema': 323.81817600000005, 'count': 215}}, 'codes_whose_best_year_is_2022': ['A61P35/00'], 'details_2022': [{'cpc_code': 'A61P35/00', 'best_year': 2022, 'best_ema': 333.56960000000004, 'best_count': 473}]}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.execute_python:40': 'file_storage/functions.execute_python:40.json', 'var_functions.list_db:48': ['publicationinfo'], 'var_functions.execute_python:50': {'total_codes': 6751, 'sample_codes': ['A61K45/06', 'A61K2039/505', 'Y02P70/50', 'A61P29/00', 'C07D471/04', 'A61K38/00', 'A61K9/0019', 'H04W72/23', 'A61P25/28', 'H04L5/0053']}}

exec(code, env_args)
