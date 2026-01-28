code = """import json
# variables from storage: var_call_H8MDDnwyPDGQ3ecZy7WyaqeI, var_call_VNqjwMvbL24gPBPiGuPX4POd
symbols_arca = var_call_H8MDDnwyPDGQ3ecZy7WyaqeI
tables = var_call_VNqjwMvbL24gPBPiGuPX4POd
# Compute intersection
set_arca = set(symbols_arca)
set_tables = set(tables)
common = sorted(list(set_arca & set_tables))
print("__RESULT__:")
print(json.dumps(common))"""

env_args = {'var_call_LY4mPHPrtieVLtzVUiAsS1RG': 'file_storage/call_LY4mPHPrtieVLtzVUiAsS1RG.json', 'var_call_H8MDDnwyPDGQ3ecZy7WyaqeI': 'file_storage/call_H8MDDnwyPDGQ3ecZy7WyaqeI.json', 'var_call_VNqjwMvbL24gPBPiGuPX4POd': 'file_storage/call_VNqjwMvbL24gPBPiGuPX4POd.json'}

exec(code, env_args)
