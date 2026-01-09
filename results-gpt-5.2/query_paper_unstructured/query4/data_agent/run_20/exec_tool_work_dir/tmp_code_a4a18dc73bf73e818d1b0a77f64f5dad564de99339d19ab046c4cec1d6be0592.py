code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

paper_docs = load_records(var_call_60gFXyEbQHGJxWhgMvL2bUmG)
citations = load_records(var_call_09vkOXiPG95Kvvnk32d6PkoJ)

year_patterns = [
    re.compile(r'\bCopyright\s+(?:\(c\)\s*)?(\d{4})\b', re.IGNORECASE),
    re.compile(r"\bCHI\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
    re.compile(r"\bUbiComp\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
    re.compile(r"\bCSCW\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
    re.compile(r"\bDIS\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
    re.compile(r"\bIUI\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
    re.compile(r"\bWWW\s*[\u2019\']?(\d{2})\b", re.IGNORECASE),
]

def infer_year(text):
    if not text:
        return None
    t = text[:4000]
    for pat in year_patterns:
        m = pat.search(t)
        if m:
            y = m.group(1)
            if len(y) == 2:
                yy = int(y)
                return 2000 + yy if yy < 50 else 1900 + yy
            return int(y)
    m = re.search(r'\b(20\d{2}|19\d{2})\b', t)
    if m:
        return int(m.group(1))
    return None

def infer_domain(text):
    if not text:
        return []
    header = text[:6000].lower()
    doms = []
    if 'physical activity' in header:
        doms.append('physical activity')
    return doms

rows = []
for d in paper_docs:
    fn = d.get('filename', '')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    year = infer_year(d.get('text', ''))
    domains = infer_domain(d.get('text', ''))
    if year == 2016 and ('physical activity' in domains):
        rows.append({'title': title, 'year': year})

papers2016 = pd.DataFrame(rows).drop_duplicates()

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

if papers2016.empty:
    result = []
else:
    merged = papers2016.merge(cit_df, on='title', how='left')
    out = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count': 'total_citation_count'})
    out = out.sort_values('total_citation_count', ascending=False)
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_60gFXyEbQHGJxWhgMvL2bUmG': 'file_storage/call_60gFXyEbQHGJxWhgMvL2bUmG.json', 'var_call_09vkOXiPG95Kvvnk32d6PkoJ': 'file_storage/call_09vkOXiPG95Kvvnk32d6PkoJ.json'}

exec(code, env_args)
