code = """import json, re
import pandas as pd

# Load citations 2018
path = var_call_FwQ6g8V3sdZaPMkvo2PJ23QG
with open(path, 'r', encoding='utf-8') as f:
    cites = json.load(f)
df_c = pd.DataFrame(cites)
df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')
df_c = df_c.dropna(subset=['citation_count'])

# Load docs
docs_path = var_call_rqp6xSjcldNIMdNhsKHetxXa
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_acm(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    # Look for strong ACM publisher markers
    patterns = [
        r'copyright\s*\d{4}\s*\u00a9\s*acm',
        r'copyright\s*\d{4}\s*\(c\)\s*acm',
        r'permission\s+to\s+make\s+digital\s+or\s+hard\s+copies.*acm',
        r'http[s]?://dx\.doi\.org/10\.1145/',
        r'doi\.org/10\.1145/',
        r'10\.1145/',
        r'permissions@acm\.org',
        r'\bacm\b\s+classification\s+keywords'
    ]
    return any(re.search(p, t, flags=re.DOTALL) for p in patterns)

acm_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_acm(d.get('text','')):
        acm_titles.append(title)

acm_set = set(acm_titles)

df_acm_2018 = df_c[df_c['title'].isin(acm_set)].copy()
avg_val = float(df_acm_2018['citation_count'].mean()) if len(df_acm_2018) else None
out = {
    'avg_citation_count_2018_for_acm_papers': avg_val,
    'num_acm_papers_with_2018_citations': int(df_acm_2018['title'].nunique()),
    'num_total_papers_with_2018_citations': int(df_c['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FwQ6g8V3sdZaPMkvo2PJ23QG': 'file_storage/call_FwQ6g8V3sdZaPMkvo2PJ23QG.json', 'var_call_rqp6xSjcldNIMdNhsKHetxXa': 'file_storage/call_rqp6xSjcldNIMdNhsKHetxXa.json', 'var_call_WpW2DavWjQQTdX76QIMwU8bf': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
