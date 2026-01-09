code = """import json, re

civic_src = var_call_tQ6djS4IuXOgjl0fxpxhx6GM
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fund_src = var_call_FZ7t7u32KMShaU4Jf6bWmwUW
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

projects = {}
begin_pat = re.compile(r"Begin\s+Construction\s*:\s*([^\n\r]+)", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','') or ''
    paras = re.split(r"\n{2,}", text)
    for i, p in enumerate(paras):
        name = p.strip()
        if not name or len(name) > 120:
            continue
        if name.endswith(':'):
            continue
        skip_headers = ['Agenda Item', 'Public Works', 'Commission', 'RECOMMENDED ACTION', 'DISCUSSION',
                        'Page ', 'To:', 'Prepared by:', 'Approved by:', 'Meeting date', 'Date prepared']
        if any(h in name for h in skip_headers):
            continue
        window = "\n\n".join(paras[i:i+8])
        m = begin_pat.search(window)
        if m:
            projects.setdefault(name, set()).add(m.group(1).strip())


def is_spring_2022(s):
    if not s:
        return False
    s_norm = s.strip()
    if re.search(r"\bSpring\b", s_norm, re.IGNORECASE) and re.search(r"\b2022\b", s_norm):
        return True
    if re.search(r"\b2022\b", s_norm) and re.search(r"\bMarch\b|\bApril\b|\bMay\b", s_norm, re.IGNORECASE):
        return True
    if re.search(r"2022\s*[-/]\s*Spring", s_norm, re.IGNORECASE) or re.search(r"Spring\s*[-/]\s*2022", s_norm, re.IGNORECASE):
        return True
    return False

spring_2022_projects = [n for n,begins in projects.items() if any(is_spring_2022(b) for b in begins)]

out = {
    'spring_2022_projects_count': len(spring_2022_projects),
    'total_funding': sum(fund_map.get(n, 0) for n in spring_2022_projects)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tQ6djS4IuXOgjl0fxpxhx6GM': 'file_storage/call_tQ6djS4IuXOgjl0fxpxhx6GM.json', 'var_call_FZ7t7u32KMShaU4Jf6bWmwUW': 'file_storage/call_FZ7t7u32KMShaU4Jf6bWmwUW.json'}

exec(code, env_args)
