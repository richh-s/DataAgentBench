code = """import json, re
import pandas as pd

# Load UC pubs computed earlier by rebuilding from file
uc_path = var_call_j55SyTVQyBw0aAybXsyxCaAM
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_rows = json.load(f)

pub_re = re.compile(r"pub\. number\s+([A-Z]{2,}-[0-9A-Z]+(?:-[A-Z][0-9])?)", re.I)
fallback_re = re.compile(r"\b([A-Z]{2,}-\d{7,}-[A-Z]\d)\b")

def extract_uc_pubs(rows):
    s=set()
    for r in rows:
        txt=r.get('Patents_info','') or ''
        m=pub_re.search(txt)
        if m:
            s.add(m.group(1))
        for mm in fallback_re.findall(txt):
            s.add(mm)
    return s

uc_pubs = extract_uc_pubs(uc_rows)

# Load all non-empty citations
cit_path = var_call_KJ7mredPpIpCLZFg4dHYGs9s
with open(cit_path, 'r', encoding='utf-8') as f:
    citing_rows = json.load(f)

# Extract assignee from Patents_info: "X holds" or "In US, ... is assigned to X" etc.
assignee_re1 = re.compile(r"^(.+?)\s+holds\b", re.I)
assignee_re2 = re.compile(r"assigned to\s+([^,\.]+)", re.I)

def get_assignee(pi):
    if not pi:
        return None
    m=assignee_re1.search(pi)
    if m:
        return m.group(1).strip()
    m=assignee_re2.search(pi)
    if m:
        return m.group(1).strip()
    return None

# Parse CPC list and get primary subclass (4 chars + 1 digit?) from first==true entries
# We'll take unique subclasses from first==true, else if none take first code's subclass.
sub_re = re.compile(r"^([A-HY]\d{2}[A-Z])")

def primary_subclasses(cpc_str):
    if not cpc_str or cpc_str.strip() in ('', '[]'):
        return []
    try:
        lst=json.loads(cpc_str)
    except Exception:
        return []
    first_codes=[d.get('code') for d in lst if isinstance(d,dict) and d.get('first')==True and d.get('code')]
    codes = first_codes if first_codes else [d.get('code') for d in lst if isinstance(d,dict) and d.get('code')][:1]
    subs=[]
    for code in codes:
        m=sub_re.match(code)
        if m:
            subs.append(m.group(1))
    return sorted(set(subs))

# Determine which rows cite UC pubs
def cites_uc(citation_str):
    if not citation_str or citation_str.strip() in ('', '[]'):
        return False
    try:
        cites=json.loads(citation_str)
    except Exception:
        return False
    for c in cites:
        if isinstance(c,dict):
            pn=c.get('publication_number') or ''
            if pn in uc_pubs:
                return True
    return False

pairs=set()
for r in citing_rows:
    if not cites_uc(r.get('citation')):
        continue
    assignee=get_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    subs=primary_subclasses(r.get('cpc'))
    for s in subs:
        pairs.add((assignee,s))

out = [{'assignee':a,'cpc_subclass':s} for a,s in sorted(pairs)]
print('__RESULT__:')
print(json.dumps({'pairs': out, 'pair_count': len(out), 'assignee_count': len(set([x['assignee'] for x in out]))}))"""

env_args = {'var_call_RXZxPa6ek2GtXCBDhmGKF66H': ['publicationinfo'], 'var_call_xRaFlt6HbwpuEGgcKr0x8ZXF': ['cpc_definition'], 'var_call_j55SyTVQyBw0aAybXsyxCaAM': 'file_storage/call_j55SyTVQyBw0aAybXsyxCaAM.json', 'var_call_zqNKJTMEJLBC8OYNvbOYtOK0': {'uc_pub_count': 59}, 'var_call_KJ7mredPpIpCLZFg4dHYGs9s': 'file_storage/call_KJ7mredPpIpCLZFg4dHYGs9s.json'}

exec(code, env_args)
