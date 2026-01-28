code = """import pandas as pd
import json

citations_data_path = locals()['var_function-call-5799397423609889934']
with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
titles = df_citations['title'].tolist()
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-5799397423609889934': 'file_storage/function-call-5799397423609889934.json'}

exec(code, env_args)
