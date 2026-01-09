code = """import json, pandas as pd, re

# Load funding projects with total_funding > 50000
funding = var_call_uSFr4G9mMF9tWYTesViJM3cp
if isinstance(funding, str):
    with open(funding, 'r', encoding='utf-8') as f:
        funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_funding'] = pd.to_numeric(fund_df['total_funding'])
fund_projects = set(fund_df['Project_Name'].astype(str))

# Load civic docs
docs = var_call_8mVoT044l4Y3A3xanMcsmdsA
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Extract project names under any 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)' sections

design_projects = set()

section_headers = [
    r'Capital Improvement Projects\s*\(Design\)',
    r'Disaster Recovery Projects\s*\(Design\)',
    r'Capital Improvement Program\s*\(Design\)',
]

stop_headers = [
    r'Capital Improvement Projects\s*\(Construction\)',
    r'Capital Improvement Projects\s*\(Not Started\)',
    r'Disaster Recovery Projects\s*\(Construction\)',
    r'Disaster Recovery Projects\s*\(Not Started\)',
    r'Capital Improvement Projects\s*\(Completed\)',
    r'Disaster Recovery Projects\s*\(Completed\)',
]

header_re = re.compile('|'.join(section_headers), re.IGNORECASE)
stop_re = re.compile('|'.join(stop_headers), re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # normalize
    t = text.replace('\r','\n')
    lines = [ln.strip() for ln in t.split('\n')]
    n = len(lines)
    i = 0
    while i < n:
        if header_re.search(lines[i]):
            i += 1
            # scan until stop header
            while i < n and not stop_re.search(lines[i]):
                ln = lines[i].strip()
                # project names are typically standalone lines followed by bullet updates
                if ln and len(ln) < 120:
                    # exclude generic headings
                    bad = {'updates:', 'project schedule:', 'estimated schedule:', 'project description:', 'project updates:', 'recommended action', 'discussion'}
                    low = ln.lower().rstrip(':')
                    if low not in bad and not low.startswith('page ') and not low.startswith('agenda item'):
                        # exclude bullet-only lines
                        if not re.match(r'^[\(\[\{]?cid[:\d\)\]\}]+', ln, flags=re.IGNORECASE) and not ln.startswith('(cid'):
                            # exclude lines that look like sentences rather than titles
                            if not re.search(r'\bcomplete design\b|\badvertise\b|\bbegin construction\b', low):
                                # likely title if next non-empty line contains 'Updates' or 'Project Description'
                                j = i+1
                                while j < n and lines[j]=='' :
                                    j += 1
                                if j < n and re.search(r'\bUpdates\b|\bProject Description\b|\bProject Updates\b|\bEstimated Schedule\b|\bProject Schedule\b', lines[j], re.IGNORECASE):
                                    design_projects.add(ln)
                i += 1
            continue
        i += 1

# Count those with funding > 50000
count = len(design_projects.intersection(fund_projects))

print('__RESULT__:')
print(json.dumps({'count': int(count)}))"""

env_args = {'var_call_IHlBhZuF8SZiTatZr48XWAHB': ['Funding'], 'var_call_8LK57qCySM3AbcZFhFWZ3Gm9': ['civic_docs'], 'var_call_uSFr4G9mMF9tWYTesViJM3cp': 'file_storage/call_uSFr4G9mMF9tWYTesViJM3cp.json', 'var_call_8mVoT044l4Y3A3xanMcsmdsA': 'file_storage/call_8mVoT044l4Y3A3xanMcsmdsA.json'}

exec(code, env_args)
