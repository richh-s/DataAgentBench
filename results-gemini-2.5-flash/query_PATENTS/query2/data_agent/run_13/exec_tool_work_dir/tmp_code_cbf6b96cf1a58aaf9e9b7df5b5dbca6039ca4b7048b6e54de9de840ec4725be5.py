code = """import json
import pandas as pd

results = json.loads(locals()['var_function-call-2951946633959904125'])
df_ema = pd.DataFrame(results)

cpc_groups = df_ema['cpc_group'].unique().tolist()
print('__RESULT__:')
print(json.dumps(cpc_groups))"""

env_args = {'var_function-call-14149568722128885365': 'file_storage/function-call-14149568722128885365.json', 'var_function-call-16241435402904186256': 'file_storage/function-call-16241435402904186256.json', 'var_function-call-2951946633959904125': [{'cpc_group': 'B60R16/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B60S9/1', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'B64D11/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'B66C23/', 'best_year': 2016, 'ema': 1.0}, {'cpc_group': 'C04B223', 'best_year': 2015, 'ema': 32.0}, {'cpc_group': 'C04B35/', 'best_year': 2015, 'ema': 12.0}, {'cpc_group': 'C04B40/', 'best_year': 2015, 'ema': 1.0}, {'cpc_group': 'C09K11/', 'best_year': 2015, 'ema': 2.0}, {'cpc_group': 'E02F3/7', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'E02F3/9', 'best_year': 2012, 'ema': 1.0}, {'cpc_group': 'E02F9/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F41H11/', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'F42B3/0', 'best_year': 2012, 'ema': 2.0}, {'cpc_group': 'H01R13/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R220', 'best_year': 2018, 'ema': 2.0}, {'cpc_group': 'H01R24/', 'best_year': 2018, 'ema': 1.0}, {'cpc_group': 'H01R35/', 'best_year': 2018, 'ema': 2.0}]}

exec(code, env_args)
