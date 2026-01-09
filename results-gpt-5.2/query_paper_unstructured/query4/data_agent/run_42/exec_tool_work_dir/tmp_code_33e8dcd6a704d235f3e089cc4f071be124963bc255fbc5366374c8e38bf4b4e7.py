code = """import json, re
import pandas as pd

def load_json(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

papers = load_json(var_call_5cnkZVwvAp6XSO55ky5h2ji1)
cits = load_json(var_call_xMirYK52jbxUxdVyHJRGrB4J)

# Build map title->domain/year using regex heuristics
records = []
for d in papers:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn).strip()
    text = d.get('text','')
    # year: look for 2016 in header copyright or venue line
    year = None
    m = re.search(r'\b(19\d{2}|20\d{2})\b', text[:500])
    if m:
        year = int(m.group(1))
    # better: look for copyright year
    m2 = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text)
    if m2:
        year = int(m2.group(1))
    # domain: detect keyword list in Author Keywords line
    domain = None
    m3 = re.search(r'Author Keywords\s*\n([^\n]+)', text, re.IGNORECASE)
    kwline = m3.group(1) if m3 else ''
    # normalize
    if re.search(r'physical\s*activity', text, re.IGNORECASE):
        domain = 'physical activity'
    # We'll use substring match on inferred domain; since we only need physical activity domain, use any mention in keywords
    in_domain = bool(re.search(r'physical\s*activity', kwline, re.IGNORECASE)) or bool(re.search(r'Domain[^\n]*physical\s*activity', text, re.IGNORECASE))
    # fallback: if paper is explicitly about physical activity in title keywords or abstract
    if not in_domain:
        in_domain = bool(re.search(r'physical\s*activity', title, re.IGNORECASE))
    if year == 2016 and in_domain:
        records.append({'title': title, 'year': year})

paper_df = pd.DataFrame(records).drop_duplicates()

cit_df = pd.DataFrame(cits)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'])

# total citations across all citation years
if paper_df.empty:
    out = []
else:
    merged = cit_df.merge(paper_df[['title']], on='title', how='inner')
    totals = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    out = totals.sort_values(['total_citation_count','title'], ascending=[False, True]).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tYkPsptcNfze4kqc5WFbwWGH': 'file_storage/call_tYkPsptcNfze4kqc5WFbwWGH.json', 'var_call_xMirYK52jbxUxdVyHJRGrB4J': 'file_storage/call_xMirYK52jbxUxdVyHJRGrB4J.json', 'var_call_5cnkZVwvAp6XSO55ky5h2ji1': 'file_storage/call_5cnkZVwvAp6XSO55ky5h2ji1.json'}

exec(code, env_args)
