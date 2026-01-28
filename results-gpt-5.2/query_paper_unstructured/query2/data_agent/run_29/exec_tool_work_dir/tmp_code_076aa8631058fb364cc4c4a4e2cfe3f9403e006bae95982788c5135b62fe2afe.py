code = """import json, pandas as pd, re

# Load citations 2018
cit_path = var_call_rLOEVyYt3SIODNzDcZxP28fR
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
df_c = pd.DataFrame(citations)
# normalize types
if not df_c.empty:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce')

# Load docs
docs_path = var_call_GhJwNOKRZQne5O2eOO752411
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def is_acm(text: str) -> bool:
    if not text:
        return False
    t = text.lower()
    # strong ACM signals
    if 'permission to make digital or hard copies' in t and 'acm' in t:
        return True
    if 'copyright' in t and 'acm' in t:
        return True
    if 'acm classification keywords' in t:
        return True
    if 'request permissions from permissions@acm.org' in t:
        return True
    if re.search(r'\b(c)\s*acm\b', t):
        return True
    if 'association for computing machinery' in t:
        return True
    return False

acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_acm(d.get('text','')):
        acm_titles.add(title)

# Join and compute average
if df_c.empty:
    avg = None
    n = 0
else:
    df_join = df_c[df_c['title'].isin(acm_titles)].copy()
    n = int(df_join.shape[0])
    avg = float(df_join['citation_count'].mean()) if n>0 else None

out = {
    "average_citation_count_2018_for_acm_papers": avg,
    "acm_papers_with_2018_citations_count": n
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rLOEVyYt3SIODNzDcZxP28fR': 'file_storage/call_rLOEVyYt3SIODNzDcZxP28fR.json', 'var_call_GhJwNOKRZQne5O2eOO752411': 'file_storage/call_GhJwNOKRZQne5O2eOO752411.json'}

exec(code, env_args)
