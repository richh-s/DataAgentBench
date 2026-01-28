code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_7VYSU082ACwozqUURP9xXR7q)
cpcdef_recs = load_records(var_call_qUPAgiEPbflmNHeXuHYcnnes)

cpc_title = {r['symbol'].replace(' ', ''): r.get('titleFull') for r in cpcdef_recs if r.get('symbol')}

def get_assignee(patents_info: str):
    s = patents_info or ''
    m = re.search(r"owned by ([^,\.]+?) and has", s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r"assigned to ([^,\.]+?) and has", s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^([^\n]+?) holds the", s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

pairs = []
for r in pub_recs:
    citing_assignee = get_assignee(r.get('Patents_info',''))
    if not citing_assignee:
        continue
    if 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue

    cpc_list = []
    cpc_raw = r.get('cpc')
    try:
        if isinstance(cpc_raw, str) and cpc_raw.strip().startswith('['):
            cpc_list = json.loads(cpc_raw)
    except Exception:
        cpc_list = []

    primary_codes = []
    for e in cpc_list:
        if isinstance(e, dict) and e.get('first') is True and e.get('code'):
            primary_codes.append(e['code'].replace(' ', ''))

    if not primary_codes:
        continue

    titles = set()
    for code in primary_codes:
        title = cpc_title.get(code)
        if title is None:
            title = cpc_title.get(code.split('/')[0])
        if title is None and len(code) >= 4:
            title = cpc_title.get(code[:4])
        if title:
            titles.add(title)

    for t in sorted(titles):
        pairs.append({'citing_assignee': citing_assignee, 'cpc_subclass_title': t})

out = pd.DataFrame(pairs).drop_duplicates().sort_values(['citing_assignee','cpc_subclass_title']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_7VYSU082ACwozqUURP9xXR7q': 'file_storage/call_7VYSU082ACwozqUURP9xXR7q.json', 'var_call_qUPAgiEPbflmNHeXuHYcnnes': 'file_storage/call_qUPAgiEPbflmNHeXuHYcnnes.json'}

exec(code, env_args)
