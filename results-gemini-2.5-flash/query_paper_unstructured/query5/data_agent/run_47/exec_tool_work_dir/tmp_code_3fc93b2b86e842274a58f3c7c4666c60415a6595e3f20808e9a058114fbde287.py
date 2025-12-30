code = """import pandas as pd
import json

with open(locals()['var_function-call-12640829769598757948'], 'r') as f:
    citations_2020 = json.load(f)

citations_df = pd.DataFrame(citations_2020)
paper_titles = citations_df['title'].tolist()
print('__RESULT__:')
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-12640829769598757948': 'file_storage/function-call-12640829769598757948.json'}

exec(code, env_args)
