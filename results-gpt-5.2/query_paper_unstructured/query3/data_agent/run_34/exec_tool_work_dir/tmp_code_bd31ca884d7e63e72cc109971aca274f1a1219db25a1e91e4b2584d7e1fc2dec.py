code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
md = var_call_zhujEzXWqbEFQNumTWDP1QCC
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_4cYVoidIvb7U58FJIKlxt842
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text: str):
    if not text:
        return None
    # look for copyright year
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(?:19|20)\d{2}', text, flags=re.IGNORECASE)
    if m:
        y = re.search(r'(19|20)\d{2}', m.group(0))
        if y:
            return int(y.group(0))
    # look for conference pattern like CHI '19 or UBICOMP '15
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|WWW|OzCHI|TEI|AH)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy <= 30 else 1900+yy
    # any standalone year near beginning
    head = text[:2000]
    yrs = re.findall(r'\b(20\d{2}|19\d{2})\b', head)
    if yrs:
        # choose max in head
        return int(max(yrs))
    return None

def has_empirical(text: str):
    if not text:
        return False
    t = text.lower()
    # include common contribution marker or metadata lines
    return ('contribution' in t and 'empirical' in t) or ('empirical' in t)

rows = []
for d in md:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical(text):
        continue
    rows.append({'title': title, 'year': year})

df_p = pd.DataFrame(rows).drop_duplicates(subset=['title'])

if df_p.empty:
    out = []
else:
    df = df_p.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_zhujEzXWqbEFQNumTWDP1QCC': 'file_storage/call_zhujEzXWqbEFQNumTWDP1QCC.json', 'var_call_4cYVoidIvb7U58FJIKlxt842': 'file_storage/call_4cYVoidIvb7U58FJIKlxt842.json'}

exec(code, env_args)
