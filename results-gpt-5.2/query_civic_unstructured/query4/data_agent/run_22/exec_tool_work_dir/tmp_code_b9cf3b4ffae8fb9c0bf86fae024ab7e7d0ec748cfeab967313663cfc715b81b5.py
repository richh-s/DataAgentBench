code = """import json, re, pandas as pd

# load mongo docs
mongo_path = var_call_p4HjSnYNUxe7NkRmq3vzuPCA
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding aggregation per project
fund_path = var_call_oek2bn0tTBOuFoCdVj0yWRYv
with open(fund_path, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: float(r['Total_Amount']) for r in fund}

# extract project names and their schedule lines from docs
# heuristic: project blocks start with a line that matches a known funded project name, then search nearby for 'Begin' or 'Start' schedule mentioning Spring 2022.
project_started_spring_2022 = set()

# precompile regexes
spring2022_re = re.compile(r"\bSpring\s+2022\b|\b2022\s*[-, ]\s*Spring\b", re.IGNORECASE)
start_re = re.compile(r"\b(Begin(ning)?|Start(ing)?)\b", re.IGNORECASE)

funded_names = sorted(fund_map.keys(), key=len, reverse=True)

for d in docs:
    text = d.get('text','') or ''
    if not text:
        continue
    # normalize whitespace
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # exact match on funded project name (case sensitive as in funding list) OR loose match
        # prefer exact
        name = None
        if ln in fund_map:
            name = ln
        else:
            # some docs may have extra bullets; try strip bullets and match
            ln2 = re.sub(r'^[\(\[]?cid:[^)\]]+[\)\]]\s*', '', ln)
            ln2 = re.sub(r'^[•\-*]+\s*','',ln2)
            if ln2 in fund_map:
                name = ln2
        if not name:
            continue
        # scan window of next 25 lines for begin/start and Spring 2022
        window = "\n".join(lines[i:i+30])
        if spring2022_re.search(window) and (re.search(r"Begin\s+Construction\s*:\s*Spring\s+2022", window, re.IGNORECASE) or re.search(r"Begin\s*:\s*Spring\s+2022", window, re.IGNORECASE) or re.search(r"Start\s*:\s*Spring\s+2022", window, re.IGNORECASE) or re.search(r"Begin\s+Design\s*:\s*Spring\s+2022", window, re.IGNORECASE) or re.search(r"Start\s+Design\s*:\s*Spring\s+2022", window, re.IGNORECASE)):
            project_started_spring_2022.add(name)

count = len(project_started_spring_2022)
total_funding = sum(fund_map.get(n,0.0) for n in project_started_spring_2022)

result = {
    "projects_started_spring_2022_count": count,
    "projects_started_spring_2022_total_funding": int(total_funding),
    "projects": sorted(project_started_spring_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_p4HjSnYNUxe7NkRmq3vzuPCA': 'file_storage/call_p4HjSnYNUxe7NkRmq3vzuPCA.json', 'var_call_oek2bn0tTBOuFoCdVj0yWRYv': 'file_storage/call_oek2bn0tTBOuFoCdVj0yWRYv.json'}

exec(code, env_args)
