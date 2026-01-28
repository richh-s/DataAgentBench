code = """import json, re
import pandas as pd

# UC publications list
src_uc = var_call_OEmJzxa5Jx9sLttUfJ6cTZgf
if isinstance(src_uc, str):
    with open(src_uc, 'r', encoding='utf-8') as f:
        uc_rows = json.load(f)
else:
    uc_rows = src_uc

uc_pub_numbers = set()
for r in uc_rows:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+(?:-[A-Z0-9]+)?)', pi)
    if m:
        uc_pub_numbers.add(m.group(1))

# Citing candidate rows
src_cite = var_call_C1EF3BJnLKr7N1qNx63L3Db0
if isinstance(src_cite, str):
    with open(src_cite, 'r', encoding='utf-8') as f:
        cite_rows = json.load(f)
else:
    cite_rows = src_cite

pairs = []  # assignee, subclass
for r in cite_rows:
    citations_txt = r.get('citation')
    if not citations_txt:
        continue
    try:
        cites = json.loads(citations_txt)
    except Exception:
        continue
    cited_pubs = {c.get('publication_number') for c in cites if isinstance(c, dict)}
    cited_pubs.discard(None)
    if not (cited_pubs & uc_pub_numbers):
        continue

    pi = r.get('Patents_info','') or ''
    # assignee: text before ' holds' or ' is owned by' or ' is assigned to'
    assignee = None
    m = re.match(r'(.+?)\s+holds\b', pi)
    if m:
        assignee = m.group(1).strip()
    else:
        m = re.search(r'is owned by\s+(.+?)\s+and\s+has', pi)
        if m:
            assignee = m.group(1).strip()
        else:
            m = re.search(r'is assigned to\s+(.+?)\s+and\s+has', pi)
            if m:
                assignee = m.group(1).strip()
    if not assignee:
        continue
    if assignee.strip().upper() == 'UNIV CALIFORNIA':
        continue

    cpc_txt = r.get('cpc')
    subclass = None
    if cpc_txt:
        try:
            cpcs = json.loads(cpc_txt)
            # find primary: first==true
            primary_codes = [d.get('code') for d in cpcs if isinstance(d, dict) and d.get('first') is True and d.get('code')]
            if primary_codes:
                code = primary_codes[0]
                # CPC subclass: first 4 chars letter+2digits+letter (e.g., H01M)
                m2 = re.match(r'^([A-HY]\d\d[A-Z])', code)
                if m2:
                    subclass = m2.group(1)
        except Exception:
            pass
    if not subclass:
        continue

    pairs.append({'citing_assignee': assignee, 'cpc_subclass': subclass})

df = pd.DataFrame(pairs).drop_duplicates().sort_values(['citing_assignee','cpc_subclass'])

print('__RESULT__:')
print(df.to_json(orient='records'))"""

env_args = {'var_call_oUoC4rgo7IbazBh2tm5OHMVZ': ['publicationinfo'], 'var_call_vLBAdBWrOlxUIGlz8ODC2r8z': ['cpc_definition'], 'var_call_bjUAB8P289iqm7W76637sZG7': [], 'var_call_OEmJzxa5Jx9sLttUfJ6cTZgf': 'file_storage/call_OEmJzxa5Jx9sLttUfJ6cTZgf.json', 'var_call_hNHoCsrBPJpcGQPhRb1o3KK3': {'uc_pub_count': 59}, 'var_call_C1EF3BJnLKr7N1qNx63L3Db0': 'file_storage/call_C1EF3BJnLKr7N1qNx63L3Db0.json'}

exec(code, env_args)
