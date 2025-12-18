code = """import json

# Load the list of CPC codes with best year 2022
with open(locals()['var_function-call-18279914507798233150'], 'r') as f:
    cpc_best_year_2022 = json.load(f)

# Format the list of CPC codes into a SQL-compatible string for an IN clause
# Each CPC code needs to be enclosed in single quotes
cpc_codes_sql_format = ", ".join([f"'{cpc}'" for cpc in cpc_best_year_2022])

print("__RESULT__:")
print(json.dumps(cpc_codes_sql_format))"""

env_args = {'var_function-call-9977547959283513273': 'file_storage/function-call-9977547959283513273.json', 'var_function-call-18279914507798233150': 'file_storage/function-call-18279914507798233150.json'}

exec(code, env_args)
