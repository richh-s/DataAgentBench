code = """import json, re

funding_path = var_call_vZhSPgXz3avl2bpUXXHLFg1D
with open(funding_path, 'r') as f:
    funding = json.load(f)

docs_path = var_call_uCGoq6Nx4nZ4fdLAOZ5BHvRp
with open(docs_path, 'r') as f:
    docs = json.load(f)

proj_to_start = {}

section_pat = re.compile(r'Disaster Recovery Projects\b.*?(?=\n\s*Staff has also prepared|\Z)', re.IGNORECASE | re.DOTALL)
name_pat = re.compile(r'^(?!\s*(?:\(cid:|Updates:|Project Description:|Project Updates:|Project Schedule:|Estimated Schedule:|Complete Design:|Final Design:|Advertise:|Begin Construction:|Complete Construction:|Begin construction:|Construction was|On \w+ \d{1,2}, \d{4}|Page \d+ of \d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION)).{3,200}$')
start_pat = re.compile(r'\b(?:Begin Construction|Begin construction|Start|Begin)\s*:\s*([^\n\r]+)', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    msec = section_pat.search(text)
    if not msec:
        continue
    sec = msec.group(0)
    lines = [ln.strip() for ln in sec.splitlines()]
    current_name = None
    for ln in lines:
        if not ln:
            continue
        if name_pat.match(ln) and not ln.lower().startswith('disaster recovery projects'):
            current_name = ln
            continue
        if current_name:
            sm = start_pat.search(ln)
            if sm:
                st = sm.group(1).strip()
                proj_to_start.setdefault(current_name, st)

projects_2022 = {p for p, st in proj_to_start.items() if '2022' in (st or '')}
funding_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

total = sum(funding_map.get(p, 0) for p in projects_2022)

out = {
    'total_funding_usd': total,
    'num_disaster_projects_started_2022': len(projects_2022),
    'projects': sorted(projects_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qEttvvUAYThtcowTlHEa6RiK': ['civic_docs'], 'var_call_SN9pZCUYKKDJrqXG3Wgc4Djd': ['Funding'], 'var_call_vZhSPgXz3avl2bpUXXHLFg1D': 'file_storage/call_vZhSPgXz3avl2bpUXXHLFg1D.json', 'var_call_uCGoq6Nx4nZ4fdLAOZ5BHvRp': 'file_storage/call_uCGoq6Nx4nZ4fdLAOZ5BHvRp.json'}

exec(code, env_args)
