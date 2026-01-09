code = """import json, re

# Load large query result
path = var_call_xwBfBeC3IMMiVFNH4qHdtSjv
with open(path, 'r', encoding='utf-8') as f:
    recs = json.load(f)

uc_pat_pubnums = set()
uc_pat_citedby = []  # (uc_pub, citing_pub)

# helper to parse publication number patterns like US-2022074631-A1, US-11081687-B2, etc.
pat_pub_re = re.compile(r"[A-Z]{2}-[0-9A-Z]+-[A-Z][0-9A-Z]*")

def extract_pubnum(pi):
    # prefer 'pub. number X.' patterns
    m = re.search(r"pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z][0-9A-Z]*)", pi)
    if m:
        return m.group(1)
    m = re.search(r"publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z][0-9A-Z]*)", pi)
    if m:
        return m.group(1)
    # fallback first match
    m = pat_pub_re.search(pi)
    return m.group(0) if m else None

def extract_assignee(pi):
    # patterns observed: "X holds the US patent application"; "... is owned by X"; "... is assigned to X"
    m = re.match(r"(.+?)\s+holds\s+the\s+US\s+patent\s+(?:application|filing)", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"is owned by\s+(.+?)\s+and has", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"is assigned to\s+(.+?)\s+and has", pi)
    if m:
        return m.group(1).strip()
    m = re.search(r"owned by\s+(.+?),\s+with publication", pi)
    if m:
        return m.group(1).strip()
    return None

# First pass: gather UC-assigned publication numbers
for r in recs:
    pi = r.get('Patents_info') or ''
    if 'UNIV CALIFORNIA' in pi:
        pub = extract_pubnum(pi)
        if pub:
            uc_pat_pubnums.add(pub)

# Second pass: find citing patents that cite any UC pub
citing_rows = []
for r in recs:
    pi = r.get('Patents_info') or ''
    assignee = extract_assignee(pi)
    pub = extract_pubnum(pi)
    if not assignee or not pub:
        continue
    # exclude UC itself (multiple possible strings)
    if assignee.strip().upper() in {'UNIV CALIFORNIA','UNIVERSITY OF CALIFORNIA'}:
        continue
    cit = r.get('citation')
    if not cit:
        continue
    try:
        cit_list = json.loads(cit)
    except Exception:
        continue
    cited_pubs = {c.get('publication_number') for c in cit_list if isinstance(c, dict)}
    cited_pubs.discard(None)
    if uc_pat_pubnums.intersection(cited_pubs):
        # extract primary CPC subclass (first==true). CPC list may have duplicates
        cpc = r.get('cpc')
        primary_subclasses = []
        if cpc:
            try:
                cpc_list = json.loads(cpc)
                for e in cpc_list:
                    if isinstance(e, dict) and e.get('first') is True and e.get('code'):
                        code = e['code']
                        # CPC subclass is first 4 chars like A61K, F25B
                        subclass = code.replace(' ', '')[:4]
                        if len(subclass)==4:
                            primary_subclasses.append(subclass)
            except Exception:
                pass
        if primary_subclasses:
            # unique
            primary_subclasses = sorted(set(primary_subclasses))
        citing_rows.append({'citing_assignee': assignee, 'primary_cpc_subclasses': primary_subclasses})

# Build unique pairs assignee-subclass
pairs = set()
for row in citing_rows:
    a = row['citing_assignee']
    for sc in row['primary_cpc_subclasses']:
        pairs.add((a, sc))

pairs_list = [{'citing_assignee': a, 'cpc_subclass': sc} for a, sc in sorted(pairs)]

import json as _json
print('__RESULT__:')
print(_json.dumps({'uc_publications_found': len(uc_pat_pubnums), 'pairs': pairs_list}))"""

env_args = {'var_call_fxJadHAUZM3iuUYaniKIswmb': ['publicationinfo'], 'var_call_Xm5UjNpEkcra457jTYGuJdzG': ['cpc_definition'], 'var_call_HA7p9pMUDTg2hLqkVm3okFYg': [], 'var_call_ApuxTjiJw5fJFB4chMvAela1': [], 'var_call_kqj7hKd756oOZmZc6YvSExWW': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_bOjwwymn92tcDpw2XPQ3iRRF': [], 'var_call_xwBfBeC3IMMiVFNH4qHdtSjv': 'file_storage/call_xwBfBeC3IMMiVFNH4qHdtSjv.json'}

exec(code, env_args)
