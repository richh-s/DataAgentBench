code = """import json, re

funding_src = var_call_DBnP30lyXWiyUFvKYz9igjn5
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    funding = json.load(open(funding_src, 'r', encoding='utf-8'))
else:
    funding = funding_src
funding_set = set(r['Project_Name'] for r in funding)

civic_src = var_call_j4YTKHRjejKMNkIxwcYyjf9y
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    civic_docs = json.load(open(civic_src, 'r', encoding='utf-8'))
else:
    civic_docs = civic_src

proj_status = {}
pattern = re.compile(r"Capital Improvement Projects \(Design\)\s*(.*?)\n\s*Capital Improvement Projects \(Construction\)", flags=re.S|re.I)

for doc in civic_docs:
    t = (doc.get('text','') or '').replace('\r','')
    m = pattern.search(t)
    if not m:
        continue
    section = m.group(1)
    for ln in section.split('\n'):
        ln = ln.strip()
        if not ln:
            continue
        if re.match(r"^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction|Final Design|Page\s+\d|Agenda Item)", ln, flags=re.I):
            continue
        if re.match(r"^(Capital Improvement Projects|Disaster Recovery Projects)", ln, flags=re.I):
            continue
        if re.search(r"\bStaff\b|\bCity\b|\bwill\b|\bis\b", ln):
            continue
        if 3 < len(ln) < 120:
            proj_status[ln] = 'design'

matched = sorted([p for p in proj_status if p in funding_set])

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'matched_projects': matched}))"""

env_args = {'var_call_RFN2vkMBUQvSAsbmC0sZFLzr': ['Funding'], 'var_call_zWKnAxPdJx0XUOenlFfrga3x': ['civic_docs'], 'var_call_DBnP30lyXWiyUFvKYz9igjn5': 'file_storage/call_DBnP30lyXWiyUFvKYz9igjn5.json', 'var_call_j4YTKHRjejKMNkIxwcYyjf9y': 'file_storage/call_j4YTKHRjejKMNkIxwcYyjf9y.json'}

exec(code, env_args)
