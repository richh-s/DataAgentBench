code = """import json
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_VFUqW3NcfYU91ZUHkCjZsNhU)
cit_rows = load_records(var_call_TQJvW4s8V8TvJmUc6cDJ8GXt)

papers_2016_pa = []
for d in paper_docs:
    fn = (d.get('filename') or '')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    head = text[:3000].lower()
    if '2016' not in head:
        continue
    if 'physical activity' not in text.lower():
        continue
    papers_2016_pa.append({'title': title})

papers_df = pd.DataFrame(papers_2016_pa).drop_duplicates()
cit_df = pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

if papers_df.empty or cit_df.empty:
    out = []
else:
    merged = papers_df.merge(cit_df, on='title', how='left')
    agg = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    out = agg.sort_values(['total_citations','title'], ascending=[False, True]).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TQJvW4s8V8TvJmUc6cDJ8GXt': 'file_storage/call_TQJvW4s8V8TvJmUc6cDJ8GXt.json', 'var_call_VFUqW3NcfYU91ZUHkCjZsNhU': 'file_storage/call_VFUqW3NcfYU91ZUHkCjZsNhU.json'}

exec(code, env_args)
