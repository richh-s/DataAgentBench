code = """import json
import pandas as pd

cpc_best_in_2022_ema = json.loads(locals()['var_function-call-17851144477517317510'])
cpc_level5_df = pd.read_json(locals()['var_function-call-4508705775201837439'])

cpc_level5_symbols = cpc_level5_df[cpc_level5_df['level'] == 5.0]['symbol'].tolist()

# Filter the CPC codes whose best year is 2022 to only include level 5 codes
result_cpc_codes = [cpc_code for cpc_code in cpc_best_in_2022_ema if cpc_code in cpc_level5_symbols]

print("__RESULT__:")
print(json.dumps(result_cpc_codes))"""

env_args = {'var_function-call-14696505315028543546': 'file_storage/function-call-14696505315028543546.json', 'var_function-call-9499660023967929457': 'file_storage/function-call-9499660023967929457.json', 'var_function-call-17851144477517317510': 'file_storage/function-call-17851144477517317510.json', 'var_function-call-4508705775201837439': 'file_storage/function-call-4508705775201837439.json'}

exec(code, env_args)
