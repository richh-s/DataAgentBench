code = """import pandas as pd
import json

ema_results_raw = locals()['var_function-call-7985360290914312870']
cpc_definitions_raw_path = locals()['var_function-call-16531042350842776160']

ema_results_df = pd.DataFrame(ema_results_raw)

with open(cpc_definitions_raw_path, 'r') as f:
    cpc_definitions_data = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_data)

# Create a 4-character CPC group from the 'symbol' in cpc_definitions_df
cpc_definitions_df['cpc_group_4_from_symbol'] = cpc_definitions_df['symbol'].apply(lambda x: x[:4] if isinstance(x, str) and len(x) >= 4 else None)

# Merge the two DataFrames on the 4-character CPC group
# We use 'cpc_group_4' from ema_results_df and 'cpc_group_4_from_symbol' from cpc_definitions_df
merged_df = pd.merge(ema_results_df, cpc_definitions_df, left_on='cpc_group_4', right_on='cpc_group_4_from_symbol', how='inner')

# Sort by max_ema in descending order to correctly select the highest EMA entry for duplicates
merged_df_sorted = merged_df.sort_values(by='max_ema', ascending=False)

# Drop duplicates based on 'cpc_group_4' to get a unique title for each group
# This assumes the first entry (which is the one with max_ema due to sorting) is the desired one
final_results = merged_df_sorted.drop_duplicates(subset=['cpc_group_4'])

# Select the required columns: full title, CPC group code, and the best year
final_results = final_results[['titleFull', 'cpc_group_4', 'best_year']]

print("__RESULT__:")
print(final_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json', 'var_function-call-7985360290914312870': [{'cpc_group_4': 'B41F', 'best_year': 2007, 'max_ema': 3.0}, {'cpc_group_4': 'B60K', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B60R', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B60S', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'B60W', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B64D', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B66C', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group_4': 'C09K', 'best_year': 2015, 'max_ema': 2.0}, {'cpc_group_4': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group_4': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group_4': 'F41H', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'F42B', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group_4': 'Y02T', 'best_year': 2013, 'max_ema': 2.0}], 'var_function-call-14655044256450552688': [], 'var_function-call-7971683790454558197': [], 'var_function-call-4188447218076284597': [], 'var_function-call-16531042350842776160': 'file_storage/function-call-16531042350842776160.json', 'var_function-call-4936180994424312443': [], 'var_function-call-11275391057877533887': [], 'var_function-call-8813159367841732341': []}

exec(code, env_args)
