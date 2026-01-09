code = """import json, re
import pandas as pd

# Load Mongo paper docs
path_docs = var_call_0ORxyL5BbHSDGwmL8cwG5idz
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_venue(text):
    if not text:
        return None
    t = text.upper()
    # common patterns for CHI
    if re.search(r"\bCHI\s*'?\d{2}\b", t) or re.search(r"\bCHI\s+\d{4}\b", t) or re.search(r"\bSIGCHI\b", t):
        return 'CHI'
    return None

chi_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    venue = infer_venue(d.get('text',''))
    if venue == 'CHI':
        chi_titles.append(title)

# Load 2020 citations
path_cit = var_call_m52Wy4JEH31TefYiBKeRS7p3
with open(path_cit, 'r', encoding='utf-8') as f:
    cites = json.load(f)

dfc = pd.DataFrame(cites)
# ensure int
dfc['citation_count'] = dfc['citation_count'].astype(int)

chi_set = set(chi_titles)
dfc_chi_2020 = dfc[dfc['title'].isin(chi_set)]

total = int(dfc_chi_2020['citation_count'].sum())

out = {
    'total_citations_2020_for_CHI_papers': total,
    'num_CHI_papers_cited_in_2020': int(dfc_chi_2020.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0ORxyL5BbHSDGwmL8cwG5idz': 'file_storage/call_0ORxyL5BbHSDGwmL8cwG5idz.json', 'var_call_m52Wy4JEH31TefYiBKeRS7p3': 'file_storage/call_m52Wy4JEH31TefYiBKeRS7p3.json'}

exec(code, env_args)
