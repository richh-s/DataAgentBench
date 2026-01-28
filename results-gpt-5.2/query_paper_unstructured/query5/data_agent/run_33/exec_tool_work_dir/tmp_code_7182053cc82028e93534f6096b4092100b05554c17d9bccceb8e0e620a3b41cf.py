code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_BeEZcCwAQWsdarGHmD24BWq0)
docs = load_records(var_call_7xOBOuWwOJMuKfQz0zpG8lso)

cit_df = pd.DataFrame(cit)
# coerce types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Build set of CHI paper titles from docs by regex on text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r"\bCHI\b", text) or re.search(r"CHI\s*'\d{2}", text) or re.search(r"Proceedings\s+of\s+the\s+SIGCHI\b", text, flags=re.I):
        chi_titles.add(title)

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

total_citations = int(chi_cit_df['citation_count'].sum())
num_papers = int(chi_cit_df['title'].nunique())

# also provide per-paper totals (already per year) sorted desc
per_paper = (chi_cit_df.groupby('title', as_index=False)['citation_count']
             .sum()
             .sort_values('citation_count', ascending=False))
per_paper_records = per_paper.to_dict(orient='records')

out = {
    'citation_year': 2020,
    'venue': 'CHI',
    'total_citations': total_citations,
    'num_papers': num_papers,
    'per_paper_citations': per_paper_records
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BeEZcCwAQWsdarGHmD24BWq0': 'file_storage/call_BeEZcCwAQWsdarGHmD24BWq0.json', 'var_call_7xOBOuWwOJMuKfQz0zpG8lso': 'file_storage/call_7xOBOuWwOJMuKfQz0zpG8lso.json'}

exec(code, env_args)
