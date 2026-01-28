code = """import json
import pandas as pd

with open(locals()['var_function-call-5959333085354367608'], 'r') as f:
    titles = json.load(f)

filenames = [title + '.txt' for title in titles]

print('__RESULT__:')
print(json.dumps(filenames))"""

env_args = {'var_function-call-13415103741321583316': 'file_storage/function-call-13415103741321583316.json', 'var_function-call-5959333085354367608': 'file_storage/function-call-5959333085354367608.json'}

exec(code, env_args)
