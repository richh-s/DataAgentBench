code = """import json, re
# var_call_lIkcWU0cAUPDcXWJMwYbGx3K is the storage key with the .json file path
path = var_call_lIkcWU0cAUPDcXWJMwYbGx3K
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def extract_pubnum(text):
    if not text:
        return None
    # try common patterns
    m = re.search(r'publication number[:\s]*([A-Z]{2}-[A-Z0-9\-]+)', text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: find patterns like US-1234567-B2 or WO-2012014846-A1
    m = re.search(r'([A-Z]{2}-\d{4,}[A-Z0-9\-]*)', text)
    if m:
        return m.group(1).strip()
    # another fallback: look for patterns like US\s+\d{7}
    m = re.search(r'(US-?\d{4,}[A-Z0-9\-]*)', text)
    if m:
        return m.group(1).replace('US','US-').strip()
    return None

def extract_assignee(text):
    if not text:
        return None
    # look for patterns like '<ASSIGNEE> holds' or 'assigned to' or 'owned by' etc
    m = re.match(r"^(.*?)\s+(?:holds|held|is assigned to|assigned to|owns|owned by|has)\b", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # try 'Assignee: NAME' pattern
    m = re.search(r'Assignee[:\s]+([^,\n\(]+)', text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: take leading words before a parenthesis
    m = re.match(r'^(.*?)\s*\(', text)
    if m:
        return m.group(1).strip()
    return None

# Build mapping from publication_number -> assignee
pub_to_assignee = {}
# Also mapping from record index to its publication number and assignee and cpc and citation
records_info = []
for rec in records:
    pinfo = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(pinfo)
    assignee = extract_assignee(pinfo)
    # normalize
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

# helper to detect Univ of California
def is_univ_cal(assignee):
    if not assignee:
        return False
    s = assignee.lower()
    return ('california' in s) and (('univ' in s) or ('university' in s))

# Parse citations and find citing assignees that cite patents assigned to Univ California
pairs = set()
for rec in records_info:
    citing_assignee = rec['assignee']
    citing_pubnum = rec['pubnum']
    if not citing_assignee:
        continue
    # parse citation JSON if possible
    cit_str = rec['citation']
    if not cit_str:
        continue
    try:
        cit_list = json.loads(cit_str)
    except Exception:
        # sometimes it's already a list
        if isinstance(cit_str, list):
            cit_list = cit_str
        else:
            continue
    # find primary cpc symbol for citing patent
    primary_subclass = None
    cpc_field = rec['cpc']
    if cpc_field:
        try:
            cpcs = json.loads(cpc_field)
            if isinstance(cpcs, list) and len(cpcs)>0:
                sym = cpcs[0].get('symbol') if isinstance(cpcs[0], dict) else None
                if sym:
                    # normalize symbol: remove spaces
                    sym_n = re.sub(r'\s+','',sym)
                    # subclass is first 4 chars
                    if len(sym_n)>=4:
                        primary_subclass = sym_n[:4]
        except Exception:
            primary_subclass = None
    for c in cit_list:
        cited_pub = c.get('publication_number') if isinstance(c, dict) else None
        if not cited_pub:
            continue
        # if cited_pub in mapping and assigned to Univ California
        assg = pub_to_assignee.get(cited_pub)
        if assg and is_univ_cal(assg):
            # exclude if citing is Univ California
            if is_univ_cal(citing_assignee):
                continue
            # record pair
            pairs.add((citing_assignee, primary_subclass))

# Convert pairs to list of dicts
result = []
for a, s in sorted(pairs):
    result.append({'citing_assignee': a, 'primary_subclass': s})

# Also collect list of unique subclass symbols to query definitions
subclasses = sorted({item['primary_subclass'] for item in result if item['primary_subclass']})

out = {'pairs': result, 'subclasses': subclasses}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FPAj8kiR2uHNByP4TiyNMUT0': ['publicationinfo'], 'var_call_dEbVmpwiOYVo0PQ99zKfXZNt': ['cpc_definition'], 'var_call_lIkcWU0cAUPDcXWJMwYbGx3K': 'file_storage/call_lIkcWU0cAUPDcXWJMwYbGx3K.json'}

exec(code, env_args)
