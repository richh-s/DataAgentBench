code = """import json, re, pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

paper_docs = load_tool_result(var_call_EDJvhCqHJlKIkWQZijPKTMy4)
citations = load_tool_result(var_call_3xBMxPGPszQAvaxYnVwj301F)

def extract_year(text):
    if not text:
        return None
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*'?\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 80 else 1900 + yy
    head = text[:2000]
    years = [int(y) for y in re.findall(r'\b(20\d{2}|19\d{2})\b', head)]
    years = [y for y in years if 1980 <= y <= 2030]
    return years[0] if years else None

def extract_dom_blob(text):
    if not text:
        return ''
    head = text[:6000]
    m = re.search(r'Author Keywords\s*(.*?)\n\s*\n', head, flags=re.IGNORECASE|re.DOTALL)
    blob = m.group(1) if m else head
    blob = blob.replace('\n', ' ')
    return blob.lower()

rows = []
for d in paper_docs:
    fn = d.get('filename', '')
    title = re.sub(r'\.txt$', '', fn)
    text = d.get('text', '') or ''
    rows.append({'title': title, 'pub_year': extract_year(text), 'dom_blob': extract_dom_blob(text)})

pdf = pd.DataFrame(rows)
mask = (pdf['pub_year'] == 2016) & (pdf['dom_blob'].str.contains('physical activity', na=False))
phys2016 = pdf.loc[mask, ['title']].drop_duplicates()

cdf = pd.DataFrame(citations)
if len(cdf):
    cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

ctot = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count': 'total_citations'})

out = phys2016.merge(ctot, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations', 'title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EDJvhCqHJlKIkWQZijPKTMy4': 'file_storage/call_EDJvhCqHJlKIkWQZijPKTMy4.json', 'var_call_3xBMxPGPszQAvaxYnVwj301F': 'file_storage/call_3xBMxPGPszQAvaxYnVwj301F.json'}

exec(code, env_args)
