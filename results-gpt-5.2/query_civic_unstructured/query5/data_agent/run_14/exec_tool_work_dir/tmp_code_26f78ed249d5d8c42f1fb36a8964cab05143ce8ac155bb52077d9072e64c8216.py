code = """import json, re

funding_path = var_call_vZhSPgXz3avl2bpUXXHLFg1D
with open(funding_path, 'r') as f:
    funding = json.load(f)

docs_path = var_call_uCGoq6Nx4nZ4fdLAOZ5BHvRp
with open(docs_path, 'r') as f:
    docs = json.load(f)

# Simple heuristic: disaster-related project if name contains FEMA/CalOES/CalJPIA/Woolsey/Fire/Disaster/Emergency
# Determine project start year 2022 from documents by searching for project name near 'Begin Construction:' with 2022

funding_map = {r['Project_Name']: int(r['total_amount']) for r in funding}
project_names = list(funding_map.keys())

# prefilter potential disaster projects by name
kw = re.compile(r'(FEMA|CalOES|CalJPIA|Woolsey|Fire|Disaster|Emergency)', re.IGNORECASE)
disaster_projects = [p for p in project_names if kw.search(p or '')]

# Build a regex alternation for project names (escaped) in chunks

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

started_2022 = set()
for ch in chunks(disaster_projects, 50):
    alt = '|'.join(re.escape(x) for x in ch)
    pat = re.compile(r'(?P<name>' + alt + r').{0,300}?(?:Begin Construction|Begin construction)\s*:\s*(?P<st>[^\n\r]{0,40})', re.IGNORECASE | re.DOTALL)
    for d in docs:
        text = d.get('text','') or ''
        for m in pat.finditer(text):
            st = (m.group('st') or '').strip()
            if '2022' in st:
                started_2022.add(m.group('name'))

# Sum funding

total = sum(funding_map.get(p, 0) for p in started_2022)

out = {
    'total_funding_usd': total,
    'num_disaster_projects_started_2022': len(started_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qEttvvUAYThtcowTlHEa6RiK': ['civic_docs'], 'var_call_SN9pZCUYKKDJrqXG3Wgc4Djd': ['Funding'], 'var_call_vZhSPgXz3avl2bpUXXHLFg1D': 'file_storage/call_vZhSPgXz3avl2bpUXXHLFg1D.json', 'var_call_uCGoq6Nx4nZ4fdLAOZ5BHvRp': 'file_storage/call_uCGoq6Nx4nZ4fdLAOZ5BHvRp.json'}

exec(code, env_args)
