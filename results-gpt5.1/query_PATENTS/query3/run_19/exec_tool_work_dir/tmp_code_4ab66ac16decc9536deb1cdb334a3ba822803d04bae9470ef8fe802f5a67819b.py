code = """import json, re

# Load all publication rows
path = var_call_GbVRr2f0neMi4Cj5uIqQZ9 if 'var_call_GbVRr2f0neMi4Cj5uIqQZ9' in globals() else var_call_GbVRPVr2f0neMi4Cj5uIqQZ9
with open(path, 'r') as f:
    all_pubs = json.load(f)

# Load cited publication numbers
cited_path = var_call_mAtPvD08WA8z7Ei4e9OrmnaG
with open(cited_path, 'r') as f:
    cited_pns = set(json.load(f))

# helper to extract pub number token from Patents_info
pat_pub = re.compile(r"(?:publication number|pub\. number|publication no\.|pub\. no\.) ([A-Z]{2}-[0-9A-Z]+)")

results = []
for rec in all_pubs:
    info = rec.get('Patents_info','')
    m = pat_pub.search(info)
    if not m:
        continue
    pn = m.group(1)
    if pn in cited_pns:
        # extract assignee (up to 'holds' or 'is owned by' etc)
        assignee = None
        m2 = re.match(r"(.*?) holds", info)
        if not m2:
            m2 = re.match(r"In [A-Z]{2}, the (?:application|patent filing|patent application) .*? is (?:owned by|assigned to) (.*?) and", info)
        if m2:
            assignee = m2.group(1).strip()
        results.append({"assignee": assignee, "Patents_info": info, "cpc": rec.get('cpc')})

# filter out UNIV CALIFORNIA assignee
filtered = [r for r in results if r['assignee'] and 'UNIV CALIFORNIA' not in r['assignee']]

# gather CPC primary subclasses (codes where 'first': true)
assignee_cpc = {}
for r in filtered:
    try:
        cpc_list = json.loads(r['cpc']) if r['cpc'] else []
    except Exception:
        cpc_list = []
    prim = sorted({c['code'] for c in cpc_list if c.get('first')})
    if not prim:
        continue
    assignee_cpc.setdefault(r['assignee'], set()).update(prim)

# prepare flat list of (assignee, code)
pairs = []
for a, codes in assignee_cpc.items():
    for code in sorted(codes):
        # take subclass part: up to '/' if present
        primary = code.split('/')[0]
        pairs.append({"assignee": a, "symbol": primary})

print("__RESULT__:")
print(json.dumps(pairs))"""

env_args = {'var_call_R4WXCjPHwFKCqiwH8iAkCVXn': [], 'var_call_Jz8AOE2Tf5zfq22MGv4M3DVc': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_HbfT9BjzhP7xXeWPLpJrtcG0': 'file_storage/call_HbfT9BjzhP7xXeWPLpJrtcG0.json', 'var_call_mAtPvD08WA8z7Ei4e9OrmnaG': 'file_storage/call_mAtPvD08WA8z7Ei4e9OrmnaG.json', 'var_call_GbVRPVr2f0neMi4Cj5uIqQZ9': 'file_storage/call_GbVRPVr2f0neMi4Cj5uIqQZ9.json'}

exec(code, env_args)
