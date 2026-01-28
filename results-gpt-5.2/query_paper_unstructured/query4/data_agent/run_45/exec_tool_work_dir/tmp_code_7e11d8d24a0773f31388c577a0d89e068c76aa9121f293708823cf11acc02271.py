code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

papers = load_records(var_call_q60r9OXK8JAzwK5qCB7j0Sjn)
citations = load_records(var_call_1OglbIrpyd4OBs4Vae7ke22V)

# parse year and domain from text
re_year1 = re.compile(r"\b(19|20)\d{2}\b")
re_year_pub = re.compile(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*['’](\d{2})\b")
re_copyright = re.compile(r"Copyright\s+(?:\d{4}\s+)?©\s*(19|20)\d{2}")

def extract_year(text):
    # Prefer patterns like UBICOMP '15 etc. Use first such match.
    m = re_year_pub.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 100 else yy
    # Try explicit "Copyright 2016" or similar
    m2 = re.search(r"Copyright\s*(?:\(c\)\s*)?(19|20)\d{2}", text)
    if m2:
        return int(m2.group(0).split()[-1])
    # fallback: find first year near beginning (first 500 chars)
    head = text[:800]
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", head)]
    return years[0] if years else None

# domain detection: require phrase 'physical activity' in text (case-insensitive)

def is_physical_activity(text):
    return re.search(r"physical\s+activity", text, flags=re.I) is not None

rows=[]
for d in papers:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    if not is_physical_activity(text):
        continue
    year = extract_year(text)
    if year != 2016:
        continue
    rows.append({'title': title})

papers_df = pd.DataFrame(rows).drop_duplicates()

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1OglbIrpyd4OBs4Vae7ke22V': 'file_storage/call_1OglbIrpyd4OBs4Vae7ke22V.json', 'var_call_q60r9OXK8JAzwK5qCB7j0Sjn': 'file_storage/call_q60r9OXK8JAzwK5qCB7j0Sjn.json'}

exec(code, env_args)
