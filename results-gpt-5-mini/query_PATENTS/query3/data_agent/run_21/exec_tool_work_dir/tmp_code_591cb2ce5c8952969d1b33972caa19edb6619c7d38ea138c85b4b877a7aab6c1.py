code = """import json, re
uc_path = var_call_FWaq87obpvltPwUmTRpRaycV
all_path = var_call_tgrM8QNXraQ65lKZy8S0oDdF
uc_records = json.load(open(uc_path, 'r'))
all_records = json.load(open(all_path, 'r'))
# pattern for publication numbers like US-12345-A
pat = re.compile("[A-Z][A-Z]-[0-9][0-9A-Za-z-]*")
uc_pubnums = set()
for rec in uc_records:
    pinfo = rec.get('Patents_info') or ''
    cit = rec.get('citation') or ''
    for m in pat.findall(pinfo):
        uc_pubnums.add(m)
    for m in pat.findall(cit):
        uc_pubnums.add(m)
# keep those starting with two letters-dash-digit
uc_pubnums = {p for p in uc_pubnums if len(p) >=4 and p[2]=='-' and p[3].isdigit()}

citing = []
for rec in all_records:
    cit_text = rec.get('citation') or ''
    if not cit_text or cit_text.strip() == '[]':
        continue
    cited_pubns = set()
    try:
        cit_list = json.loads(cit_text)
        if isinstance(cit_list, list):
            for c in cit_list:
                if isinstance(c, dict):
                    pubn = c.get('publication_number','')
                    if pubn:
                        cited_pubns.add(pubn)
    except Exception:
        for m in pat.findall(cit_text):
            cited_pubns.add(m)
    if not (cited_pubns & uc_pubnums):
        continue
    pinfo = rec.get('Patents_info','')
    assignee = ''
    low = pinfo.lower()
    if ' is owned by ' in low:
        # get substring after ' is owned by '
        idx = low.find(' is owned by ')
        assignee = pinfo[idx+12:]
    elif ' is assigned to ' in low:
        idx = low.find(' is assigned to ')
        assignee = pinfo[idx+16:]
    elif ' holds the ' in low:
        idx = low.find(' holds the ')
        assignee = pinfo[:idx]
    elif ' holds ' in low:
        idx = low.find(' holds ')
        assignee = pinfo[:idx]
    else:
        # take up to first comma or '(' or ' with '
        for sep in [',','(',' with ','.']:
            if sep in pinfo:
                assignee = pinfo.split(sep)[0]
                break
        if not assignee:
            assignee = pinfo
    assignee = assignee.strip()
    # remove trailing phrases like 'the US patent application'
    assignee = re.split('\s+the\s+[A-Z]{2}\s+patent|\s+the\s+US\s+patent', assignee, flags=re.IGNORECASE)[0].strip()
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    # parse cpc
    cpc_text = rec.get('cpc') or '[]'
    primary = None
    try:
        cpc_list = json.loads(cpc_text)
        if isinstance(cpc_list, list) and cpc_list:
            for e in cpc_list:
                if isinstance(e, dict) and e.get('first'):
                    primary = e.get('code')
                    break
            if not primary:
                first = cpc_list[0]
                if isinstance(first, dict):
                    primary = first.get('code')
                else:
                    primary = first
    except Exception:
        # try to find a segment-like code with a letter then digit then maybe slash
        m = re.search('[A-Z][0-9][A-Z0-9/\-]+', cpc_text)
        if m:
            primary = m.group(0)
    if not primary:
        continue
    citing.append({'assignee': assignee, 'cpc_code': primary})

# dedupe
pairs = []
seen = set()
for c in citing:
    key = (c['assignee'], c['cpc_code'])
    if key in seen:
        continue
    seen.add(key)
    pairs.append({'assignee': c['assignee'], 'cpc_code': c['cpc_code']})

cpc_codes = sorted({p['cpc_code'] for p in pairs})
output = {'pairs': pairs, 'cpc_codes': cpc_codes}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json', 'var_call_xPULEoxuCI0R7gn4s9WmVLxr': 'file_storage/call_xPULEoxuCI0R7gn4s9WmVLxr.json', 'var_call_tgrM8QNXraQ65lKZy8S0oDdF': 'file_storage/call_tgrM8QNXraQ65lKZy8S0oDdF.json'}

exec(code, env_args)
