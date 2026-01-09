code = """import json, re
import pandas as pd

# load funding >50k
funding_src = var_call_DBnP30lyXWiyUFvKYz9igjn5
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src
funding_set = set([r['Project_Name'] for r in funding])

# load civic docs
civic_src = var_call_j4YTKHRjejKMNkIxwcYyjf9y
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# extract projects listed under 'Capital Improvement Projects (Design)'
proj_status = {}  # name -> status
for doc in civic_docs:
    text = doc.get('text','')
    # normalize
    t = text.replace('\r','')
    # find section
    m = re.search(r'Capital Improvement Projects \(Design\)\s*(.*?)\n\s*Capital Improvement Projects \(Construction\)', t, flags=re.S|re.I)
    if not m:
        continue
    section = m.group(1)
    # split lines and pick candidate project name lines: non-empty, not bullet/update/schedule/page/item
    lines = [ln.strip() for ln in section.split('\n')]
    for ln in lines:
        if not ln:
            continue
        if re.match(r'^(\(cid:|Updates:|Project Schedule|Estimated Schedule|Complete Design|Advertise|Begin Construction|Final Design|Page\s+\d|Agenda Item)', ln, flags=re.I):
            continue
        if ':' in ln and ln.lower().startswith('project'):
            continue
        # ignore headings
        if re.match(r'^(Capital Improvement Projects|Disaster Recovery Projects)', ln, flags=re.I):
            continue
        # heuristic: project names are title-like and not too long
        if len(ln) > 3 and len(ln) < 120:
            # avoid lines that are clearly narrative sentences
            if re.search(r'\bStaff\b|\bCity\b|\bwill\b|\bis\b', ln):
                continue
            proj_status[ln] = 'design'

# count those with funding >50k
count = sum(1 for p,s in proj_status.items() if s=='design' and p in funding_set)

print('__RESULT__:')
print(json.dumps({'count': int(count), 'matched_projects': sorted([p for p in proj_status if p in funding_set])}))"""

env_args = {'var_call_RFN2vkMBUQvSAsbmC0sZFLzr': ['Funding'], 'var_call_zWKnAxPdJx0XUOenlFfrga3x': ['civic_docs'], 'var_call_DBnP30lyXWiyUFvKYz9igjn5': 'file_storage/call_DBnP30lyXWiyUFvKYz9igjn5.json', 'var_call_j4YTKHRjejKMNkIxwcYyjf9y': 'file_storage/call_j4YTKHRjejKMNkIxwcYyjf9y.json'}

exec(code, env_args)
