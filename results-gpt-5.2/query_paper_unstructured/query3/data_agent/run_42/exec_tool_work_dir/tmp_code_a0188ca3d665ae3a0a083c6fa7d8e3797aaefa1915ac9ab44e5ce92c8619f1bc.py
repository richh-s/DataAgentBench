code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
md = var_call_C8YeM5aHfGFgYH9W6E8Ej9My
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_X5guGuxvn60u6azLsw8ZjZnj
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce')

# heuristics to extract year and contribution
year_patterns = [
    re.compile(r'\b(19|20)\d{2}\b'),
]

def extract_year(text):
    # Prefer patterns like CHI '19, Ubicomp '18 etc.
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|TEI|OzCHI|WWW|AH|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(\d{4})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # fallback: first reasonable year 2000-2026
    years = [int(y) for y in re.findall(r'\b(20\d{2}|19\d{2})\b', text)]
    years = [y for y in years if 2000 <= y <= 2026]
    return years[0] if years else None

def has_empirical(text):
    return bool(re.search(r'\bempirical\b', text, flags=re.IGNORECASE))

rows = []
for d in md:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    y = extract_year(text)
    emp = has_empirical(text)
    if y is not None and y > 2016 and emp:
        rows.append({'title': title, 'year': y})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_C8YeM5aHfGFgYH9W6E8Ej9My': 'file_storage/call_C8YeM5aHfGFgYH9W6E8Ej9My.json', 'var_call_X5guGuxvn60u6azLsw8ZjZnj': 'file_storage/call_X5guGuxvn60u6azLsw8ZjZnj.json'}

exec(code, env_args)
