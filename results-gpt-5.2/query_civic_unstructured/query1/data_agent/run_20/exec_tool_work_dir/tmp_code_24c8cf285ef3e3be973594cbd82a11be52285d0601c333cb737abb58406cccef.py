code = """import json, pandas as pd, re

funding = var_call_uSFr4G9mMF9tWYTesViJM3cp
if isinstance(funding, str):
    with open(funding, 'r', encoding='utf-8') as f:
        funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_funding'] = pd.to_numeric(fund_df['total_funding'])
fund_projects = set(fund_df['Project_Name'].astype(str))

docs = var_call_8mVoT044l4Y3A3xanMcsmdsA
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

nl = chr(10)
header_re = re.compile(r'(Capital Improvement Projects\s*\(Design\)|Disaster Recovery Projects\s*\(Design\)|Capital Improvement Program\s*\(Design\))', re.IGNORECASE)
stop_re = re.compile(r'(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects\s*\(Construction\)|Disaster Recovery Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(Completed\)|Disaster Recovery Projects\s*\(Completed\))', re.IGNORECASE)

def next_nonempty(lines, start):
    j = start
    n = len(lines)
    while j < n and str(lines[j]).strip() == '':
        j += 1
    return j

design_projects = set()

for d in docs:
    text = d.get('text', '') or ''
    if not text:
        continue
    text = text.replace('\r', nl)
    lines = [ln.strip() for ln in text.split(nl)]
    n = len(lines)
    i = 0
    while i < n:
        if header_re.search(lines[i] or ''):
            i += 1
            while i < n and not stop_re.search(lines[i] or ''):
                ln = (lines[i] or '').strip()
                if ln and len(ln) < 160:
                    low = ln.lower().rstrip(':')
                    if (not low.startswith('page ')) and (not low.startswith('agenda item')) and (not ln.startswith('(cid')):
                        if not re.search(r'\bcomplete design\b|\badvertise\b|\bbegin construction\b', low):
                            j = next_nonempty(lines, i + 1)
                            if j < n and re.search(r'\bUpdates\b|\bProject Description\b|\bProject Updates\b|\bEstimated Schedule\b|\bProject Schedule\b', lines[j] or '', re.IGNORECASE):
                                design_projects.add(ln)
                i += 1
            continue
        i += 1

count = len(design_projects.intersection(fund_projects))

print('__RESULT__:')
print(json.dumps({'count': int(count)}))"""

env_args = {'var_call_IHlBhZuF8SZiTatZr48XWAHB': ['Funding'], 'var_call_8LK57qCySM3AbcZFhFWZ3Gm9': ['civic_docs'], 'var_call_uSFr4G9mMF9tWYTesViJM3cp': 'file_storage/call_uSFr4G9mMF9tWYTesViJM3cp.json', 'var_call_8mVoT044l4Y3A3xanMcsmdsA': 'file_storage/call_8mVoT044l4Y3A3xanMcsmdsA.json'}

exec(code, env_args)
