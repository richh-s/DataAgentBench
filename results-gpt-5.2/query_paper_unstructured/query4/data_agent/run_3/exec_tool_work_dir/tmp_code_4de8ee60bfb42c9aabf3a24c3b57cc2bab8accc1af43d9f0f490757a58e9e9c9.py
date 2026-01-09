code = """import json, re
import pandas as pd

path = var_call_mzEs9wvQviQg6w4yoj2bxDzv
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# citations might be a file path if large
cit_src = var_call_iRlke4uzoyUETL62Q2UyCotj
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_records = json.load(f)
else:
    cit_records = cit_src

cit = pd.DataFrame(cit_records if isinstance(cit_records, list) else [])
if not cit.empty:
    cit['total_citations'] = pd.to_numeric(cit['total_citations'], errors='coerce').fillna(0).astype(int)


def extract_year(text):
    years = []
    for m in re.finditer(r'\b(?:19|20)\d{2}\b', text):
        y = int(m.group(0))
        if 1990 <= y <= 2026:
            years.append(y)
    if not years:
        return None
    s = pd.Series(years)
    vc = s.value_counts()
    top = vc[vc==vc.max()].index.tolist()
    return int(min(top))


def is_physical_activity(text):
    return re.search(r'physical\s+activity', text, flags=re.I) is not None

rows = []
for d in docs:
    fn = d.get('filename','') or ''
    title = re.sub(r'\.txt$', '', fn)
    text = d.get('text','') or ''
    if not is_physical_activity(text):
        continue
    year = extract_year(text)
    if year != 2016:
        continue
    rows.append({'title': title})

papers = pd.DataFrame(rows).drop_duplicates()

if papers.empty:
    out = []
else:
    merged = papers.merge(cit, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mzEs9wvQviQg6w4yoj2bxDzv': 'file_storage/call_mzEs9wvQviQg6w4yoj2bxDzv.json', 'var_call_iRlke4uzoyUETL62Q2UyCotj': 'file_storage/call_iRlke4uzoyUETL62Q2UyCotj.json'}

exec(code, env_args)
