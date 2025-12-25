code = """import json, re
from pathlib import Path

all_path = Path(var_call_XKK2TFU3M8UwKzHnr83vZV0i)
all_records = json.loads(all_path.read_text())

uc_pubs = set(json.loads(str(var_call_ZgOyzUp6YFvyBd4qF6MzfAJI)))

citing = []
for r in all_records:
    info = r['Patents_info']
    assignee = None
    m = re.search(r'assignee_harmonized: ([^,]+)', info)
    if m:
        assignee = m.group(1).strip()
    else:
        m = re.match(r'([^,]+?) (holds|owns|is assigned)', info)
        if m:
            assignee = m.group(1).strip()
    if not assignee or 'UNIV CALIFORNIA' in assignee:
        continue
    cits = r['citation']
    if not cits or cits == '[]':
        continue
    try:
        cits_list = json.loads(cits)
    except Exception:
        continue
    cited_uc = [c for c in cits_list if c.get('publication_number') in uc_pubs]
    if not cited_uc:
        continue
    citing.append({'assignee': assignee, 'cpc': r['cpc']})

assignee_cpc = {}
for rec in citing:
    assignee = rec['assignee']
    try:
        cpcs = json.loads(rec['cpc'])
    except Exception:
        continue
    prim = [c['code'] for c in cpcs if c.get('first')]
    if not prim:
        prim = [cpcs[0]['code']] if cpcs else []
    if not prim:
        continue
    assignee_cpc.setdefault(assignee, set()).update(prim)

out = {a: sorted(list(codes)) for a, codes in assignee_cpc.items()}

result = json.dumps(out)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_f5nD18lCH9HTL08v5QdyMQfM': [], 'var_call_yclU1bCm27mmuF5eNMS97xEb': 'file_storage/call_yclU1bCm27mmuF5eNMS97xEb.json', 'var_call_r7aZ0icSfjONnw4m9F4jrJXm': 'file_storage/call_r7aZ0icSfjONnw4m9F4jrJXm.json', 'var_call_XKK2TFU3M8UwKzHnr83vZV0i': 'file_storage/call_XKK2TFU3M8UwKzHnr83vZV0i.json', 'var_call_ZgOyzUp6YFvyBd4qF6MzfAJI': ['AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2019275518-B2', 'AU-6535890-A', 'CA-2550552-A1', 'CA-2562038-C', 'CN-100339724-C', 'CN-102067370-B', 'CN-102584712-A', 'EP-1212462-A1', 'HK-1250569-A1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2014224156-A', 'JP-S6163700-A', 'RO-70061-A', 'TW-201925402-A', 'US-11376346-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-2006292670-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2021000566-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023321419-A1', 'US-5304932-A', 'WO-2010045542-A3', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2024044766-A3']}

exec(code, env_args)
