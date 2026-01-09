code = """import json, re

civic_path = var_call_T4Ojw85gpLpoASrRx4vCTzoJ
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

fund_path = var_call_XlaC5SXo3fAX4eJY28nmeBkQ
with open(fund_path, 'r', encoding='utf-8') as f:
    funded = json.load(f)
funded_set = set(r['Project_Name'] for r in funded)

projects_design_capital = set()

stop_headers = [
    'Capital Improvement Projects (Construction)',
    'Capital Improvement Projects (Not Started)',
    'Disaster Recovery Projects',
    'Disaster Recovery Project'
]
stop_re = re.compile('|'.join(re.escape(h) for h in stop_headers), re.IGNORECASE)

for doc in civic_docs:
    text = (doc.get('text') or '').replace('\r', '')
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*)', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    after = m.group(1)
    sm = stop_re.search(after)
    section = after[:sm.start()] if sm else after

    for line in section.split('\n'):
        ln = line.strip()
        if not ln or len(ln) < 4 or len(ln) > 120:
            continue
        if ln.endswith('.'):
            continue
        if re.search(r'\b(cid:|Agenda Item|Page \d+ of)\b', ln, flags=re.IGNORECASE):
            continue
        if re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)', ln, flags=re.IGNORECASE):
            continue
        if re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', ln, flags=re.IGNORECASE):
            continue
        if re.match(r'^(Complete Design|Advertise|Begin Construction|Final Design|Begin construction|Complete Construction)\s*:', ln, flags=re.IGNORECASE):
            continue
        if re.match(r'^\(cid:', ln):
            continue
        projects_design_capital.add(ln)

intersection = projects_design_capital & funded_set

print('__RESULT__:')
print(json.dumps({'count': len(intersection)}))"""

env_args = {'var_call_aPDVTux9oknE8VfTjSjsf1Jj': [{'cnt': '276'}], 'var_call_T4Ojw85gpLpoASrRx4vCTzoJ': 'file_storage/call_T4Ojw85gpLpoASrRx4vCTzoJ.json', 'var_call_XlaC5SXo3fAX4eJY28nmeBkQ': 'file_storage/call_XlaC5SXo3fAX4eJY28nmeBkQ.json'}

exec(code, env_args)
