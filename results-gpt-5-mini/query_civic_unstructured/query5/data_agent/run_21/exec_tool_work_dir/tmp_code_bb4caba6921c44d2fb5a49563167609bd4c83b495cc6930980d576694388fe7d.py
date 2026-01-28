code = """import json

civic_path = var_call_eA0xJZWygM8q62BlCiIPmWwv
funding_path = var_call_CVAV72xeKdGMECzEU9GvpR7x

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

all_text = "\n".join([d.get('text','') for d in civic_docs]).lower()

indicators = ['fema', 'caloes', 'caljpia', 'fema/caloes']

matches = []

for r in funding:
    pname = (r.get('Project_Name') or '').lower()
    psource = (r.get('Funding_Source') or '').lower()
    # amount
    raw = r.get('Amount', 0)
    try:
        amt = int(str(raw))
    except:
        try:
            amt = int(float(str(raw)))
        except:
            amt = 0
    # disaster detection
    is_disaster = False
    for ind in indicators:
        if ind in pname or ind in psource:
            is_disaster = True
            break
    if not is_disaster and 'federal assistance' in psource:
        is_disaster = True
    if not is_disaster:
        continue
    # search for project name or base name
    base = pname.split('(')[0].strip()
    terms = [pname]
    if base and base != pname:
        terms.append(base)
    found_2022 = False
    for t in terms:
        if not t:
            continue
        idx = all_text.find(t)
        if idx != -1:
            start = max(0, idx-300)
            end = min(len(all_text), idx+300)
            window = all_text[start:end]
            if '2022' in window:
                found_2022 = True
            break
    # if not found by combined text, check per doc
    if not found_2022:
        for d in civic_docs:
            txt = (d.get('text') or '').lower()
            for t in terms:
                if not t:
                    continue
                idx = txt.find(t)
                if idx != -1:
                    start = max(0, idx-300)
                    end = min(len(txt), idx+300)
                    window = txt[start:end]
                    if '2022' in window:
                        found_2022 = True
                    break
            if found_2022:
                break
    if found_2022:
        try:
            fid = int(r.get('Funding_ID'))
        except:
            fid = r.get('Funding_ID')
        matches.append({'Funding_ID': fid, 'Project_Name': r.get('Project_Name'), 'Amount': amt})

total = sum(m['Amount'] for m in matches)
res = {'total_funding': total, 'matched_projects_count': len(matches), 'matched_projects': matches}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_9m8TflfbCJWo96QQhMCIesyq': ['civic_docs'], 'var_call_eA0xJZWygM8q62BlCiIPmWwv': 'file_storage/call_eA0xJZWygM8q62BlCiIPmWwv.json', 'var_call_81lfzMGYLNjxzefeEW7o1uY3': ['Funding'], 'var_call_CVAV72xeKdGMECzEU9GvpR7x': 'file_storage/call_CVAV72xeKdGMECzEU9GvpR7x.json', 'var_call_yZiaFc25sB2M7suCKEOol9JH': {'v1': 'str', 'v2': 'str'}}

exec(code, env_args)
