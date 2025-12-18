code = """import pandas as pd
import json

df_ema = pd.DataFrame(json.loads(locals()['var_function-call-16247507826098301599']))

with open(locals()['var_function-call-12330826191697419170'], 'r') as f:
    cpc_definitions = json.load(f)

df_cpc_def = pd.DataFrame(cpc_definitions)

# The cpc_definition query already filtered for level = 4, so df_cpc_def contains only level 4 entries.
# We need to ensure that the 'symbol' column is treated as a string and can be directly matched.
df_cpc_def['symbol'] = df_cpc_def['symbol'].astype(str)

# Merge EMA results with CPC definitions directly on 'cpc_group_level_4' and 'symbol'
final_df = pd.merge(
    df_ema,
    df_cpc_def,
    left_on='cpc_group_level_4',
    right_on='symbol',
    how='inner'
)

# Select and rename required columns
result = final_df[['titleFull', 'cpc_group_level_4', 'best_year', 'highest_ema']]
result = result.rename(columns={
    'titleFull': 'Full Title',
    'cpc_group_level_4': 'CPC Group Code',
    'best_year': 'Best Year',
    'highest_ema': 'Highest EMA'
})

# Sort by Highest EMA in descending order
result = result.sort_values(by='Highest EMA', ascending=False)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-7298381649333719606': ['publicationinfo'], 'var_function-call-8434204621663570373': 'file_storage/function-call-8434204621663570373.json', 'var_function-call-12095643007052923168': 'file_storage/function-call-12095643007052923168.json', 'var_function-call-16247507826098301599': [{'cpc_group_level_4': 'B60R', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'B64D', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'H01R', 'best_year': 2018, 'highest_ema': 6.0}], 'var_function-call-7122098310074441054': ['cpc_definition'], 'var_function-call-16813371779759195505': 'file_storage/function-call-16813371779759195505.json', 'var_function-call-10657816103043330684': [], 'var_function-call-9121148012994898981': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': []}, 'var_function-call-5641823074733642942': 'file_storage/function-call-5641823074733642942.json', 'var_function-call-8396501181211844299': [], 'var_function-call-17128003059848742128': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': [None]}, 'var_function-call-14654141173622321380': 'file_storage/function-call-14654141173622321380.json', 'var_function-call-18158750276094350530': [], 'var_function-call-12330826191697419170': 'file_storage/function-call-12330826191697419170.json', 'var_function-call-6726834473258811997': [], 'var_function-call-9247441433640273810': [], 'var_function-call-11778823623185222295': 'file_storage/function-call-11778823623185222295.json'}

exec(code, env_args)
