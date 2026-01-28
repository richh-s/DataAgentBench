code = """import pandas as pd
import json

with open(locals()['var_function-call-3837160533205138976'], 'r') as f:
    citations_2020 = json.load(f)

df_citations_2020 = pd.DataFrame(citations_2020)
df_citations_2020['citation_count'] = pd.to_numeric(df_citations_2020['citation_count'])

paper_titles = df_citations_2020['title'].tolist()
print("__RESULT__:")
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-3837160533205138976': 'file_storage/function-call-3837160533205138976.json'}

exec(code, env_args)
