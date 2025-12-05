code = """import json, re, pandas as pd, os
from collections import defaultdict

path = var_call_ShrFl7yR5D8Q4biCufy1hJCQ
with open(path, 'r') as f:
    data = json.load(f)

# helper to extract publication_number and assignee from Patents_info
pub_re = re.compile(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A0-9]+)')
assignee_re = re.compile(r'assignee_harmonized: ([^,;]+)')

records = []
for row in data:
    info = row.get('Patents_info','')
    m_pub = pub_re.search(info)
    pubnum = m_pub.group(1) if m_pub else None
    m_ass = assignee_re.search(info)
    assignee = m_ass.group(1).strip() if m_ass else None
    try:
        cits = json.loads(row.get('citation','[]'))
    except Exception:
        cits = []
    for c in cits:
        c_pub = c.get('publication_number')
        if not c_pub:
            continue
        records.append({'citing_pub': pubnum, 'citing_assignee': assignee, 'cited_pub': c_pub})

# unique cited publication numbers
cited_pubs = sorted({r['cited_pub'] for r in records})

result = {
    'records': records[:100],
    'num_records': len(records),
    'num_cited_pubs': len(cited_pubs),
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nxvCiyIQ1gzIfwIWrDwTCVbQ': [], 'var_call_z2jbjgQL5wypfL42JtQP2Afi': ['cpc_definition'], 'var_call_ShrFl7yR5D8Q4biCufy1hJCQ': 'file_storage/call_ShrFl7yR5D8Q4biCufy1hJCQ.json'}

exec(code, env_args)
