code = """import json, re
uc_path = var_call_FWaq87obpvltPwUmTRpRaycV
all_path = var_call_tgrM8QNXraQ65lKZy8S0oDdF
uc_records = json.load(open(uc_path, 'r'))
all_records = json.load(open(all_path, 'r'))
pat = re.compile("[A-Z]{2}-[0-9][0-9A-Za-z-]*")
uc_pubnums = set()
for rec in uc_records:
    text = (rec.get('Patents_info') or '') + '\n' + (rec.get('citation') or '')
    for m in pat.findall(text):
        uc_pubnums.add(m)
uc_pubnums = {p for p in uc_pubnums if re.match('^[A-Z]{2}-[0-9]', p)}
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
    assignee = None
    m = re.search('is owned by ([^,\.\n]+)', pinfo, re.IGNORECASE)
    if m:
        assignee = m.group(1).strip()
    if not assignee:
        m = re.search('is assigned to ([^,\.\n]+)', pinfo, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        m = re.search('^(.*?) holds the', pinfo, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        m = re.match('([^,\n]+)', pinfo)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        assignee = ''
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
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
                primary = first.get('code') if isinstance(first, dict) else first
    except Exception:
        for m in pat.findall(cpc_text):
            primary = m
            break
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
