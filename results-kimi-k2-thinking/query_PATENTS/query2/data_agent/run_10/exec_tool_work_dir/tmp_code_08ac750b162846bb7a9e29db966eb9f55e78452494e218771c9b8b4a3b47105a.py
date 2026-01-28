code = """import json

# Get the CPC4 codes to query
cpc4_data = locals()['var_functions.execute_python:84']
cpc4_codes = cpc4_data['cpc4_codes']
print('Need to get titles for %d CPC4 codes' % len(cpc4_codes))
print('First 10 codes:', cpc4_codes[:10])
print('Sample EMA results:', cpc4_data['ema_sample'])

# Since we need to query PostgreSQL with quoted column names, let's prepare
cpc4_formatted = ['"' + code + '"' for code in cpc4_codes]
print('Formatted for SQL query')

result = {
    'cpc4_codes_to_query': cpc4_codes,
    'total_count': len(cpc4_codes),
    'ema_sample_data': cpc4_data['ema_sample']
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:20': {'status': 'attempting to access data'}, 'var_functions.query_db:26': [{'count': '11644'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:52': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': [{'total': '11644'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:78': {'patents_h2_2019': 16, 'years': [2015, 2016, 2017, 2018, 2019, 2020]}, 'var_functions.execute_python:84': {'cpc4_codes': ['H05G2/00', 'F01D5/00', 'G03F7/00', 'F02P3/00', 'F23N1/00', 'B60Q1/00', 'B60S9/00', 'B60N2/00', 'A61B1/00', 'F24B5/00', 'H02J7/00', 'A61M5/00', 'H04L5/00', 'B60J5/00', 'C10J3/00', 'B60K1/00', 'B62M7/00', 'C09G1/00', 'E02F3/00', 'A21C9/00', 'A61F5/00', 'F23L1/00', 'B60R7/00', 'H03L7/00', 'B23K1/00', 'B27N3/00', 'B25J9/00', 'A23B7/00', 'G02B5/00', 'F42B3/00', 'G07C9/00', 'F16D1/00', 'H01H9/00', 'H01F6/00', 'H02J1/00', 'G01M1/00', 'F16H3/00', 'H04L7/00', 'B24D3/00', 'C09K3/00', 'E02F9/00', 'B30B5/00', 'F26B3/00', 'G01P5/00', 'A23L3/00', 'H04L1/00', 'F16D3/00', 'B60K6/00', 'A43B7/00', 'A61L2/00'], 'ema_sample': [['H05G2/00', 2015, 0], ['F01D5/00', 2015, 0], ['G03F7/00', 2015, 0], ['F02P3/00', 2019, 0.2], ['F23N1/00', 2015, 0], ['B60Q1/00', 2017, 0.4], ['B60S9/00', 2019, 0.1], ['B60N2/00', 2019, 0.2], ['A61B1/00', 2020, 0.47], ['F24B5/00', 2015, 0]]}}

exec(code, env_args)
