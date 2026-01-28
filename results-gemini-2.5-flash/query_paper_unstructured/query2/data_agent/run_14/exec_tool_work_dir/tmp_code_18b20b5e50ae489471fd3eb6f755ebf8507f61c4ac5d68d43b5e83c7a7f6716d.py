code = """import json
import pandas as pd

with open(locals()['var_function-call-10626874306656494420'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
titles = df_citations['title'].tolist()

print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-10626874306656494420': 'file_storage/function-call-10626874306656494420.json'}

exec(code, env_args)
