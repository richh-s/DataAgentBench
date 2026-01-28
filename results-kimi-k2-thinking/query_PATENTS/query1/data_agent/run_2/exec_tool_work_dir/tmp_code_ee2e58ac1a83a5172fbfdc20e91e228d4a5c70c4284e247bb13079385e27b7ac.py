code = """import json
import os

# Load the result from previous execution
filepath = locals()['var_functions.execute_python:38']

with open(filepath, 'r') as f:
    cpc_codes_2022 = json.load(f)

print(f'Number of CPC level 5 codes with best year 2022: {len(cpc_codes_2022)}')
print(f'First 20 codes: {cpc_codes_2022[:20]}')

# Return the full list
print('__RESULT__:')
print(json.dumps(cpc_codes_2022))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A61K9/06', 'A61K45/06', 'G06N3/08', 'G06N20/00', 'G02B6/3897', 'A61K31/675', 'C07D471/04', 'C07D401/14', 'A61K47/60', 'H04L69/326', 'A61B5/7267', 'G06T2207/10024', 'G06T7/90', 'A61P29/00', 'A61P35/00', 'A61P43/00', 'A61P3/10', 'A61P31/14', 'A61P25/16', 'A61P25/28', 'G06F3/011', 'A61P3/04', 'A61K47/26', 'A61P9/12', 'A61P9/10', 'A61P1/00', 'A61K31/606', 'A61K47/02', 'H01M10/613', 'G02F1/294', 'A61P9/04', 'A61P11/06', 'A61K9/2059', 'A61P3/00', 'A61P17/00', 'A61P25/20', 'A61P15/10', 'A61P25/06', 'A61P25/14', 'A61P13/12', 'A61P15/00', 'A61P13/10', 'A61P15/08', 'A61K47/12', 'A61K9/4866', 'A61P11/16', 'A61P13/00', 'A61P27/16', 'A61P25/30', 'A61P25/22', 'A61P25/24', 'A61P7/02', 'A61P37/06', 'A61P3/06', 'A61P9/02', 'H04J11/0079', 'A61P9/06', 'A61P9/00', 'C08G18/7671', 'H04N7/185', 'H04N23/51', 'H04W88/18', 'B60W2556/50'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
