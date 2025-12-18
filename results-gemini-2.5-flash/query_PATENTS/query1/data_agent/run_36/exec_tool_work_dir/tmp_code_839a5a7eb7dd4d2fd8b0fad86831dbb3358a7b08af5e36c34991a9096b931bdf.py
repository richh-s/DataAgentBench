code = """import json
import pandas as pd

# Load the list of CPC codes with best year 2022
with open(locals()['var_function-call-18279914507798233150'], 'r') as f:
    cpc_best_year_2022 = json.load(f)

# Load the list of CPC symbols at level 5
with open(locals()['var_function-call-2004928542684280443'], 'r') as f:
    cpc_level_5_data = json.load(f)

cpc_level_5_symbols = {item['symbol'] for item in cpc_level_5_data if 'symbol' in item}

# Filter the cpc_best_year_2022 list to include only those that are at level 5
final_cpc_codes = [cpc_code for cpc_code in cpc_best_year_2022 if cpc_code in cpc_level_5_symbols]

print("__RESULT__:")
print(json.dumps(final_cpc_codes))"""

env_args = {'var_function-call-9977547959283513273': 'file_storage/function-call-9977547959283513273.json', 'var_function-call-18279914507798233150': 'file_storage/function-call-18279914507798233150.json', 'var_function-call-10286633462980733954': 'file_storage/function-call-10286633462980733954.json', 'var_function-call-2004928542684280443': 'file_storage/function-call-2004928542684280443.json'}

exec(code, env_args)
