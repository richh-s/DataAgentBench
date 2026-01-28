code = """import json, re, pandas as pd

# Load civic docs
civic_src = var_call_2t22R3UaX4Znxt0xz8fGYIAP
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding per project
fund_src = var_call_CAVbt0EfwT8uPhTQKJt2uLzX
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}
project_names = sorted(fund_map.keys(), key=len, reverse=True)

# Identify projects that started in Spring 2022 by searching for schedule lines.
# Heuristic: within ~250 chars after project name, find 'Begin' or 'Start' and 'Spring 2022' (or 'Spring, 2022' etc)
start_spring_2022 = set()

def norm(s):
    return re.sub(r'\s+', ' ', s)

spring_pat = re.compile(r"\bSpring\s*,?\s*2022\b", re.IGNORECASE)
begin_pat = re.compile(r"\b(Begin|Start)(?:\s+Construction|\s+Work|\s+Design|\s+Project)?\s*:\s*", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    t = text
    for pn in project_names:
        # quick containment check
        if pn not in t:
            continue
        for m in re.finditer(re.escape(pn), t):
            window = t[m.start(): m.start()+400]  # lookahead window
            if spring_pat.search(window) and begin_pat.search(window):
                start_spring_2022.add(pn)
                break

count_projects = len(start_spring_2022)
total_funding = sum(fund_map.get(p,0) for p in start_spring_2022)

out = {
    "projects_started_spring_2022_count": count_projects,
    "projects_started_spring_2022_total_funding": total_funding,
    "projects": sorted(start_spring_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KGer4GH8D7ZnCWgfNaReubzl': ['Funding'], 'var_call_2t22R3UaX4Znxt0xz8fGYIAP': 'file_storage/call_2t22R3UaX4Znxt0xz8fGYIAP.json', 'var_call_CAVbt0EfwT8uPhTQKJt2uLzX': 'file_storage/call_CAVbt0EfwT8uPhTQKJt2uLzX.json'}

exec(code, env_args)
