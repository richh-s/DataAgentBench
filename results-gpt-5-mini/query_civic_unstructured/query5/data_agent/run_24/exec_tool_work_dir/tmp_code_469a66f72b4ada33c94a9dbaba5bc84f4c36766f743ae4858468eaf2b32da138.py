code = """import json
import re
from pathlib import Path

funding_path = Path(var_call_4wM5k3GTyzdYzrzkX7moL6ZN)
docs_path = Path(var_call_rAaA0qkh81fh2IyO6Se144fH)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# normalize amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount',0))
    except:
        s = re.sub('[^0-9]', '', str(r.get('Amount','0')))
        r['Amount'] = int(s) if s else 0

all_texts = [d.get('text','') for d in docs]

def base_name(name):
    return re.sub('\s*\([^)]*\)', '', name).strip()

disaster_keywords = ['fema','caloes','cal o es','calo es','disaster','fire','woolsey','emergency']
start_patterns = ['begin construction','construction started','start construction','beginning construction']

matches = []
for r in funding:
    pname = r.get('Project_Name','')
    pname_low = pname.lower()
    bname = base_name(pname).lower()
    contexts = []
    for txt in all_texts:
        txt_low = txt.lower()
        idx = txt_low.find(pname_low)
        if idx == -1:
            idx = txt_low.find(bname)
        if idx != -1:
            start = max(0, idx-200)
            end = min(len(txt_low), idx+200)
            contexts.append(txt_low[start:end])
    if not contexts:
        continue
    # disaster check
    is_disaster = False
    for kw in disaster_keywords:
        if kw in pname_low:
            is_disaster = True
            break
    if not is_disaster:
        for c in contexts:
            for kw in disaster_keywords:
                if kw in c:
                    is_disaster = True
                    break
            if is_disaster:
                break
    # started in 2022 check
    started_2022 = False
    for c in contexts:
        if '2022' in c:
            for sp in start_patterns:
                if sp in c:
                    started_2022 = True
                    break
        # explicit patterns like 'begin construction: fall 2022'
        if re.search('begin construction\s*[:\-]?\s*[^\n]{0,30}2022', c):
            started_2022 = True
        if started_2022:
            break
    matches.append({'Project_Name': pname, 'Amount': r['Amount'], 'is_disaster': is_disaster, 'started_2022': started_2022, 'contexts_count': len(contexts)})

total = sum(m['Amount'] for m in matches if m['is_disaster'] and m['started_2022'])
selected = [m for m in matches if m['is_disaster'] and m['started_2022']]

result = {'total_funding_for_disaster_projects_started_in_2022': total, 'matched_projects': selected}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ppCisfN2tRpTi42dyxTwHA6j': ['civic_docs'], 'var_call_nCM4EklzTtjpxEpVDK5Li7Kx': ['Funding'], 'var_call_4wM5k3GTyzdYzrzkX7moL6ZN': 'file_storage/call_4wM5k3GTyzdYzrzkX7moL6ZN.json', 'var_call_rAaA0qkh81fh2IyO6Se144fH': 'file_storage/call_rAaA0qkh81fh2IyO6Se144fH.json'}

exec(code, env_args)
