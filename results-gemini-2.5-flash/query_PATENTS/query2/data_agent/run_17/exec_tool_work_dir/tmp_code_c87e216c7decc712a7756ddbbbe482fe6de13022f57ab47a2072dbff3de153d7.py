code = """import pandas as pd
import json

top_cpc_groups_df = pd.read_json(locals()['var_function-call-5337988088047697233'])

# The variable var_function-call-16282831282853032359 contains the file path (string)
file_path_cpc_definitions = locals()['var_function-call-16282831282853032359']

with open(file_path_cpc_definitions, 'r') as f:
    cpc_definitions_data = json.load(f)
cpc_definitions_all = pd.DataFrame(cpc_definitions_data)

# Filter cpc_definitions_all to include only the cpc_groups from top_cpc_groups_df
merged_df = pd.merge(top_cpc_groups_df, cpc_definitions_all, left_on="cpc_group", right_on="symbol", how="inner")

# Select and rename columns as required by the problem statement
final_result = merged_df[["titleFull", "cpc_group", "best_year"]].rename(columns={
    "titleFull": "full_title",
    "cpc_group": "cpc_group_code",
    "best_year": "best_year_for_cpc_group"
})

print("__RESULT__:")
print(final_result.to_json(orient="records"))"""

env_args = {'var_function-call-3776247780831150037': 'file_storage/function-call-3776247780831150037.json', 'var_function-call-5337988088047697233': [{'cpc_group': 'C04B', 'best_year': 2015, 'max_ema': 45.0}, {'cpc_group': 'F02M', 'best_year': 2014, 'max_ema': 10.0}, {'cpc_group': 'H01J', 'best_year': 2013, 'max_ema': 10.0}, {'cpc_group': 'G02B', 'best_year': 2018, 'max_ema': 8.0}, {'cpc_group': 'F02D', 'best_year': 2017, 'max_ema': 8.0}, {'cpc_group': 'F02N', 'best_year': 2013, 'max_ema': 7.0}, {'cpc_group': 'H01R', 'best_year': 2018, 'max_ema': 6.0}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 6.0}, {'cpc_group': 'E02F', 'best_year': 2012, 'max_ema': 5.0}, {'cpc_group': 'G01L', 'best_year': 2017, 'max_ema': 4.0}], 'var_function-call-1135313935533368253': [], 'var_function-call-16282831282853032359': 'file_storage/function-call-16282831282853032359.json'}

exec(code, env_args)
