code = """import json, re
path = var_call_lIkcWU0cAUPDcXWJMwYbGx3K
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def extract_pubnum(text):
    if not text:
        return None
    m = re.search(r'([A-Z]{2}-[A-Z0-9\-]+)', text)
    if m:
        return m.group(1).strip()
    m = re.search(r'(US-?\d{4,}[A-Z0-9\-]*)', text)
    if m:
        return m.group(1).strip()
    return None

def extract_assignee(text):
    if not text:
        return None
    m = re.match(r"^(.*?)\s+(?:holds|held|is assigned to|assigned to|owns|owned by|has)\b", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'Assignee[:\s]+([^,\n\(]+)', text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.match(r'^(.*?)\s*\(', text)
    if m:
        return m.group(1).strip()
    return None

pub_to_assignee = {}
records_info = []
for rec in records:
    pinfo = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(pinfo)
    assignee = extract_assignee(pinfo)
    if assignee:
        assignee_norm = re.sub(r'\s+', ' ', assignee).strip()
    else:
        assignee_norm = None
    if pubnum and assignee_norm:
        pub_to_assignee[pubnum] = assignee_norm
    records_info.append({
        'pubnum': pubnum,
        'assignee': assignee_norm,
        'citation': rec.get('citation'),
        'cpc': rec.get('cpc')
    })

def is_univ_cal(assignee):
    if not assignee:
        return False
    s = assignee.lower()
    return ('california' in s) and (('univ' in s) or ('university' in s))

pairs = set()
for rec in records_info:
    citing_assignee = rec['assignee']
    if not citing_assignee:
        continue
    cit_field = rec['citation']
    if not cit_field:
        continue
    try:
        cit_list = json.loads(cit_field)
    except Exception:
        if isinstance(cit_field, list):
            cit_list = cit_field
        else:
            continue
    primary_subclass = None
    cpc_field = rec['cpc']
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list) and len(cpcs) > 0:
                first = cpcs[0]
                if isinstance(first, dict):
                    sym = first.get('symbol')
                    if sym:
                        sym_n = re.sub(r'\s+','',sym)
                        if len(sym_n) >= 4:
                            primary_subclass = sym_n[:4]
        except Exception:
            primary_subclass = None
    for c in cit_list:
        if not isinstance(c, dict):
            continue
        cited_pub = c.get('publication_number')
        if not cited_pub:
            continue
        assg = pub_to_assignee.get(cited_pub)
        if assg and is_univ_cal(assg):
            if is_univ_cal(citing_assignee):
                continue
            pairs.add((citing_assignee, primary_subclass))

result = []
for a, s in sorted(pairs):
    result.append({'citing_assignee': a, 'primary_subclass': s})
subclasses = sorted({x['primary_subclass'] for x in result if x['primary_subclass']})
out = {'pairs': result, 'subclasses': subclasses}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json'}

exec(code, env_args)
