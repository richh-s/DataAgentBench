code = """import pandas as pd
import json

df_ema = pd.DataFrame(locals()['var_function-call-16247507826098301599'])

with open(locals()['var_function-call-5641823074733642942'], 'r') as f:
    cpc_definitions = json.load(f)

df_cpc_def = pd.DataFrame(cpc_definitions)

# Convert 'level' column to numeric, coercing errors to NaN
df_cpc_def['level'] = pd.to_numeric(df_cpc_def['level'], errors='coerce')

# Filter for level 4 CPC codes
df_cpc_def_level_4 = df_cpc_def[df_cpc_def['level'] == 4].copy()

# Extract the 4-character group code from the symbol
df_cpc_def_level_4['cpc_group_code_from_def'] = df_cpc_def_level_4['symbol'].apply(lambda x: x[:4] if isinstance(x, str) and len(x) >= 4 else None)

# Drop duplicates to ensure unique group codes and their titles
df_cpc_def_level_4_groups = df_cpc_def_level_4.drop_duplicates(subset=['cpc_group_code_from_def'])

print("__RESULT__:")
print(json.dumps({
    "df_ema_cpc_groups": df_ema['cpc_group_level_4'].unique().tolist(),
    "df_cpc_def_level_4_symbols": df_cpc_def_level_4_groups['cpc_group_code_from_def'].unique().tolist()
}))"""

env_args = {'var_function-call-7298381649333719606': ['publicationinfo'], 'var_function-call-8434204621663570373': 'file_storage/function-call-8434204621663570373.json', 'var_function-call-12095643007052923168': 'file_storage/function-call-12095643007052923168.json', 'var_function-call-16247507826098301599': [{'cpc_group_level_4': 'B60R', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'B64D', 'best_year': 2018, 'highest_ema': 1.0}, {'cpc_group_level_4': 'H01R', 'best_year': 2018, 'highest_ema': 6.0}], 'var_function-call-7122098310074441054': ['cpc_definition'], 'var_function-call-16813371779759195505': 'file_storage/function-call-16813371779759195505.json', 'var_function-call-10657816103043330684': [], 'var_function-call-9121148012994898981': {'df_ema_cpc_groups': ['B60R', 'B64D', 'H01R'], 'df_cpc_def_level_4_symbols': []}, 'var_function-call-5641823074733642942': 'file_storage/function-call-5641823074733642942.json', 'var_function-call-8396501181211844299': []}

exec(code, env_args)
