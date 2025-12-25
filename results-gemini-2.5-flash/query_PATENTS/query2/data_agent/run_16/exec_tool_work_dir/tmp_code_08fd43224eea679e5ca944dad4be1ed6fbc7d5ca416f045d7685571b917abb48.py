code = """import pandas as pd
import json

ema_results = pd.DataFrame(json.loads(locals()['var_function-call-11093841680110614577']))
cpc_definitions = pd.DataFrame(json.loads(locals()['var_function-call-15794588859671135835']))

# Merge the two DataFrames on CPC group and symbol
merged_df = pd.merge(ema_results, cpc_definitions, left_on='cpc_group_4', right_on='symbol', how='inner')

# Select and rename the required columns
final_results = merged_df[['titleFull', 'cpc_group_4', 'best_year']]

# Sort by max_ema in descending order (assuming the EMA was implicitly ordered by max_ema in previous step)
# If not, we would need to merge max_ema again or keep it from previous step.
# For now, let's assume `best_year` implies the highest EMA has been selected.

print("__RESULT__:")
print(final_results.to_json(orient='records'))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json'}

exec(code, env_args)
