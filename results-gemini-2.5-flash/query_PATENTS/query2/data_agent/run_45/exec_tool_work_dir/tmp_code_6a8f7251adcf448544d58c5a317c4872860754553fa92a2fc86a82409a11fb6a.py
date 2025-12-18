code = """import json
import pandas as pd

cpc_ema_data = locals()['var_function-call-1317980778041560380']
cpc_definitions_full = pd.read_json(locals()['var_function-call-10114930463046135881'])

# Convert 'level' to numeric, coercing errors will turn invalid parsing into NaN
cpc_definitions_full['level'] = pd.to_numeric(cpc_definitions_full['level'], errors='coerce')

final_results = []

for entry in cpc_ema_data:
    cpc_group_prefix = entry['cpc_group']
    best_year = entry['best_year']
    max_ema = entry['max_ema']

    # Filter for level 4 CPC symbols that start with the cpc_group_prefix
    # Also ensure 'level' is not NaN after conversion and is equal to 4
    matching_definitions = cpc_definitions_full[
        (cpc_definitions_full['symbol'].str.startswith(cpc_group_prefix, na=False)) & 
        (cpc_definitions_full['level'] == 4)
    ]

    if not matching_definitions.empty:
        for _, def_row in matching_definitions.iterrows():
            final_results.append({
                'cpc_group_code': def_row['symbol'],
                'full_title': def_row['titleFull'],
                'best_year_ema': best_year,
                'max_ema': max_ema
            })

# Sort the final results by max_ema in descending order
final_results_sorted = sorted(final_results, key=lambda x: x['max_ema'], reverse=True)

# Format the output for readability
formatted_output = []
for item in final_results_sorted:
    formatted_output.append(
        "CPC Group Code: " + str(item['cpc_group_code']) + "\n" +
        "Full Title: " + str(item['full_title']) + "\n" +
        "Best Year for EMA: " + str(item['best_year_ema']) + "\n" +
        "Max EMA: " + f"{item['max_ema']:.2f}"
    )

print("__RESULT__:")
print(json.dumps("\n\n".join(formatted_output)))"""

env_args = {'var_function-call-13781591671737650296': [], 'var_function-call-159961854333049397': 'file_storage/function-call-159961854333049397.json', 'var_function-call-14805747375982610187': [], 'var_function-call-10929909419482869292': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}], 'var_function-call-15674998834885795494': [], 'var_function-call-3203908515550012934': 'file_storage/function-call-3203908515550012934.json', 'var_function-call-600729039729646520': [], 'var_function-call-11435041568651700914': 'file_storage/function-call-11435041568651700914.json', 'var_function-call-8517005424988983734': [], 'var_function-call-656837194378036393': 'file_storage/function-call-656837194378036393.json', 'var_function-call-7737786209067804494': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-541724979457509416': ['A61F', 'H02J', 'H03L', 'A43B', 'G01M', 'F01D', 'F05D', 'H04L', 'F04D', 'F16F'], 'var_function-call-12857969857747079952': [], 'var_function-call-6666716879358711252': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-10749211325850591547': ['A61F', 'H02J', 'H03L', 'A43B', 'G01M', 'F01D', 'F05D', 'H04L', 'F04D', 'F16F'], 'var_function-call-10114930463046135881': 'file_storage/function-call-10114930463046135881.json', 'var_function-call-17116891878385305191': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}], 'var_function-call-4837316381396745111': 'file_storage/function-call-4837316381396745111.json', 'var_function-call-1317980778041560380': [{'cpc_group': 'A61F', 'best_year': 2016, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H02J', 'best_year': 2009, 'max_ema': 0.6000000000000001}, {'cpc_group': 'H03L', 'best_year': 2015, 'max_ema': 0.6000000000000001}, {'cpc_group': 'A43B', 'best_year': 2016, 'max_ema': 0.5}, {'cpc_group': 'G01M', 'best_year': 2018, 'max_ema': 0.4}, {'cpc_group': 'F01D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'F05D', 'best_year': 2018, 'max_ema': 0.2}, {'cpc_group': 'H04L', 'best_year': 2015, 'max_ema': 0.2}, {'cpc_group': 'F04D', 'best_year': 2018, 'max_ema': 0.1}, {'cpc_group': 'F16F', 'best_year': 2018, 'max_ema': 0.1}]}

exec(code, env_args)
