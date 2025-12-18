code = """import pandas as pd
import json

# Load df_ema correctly. It's already a list of dicts.
df_ema = pd.DataFrame(locals()['var_function-call-16247507826098301599'])

# Load cpc_definitions from the file
with open(locals()['var_function-call-16932852459668994472'], 'r') as f:
    cpc_definitions = json.load(f)

df_cpc_def = pd.DataFrame(cpc_definitions)

# Ensure 'level' is numeric and filter for level 4 entries from CPC definition
df_cpc_def['level'] = pd.to_numeric(df_cpc_def['level'], errors='coerce')
df_cpc_def_level_4 = df_cpc_def[df_cpc_def['level'] == 4].copy()

# Ensure the 'symbol' column in df_cpc_def_level_4 is a string and has a length of 4
df_cpc_def_level_4['symbol'] = df_cpc_def_level_4['symbol'].astype(str)
df_cpc_def_level_4 = df_cpc_def_level_4[df_cpc_def_level_4['symbol'].apply(lambda x: len(x) == 4)]

# Merge EMA results with CPC definitions on the CPC group code
final_df = pd.merge(
    df_ema,
    df_cpc_def_level_4,
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

env_args = {'var_function-call-7298381649333719606': ['publicationinfo'], 'var_function-call-8434204621663570373': 'file_storage/function-call-8434204621663570373.json', 'var_function-call-12095643007052923168': 'file_storage/function-call-12095643007052923168.json', 'var_function-call-16247507826098301599': [{'cpc_group_level_4': 'B60R', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'B64D', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'H01R', 'best_year': 2018, 'highest_ema': 6.0}], 'var_function-call-7122098310074441054': ['cpc_definition'], 'var_function-call-16813371779759195505': 'file_storage/function-call-16813371779759195505.json', 'var_function-call-10657816103043330684': [], 'var_function-call-9121148012994898981': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': []}, 'var_function-call-5641823074733642942': 'file_storage/function-call-5641823074733642942.json', 'var_function-call-8396501181211844299': [], 'var_function-call-17128003059848742128': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': [None]}, 'var_function-call-14654141173622321380': 'file_storage/function-call-14654141173622321380.json', 'var_function-call-18158750276094350530': [], 'var_function-call-12330826191697419170': 'file_storage/function-call-12330826191697419170.json', 'var_function-call-6726834473258811997': [], 'var_function-call-9247441433640273810': [], 'var_function-call-11778823623185222295': 'file_storage/function-call-11778823623185222295.json', 'var_function-call-9675507773396479474': [], 'var_function-call-16932852459668994472': 'file_storage/function-call-16932852459668994472.json', 'var_function-call-6793678442724995748': [], 'var_function-call-5279222753066205063': []}

exec(code, env_args)
