code = """import json

symbols_to_company_names_path = locals()['var_function-call-2114712205295823325']
with open(symbols_to_company_names_path, 'r') as f:
    symbols_to_company_names = json.load(f)

available_tables_path = locals()['var_function-call-2856734424882258224']
with open(available_tables_path, 'r') as f:
    available_tables = json.load(f)

relevant_symbols = [symbol for symbol in symbols_to_company_names.keys() if symbol in available_tables]

print('__RESULT__:')
print(json.dumps(relevant_symbols))"""

env_args = {'var_function-call-12975220063519284981': 'file_storage/function-call-12975220063519284981.json', 'var_function-call-2114712205295823325': 'file_storage/function-call-2114712205295823325.json', 'var_function-call-2856734424882258224': 'file_storage/function-call-2856734424882258224.json'}

exec(code, env_args)
