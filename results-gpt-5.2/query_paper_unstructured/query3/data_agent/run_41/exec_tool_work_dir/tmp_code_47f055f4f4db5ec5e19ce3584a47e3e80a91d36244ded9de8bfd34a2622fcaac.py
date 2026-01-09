code = """import json, re
import pandas as pd

# load docs
_docs_src = var_call_gdpScBbhv5TooWljmDT7Dc6G
if isinstance(_docs_src, str):
    with open(_docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = _docs_src

# load citations totals
_cits_src = var_call_2F1arjDMEJ90CApnyrEodfYU
if isinstance(_cits_src, str):
    with open(_cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = _cits_src


def extract_year(text):
    if not text:
        return None
    t = text[:6000]
    m = re.search(r'Copyright\s*(?:©|\(C\)|\u00a9)?\s*(19\d{2}|20\d{2})', t, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', t)]
    years = [y for y in years if 1980 <= y <= 2030]
    if years:
        return max(years)
    return None


def is_empirical(text):
    if not text:
        return False
    tl = text.lower()
    m = re.search(r'contribution\s*[:\-]\s*([^\n\r]+)', tl)
    if m and ('empirical' in m.group(1)):
        return True
    # heuristic
    has_methods = ('method' in tl) or ('methods' in tl)
    has_participants = ('participants' in tl) or ('we interviewed' in tl) or ('we surveyed' in tl) or ('user study' in tl) or ('field study' in tl) or ('we conducted' in tl)
    return has_methods and has_participants


paper_rows = []
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    emp = is_empirical(text)
    paper_rows.append({'title': title, 'year': year, 'empirical': emp})

papers = pd.DataFrame(paper_rows)
papers_f = papers[(papers['empirical']) & (papers['year'].notna()) & (papers['year'] > 2016)][['title','year']]

cits_df = pd.DataFrame(cits)
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = papers_f.merge(cits_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_gdpScBbhv5TooWljmDT7Dc6G': 'file_storage/call_gdpScBbhv5TooWljmDT7Dc6G.json', 'var_call_2F1arjDMEJ90CApnyrEodfYU': 'file_storage/call_2F1arjDMEJ90CApnyrEodfYU.json', 'var_call_3JcGcuFadE6mc0uD7bJMqbKe': {'ok': True}, 'var_call_8OFg0uzq0hzWiLuD1Own2ewT': {'test': True}, 'var_call_Gq2Fk7gz40Nf6rOjRtweLch0': {'note': 'noop'}}

exec(code, env_args)
