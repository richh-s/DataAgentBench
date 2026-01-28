code = """import json
import pandas as pd

with open(locals()['var_function-call-11924547492432796297'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['title'] = citations_df['title'].str.replace('.txt', '', regex=False)
paper_titles = citations_df['title'].tolist()

print('__RESULT__:')
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-11924547492432796297': 'file_storage/function-call-11924547492432796297.json'}

exec(code, env_args)
