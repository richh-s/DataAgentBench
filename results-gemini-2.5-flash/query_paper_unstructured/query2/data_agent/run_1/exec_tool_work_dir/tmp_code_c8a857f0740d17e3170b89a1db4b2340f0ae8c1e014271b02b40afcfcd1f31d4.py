code = """import json
import pandas as pd

with open(locals()['var_function-call-2303352090281735151'], 'r') as f:
    citations_2018 = json.load(f)

titles_2018 = [item['title'] for item in citations_2018]
print('__RESULT__:')
print(json.dumps(titles_2018))"""

env_args = {'var_function-call-2303352090281735151': 'file_storage/function-call-2303352090281735151.json'}

exec(code, env_args)
