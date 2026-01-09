code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_OG5mKrxRUa6HzkclVyHwauDM
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding aggregated by project
path_fund = var_call_GSCrnvURhXDKm8mhIi6Lg1L6
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name'].strip(): float(r['total_amount']) for r in fund if r.get('Project_Name') is not None}

spring_2022_projects = set()

# Heuristic parse: identify project blocks with "Project Schedule" and a "Begin Construction: Spring 2022" or similar
spring_pat = re.compile(r"Begin\s+Construction\s*:\s*Spring\s+2022", re.IGNORECASE)
# capture project name: nearest preceding non-empty line that is not a bullet/label
for d in docs:
    text = d.get('text','')
    if not text:
        continue
    if 'Spring 2022' not in text and 'spring 2022' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not spring_pat.search(ln):
            continue
        # walk back to find project name
        j = i-1
        proj = None
        stopwords = {'project schedule','updates','estimated schedule','project description','project updates','capital improvement projects (design)','capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects','recommended action','discussion'}
        while j >= 0:
            cand = lines[j].strip()
            if cand == '' or cand.startswith('(cid'):
                j -= 1
                continue
            lc = cand.lower().strip(':')
            if lc in stopwords or lc.startswith('page ') or lc.startswith('agenda item'):
                j -= 1
                continue
            # skip lines that look like schedule entries
            if re.search(r":\s*(spring|summer|fall|winter)\s+\d{4}$", cand, flags=re.IGNORECASE):
                j -= 1
                continue
            if cand.endswith('Project Schedule') or cand.endswith('Estimated Schedule'):
                j -= 1
                continue
            proj = cand
            break
        if proj:
            spring_2022_projects.add(proj)

# Some docs may use "Begin Design" or just "Start"; also accept "Begin construction: Spring 2022" case handled.

count = len(spring_2022_projects)

total_funding = 0.0
missing = []
for p in sorted(spring_2022_projects):
    if p in fund_map:
        total_funding += fund_map[p]
    else:
        missing.append(p)

result = {
    "projects_started_spring_2022_count": int(count),
    "total_funding_usd": int(round(total_funding)),
    "projects": sorted(spring_2022_projects),
    "projects_missing_funding_match": missing
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OG5mKrxRUa6HzkclVyHwauDM': 'file_storage/call_OG5mKrxRUa6HzkclVyHwauDM.json', 'var_call_GSCrnvURhXDKm8mhIi6Lg1L6': 'file_storage/call_GSCrnvURhXDKm8mhIi6Lg1L6.json'}

exec(code, env_args)
