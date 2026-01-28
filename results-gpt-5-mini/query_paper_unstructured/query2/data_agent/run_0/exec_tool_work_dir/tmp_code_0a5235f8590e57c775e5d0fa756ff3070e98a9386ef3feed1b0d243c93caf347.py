code = """import json
import pandas as pd
rl = var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N
# rl is a list of records with 'title' and 'citation_count' (strings)
df = pd.DataFrame(rl)
df['citation_count'] = df['citation_count'].astype(int)
df['filename'] = df['title'] + '.txt'
filenames = df['filename'].tolist()
title_citations = dict(zip(df['title'], df['citation_count']))
out = {'filenames': filenames, 'title_citations': title_citations}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BMQZZ8eg5m7Zh9DJLBFwpd6N': 'file_storage/call_BMQZZ8eg5m7Zh9DJLBFwpd6N.json'}

exec(code, env_args)
