code = """import json, pandas as pd, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_maybe_path(var_call_6rTeQEQAZgKGOBxvZpmROagG)
docs = load_maybe_path(var_call_RZlNS97SQlUlupjP0QBop1zH)

df_c = pd.DataFrame(cit)
df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')
df_c = df_c.dropna(subset=['citation_count'])

titles_all = set([re.sub(r'\.txt$', '', d.get('filename','')) for d in docs if isinstance(d, dict)])

acm_titles = {t for t in titles_all if t.startswith('ACM - ')}

# filter citations for ACM titles
mask = df_c['title'].astype(str).isin(acm_titles)
df_acm = df_c.loc[mask].copy()

avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None
out = {
    'average_citation_count_2018_acm': avg,
    'acm_papers_with_citations_2018_n': int(len(df_acm)),
    'total_papers_cited_2018_n': int(len(df_c))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6rTeQEQAZgKGOBxvZpmROagG': 'file_storage/call_6rTeQEQAZgKGOBxvZpmROagG.json', 'var_call_RZlNS97SQlUlupjP0QBop1zH': 'file_storage/call_RZlNS97SQlUlupjP0QBop1zH.json'}

exec(code, env_args)
