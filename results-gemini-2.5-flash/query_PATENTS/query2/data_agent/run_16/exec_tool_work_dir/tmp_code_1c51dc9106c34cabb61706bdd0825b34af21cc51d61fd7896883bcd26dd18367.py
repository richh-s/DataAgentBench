code = """import pandas as pd
import json

ema_results_raw = locals()['var_function-call-7985360290914312870']
cpc_definitions_raw_path = locals()['var_function-call-14745830415751959940']

ema_results_df = pd.DataFrame(ema_results_raw)

with open(cpc_definitions_raw_path, 'r') as f:
    cpc_definitions_data = json.load(f)
cpc_definitions_df = pd.DataFrame(cpc_definitions_data)

# Convert 'level' to numeric, coercing errors to NaN
cpc_definitions_df['level'] = pd.to_numeric(cpc_definitions_df['level'], errors='coerce')

# Filter cpc_definitions_df to include only records where 'level' is 4
cpc_definitions_level_4_df = cpc_definitions_df[cpc_definitions_df['level'] == 4.0].copy()

# Extract unique cpc_group_4 values from ema_results_df
ema_cpc_groups = set(ema_results_df['cpc_group_4'].unique())

# Extract unique symbol values from cpc_definitions_level_4_df
def_symbols_level_4 = set(cpc_definitions_level_4_df['symbol'].unique())

# Find the intersection of these two sets
common_cpc_groups = ema_cpc_groups.intersection(def_symbols_level_4)

# Convert the set to a list for JSON serialization
print("__RESULT__:")
print(json.dumps(list(common_cpc_groups)))"""

env_args = {'var_function-call-297126640787404012': 'file_storage/function-call-297126640787404012.json', 'var_function-call-5068727344322754251': 'file_storage/function-call-5068727344322754251.json', 'var_function-call-11093841680110614577': [{'cpc_group_4': 'B41F', 'best_year': 2007}, {'cpc_group_4': 'B60K', 'best_year': 2013}, {'cpc_group_4': 'B60R', 'best_year': 2018}, {'cpc_group_4': 'B60S', 'best_year': 2016}, {'cpc_group_4': 'B60W', 'best_year': 2013}, {'cpc_group_4': 'B64D', 'best_year': 2018}, {'cpc_group_4': 'B66C', 'best_year': 2016}, {'cpc_group_4': 'C04B', 'best_year': 2015}, {'cpc_group_4': 'C09K', 'best_year': 2015}, {'cpc_group_4': 'E02F', 'best_year': 2012}, {'cpc_group_4': 'F02N', 'best_year': 2013}, {'cpc_group_4': 'F41H', 'best_year': 2012}, {'cpc_group_4': 'F42B', 'best_year': 2012}, {'cpc_group_4': 'H01R', 'best_year': 2018}, {'cpc_group_4': 'Y02T', 'best_year': 2013}], 'var_function-call-15794588859671135835': 'file_storage/function-call-15794588859671135835.json', 'var_function-call-7985360290914312870': [{'cpc_group_4': 'B41F', 'best_year': 2007, 'max_ema': 3.0}, {'cpc_group_4': 'B60K', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B60R', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B60S', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'B60W', 'best_year': 2013, 'max_ema': 1.0}, {'cpc_group_4': 'B64D', 'best_year': 2018, 'max_ema': 1.0}, {'cpc_group_4': 'B66C', 'best_year': 2016, 'max_ema': 1.0}, {'cpc_group_4': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group_4': 'C09K', 'best_year': 2015, 'max_ema': 2.0}, {'cpc_group_4': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group_4': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group_4': 'F41H', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'F42B', 'best_year': 2012, 'max_ema': 2.0}, {'cpc_group_4': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group_4': 'Y02T', 'best_year': 2013, 'max_ema': 2.0}], 'var_function-call-14655044256450552688': [], 'var_function-call-7971683790454558197': [], 'var_function-call-4188447218076284597': [], 'var_function-call-16531042350842776160': 'file_storage/function-call-16531042350842776160.json', 'var_function-call-4936180994424312443': [], 'var_function-call-11275391057877533887': [], 'var_function-call-8813159367841732341': [], 'var_function-call-12758969213205302255': [], 'var_function-call-12880038949360923757': 'file_storage/function-call-12880038949360923757.json', 'var_function-call-6613148521276364075': [], 'var_function-call-11731273159119014989': 'file_storage/function-call-11731273159119014989.json', 'var_function-call-17101546386702363979': [], 'var_function-call-6553186611529925794': 'file_storage/function-call-6553186611529925794.json', 'var_function-call-5794199066746412496': [], 'var_function-call-2955801480948424602': [], 'var_function-call-16416045839829885028': 'file_storage/function-call-16416045839829885028.json', 'var_function-call-6993928978843861115': [], 'var_function-call-9351177106290979055': [], 'var_function-call-14745830415751959940': 'file_storage/function-call-14745830415751959940.json'}

exec(code, env_args)
