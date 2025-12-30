code = """import json

with open(locals()['var_function-call-3599675758928509690'], 'r') as f:
    civic_docs = json.load(f)

filenames = [d.get('filename', 'NO_FILENAME') for d in civic_docs]
print("__RESULT__:")
print(filenames)"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json', 'var_function-call-7727963684795353611': 10, 'var_function-call-7768305805941479735': 'file_storage/function-call-7768305805941479735.json'}

exec(code, env_args)
