code = """import json, re
import pandas as pd

def load(tool_var):
    if isinstance(tool_var, str):
        with open(tool_var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return tool_var

paper_docs = load(var_call_4piSfAJq60xHSKfWTA4o3JbG)
cit_totals = load(var_call_TRPMNs6MKPVR0nM0Wcl6jNjT)

def infer_year(text):
    m = re.search(r'Copyright\s+(?:\u00a9\s*)?(20\d{2})', text)
    if m:
        return int(m.group(1))
    if '2016' in text[:3000]:
        return 2016
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth|AH)\s*['’]?\s*(\d{2})\b", text)
    if m:
        return 2000 + int(m.group(1))
    return None

rows=[]
for d in paper_docs:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if infer_year(text)!=2016:
        continue
    if not re.search(r'physical\s+activity', text, flags=re.IGNORECASE):
        continue
    rows.append({'title': title})

cit_df = pd.DataFrame(cit_totals)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

papers_df = pd.DataFrame(rows).drop_duplicates()
if papers_df.empty:
    out=[]
else:
    merged = papers_df.merge(cit_df, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mZ5W0xwNUiQwyPuRuhCmrKbN': 'file_storage/call_mZ5W0xwNUiQwyPuRuhCmrKbN.json', 'var_call_TRPMNs6MKPVR0nM0Wcl6jNjT': 'file_storage/call_TRPMNs6MKPVR0nM0Wcl6jNjT.json', 'var_call_CQMRHHBh1cwqBTWcM1bTa7zC': [], 'var_call_4piSfAJq60xHSKfWTA4o3JbG': 'file_storage/call_4piSfAJq60xHSKfWTA4o3JbG.json'}

exec(code, env_args)
