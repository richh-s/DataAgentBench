code = """import json, re, pandas as pd

# Load mongo results (may be file path)
md = var_call_BnFG7NMNwOlOF78McYE12CcR
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_NGUDu0rlWfSbJltgy6x0eoxR
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

# helper to extract year and domain from text

def extract_year(text):
    # prefer explicit conference year patterns like 'CHI 2016' etc.
    m = re.search(r'\b(19|20)\d{2}\b', text)
    if m:
        y = int(m.group(0))
        if 1980 <= y <= 2026:
            return y
    return None

# domain heuristic: physical activity if mentions activity tracking/physical activity/fitness/exercise/steps etc.
pa_pat = re.compile(r'(?i)\b(physical activity|activity\s+tracking|fitness\s+tracker|fitness\s+tracking|exercise\s+technology|step\s*count|steps\b|sedentary|workout|walking\b|running\b)\b')

papers = []
for d in md:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    if not pa_pat.search(text):
        continue
    year = None
    # try to find publication year near beginning where venue lines exist
    head = text[:5000]
    m = re.search(r'\b(ACM|IEEE)\b.*?\b(19|20)\d{2}\b', head, flags=re.S)
    if m:
        y = re.search(r'\b(19|20)\d{2}\b', m.group(0)).group(0)
        year = int(y)
    if year is None:
        # CHI/UbiComp style: 'CHI 2016' or 'UbiComp 2016'
        m2 = re.search(r'\b(CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(19|20)\d{2}\b', head)
        if m2:
            year = int(re.search(r'(19|20)\d{2}', m2.group(0)).group(0))
    if year is None:
        year = extract_year(head)
    if year == 2016:
        papers.append({'title': title})

pa_titles = {p['title'] for p in papers}

# join with citations totals
cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'])
    cit_df = cit_df[cit_df['title'].isin(pa_titles)].copy()

out = cit_df.sort_values('total_citations', ascending=False).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BnFG7NMNwOlOF78McYE12CcR': 'file_storage/call_BnFG7NMNwOlOF78McYE12CcR.json', 'var_call_NGUDu0rlWfSbJltgy6x0eoxR': 'file_storage/call_NGUDu0rlWfSbJltgy6x0eoxR.json'}

exec(code, env_args)
