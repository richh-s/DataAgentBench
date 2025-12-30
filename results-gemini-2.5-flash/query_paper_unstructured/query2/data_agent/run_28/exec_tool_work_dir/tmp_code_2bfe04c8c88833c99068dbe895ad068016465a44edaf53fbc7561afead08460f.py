code = """import json
import pandas as pd

with open(locals()['var_function-call-11619731206948321460'], 'r') as f:
    titles = json.load(f)

filenames = [title + ".txt" for title in titles]
print('__RESULT__:')
print(json.dumps(filenames))"""

env_args = {'var_function-call-8849522580783967415': 'file_storage/function-call-8849522580783967415.json', 'var_function-call-11619731206948321460': 'file_storage/function-call-11619731206948321460.json'}

exec(code, env_args)
