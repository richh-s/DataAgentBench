code = """import json
import pandas as pd

with open(locals()['var_function-call-8849522580783967415'], 'r') as f:
    citation_data = json.load(f)

titles = [item['title'] for item in citation_data]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-8849522580783967415': 'file_storage/function-call-8849522580783967415.json'}

exec(code, env_args)
