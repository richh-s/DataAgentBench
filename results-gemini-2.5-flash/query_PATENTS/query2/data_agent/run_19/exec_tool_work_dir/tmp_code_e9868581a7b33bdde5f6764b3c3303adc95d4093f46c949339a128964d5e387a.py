code = """import json
import pandas as pd

# Load EMA results
ema_results = json.loads(locals()['var_function-call-14768448611898660171'])
df_ema = pd.DataFrame(ema_results)

# Load CPC definitions (level 4)
with open(locals()['var_function-call-6065871069815242158'], 'r') as f:
    cpc_definitions_raw = json.load(f)

df_cpc_def = pd.DataFrame(cpc_definitions_raw)

# Filter for level 4 CPC definitions
df_cpc_def_level4 = df_cpc_def[df_cpc_def['level'].astype(str) == '4.0'].copy()
df_cpc_def_level4 = df_cpc_def_level4[['symbol', 'titleFull']]

# Sort symbols by length in descending order to find the longest matching prefix first
level4_symbols = sorted(df_cpc_def_level4['symbol'].unique().tolist(), key=len, reverse=True)

def find_level4_cpc_group(cpc_code, symbols_list):
    for symbol in symbols_list:
        if cpc_code.startswith(symbol):
            return symbol
    return None

df_ema['cpc_group_level_4'] = df_ema['cpc_code'].apply(lambda x: find_level4_cpc_group(x, level4_symbols))

# Filter out rows where no level 4 CPC group was found
df_ema_matched = df_ema.dropna(subset=['cpc_group_level_4'])

# Merge with CPC definitions to get the full title
final_results = pd.merge(
    df_ema_matched,
    df_cpc_def_level4,
    left_on='cpc_group_level_4',
    right_on='symbol',
    how='inner'
)

# Select and reorder columns as required
output_columns = ['titleFull', 'cpc_group_level_4', 'best_year']
final_output = final_results[output_columns].drop_duplicates().to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_function-call-2218518486593243679': 'file_storage/function-call-2218518486593243679.json', 'var_function-call-14768448611898660171': [{'cpc_code': 'A43B13/223', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'A43B17/00', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'A43B7/20', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'A61B1/00', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'A61B1/00188', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'A61F5/0111', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'A61F5/0127', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'A61F5/14', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'B60R16/027', 'best_year': 2018, 'ema': 1.0}, {'cpc_code': 'B60S9/10', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'B63B21/50', 'best_year': 2014, 'ema': 1.0}, {'cpc_code': 'B64D11/0624', 'best_year': 2018, 'ema': 1.0}, {'cpc_code': 'B66C23/80', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'C04B2235/3203', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/3224', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/3229', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/3287', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/445', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/5436', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/5481', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/6565', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/6567', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/6581', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/661', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/662', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/666', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/72', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/77', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B2235/9653', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/5156', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/547', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/6261', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/64', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/645', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B35/6455', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'C04B40/0007', 'best_year': 2015, 'ema': 1.0}, {'cpc_code': 'C09K11/7772', 'best_year': 2015, 'ema': 2.0}, {'cpc_code': 'E02F9/085', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B13/02', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B13/18', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B15/143507', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'G02B15/15', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'G02B15/167', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B23/24', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B23/2415', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B23/243', 'best_year': 2016, 'ema': 1.0}, {'cpc_code': 'G02B23/2438', 'best_year': 2016, 'ema': 2.0}, {'cpc_code': 'H01R13/633', 'best_year': 2018, 'ema': 1.0}, {'cpc_code': 'H01R2201/26', 'best_year': 2018, 'ema': 2.0}, {'cpc_code': 'H01R24/60', 'best_year': 2018, 'ema': 1.0}, {'cpc_code': 'H01R35/02', 'best_year': 2018, 'ema': 1.0}, {'cpc_code': 'H01R35/04', 'best_year': 2018, 'ema': 1.0}], 'var_function-call-6065871069815242158': 'file_storage/function-call-6065871069815242158.json'}

exec(code, env_args)
