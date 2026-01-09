code = """import json, re, pandas as pd

# Load civic docs
_docs = var_call_0NxPrbwyuGdFf83H0WzG8QVN
if isinstance(_docs, str) and _docs.endswith('.json'):
    with open(_docs, 'r', encoding='utf-8') as f:
        _docs = json.load(f)

_fund = var_call_OFVqNgOlPQ2HaSZl0rQqIF7N
if isinstance(_fund, str) and _fund.endswith('.json'):
    with open(_fund, 'r', encoding='utf-8') as f:
        _fund = json.load(f)

status_map = {}
section_to_status = {'design':'design','construction':'design','not started':'not started','completed':'completed'}

for d in _docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for i, ln in enumerate(lines):
        lnl = ln.lower()
        # detect status section headings like 'Capital Improvement Projects (Design)'
        if '(' in ln and ')' in ln and ('projects' in lnl):
            m = re.search(r'\((Design|Construction|Not Started|Completed)\)', ln, flags=re.I)
            if m:
                current_status = section_to_status.get(m.group(1).lower(), current_status)

        # project name heuristic: line followed soon by a line containing 'Updates:'
        if not ln:
            continue
        if any(k in lnl for k in ['agenda', 'page ', 'item', 'recommended action', 'discussion']):
            continue
        window = ' '.join(lines[i+1:i+5]).lower()
        if 'updates:' in window:
            pname = re.sub(r'\s{2,}',' ',ln).strip()
            if 4 <= len(pname) <= 140:
                status_map.setdefault(pname, current_status)

fdf = pd.DataFrame(_fund)
if 'Amount' in fdf.columns:
    fdf['Amount'] = pd.to_numeric(fdf['Amount'], errors='coerce')

mask = fdf['Project_Name'].astype(str).str.contains(r'(FEMA|Emergency)', case=False, na=False) | \
       fdf['Funding_Source'].astype(str).str.contains(r'(FEMA|Emergency)', case=False, na=False)
rel = fdf[mask].copy()

def canon(name):
    return re.sub(r'\s*\([^)]*\)\s*','', str(name)).strip().lower()

canon_to_status = {}
for k,v in status_map.items():
    canon_to_status.setdefault(canon(k), v)

rel['Status'] = [status_map.get(pn) or canon_to_status.get(canon(pn)) for pn in rel['Project_Name']]

out = rel[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

out = out.fillna('')
out['Amount'] = out['Amount'].apply(lambda x: '' if x=='' or pd.isna(x) else f"${int(x):,}")

records = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_0NxPrbwyuGdFf83H0WzG8QVN': 'file_storage/call_0NxPrbwyuGdFf83H0WzG8QVN.json', 'var_call_OFVqNgOlPQ2HaSZl0rQqIF7N': 'file_storage/call_OFVqNgOlPQ2HaSZl0rQqIF7N.json'}

exec(code, env_args)
