code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

uc_assigned = load_records(var_call_XHgY6nBpBlS88OG9UNxHXTwS)
uc_citing = load_records(var_call_rd6q2k1nn4kkf2DchDYz9XCb)

def parse_pub_numbers(citation_str):
    try:
        arr = json.loads(citation_str) if citation_str else []
    except Exception:
        return []
    pubs = []
    for x in arr:
        if isinstance(x, dict):
            pn = x.get('publication_number')
            if pn:
                pubs.append(pn)
    return pubs

# Build set of UC publication numbers
uc_pub_set = set()
for r in uc_assigned:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\.? number\s+([A-Z]{2}-[^\s\.,]+)', pi)
    if not m:
        m = re.search(r'publication number\s+([A-Z]{2}-[^\s\.,]+)', pi)
    if m:
        uc_pub_set.add(m.group(1))

# Filter citing records that cite any UC pub
rows = []
for r in uc_citing:
    cited_pubs = parse_pub_numbers(r.get('citation',''))
    if any(p in uc_pub_set for p in cited_pubs):
        pi = r.get('Patents_info','') or ''
        # assignee parsing
        m = re.search(r'owned by\s+([^\.,]+)', pi)
        if not m:
            m = re.search(r'assigned to\s+([^\.,]+)', pi)
        if not m:
            m = re.search(r'belonging to\s+([^\.,]+)', pi)
        assignee = m.group(1).strip() if m else None
        # primary CPC subclass from cpc json where first==true
        primary_codes=[]
        try:
            cpcs = json.loads(r.get('cpc','') or '[]')
        except Exception:
            cpcs=[]
        for c in cpcs:
            if isinstance(c, dict) and c.get('first') is True:
                code = c.get('code')
                if code:
                    primary_codes.append(code)
        # normalize to subclass level: first 4 chars (e.g., A61P)
        primary_subclasses = sorted({pc.replace(' ', '')[:4] for pc in primary_codes if len(pc)>=4})
        if assignee:
            rows.append({'citing_assignee': assignee, 'primary_subclass': primary_subclasses})

# explode
out=[]
for row in rows:
    if row['citing_assignee'].upper().strip()== 'UNIV CALIFORNIA':
        continue
    for sc in (row['primary_subclass'] or []):
        out.append({'citing_assignee': row['citing_assignee'], 'primary_subclass': sc})

df = pd.DataFrame(out).drop_duplicates()
subclasses = sorted(df['primary_subclass'].dropna().unique().tolist())
print('__RESULT__:')
print(json.dumps({'pairs': df.to_dict(orient='records'), 'subclasses': subclasses}))"""

env_args = {'var_call_3o5ZfMoc3y5EVYsylulSjg2n': ['publicationinfo'], 'var_call_ACAgPfNB0bEgERYmClAeaOHs': ['cpc_definition'], 'var_call_XHgY6nBpBlS88OG9UNxHXTwS': 'file_storage/call_XHgY6nBpBlS88OG9UNxHXTwS.json', 'var_call_rd6q2k1nn4kkf2DchDYz9XCb': 'file_storage/call_rd6q2k1nn4kkf2DchDYz9XCb.json'}

exec(code, env_args)
