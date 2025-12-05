code = """import json, pandas as pd

best = var_call_KPnK4obnp65iJn5gjD523s8q

# Load CPC level-4 definitions
with open(var_call_wXZTOBJamxc1YxAIxc1zoTcs, 'r') as f:
    defs = json.load(f)

def_df = pd.DataFrame(defs)[['symbol','titleFull']]

best_df = pd.DataFrame(best)
merged = best_df.merge(def_df, left_on='cpc_group4', right_on='symbol', how='left')
merged = merged[['cpc_group4','titleFull','best_year','best_ema']]

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SsgIdKfqvKy6AQNDwhGONP1j': 'file_storage/call_SsgIdKfqvKy6AQNDwhGONP1j.json', 'var_call_wXZTOBJamxc1YxAIxc1zoTcs': 'file_storage/call_wXZTOBJamxc1YxAIxc1zoTcs.json', 'var_call_KPnK4obnp65iJn5gjD523s8q': [{'cpc_group4': 'C04B2235', 'best_year': 2019, 'best_ema': 32}, {'cpc_group4': 'B01J2219', 'best_year': 2019, 'best_ema': 28}, {'cpc_group4': 'B01L3', 'best_year': 2019, 'best_ema': 22}, {'cpc_group4': 'A61B17', 'best_year': 2019, 'best_ema': 15}, {'cpc_group4': 'A61M5', 'best_year': 2019, 'best_ema': 14}, {'cpc_group4': 'C04B35', 'best_year': 2019, 'best_ema': 12}, {'cpc_group4': 'H04L12', 'best_year': 2019, 'best_ema': 12}, {'cpc_group4': 'H04W52', 'best_year': 2019, 'best_ema': 12}, {'cpc_group4': 'B01L2300', 'best_year': 2019, 'best_ema': 10}, {'cpc_group4': 'B23K26', 'best_year': 2019, 'best_ema': 10}, {'cpc_group4': 'H04L1', 'best_year': 2019, 'best_ema': 10}, {'cpc_group4': 'B29C43', 'best_year': 2019, 'best_ema': 9}, {'cpc_group4': 'G01N27', 'best_year': 2019, 'best_ema': 9}, {'cpc_group4': 'G01N33', 'best_year': 2019, 'best_ema': 9}, {'cpc_group4': 'B29C2049', 'best_year': 2019, 'best_ema': 9}, {'cpc_group4': 'H04W72', 'best_year': 2019, 'best_ema': 9}, {'cpc_group4': 'A61M2005', 'best_year': 2019, 'best_ema': 8}, {'cpc_group4': 'G01N1', 'best_year': 2019, 'best_ema': 8}, {'cpc_group4': 'H04L41', 'best_year': 2019, 'best_ema': 8}, {'cpc_group4': 'F02M59', 'best_year': 2019, 'best_ema': 8}]}

exec(code, env_args)
