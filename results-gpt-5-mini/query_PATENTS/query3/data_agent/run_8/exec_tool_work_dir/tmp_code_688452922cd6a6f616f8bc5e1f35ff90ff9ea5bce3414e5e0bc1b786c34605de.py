code = """import json
path = var_call_lIkcWU0cAUPDcXWJMwYbGx3K
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def find_pubnum(text):
    if not text:
        return None
    low = text.lower()
    # try find 'publication number' phrase
    key = 'publication number'
    if key in low:
        idx = low.find(key)
        after = text[idx+len(key):]
        # take first token after punctuation and spaces
        for sep in [':', ' ', '\t']:
            if sep in after:
                after = after.split(sep,1)[1]
                break
        token = after.strip().split()[0]
        # clean token
        token = token.strip(' .,')
        return token
    # fallback: look for patterns like 'US-' or 'WO-'
    for prefix in ['US-','WO-','JP-','EP-','KR-']:
        if prefix in text:
            i = text.find(prefix)
            tail = text[i:]
            token = tail.split()[0].strip(' .,')
            return token
    return None

def find_assignee(text):
    if not text:
        return None
    low = text
    # look for ' holds ' pattern
    parts = None
    if ' holds ' in low:
        parts = low.split(' holds ',1)
    elif ' assigned to ' in low:
        parts = low.split(' assigned to ',1)
    elif ' owned by ' in low:
        parts = low.split(' owned by ',1)
    if parts:
        return parts[0].strip()
    # try 'Assignee:'
    if 'Assignee:' in text:
        return text.split('Assignee:',1)[1].split(',')[0].strip()
    # fallback: before first parenthesis
    if '(' in text:
        return text.split('(',1)[0].strip()
    # otherwise first few words
    return ' '.join(text.split()[:3])

pub_to_assignee = {}
records_info = []
for rec in records:
    pinfo = rec.get('Patents_info') or ''
    pubnum = find_pubnum(pinfo)
    assignee = find_assignee(pinfo)
    if assignee:
        assignee = ' '.join(assignee.split())
    if pubnum and assignee:
        pub_to_assignee[pubnum] = assignee
    records_info.append({'pubnum': pubnum, 'assignee': assignee, 'citation': rec.get('citation'), 'cpc': rec.get('cpc')})

def is_univ_cal(assignee):
    if not assignee:
        return False
    s = assignee.lower()
    return 'california' in s and ('univ' in s or 'university' in s)

pairs = set()
for rec in records_info:
    citing_assignee = rec['assignee']
    if not citing_assignee:
        continue
    cit_field = rec['citation']
    if not cit_field:
        continue
    # parse citation
    try:
        cit_list = json.loads(cit_field)
    except Exception:
        if isinstance(cit_field, list):
            cit_list = cit_field
        else:
            continue
    # primary subclass from cpc
    primary_sub = None
    cpc_field = rec['cpc']
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list) and len(cpcs)>0:
                first = cpcs[0]
                if isinstance(first, dict) and 'symbol' in first:
                    sym = first['symbol'].replace(' ', '')
                    if len(sym) >= 4:
                        primary_sub = sym[:4]
        except Exception:
            pass
    for c in cit_list:
        if not isinstance(c, dict):
            continue
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        cited_assg = pub_to_assignee.get(cited_pub)
        if cited_assg and is_univ_cal(cited_assg):
            if is_univ_cal(citing_assignee):
                continue
            pairs.add((citing_assignee, primary_sub))

result = []
for a,s in sorted(pairs):
    result.append({'citing_assignee': a, 'primary_subclass': s})
subclasses = sorted({x['primary_subclass'] for x in result if x['primary_subclass']})
out = {'pairs': result, 'subclasses': subclasses}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json'}

exec(code, env_args)
