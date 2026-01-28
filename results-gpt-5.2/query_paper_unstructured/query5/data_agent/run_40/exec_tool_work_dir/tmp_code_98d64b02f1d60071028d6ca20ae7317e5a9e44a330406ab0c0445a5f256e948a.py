code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_0hvZYWNzDy3iqrylut7ycEik)
docs = load_records(var_call_UaE8dgtnbDsQe1W7LMuL6zgu)

cit_df = pd.DataFrame(cit)
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

chi_titles = set()
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    if re.search(r"\bCHI\b\s*\d{2}", text):
        chi_titles.add(title)
    elif re.search(r"\bCHI\s*\d{4}\b", text):
        chi_titles.add(title)
    elif re.search(r"\bSIGCHI\b", text, flags=re.IGNORECASE):
        chi_titles.add(title)

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

total_citations = int(chi_cit_df['citation_count'].sum())

out = {
    'total_citations_2020_for_CHI_papers': total_citations,
    'num_CHI_papers_cited_in_2020': int(chi_cit_df['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0hvZYWNzDy3iqrylut7ycEik': 'file_storage/call_0hvZYWNzDy3iqrylut7ycEik.json', 'var_call_UaE8dgtnbDsQe1W7LMuL6zgu': 'file_storage/call_UaE8dgtnbDsQe1W7LMuL6zgu.json'}

exec(code, env_args)
