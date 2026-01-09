code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_5yvNLJFPZgQr02sdpdWuWgUN)
docs = load_records(var_call_flO3g4fMpgesjxsJcaw877Op)

docs_titles = set([d.get('filename','')[:-4] if d.get('filename','').endswith('.txt') else d.get('filename','') for d in docs])

df = pd.DataFrame(cit)
# coerce citation_count to numeric
if 'citation_count' in df.columns:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce')

df_acm = df[df['title'].isin(docs_titles)].copy()

avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None
out = {
    'average_citation_count_2018_for_acm_papers': avg,
    'n_acm_papers_matched': int(len(df_acm)),
    'n_total_citation_records_2018': int(len(df))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5yvNLJFPZgQr02sdpdWuWgUN': 'file_storage/call_5yvNLJFPZgQr02sdpdWuWgUN.json', 'var_call_flO3g4fMpgesjxsJcaw877Op': 'file_storage/call_flO3g4fMpgesjxsJcaw877Op.json'}

exec(code, env_args)
