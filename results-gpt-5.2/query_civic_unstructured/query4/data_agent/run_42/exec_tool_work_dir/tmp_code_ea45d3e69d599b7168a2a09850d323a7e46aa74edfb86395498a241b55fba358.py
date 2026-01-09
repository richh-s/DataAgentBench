code = """import json, re

civic_src = var_call_pcS8Ol3ZlMwwAKeMjQjVPd6k
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fund_src = var_call_qFyvDzDeLvA40E6T8EW7hTMj
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

spring_pat = re.compile(r'(?i)(?:\bstart(?:ed)?\b|\bst\b|\bbegin(?:\s+construction)?\b|\bstart\s+date\b|\bscheduled\s+start\b|\bcommence\b)?[^\\n]{0,80}(?:Spring\s*[,\-]?\s*2022|2022\s*[,\-]?\s*Spring|2022-Spring)')

projects_started = set()
fund_names = sorted(fund_map.keys(), key=len, reverse=True)

for doc in civic_docs:
    text = doc.get('text','') or ''
    if not text:
        continue
    if '2022' not in text or ('Spring' not in text and 'spring' not in text and '2022-Spring' not in text):
        continue
    for pname in fund_names:
        if pname not in text:
            continue
        for m in re.finditer(re.escape(pname), text):
            window = text[max(0, m.start()-500): min(len(text), m.end()+800)]
            if spring_pat.search(window):
                projects_started.add(pname)
                break

count = len(projects_started)
total_funding = sum(fund_map.get(p, 0) for p in projects_started)

out = {'projects_started_spring_2022_count': count, 'total_funding': total_funding, 'projects': sorted(projects_started)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_htAYovui5hnnVcxO2DwKFvnL': ['Funding'], 'var_call_pcS8Ol3ZlMwwAKeMjQjVPd6k': 'file_storage/call_pcS8Ol3ZlMwwAKeMjQjVPd6k.json', 'var_call_qFyvDzDeLvA40E6T8EW7hTMj': 'file_storage/call_qFyvDzDeLvA40E6T8EW7hTMj.json'}

exec(code, env_args)
