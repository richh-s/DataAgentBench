code = """import json, re
import pandas as pd

# Load mongo docs
mongo_path = var_call_OKl3samXQcDfcp24HvWR98Lq
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# helper to extract year from text
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_pub_year(text):
    # prioritize copyright year
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(\d{4})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # conference string like "CHI '18" or "UbiComp '17"
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|TEI|OzCHI|WWW|AH|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 70 else 1900 + yy
    # fallback: earliest year >= 1990
    years = [int(y) for y in year_pat.findall(text)]
    years = [y for y in years if 1990 <= y <= 2026]
    return min(years) if years else None

papers = []
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r'\.txt$','', filename)
    text = d.get('text','') or ''
    pub_year = extract_pub_year(text)
    # contribution heuristic: contains word empirical (case-insensitive)
    is_empirical = bool(re.search(r'\bempirical\b', text, flags=re.IGNORECASE))
    papers.append({'title': title, 'pub_year': pub_year, 'is_empirical': is_empirical})

pdf = pd.DataFrame(papers)
# Filter after 2016 and empirical
pdf_filt = pdf[(pdf['is_empirical']) & (pdf['pub_year'].notna()) & (pdf['pub_year'] > 2016)].copy()

# citations
cit_path = var_call_8ChWFSilOVaYLy46HeCEYRfm
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cdf = pd.DataFrame(cits)
# ensure numeric
cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

taggr = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = pdf_filt.merge(taggr, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
res = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_OKl3samXQcDfcp24HvWR98Lq': 'file_storage/call_OKl3samXQcDfcp24HvWR98Lq.json', 'var_call_8ChWFSilOVaYLy46HeCEYRfm': 'file_storage/call_8ChWFSilOVaYLy46HeCEYRfm.json'}

exec(code, env_args)
