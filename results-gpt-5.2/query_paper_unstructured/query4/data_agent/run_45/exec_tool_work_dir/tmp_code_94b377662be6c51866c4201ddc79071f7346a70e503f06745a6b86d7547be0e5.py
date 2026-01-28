code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

papers = load_records(var_call_q60r9OXK8JAzwK5qCB7j0Sjn)
citations = load_records(var_call_1OglbIrpyd4OBs4Vae7ke22V)

re_year_pub = re.compile(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*['’](\d{2})\b")

def extract_year(text):
    m = re_year_pub.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy
    m2 = re.search(r"\bCopyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})\b", text)
    if m2:
        return int(m2.group(1))
    head = text[:800]
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", head)]
    return years[0] if years else None


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
# normalize column names from sqlite output
if not cit_df.empty:
    if 'total_citations' not in cit_df.columns and 'SUM(citation_count)' in cit_df.columns:
        cit_df = cit_df.rename(columns={'SUM(citation_count)':'total_citations'})
    cit_df['total_citations'] = pd.to_numeric(cit_df.get('total_citations',0), errors='coerce').fillna(0).astype(int)

if papers_df.empty:
    result = []
else:
    out = papers_df.merge(cit_df[['title','total_citations']], on='title', how='left')
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1OglbIrpyd4OBs4Vae7ke22V': 'file_storage/call_1OglbIrpyd4OBs4Vae7ke22V.json', 'var_call_q60r9OXK8JAzwK5qCB7j0Sjn': 'file_storage/call_q60r9OXK8JAzwK5qCB7j0Sjn.json'}

exec(code, env_args)
