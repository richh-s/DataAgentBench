code = """import json, re, pandas as pd
from collections import defaultdict

# load full result
path = var_call_5a85y1KrAKxrV771uPSMj0EF
with open(path, 'r') as f:
    data = json.load(f)

# extract assignee, pub number, cpc codes, citations
records = []
for row in data:
    info = row.get('Patents_info','')
    m_pub = re.search(r'pub\. number ([A-Z0-9-]+)', info)
    pub_no = m_pub.group(1) if m_pub else None
    # extract assignee_harmonized if present
    m_assignee = re.search(r'assignee_harmonized: ([^;,.]+)', info)
    assignee = m_assignee.group(1).strip() if m_assignee else None
    cpc_raw = row.get('cpc') or '[]'
    try:
        cpcs = [e['code'] for e in json.loads(cpc_raw)]
    except Exception:
        cpcs = []
    cit_raw = row.get('citation') or '[]'
    try:
        cits = json.loads(cit_raw)
    except Exception:
        cits = []
    cit_pubnos = [c.get('publication_number') for c in cits if c.get('publication_number')]
    records.append({'assignee': assignee, 'pub_no': pub_no, 'cpcs': cpcs, 'citations': cit_pubnos})

# build mapping from cited pub_no to list of citing pub_no and assignee
cited_to_citers = defaultdict(list)
for r in records:
    for cp in r['citations']:
        cited_to_citers[cp].append((r['pub_no'], r['assignee']))

# we need patents assigned to UNIV CALIFORNIA that are cited by others.
# among data we only have UC-owned ones (query filter), so cited publications likely include non-UC. But question: assignees that cite UC patents.
# To proceed, we assume cited publication_numbers in this UC-owned subset correspond to UC patents as well not ideal. We can't reliably know.

result = {'note': 'Insufficient structured data: cannot identify which cited patents are assigned to UNIV CALIFORNIA, nor assignees of citing patents, from provided subset.', 'sample_extracted_records': records[:5]}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_MqJxW0u2SHDYnu1mCfIzyd0G': [], 'var_call_5a85y1KrAKxrV771uPSMj0EF': 'file_storage/call_5a85y1KrAKxrV771uPSMj0EF.json'}

exec(code, env_args)
