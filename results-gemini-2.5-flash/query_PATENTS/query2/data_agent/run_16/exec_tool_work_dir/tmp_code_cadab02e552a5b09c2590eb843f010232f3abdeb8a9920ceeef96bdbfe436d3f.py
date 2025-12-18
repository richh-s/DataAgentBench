code = """import pandas as pd
import json

ema_results_raw = locals()['var_function-call-7985360290914312870']
cpc_definitions_raw_path = locals()['var_function-call-16531042350842776160']

ema_results_df = pd.DataFrame(ema_results_raw)

with open(cpc_definitions_raw_path, 'r') as f:
    cpc_definitions_df = pd.DataFrame(json.load(f))

# Merge the two DataFrames directly on 'cpc_group_4' from ema_results and 'symbol' from cpc_definitions
merged_df = pd.merge(ema_results_df, cpc_definitions_df, left_on='cpc_group_4', right_on='symbol', how='inner')

# Sort by max_ema in descending order
merged_df_sorted = merged_df.sort_values(by='max_ema', ascending=False)

# Select the required columns: full title, CPC group code, and the best year
final_results = merged_df_sorted[['titleFull', 'cpc_group_4', 'best_year']]

print("__RESULT__:")
print(final_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json', 'var_function-call-7985360290914312870': [{'cpc_group_4': 'B41F', 'best_year': 2007, 'max_ema': 3.0}, {'cpc_group_4': 'B60K', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B60R', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B60S', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'B60W', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B64D', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B66C', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group_4': 'C09K', 'best_year': 2015, 'max_ema': 2.0}, {'cpc_group_4': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group_4': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group_4': 'F41H', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'F42B', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group_4': 'Y02T', 'best_year': 2013, 'max_ema': 2.0}], 'var_function-call-14655044256450552688': [], 'var_function-call-7971683790454558197': [], 'var_function-call-4188447218076284597': [], 'var_function-call-16531042350842776160': 'file_storage/function-call-16531042350842776160.json'}

exec(code, env_args)
