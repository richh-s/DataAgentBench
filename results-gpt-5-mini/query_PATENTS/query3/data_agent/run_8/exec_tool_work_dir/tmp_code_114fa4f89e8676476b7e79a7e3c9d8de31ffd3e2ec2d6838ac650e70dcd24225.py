code = """import json, re
path = var_call_lIkcWU0cAUPDcXWJMwYbGx3K
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Load Univ California rows to get their publication numbers
path_univ = var_call_B8JJOFd47fc03V6045GS9Gbw
with open(path_univ, 'r', encoding='utf-8') as f:
    univ_rows = json.load(f)

def extract_pubnums_from_patents_info(text):
    if not text:
        return []
    # find all occurrences like US-1234567-B2 or WO-2012014846-A1 or TW-201925402-A
    matches = re.findall(r'[A-Z]{2}-\d{4,}[A-Z0-9\-]*', text)
    return matches

univ_pubnums = set()
for r in univ_rows:
    p = r.get('Patents_info','')
    for m in extract_pubnums_from_patents_info(p):
        # normalize by removing non-alphanum and upper
        norm = re.sub(r'[^A-Z0-9]','', m.upper())
        univ_pubnums.add(norm)

# Now scan all records and find citations that reference any of these univ_pubnums
def normalize_pub(pub):
    if not pub:
        return None
    return re.sub(r'[^A-Z0-9]','', pub.upper())

def extract_assignee(pinfo):
    if not pinfo:
        return None
    s = pinfo
    # common patterns
    for kw in [' holds ', ' is owned by ', ' owned by ', ' assigned to ', ' owned by ']:
        if kw in s:
            left, right = None, None
            if kw == ' holds ':
                left = s.split(kw,1)[0].strip()
                return left
            else:
                # for 'assigned to' or 'owned by' return right side up to comma or 'and' or 'with'
                parts = s.split(kw,1)[1]
                return parts.split(',')[0].split(' and ')[0].split(' with ')[0].strip()
    # fallback before parenthesis
    if '(' in s:
        return s.split('(',1)[0].strip()
    # else first 3 words
    return ' '.join(s.split()[:3])

def is_univ(assg):
    if not assg:
        return False
    a = assg.lower()
    return 'california' in a and ('univ' in a or 'university' in a)

citing_map = {}  # assignee -> set of primary subclass codes

for r in records:
    pinfo = r.get('Patents_info','')
    citing_assg = extract_assignee(pinfo)
    if not citing_assg:
        continue
    if is_univ(citing_assg):
        continue
    # get primary cpc code from cpc field
    primary = None
    cpc_field = r.get('cpc')
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list) and len(cpcs) > 0:
                first = cpcs[0]
                # code may be under 'code' or 'symbol'
                code = None
                if isinstance(first, dict):
                    code = first.get('code') or first.get('symbol') or first.get('symbol')
                elif isinstance(first, str):
                    code = first
                if code:
                    # normalize and take first 4 chars of letters+digits
                    code_no = re.sub(r'[^A-Z0-9]','', code.upper())
                    if len(code_no) >= 4:
                        primary = code_no[:4]
        except Exception:
            pass
    # parse citations
    cit_field = r.get('citation')
    if not cit_field:
        continue
    try:
        cit_list = json.loads(cit_field)
    except Exception:
        continue
    cited_univ = False
    for c in cit_list:
        if not isinstance(c, dict):
            continue
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        if normalize_pub(cited_pub) in univ_pubnums:
            cited_univ = True
            break
    if cited_univ:
        if primary:
            citing_map.setdefault(citing_assg, set()).add(primary)
        else:
            citing_map.setdefault(citing_assg, set()).add(None)

# prepare result
pairs = []
all_subclasses = set()
for assg, subs in citing_map.items():
    for s in subs:
        pairs.append({'citing_assignee': assg, 'primary_subclass': s})
        if s:
            all_subclasses.add(s)

out = {'pairs': sorted(pairs, key=lambda x: (x['citing_assignee'] or '', x['primary_subclass'] or '')),
       'subclasses': sorted(list(all_subclasses))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json', 'var_call_uhZPtxfUJEEwobfhVN8uLJfv': {'pairs': [], 'subclasses': []}, 'var_call_B8JJOFd47fc03V6045GS9Gbw': 'file_storage/call_B8JJOFd47fc03V6045GS9Gbw.json', 'var_call_iSikYemGpJjCyiuMbOeMopAo': {'count': 113, 'sample': {'US-202117472182-A': 'UNIV CALIFORNIA', 'TW-107142982-A': 'UNIV CALIFORNIA', 'US-201916454755-A': 'UNIV CALIFORNIA', 'AU-2019275518-A': 'UNIV CALIFORNIA', 'US-201515313510-A': 'UNIV CALIFORNIA', 'JP-13313985-A': 'UNIV CALIFORNIA', 'US-201715625819-A': 'UNIV CALIFORNIA', 'EP-00992018-A': 'UNIV CALIFORNIA', 'EP-21763795-A': 'THE REGENTS OF UNIV OF CALIFORNIA', 'US-55161904-A': 'UNIV CALIFORNIA'}}, 'var_call_uxK6ufKP7sP5MNcbECREGAlY': 'file_storage/call_uxK6ufKP7sP5MNcbECREGAlY.json', 'var_call_JbQY1XbRgmizlgigvQtExcn3': {'pairs': [], 'subclasses': [], 'pub_to_assignee_count': 1267}}

exec(code, env_args)
