code = """import json, re
import pandas as pd

# load records
src = var_call_GYAWO6qr1r7qnkcH97SYl3D4
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = src

# helpers
ASSIGNEE_RE = re.compile(r"owned by ([^\.]+?) and has pub\.")
ASSIGNEE_RE2 = re.compile(r"is assigned to ([^\.]+?) and has")
ASSIGNEE_RE3 = re.compile(r"holds the [A-Z]{2} patent filing .*? is owned by ([^\.]+?)(?: and|\.)")
ASSIGNEE_RE4 = re.compile(r"assigned to ([^\.]+?) and has")

PUBNO_RE = re.compile(r"pub\.? number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")
PUBNO_RE2 = re.compile(r"publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")

def extract_assignee(patents_info:str):
    for r in (ASSIGNEE_RE, ASSIGNEE_RE2, ASSIGNEE_RE3, ASSIGNEE_RE4):
        m = r.search(patents_info or '')
        if m:
            return m.group(1).strip()
    # fallback: find 'owned by X'
    m = re.search(r"owned by ([^\.]+?)(?:\.| and)", patents_info or '')
    if m:
        return m.group(1).strip()
    return None

def extract_pubno(patents_info:str):
    for r in (PUBNO_RE, PUBNO_RE2):
        m = r.search(patents_info or '')
        if m:
            return m.group(1).strip()
    return None

def parse_json_field(s):
    if not s:
        return []
    if isinstance(s, list):
        return s
    ss = s.strip()
    if ss == '[]':
        return []
    try:
        return json.loads(ss)
    except Exception:
        return []

def normalize_pubno(pubno):
    if not pubno:
        return None
    return pubno.strip()

# build map of UC patents -> set of primary CPC subclass (first==true) codes -> subclass (4 chars)
uc_pubno_to_primary_subclass = {}
for rec in records:
    pi = rec.get('Patents_info','')
    assignee = extract_assignee(pi)
    if not assignee or 'UNIV CALIFORNIA' not in assignee.upper():
        continue
    pubno = extract_pubno(pi)
    pubno = normalize_pubno(pubno)
    cpcs = parse_json_field(rec.get('cpc'))
    primary_codes = [c.get('code') for c in cpcs if isinstance(c, dict) and c.get('first') is True and c.get('code')]
    subclasses = sorted({code.replace(' ', '')[:4] for code in primary_codes if isinstance(code,str) and len(code.replace(' ',''))>=4})
    if pubno:
        uc_pubno_to_primary_subclass[pubno] = subclasses

# now find citations to UC patents by scanning all records that have citations referencing UC pubnos
citing = []  # rows: citing_pubno, citing_assignee, cited_uc_pubno, subclass
for rec in records:
    pi = rec.get('Patents_info','')
    citing_assignee = extract_assignee(pi)
    if not citing_assignee:
        continue
    if 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    citing_pubno = extract_pubno(pi)

    cits = parse_json_field(rec.get('citation'))
    for c in cits:
        if not isinstance(c, dict):
            continue
        cited = normalize_pubno(c.get('publication_number'))
        if cited in uc_pubno_to_primary_subclass:
            for subclass in uc_pubno_to_primary_subclass[cited]:
                citing.append({'citing_assignee': citing_assignee, 'cpc_subclass': subclass})

# unique pairs
pairs = sorted({(r['citing_assignee'], r['cpc_subclass']) for r in citing})
subclasses = sorted({sub for _, sub in pairs})

print('__RESULT__:')
print(json.dumps({'pairs': pairs, 'subclasses': subclasses}))"""

env_args = {'var_call_ZSyNIgN7aBSNAiZM7qedGzE1': ['publicationinfo'], 'var_call_Gj7WHr85gETDG1tp4fJxUlUA': ['cpc_definition'], 'var_call_GYAWO6qr1r7qnkcH97SYl3D4': 'file_storage/call_GYAWO6qr1r7qnkcH97SYl3D4.json'}

exec(code, env_args)
