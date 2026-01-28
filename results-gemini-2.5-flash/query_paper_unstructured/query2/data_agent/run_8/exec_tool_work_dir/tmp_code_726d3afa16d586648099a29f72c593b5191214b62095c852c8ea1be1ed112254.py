code = """import json
import pandas as pd

with open(locals()['var_function-call-3190855524824393528'], 'r') as f:
    citations_2018 = json.load(f)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df_citations = pd.DataFrame(citations_2018)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

print('__RESULT__:')
print(df_citations['title'].to_json(orient='records'))"""

env_args = {'var_function-call-3190855524824393528': 'file_storage/function-call-3190855524824393528.json'}

exec(code, env_args)
