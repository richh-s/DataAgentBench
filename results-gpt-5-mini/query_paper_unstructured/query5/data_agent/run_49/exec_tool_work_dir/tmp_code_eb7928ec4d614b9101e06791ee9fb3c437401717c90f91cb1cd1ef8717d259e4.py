code = """import json
import pandas as pd

with open(var_call_fyy8qeXrrcwP3ziXUvVy0mmB, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_i0bVz9Wu1fG8bFGs1JMg6jmP, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_c = pd.DataFrame(citations)
df_docs = pd.DataFrame(docs)

sample_c = df_c['title'].head(20).tolist()
sample_docs = df_docs['filename'].head(50).tolist()

out = {'sample_citation_titles_first_20': sample_c, 'sample_doc_filenames_first_50': sample_docs}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fyy8qeXrrcwP3ziXUvVy0mmB': 'file_storage/call_fyy8qeXrrcwP3ziXUvVy0mmB.json', 'var_call_i0bVz9Wu1fG8bFGs1JMg6jmP': 'file_storage/call_i0bVz9Wu1fG8bFGs1JMg6jmP.json', 'var_call_Zj5sk21Zs04TPPnVwAeZMNyZ': {'papers': [], 'total_citations_2020': 0}, 'var_call_5R56JzxbhTxICTwkZKogpw0n': {'papers': [], 'total_citations_2020': 0}}

exec(code, env_args)
