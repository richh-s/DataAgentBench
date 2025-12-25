code = """import pandas as pd
import json

# Load df_ema from the previous tool output
df_ema = pd.DataFrame(locals()['var_function-call-16247507826098301599'])

# Load cpc_definitions from the file
with open(locals()['var_function-call-16932852459668994472'], 'r') as f:
    cpc_definitions = json.load(f)

df_cpc_def = pd.DataFrame(cpc_definitions)

# Ensure 'level' is numeric and filter for level 4
df_cpc_def['level'] = pd.to_numeric(df_cpc_def['level'], errors='coerce')
df_cpc_def_level_4 = df_cpc_def[df_cpc_def['level'] == 4].copy()

# Ensure the 'symbol' column in df_cpc_def_level_4 is a string and has a length of 4
df_cpc_def_level_4['symbol'] = df_cpc_def_level_4['symbol'].astype(str)
df_cpc_def_level_4 = df_cpc_def_level_4[df_cpc_def_level_4['symbol'].apply(lambda x: len(x) == 4)]

# Print unique symbols from both dataframes for debugging
print("__RESULT__:")
print(json.dumps({
    "df_ema_cpc_groups": df_ema['cpc_group_level_4'].unique().tolist(),
    "df_cpc_def_level_4_symbols_after_filter": df_cpc_def_level_4['symbol'].unique().tolist()
}))"""

env_args = {'var_function-call-7298381649333719606': ['publicationinfo'], 'var_function-call-8434204621663570373': 'file_storage/function-call-8434204621663570373.json', 'var_function-call-12095643007052923168': 'file_storage/function-call-12095643007052923168.json', 'var_function-call-16247507826098301599': [{'cpc_group_level_4': 'B60R', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'B64D', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'H01R', 'best_year': 2018, 'highest_ema': 6.0}], 'var_function-call-7122098310074441054': ['cpc_definition'], 'var_function-call-16813371779759195505': 'file_storage/function-call-16813371779759195505.json', 'var_function-call-10657816103043330684': [], 'var_function-call-9121148012994898981': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': []}, 'var_function-call-5641823074733642942': 'file_storage/function-call-5641823074733642942.json', 'var_function-call-8396501181211844299': [], 'var_function-call-17128003059848742128': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': [None]}, 'var_function-call-14654141173622321380': 'file_storage/function-call-14654141173622321380.json', 'var_function-call-18158750276094350530': [], 'var_function-call-12330826191697419170': 'file_storage/function-call-12330826191697419170.json', 'var_function-call-6726834473258811997': [], 'var_function-call-9247441433640273810': [], 'var_function-call-11778823623185222295': 'file_storage/function-call-11778823623185222295.json', 'var_function-call-9675507773396479474': [], 'var_function-call-16932852459668994472': 'file_storage/function-call-16932852459668994472.json', 'var_function-call-6793678442724995748': [], 'var_function-call-5279222753066205063': [], 'var_function-call-5096290531346369387': [], 'var_function-call-1548625277261441538': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': []}, 'var_function-call-14420364626394245998': []}

exec(code, env_args)
