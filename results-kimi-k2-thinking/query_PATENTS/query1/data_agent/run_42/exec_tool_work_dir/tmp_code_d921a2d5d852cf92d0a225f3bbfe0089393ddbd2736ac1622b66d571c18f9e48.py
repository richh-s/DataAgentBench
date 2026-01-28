code = """import json

# Read the result file
file_path = str(locals()['var_functions.execute_python:20']).strip("'")
with open(file_path, 'r') as f:
    cpc_codes = json.load(f)

# Create a formatted answer
answer_text = ", ".join(sorted(cpc_codes))

print('__RESULT__:')
print(answer_text)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'cpc_yearly_counts': {}, 'year_range': None, 'total_cpc_codes': 0, 'total_publications': 277813}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:20': ['A01B', 'A01G', 'A01L', 'A21B', 'A23B', 'A41B', 'A41C', 'A41D', 'A41H', 'A42B', 'A43B', 'A43D', 'A44C', 'A45D', 'A45F', 'A47B', 'A47C', 'A47F', 'A47J', 'A61B', 'A61C', 'A61D', 'A61G', 'A61H', 'A61K', 'A61L', 'A61P', 'B01F', 'B01L', 'B02B', 'B02C', 'B05B', 'B05C', 'B05D', 'B06B', 'B07B', 'B07C', 'B21F', 'B21J', 'B21L', 'B22F', 'B23K', 'B24C', 'B25B', 'B25H', 'B27C', 'B27G', 'B28D', 'B29C', 'B30B', 'B31C', 'B31F', 'B43K', 'B43L', 'B44F', 'B60B', 'B60G', 'B60H', 'B60L', 'B60Q', 'B60R', 'B60T', 'B61G', 'B61H', 'B61K', 'B61L', 'B62B', 'B62J', 'B62K', 'B63B', 'B64B', 'B64C', 'B64D', 'B64F', 'B64U', 'B65D', 'B65H', 'B66C', 'B66D', 'B67D', 'B82Y', 'C01C', 'C01D', 'C01F', 'C01P', 'C02F', 'C04B', 'C05C', 'C05F', 'C06B', 'C07C', 'C07G', 'C07H', 'C08F', 'C08K', 'C09C', 'C09D', 'C09J', 'C10G', 'C10L', 'C12L', 'C12M', 'C12Q', 'C12Y', 'C21C', 'C21D', 'C22C', 'C23G', 'C25C', 'C30B', 'D01D', 'D01F', 'D02G', 'D06M', 'D06Q', 'D07B', 'E01B', 'E01C', 'E01D', 'E02B', 'E03F', 'E04B', 'E04C', 'E04H', 'E05B', 'E21B', 'E21D', 'F01C', 'F01K', 'F01M', 'F02K', 'F03D', 'F04B', 'F04C', 'F04D', 'F04F', 'F15B', 'F16B', 'F16C', 'F16F', 'F16J', 'F16K', 'F17C', 'F21W', 'F23G', 'F24D', 'F24T', 'F24V', 'F25B', 'F26B', 'F28G', 'F41G', 'G01B', 'G01D', 'G01F', 'G01G', 'G01J', 'G01L', 'G01N', 'G01P', 'G02B', 'G02C', 'G03B', 'G03F', 'G05B', 'G06F', 'G06K', 'G07C', 'G07G', 'G09B', 'G09F', 'G11C', 'G16B', 'G21C', 'G21H', 'G21K', 'H01B', 'H01F', 'H01G', 'H01L', 'H01Q', 'H01R', 'H02N', 'H03L', 'H03M', 'H04L', 'H04N', 'H04R', 'H04S', 'H04W', 'H05B', 'Y04S']}

exec(code, env_args)
