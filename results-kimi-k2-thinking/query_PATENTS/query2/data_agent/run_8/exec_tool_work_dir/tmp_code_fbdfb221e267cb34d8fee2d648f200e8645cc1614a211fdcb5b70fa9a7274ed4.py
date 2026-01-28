code = """import json

# Load the patent data from storage and analyze what we have
file_path_2019 = locals()['var_functions.query_db:2']
with open(file_path_2019, 'r') as f:
    patents_2019 = json.load(f)

# Check if we have multi-year data
file_path_multi = locals()['var_functions.query_db:36']
with open(file_path_multi, 'r') as f:
    patents_multi = json.load(f)

print('2019 patents count:', len(patents_2019))
print('Multi-year patents count:', len(patents_multi))

# Sample to see date ranges
sample_dates_2019 = [p['grant_date'] for p in patents_2019[:10]]
sample_dates_multi = [p['grant_date'] for p in patents_multi[:10]]

print('Sample 2019 dates:', sample_dates_2019)
print('Sample multi-year dates:', sample_dates_multi)

result = {
    'patents_2019_count': len(patents_2019),
    'patents_multi_count': len(patents_multi),
    'has_enough_data': True
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_patents_2019': 3838, 'sample_records_count': 3}, 'var_functions.execute_python:10': {'total_de_patents_2019': 25, 'de_patents_h2_2019': 12}, 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 13, 'total_cpc_entries': 137, 'total_cpc_level4_entries': 137, 'unique_cpc_level4_codes': 81, 'sample_codes': ['B29C49/06', 'F02N2200/022', 'C04B2235/543', 'H01R35/04', 'H01J49/003', 'B29C49/58', 'H02J7/34', 'A61B90/70', 'F02N11/04', 'H01J49/421']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:26': {'total_patents': 129, 'unique_cpc_codes': 77, 'top_cpc_codes': [['C04B2235/656', 4], ['C04B2235/322', 4], ['C04B35/645', 4], ['H01J49/164', 3], ['H01J49/046', 3], ['B29C2049/589', 3], ['A61F5/14', 2], ['A61F5/012', 2], ['A61F5/011', 2], ['A43B17/00', 2], ['A43B7/20', 2], ['H01J49/043', 2], ['H01R2201/26', 2], ['C04B2235/965', 2], ['C04B2235/77', 2], ['C04B2235/72', 2], ['C04B2235/666', 2], ['C04B2235/662', 2], ['C04B2235/661', 2], ['C04B2235/658', 2]]}, 'var_functions.execute_python:28': {'total_cpc_level4_codes': 77, 'unique_main_groups': 40, 'main_groups': ['H01R13', 'H01R2201', 'A61B2090', 'A21C9', 'C09K11', 'A43B13', 'B29C2949', 'F02N2300', 'B29C49', 'C04B40', 'B29C2049', 'B60K6', 'B60R16', 'H01R35', 'F02P3', 'A43B7', 'H01F38', 'G01N27', 'H01J49', 'F02N11', 'A61B90', 'H01R24', 'F02D15', 'A43B17', 'C04B35', 'A61L2', 'B60W30', 'F02P15', 'H01F27', 'F02D13', 'B64D11', 'H02J7', 'Y02T10', 'A47J37', 'H02J1', 'F02N2200', 'C04B2235', 'G01F23', 'F02D41', 'A61F5']}, 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
