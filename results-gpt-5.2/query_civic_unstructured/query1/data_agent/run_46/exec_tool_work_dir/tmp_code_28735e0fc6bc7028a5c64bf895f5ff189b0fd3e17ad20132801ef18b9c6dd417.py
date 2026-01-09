code = """import json, re, pandas as pd

# Load civic docs
civic_path = var_call_T4Ojw85gpLpoASrRx4vCTzoJ
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funded projects > 50k (summed)
fund_path = var_call_XlaC5SXo3fAX4eJY28nmeBkQ
with open(fund_path, 'r', encoding='utf-8') as f:
    funded = json.load(f)
funded_set = set([r['Project_Name'] for r in funded])

# Extract projects under "Capital Improvement Projects (Design)" sections
projects_design_capital = set()

# pattern: section header then list of project titles each on its own line; stop at next section header
stop_headers = [
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)',
    'Disaster Recovery Projects',
    'Disaster Recovery Project',
]
stop_re = re.compile('|'.join([re.escape(h) for h in stop_headers]), re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','')
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*)', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    after = m.group(1)
    sm = stop_re.search(after)
    section = after[:sm.start()] if sm else after
    # clean weird chars
    section = section.replace('\r','')
    # Candidate lines: non-empty, not bullet markers, not updates/schedule/page headings
    for line in section.split('\n'):
        ln = line.strip()
        if not ln:
            continue
        if len(ln) < 4:
            continue
        if re.match(r'^(\(cid:|Page\s+\d+|Agenda Item|To:|Prepared by:|Approved by:|Date prepared|Meeting date|Subject:|RECOMMENDED ACTION|DISCUSSION:)$', ln, flags=re.IGNORECASE):
            continue
        if re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', ln, flags=re.IGNORECASE):
            continue
        if re.match(r'^[•\-\*\(]?(cid:)?\d+', ln):
            continue
        # Exclude lines that look like schedule entries
        if re.search(r'^(Complete Design|Advertise|Begin Construction|Final Design|Begin construction|Complete Construction)\s*:', ln, flags=re.IGNORECASE):
            continue
        # Heuristic: project titles are mostly Title Case and not sentences with periods
        if ln.endswith('.'):
            continue
        # Exclude very long lines (likely paragraphs)
        if len(ln) > 120:
            continue
        projects_design_capital.add(ln)

# Intersection with funded projects > 50k
answer_count = len(projects_design_capital & funded_set)

print('__RESULT__:')
print(json.dumps({
    'count': answer_count,
    'design_capital_projects': sorted(list(projects_design_capital & funded_set))
}))"""

env_args = {'var_call_aPDVTux9oknE8VfTjSjsf1Jj': [{'cnt': '276'}], 'var_call_T4Ojw85gpLpoASrRx4vCTzoJ': 'file_storage/call_T4Ojw85gpLpoASrRx4vCTzoJ.json', 'var_call_XlaC5SXo3fAX4eJY28nmeBkQ': 'file_storage/call_XlaC5SXo3fAX4eJY28nmeBkQ.json'}

exec(code, env_args)
