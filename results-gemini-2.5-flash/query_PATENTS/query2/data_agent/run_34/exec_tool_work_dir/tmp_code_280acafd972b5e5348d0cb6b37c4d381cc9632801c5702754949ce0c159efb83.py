code = """import pandas as pd
import json

# Load the best_year_per_cpc data
best_year_per_cpc = json.loads(locals()['var_function-call-3619053925715813172'])
df_best_year = pd.DataFrame(best_year_per_cpc)

# Load the full CPC definitions from the file
with open(locals()['var_function-call-7886444875792061773'], 'r') as f:
    cpc_definitions = json.load(f)
df_cpc_definitions = pd.DataFrame(cpc_definitions)

# Extract CPC level 4 from the symbol in cpc_definitions
df_cpc_definitions['cpc_group_code'] = df_cpc_definitions['symbol'].str[:4]

# Merge to get the full title
final_results = pd.merge(df_best_year, df_cpc_definitions, on='cpc_group_code', how='left')

# Select and rename columns for the final output
final_output = final_results[['titleFull', 'cpc_group_code', 'best_year']].drop_duplicates()

print('__RESULT__:')
print(final_output.to_json(orient='records'))"""

env_args = {'var_function-call-11734270909720189975': 'file_storage/function-call-11734270909720189975.json', 'var_function-call-5628256844691457939': 'file_storage/function-call-5628256844691457939.json', 'var_function-call-3619053925715813172': [], 'var_function-call-7886444875792061773': 'file_storage/function-call-7886444875792061773.json'}

exec(code, env_args)
