code = """import json, pandas as pd

# load mongo filenames
p = var_call_eyaNhLST6KF2lmRiOPmtnilt
if isinstance(p, str):
    with open(p, 'r', encoding='utf-8') as f:
        paper_files = json.load(f)
else:
    paper_files = p

# food domain papers inferred by filename containing 'food'
food_titles = set()
for rec in paper_files:
    fn = (rec.get('filename') or '').strip()
    if not fn:
        continue
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if 'food' in title.lower():
        food_titles.add(title)

# load citations
c = var_call_kLBEszgPt6oT2SuBTvdwxnKp
if isinstance(c, str):
    with open(c, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = c

df = pd.DataFrame(citations)
if df.empty:
    total = 0
else:
    df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)
    df_food = df[df['title'].isin(food_titles)]
    total = int(df_food['citation_count'].sum())

out = {"total_citation_count_food_domain": total, "food_paper_count_matched": len(food_titles)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_eyaNhLST6KF2lmRiOPmtnilt': 'file_storage/call_eyaNhLST6KF2lmRiOPmtnilt.json', 'var_call_kLBEszgPt6oT2SuBTvdwxnKp': 'file_storage/call_kLBEszgPt6oT2SuBTvdwxnKp.json'}

exec(code, env_args)
