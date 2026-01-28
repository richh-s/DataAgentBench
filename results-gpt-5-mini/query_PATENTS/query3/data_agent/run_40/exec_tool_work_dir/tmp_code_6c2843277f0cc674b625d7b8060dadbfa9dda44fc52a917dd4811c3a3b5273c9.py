code = """import json, re
path = var_call_HFE9STUvy7701VvFcI1zafnZ
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# helper to parse citation field
def parse_citation_field(cit_field):
    if not cit_field:
        return []
    if isinstance(cit_field, list):
        return cit_field
    try:
        lst = json.loads(cit_field)
        if isinstance(lst, list):
            return lst
    except Exception:
        pass
    # fallback: try to extract publication_number tokens
    pubnums = re.findall(r'[A-Z]{2}-\d{4,}(?:-[A-Z0-9]+)?', str(cit_field).upper())
    out = []
    for p in pubnums:
        out.append({'publication_number': p})
    return out

# extract publication numbers from Patents_info
def extract_pubnums_from_info(info):
    if not info:
        return []
    info_up = info.upper()
    pubnums = re.findall(r'[A-Z]{2}-\d{4,}(?:-[A-Z0-9]+)?', info_up)
    return pubnums

# extract assignee from Patents_info
def extract_assignee(info):
    if not info:
        return None
    # try before 'holds' or 'holds the' or 'owns' or 'is owned by' or 'is assigned to' or 'assigned to'
    m = re.match(r'^([A-Z0-9 &\-\.,]{3,200}?)\s+(?:HOLDS|HOLDS THE|OWNS|IS OWNED|IS OWNED BY|IS ASSIGNED|ASSIGNED TO|HAS|HOLDING)', info.upper())
    if m:
        name = m.group(1).strip()
        # clean trailing punctuation
        name = re.sub(r'[.,;:\s]+$', '', name)
        return name
    # fallback: look for leading all-caps phrase until 'the' or 'US' or 'PATENT'
    m = re.match(r'^([A-Z0-9 &\-\.,]{3,200}?)\s+(?:THE|US|PATENT|APPLICATION|WITH|HAVE|HAS)', info.upper())
    if m:
        name = m.group(1).strip()
        name = re.sub(r'[.,;:\s]+$', '', name)
        return name
    # fallback: find any all-caps phrase of words
    m = re.search(r'([A-Z]{3,}(?: [A-Z0-9&\-\.,]+)*)', info.upper())
    if m:
        name = m.group(1).strip()
        name = re.sub(r'[.,;:\s]+$', '', name)
        return name
    return None

# build map of publication_number -> record row
pubnum_to_record = {}
for rec in records:
    info = rec.get('Patents_info', '') or ''
    pubnums = extract_pubnums_from_info(info)
    for p in pubnums:
        pubnum_to_record[p] = rec

# identify Univ California publication numbers
uc_pubnums = set()
for p, rec in pubnum_to_record.items():
    info = rec.get('Patents_info','') or ''
    if 'UNIV CALIFORNIA' in info.upper() or 'UNIVERSITY OF CALIFORNIA' in info.upper():
        uc_pubnums.add(p)

# iterate over records to find citations referencing uc_pubnums
assignee_to_codes = {}
all_primary_codes = set()
for rec in records:
    info = rec.get('Patents_info','') or ''
    citation_field = rec.get('citation','')
    citations = parse_citation_field(citation_field)
    cited_pubnums = set()
    for c in citations:
        pn = (c.get('publication_number') or '').upper()
        if pn:
            cited_pubnums.add(pn)
    if not (cited_pubnums & uc_pubnums):
        continue
    # this record cites a Univ California patent
    assignee = extract_assignee(info)
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee or 'UNIVERSITY OF CALIFORNIA' in assignee:
        continue
    # parse cpc field
    cpc_field = rec.get('cpc','')
    primary_codes = []
    try:
        cpcs = json.loads(cpc_field) if isinstance(cpc_field, str) else (cpc_field if isinstance(cpc_field, list) else [])
        if isinstance(cpcs, list):
            for e in cpcs:
                if isinstance(e, dict) and e.get('first') is True:
                    code = e.get('code') or e.get('symbol')
                    if code:
                        primary_codes.append(code)
    except Exception:
        cpcs = []
    # fallback: if no primary code, take first code present
    if not primary_codes and isinstance(cpcs, list) and len(cpcs)>0:
        for e in cpcs:
            if isinstance(e, dict) and (e.get('code') or e.get('symbol')):
                primary_codes.append(e.get('code') or e.get('symbol'))
                break
    if not primary_codes:
        continue
    # normalize assignee spacing and trim
    assignee_norm = re.sub(r'\s+', ' ', assignee).strip()
    s = assignee_to_codes.get(assignee_norm, set())
    for pc in primary_codes:
        s.add(pc)
        all_primary_codes.add(pc)
    assignee_to_codes[assignee_norm] = s

# prepare output
out_assignees = []
for a, codes in assignee_to_codes.items():
    out_assignees.append({'assignee': a, 'codes': sorted(list(codes))})

out = {'assignees': out_assignees, 'primary_codes': sorted(list(all_primary_codes)), 'uc_pubnums': sorted(list(uc_pubnums))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YhT3RtPYuPUxiQPaMOH5T3TG': ['publicationinfo'], 'var_call_5SwPYlRI2uvKKcds69kZ4mQk': ['cpc_definition'], 'var_call_mgnuO1NLUamXno1MDIunxmSO': 'file_storage/call_mgnuO1NLUamXno1MDIunxmSO.json', 'var_call_UZHrpCM1o7Isc6uUEuKxvm26': {'assignees': [], 'codes': []}, 'var_call_exGtc5EsutV9egxa6nc6aZt4': 'file_storage/call_exGtc5EsutV9egxa6nc6aZt4.json', 'var_call_vq8FiVifuMY4ELqK3HZS0s83': 'file_storage/call_vq8FiVifuMY4ELqK3HZS0s83.json', 'var_call_HFE9STUvy7701VvFcI1zafnZ': 'file_storage/call_HFE9STUvy7701VvFcI1zafnZ.json'}

exec(code, env_args)
