code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

paper_docs = load_records(var_call_5hmDHyqeXeEQ3xyhzw2SLdK5)
citations = load_records(var_call_x4StX7qtvYdw5NJm84R7n1bi)

# Build citations df
cdf = pd.DataFrame(citations)
if not cdf.empty:
    cdf['total_citations'] = pd.to_numeric(cdf['total_citations'], errors='coerce').fillna(0).astype(int)

# Extract year and contribution from text
contribution_re = re.compile(r'\b(empirical|artifact|theoretical|survey|methodological)\b', re.IGNORECASE)
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Prefer explicit copyright year
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(\d{4})', text, re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1990 <= y <= 2030:
            return y
    # Prefer patterns like CHI '19, or UBICOMP '15
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|OzCHI|TEI|WWW|AH|PervasiveHealth)\s*'?\s*(\d{2})\b", text)
    if m:
        y2 = int(m.group(1))
        y = 2000 + y2 if y2 <= 30 else 1900 + y2
        if 1990 <= y <= 2030:
            return y
    # Fallback: take max reasonable year in first 2000 chars
    head = text[:2000]
    years = [int(x) for x in year_re.findall(head)]
    years = [y for y in years if 1990 <= y <= 2030]
    return max(years) if years else None


def has_empirical(text):
    if not isinstance(text, str):
        return False
    # require the word empirical anywhere
    return bool(re.search(r'\bempirical\b', text, re.IGNORECASE))

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    year = extract_year(text)
    empirical = has_empirical(text)
    if year is None:
        continue
    if year > 2016 and empirical:
        rows.append({'title': title, 'year': year})

pdf = pd.DataFrame(rows).drop_duplicates(subset=['title'])

if pdf.empty:
    out = []
else:
    merged = pdf.merge(cdf, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5hmDHyqeXeEQ3xyhzw2SLdK5': 'file_storage/call_5hmDHyqeXeEQ3xyhzw2SLdK5.json', 'var_call_x4StX7qtvYdw5NJm84R7n1bi': 'file_storage/call_x4StX7qtvYdw5NJm84R7n1bi.json'}

exec(code, env_args)
