code = """import json, re
import pandas as pd

def load(tool_var):
    if isinstance(tool_var, str):
        with open(tool_var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return tool_var

paper_docs = load(var_call_mZ5W0xwNUiQwyPuRuhCmrKbN)
cit_totals = load(var_call_TRPMNs6MKPVR0nM0Wcl6jNjT)

def infer_year(text):
    m = re.search(r'Copyright\s+(?:\u00a9\s*)?(20\d{2})', text)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth|AH)\s*['’]?\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy
    m = re.search(r'\b(2016)\b', text[:2000])
    if m:
        return 2016
    return None

def infer_domain(text):
    m = re.search(r'Author Keywords\s*(.*?)\n\n', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        m = re.search(r'Keywords\s*(.*?)\n\n', text, flags=re.IGNORECASE|re.DOTALL)
    kw = m.group(1) if m else ''
    if re.search(r'physical\s+activity', kw, flags=re.IGNORECASE):
        return 'physical activity'
    if re.search(r'physical\s+activity', text, flags=re.IGNORECASE):
        return 'physical activity'
    return None

rows = []
for d in paper_docs:
    title = d['filename'].rsplit('.txt', 1)[0]
    text = d.get('text', '') or ''
    year = infer_year(text)
    if year != 2016:
        continue
    dom = infer_domain(text)
    if dom != 'physical activity':
        continue
    rows.append({'title': title})

cit_df = pd.DataFrame(cit_totals)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

papers_df = pd.DataFrame(rows).drop_duplicates()
if papers_df.empty:
    out = []
else:
    merged = papers_df.merge(cit_df, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations', 'title'], ascending=[False, True])
    out = merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mZ5W0xwNUiQwyPuRuhCmrKbN': 'file_storage/call_mZ5W0xwNUiQwyPuRuhCmrKbN.json', 'var_call_TRPMNs6MKPVR0nM0Wcl6jNjT': 'file_storage/call_TRPMNs6MKPVR0nM0Wcl6jNjT.json'}

exec(code, env_args)
