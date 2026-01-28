code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_records(var_call_6S3fWynTViCcSU89pTWYLcsU)
docs = load_records(var_call_5juurVMPM099pFxUrrGCI4sL)

cit_df = pd.DataFrame(cit)
# coerce counts to int
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# build set of CHI titles from docs by detecting venue in text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    # heuristic: accept if CHI appears as venue marker (e.g., "CHI '20" or "Proceedings of the CHI" etc.)
    if re.search(r"\bCHI\b", text):
        chi_titles.add(title)

chi_cit_2020 = cit_df[cit_df['title'].isin(chi_titles)]

# total citations for CHI papers cited in 2020
total = int(chi_cit_2020['citation_count'].sum())

out = {
    "total_citation_count": total,
    "num_papers": int(chi_cit_2020['title'].nunique())
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6S3fWynTViCcSU89pTWYLcsU': 'file_storage/call_6S3fWynTViCcSU89pTWYLcsU.json', 'var_call_5juurVMPM099pFxUrrGCI4sL': 'file_storage/call_5juurVMPM099pFxUrrGCI4sL.json'}

exec(code, env_args)
