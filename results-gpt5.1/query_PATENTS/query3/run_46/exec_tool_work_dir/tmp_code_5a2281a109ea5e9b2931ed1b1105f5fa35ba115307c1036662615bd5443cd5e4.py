code = """import json, re, pandas as pd
from pathlib import Path

path = Path(var_call_ZWoyq0N426C8voVRyLT5IXbs)
rows = json.loads(path.read_text())

records = []
for r in rows:
    pi = r['Patents_info']
    m = re.search(r'assignee_harmonized: ([^,;]+)', pi)
    assignee = m.group(1).strip() if m else None
    if not assignee:
        # fallback: owner/owned by/assigned to phrase
        m2 = re.search(r'owned by ([^,.;]+)', pi)
        if not m2:
            m2 = re.search(r'assigned to ([^,.;]+)', pi)
        if not m2:
            m2 = re.search(r'holds the [A-Z]{2} patent filing .* is ([^,.;]+)', pi)
        assignee = m2.group(1).strip() if m2 else None
    # parse citing pub number
    mnum = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[AB][0-9])', pi)
    if not mnum:
        mnum = re.search(r'publication number ([A-Z]{2}-[0-9A-Z]+-[AB][0-9])', pi)
    pubnum = mnum.group(1) if mnum else None
    cites = json.loads(r['citation']) if r['citation'] else []
    cpc_list = json.loads(r['cpc']) if r['cpc'] else []
    prim_codes = sorted({e['code'] for e in cpc_list if e.get('first')})
    for c in cites:
        cpub = c.get('publication_number')
        if not cpub:
            continue
        records.append({'citing_assignee': assignee, 'citing_pub': pubnum, 'cited_pub': cpub, 'primary_cpc': prim_codes})

# deduplicate by cited_pub to later find which cited pubs belong to UNIV CALIFORNIA
cited_pubs = sorted({r['cited_pub'] for r in records})

result = {
  'records': records[:50],
  'num_rows': len(rows),
  'num_relations': len(records),
  'sample_cited_pubs': cited_pubs[:50]
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uQANuj8MAsLxyJnznAiafEGt': [], 'var_call_dViraW13HaF6dn3FuimMKgJO': ['cpc_definition'], 'var_call_ZWoyq0N426C8voVRyLT5IXbs': 'file_storage/call_ZWoyq0N426C8voVRyLT5IXbs.json'}

exec(code, env_args)
