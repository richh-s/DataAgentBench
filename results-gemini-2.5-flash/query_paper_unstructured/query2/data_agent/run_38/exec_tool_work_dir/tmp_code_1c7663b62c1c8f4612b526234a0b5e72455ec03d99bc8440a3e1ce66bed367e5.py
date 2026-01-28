code = """import json
import pandas as pd

with open(locals()['var_function-call-5776649139784473340'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

titles = citations_df['title'].tolist()
print('__RESULT__:')
print(json.dumps({'titles': titles}))"""

env_args = {'var_function-call-5776649139784473340': 'file_storage/function-call-5776649139784473340.json'}

exec(code, env_args)
