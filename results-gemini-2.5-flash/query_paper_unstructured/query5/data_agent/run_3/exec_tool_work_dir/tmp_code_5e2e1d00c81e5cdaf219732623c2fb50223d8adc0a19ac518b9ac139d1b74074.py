code = """import json
import pandas as pd

with open(locals()['var_function-call-688809817332979845'], 'r') as f:
    citations_2020_data = json.load(f)

citations_2020_df = pd.DataFrame(citations_2020_data)
citations_2020_df['citation_count'] = pd.to_numeric(citations_2020_df['citation_count'])

titles = citations_2020_df['title'].tolist()
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-688809817332979845': 'file_storage/function-call-688809817332979845.json'}

exec(code, env_args)
