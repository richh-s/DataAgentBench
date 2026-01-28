code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub_recs = load_records(var_call_aEurZQskU9RMtLPBF2ylKUbf)
cpc_defs = load_records(var_call_8GGYsLd0C75M2hfVRT2gvpjY)

# Build CPC symbol->title map
sym2title = {r['symbol']: r.get('titleFull') for r in cpc_defs if r.get('symbol')}

# Helpers to parse assignee and citations and primary CPC subclass
assignee_pat = re.compile(r"owned by (.+?) and has|assigned to (.+?) and has|holds the [A-Z]{2} patent filing .*? is (?:owned by|assigned to) (.+?) and has|holds the .*? is owned by (.+?) and has", re.IGNORECASE)

# More robust: extract after 'owned by' or 'assigned to' or 'holds the' ... 'UNIV CALIFORNIA'

def extract_assignee(pi):
    m = re.search(r"(?:owned by|assigned to)\s+(.+?)\s+and has", pi, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('.')
    m = re.search(r"^(.+?)\s+holds\b", pi, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('.')
    # fallback: UNIV CALIFORNIA ...
    if 'UNIV CALIFORNIA' in pi:
        return 'UNIV CALIFORNIA'
    return None


def parse_json_list(s):
    if s is None:
        return []
    if isinstance(s, list):
        return s
    s = s.strip()
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        return []


def cpc_to_subclass(code):
    # CPC subclass is like A01B, C12Q, F25B etc: 4 chars: letter + 2 digits + letter
    if not code:
        return None
    m = re.match(r"^([A-HY][0-9]{2}[A-Z])", code)
    return m.group(1) if m else None

rows=[]
uc_pubs=set()
for r in pub_recs:
    pi=r.get('Patents_info','') or ''
    ass=extract_assignee(pi)
    if ass and ass.upper().find('UNIV CALIFORNIA')!=-1:
        # this record is a UC-assigned patent publication
        # extract its publication number to match citations
        m=re.search(r"pub\. number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\.", pi)
        if not m:
            m=re.search(r"publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\.", pi)
        if m:
            uc_pubs.add(m.group(1))

# Now scan all publications (not just UC) for citations to UC pubs, and capture citing assignee and primary CPC subclass
# Need all publications; but we only queried UC ones. So instead, treat citations field in UC patents as "cited by"? No.
# Therefore, we must search all publicationinfo for citations to UC pubs. We'll do it by additional query via SQL if needed.

print('__RESULT__:')
print(json.dumps({'uc_publications': sorted(list(uc_pubs))[:50], 'uc_publications_count': len(uc_pubs)}))"""

env_args = {'var_call_aEurZQskU9RMtLPBF2ylKUbf': 'file_storage/call_aEurZQskU9RMtLPBF2ylKUbf.json', 'var_call_8GGYsLd0C75M2hfVRT2gvpjY': 'file_storage/call_8GGYsLd0C75M2hfVRT2gvpjY.json'}

exec(code, env_args)
