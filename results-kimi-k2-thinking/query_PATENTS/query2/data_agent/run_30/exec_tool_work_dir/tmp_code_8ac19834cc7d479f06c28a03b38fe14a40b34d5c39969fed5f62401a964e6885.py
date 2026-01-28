code = """import json

# Get previous results
result = locals()['var_functions.execute_python:12']
cpc_codes = result['cpc_code_list']

print('Number of CPC codes to look up:', len(cpc_codes))
print('Sample CPC codes:', cpc_codes[:10])

# Format the result
formatted_result = {
    'total_cpc_groups': len(cpc_codes),
    'cpc_codes': cpc_codes,
    'top_groups': result['top_cpc'][:20]
}

print('__RESULT__:')
print(json.dumps(formatted_result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'filtered_patents_count': 72, 'cpc_level4_entries': 878, 'unique_cpc_codes_count': 97, 'top_cpc_codes': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]], 'all_unique_cpc_codes': ['B29L', 'A61K', 'F23L', 'C04B', 'F21V', 'E01F', 'B64D', 'B60Y', 'B01L', 'Y02D', 'C22F', 'B29D', 'F23N', 'G06N', 'G01R', 'A61P', 'G01L', 'H01L', 'F24F', 'G01N', 'B60W', 'B81C', 'Y04S', 'G06E', 'A61C', 'G01J', 'H01H', 'B60R', 'Y02A', 'B41F', 'C09K', 'F02M', 'B23K', 'B30B', 'F02D', 'F24B', 'G06T', 'B81B', 'Y02T', 'F04B', 'B60S', 'G01B', 'B82Y', 'H02K', 'F41H', 'A61F', 'F23B', 'F42B', 'E21B', 'Y02W', 'G02B', 'B01J', 'H04N', 'F04C', 'F02N', 'G05D', 'Y02P', 'E05Y', 'A61M', 'G08C', 'G07C', 'E05F', 'F01C', 'B27L', 'C22C', 'B22F', 'A61G', 'Y02B', 'F17C', 'E05B', 'B02C', 'G08B', 'A24C', 'B62B', 'C23F', 'F16C', 'Y02E', 'Y10T', 'H04W', 'H04L', 'B60K', 'B29K', 'F04D', 'B29C', 'G06F', 'G01D', 'C07K', 'H01R', 'F16H', 'A43B', 'A61B', 'B66C', 'F16K', 'A47C', 'B63B', 'E02F', 'B60N']}, 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:12': {'german_patents_2019_h2': 72, 'cpc_entries': 878, 'unique_cpc_codes': 97, 'cpc_code_list': ['A61M', 'F04C', 'F01C', 'E21B', 'G02B', 'G01J', 'G01B', 'G01D', 'G01R', 'H02K', 'F04D', 'G08C', 'G07C', 'B60R', 'E05B', 'B41F', 'F02D', 'F02M', 'F04B', 'B23K', 'B63B', 'H04W', 'H04L', 'Y02D', 'B66C', 'E02F', 'B60S', 'G06E', 'G06N', 'A61P', 'A61K', 'G06T', 'H04N', 'G06F', 'B60K', 'B30B', 'G01L', 'Y02T', 'F16C', 'A61F', 'A43B', 'F24B', 'F23L', 'F23B', 'F23N', 'Y02E', 'H01R', 'B64D', 'H01L', 'F02N', 'B60W', 'C04B', 'C09K', 'B29C', 'A61B', 'F21V', 'Y02P', 'Y02B', 'G01N', 'B81B', 'B01L', 'B81C', 'B01J', 'Y10T', 'B29D', 'H01H', 'A61G', 'A47C', 'E01F', 'B29K', 'C07K', 'B22F', 'C22C', 'Y02W', 'B27L', 'C22F', 'F24F', 'E05Y', 'B60Y', 'E05F', 'A61C', 'C23F', 'F16H', 'A24C', 'B82Y', 'B62B', 'Y04S', 'Y02A', 'B29L', 'B60N', 'F42B', 'F41H', 'G08B', 'B02C', 'F17C', 'G05D', 'F16K'], 'top_cpc': [['C04B', 58], ['A61M', 54], ['B29C', 45], ['H04L', 44], ['B60N', 43], ['B01L', 42], ['G01N', 36], ['H04W', 35], ['B01J', 32], ['G02B', 30], ['F17C', 30], ['G06F', 28], ['A61B', 28], ['B60K', 17], ['H02K', 16], ['F04C', 14], ['B23K', 14], ['G01R', 13], ['B29K', 13], ['F04D', 11]]}}

exec(code, env_args)
