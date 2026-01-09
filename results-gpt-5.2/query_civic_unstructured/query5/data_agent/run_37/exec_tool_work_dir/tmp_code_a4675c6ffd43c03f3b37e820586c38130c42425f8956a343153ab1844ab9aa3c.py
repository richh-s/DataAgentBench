code = """import json, re, pandas as pd
from pathlib import Path

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        return json.loads(Path(path_or_obj).read_text())
    return path_or_obj

funding = load_json_maybe(var_call_GCrz7PZzTsfBZVJ15IQgHB5f)
docs = load_json_maybe(var_call_rg2So0OGkK4XssNZ4JbiVkKf)

fund_map = {r['Project_Name']: float(r['total_amount']) for r in funding}

# parse each doc for Disaster Recovery Projects block and extract project names with schedules
results = []
for d in docs:
    text = d.get('text','')
    # isolate disaster section if present
    # common header: "Disaster Recovery Projects" followed by blocks and then maybe next section
    m = re.search(r"Disaster Recovery Projects.*?(?=\n\s*Capital Improvement Projects|\n\s*Public Works Quarterly|\Z)", text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    sec = m.group(0)
    # split into candidate project blocks by blank lines with title-like line
    lines = [ln.strip() for ln in sec.splitlines()]
    # find indices of lines that look like project titles: non-empty, not bullets, not 'Updates' etc.
    title_idx = []
    bad = set(['disaster recovery projects','disaster recovery project','recommended action','discussion','project schedule','updates','page'])
    for i, ln in enumerate(lines):
        if not ln:
            continue
        lnl = ln.lower()
        if any(lnl.startswith(b) for b in ['(cid', '•','-','']):
            continue
        if lnl in bad or lnl.startswith('page '):
            continue
        # heuristic: title line with no ':' and not too long
        if ':' in ln:
            continue
        if len(ln) > 120:
            continue
        # exclude generic phrases
        if 'agenda' in lnl and 'item' in lnl:
            continue
        # likely title if contains keyword like FEMA/CalOES/CalJPIA or common project words
        if re.search(r"\b(FEMA|CalOES|CalJPIA|fire|storm|culvert|drain|bridge|slope|retaining|sirens|warning)\b", ln, flags=re.I):
            title_idx.append(i)
    # deduplicate consecutive
    title_idx2=[]
    for i in title_idx:
        if not title_idx2 or i-title_idx2[-1]>1:
            title_idx2.append(i)
    title_idx=title_idx2
    for j, i in enumerate(title_idx):
        title = lines[i]
        end = title_idx[j+1] if j+1 < len(title_idx) else len(lines)
        block = "\n".join(lines[i:end])
        # find start markers, typical: Begin Construction: <date> or Start: <date>
        st = None
        # capture Begin Construction
        m2 = re.search(r"Begin Construction\s*:\s*([^\n]+)", block, flags=re.I)
        if m2:
            st = m2.group(1).strip()
        else:
            m3 = re.search(r"Start(?: Date)?\s*:\s*([^\n]+)", block, flags=re.I)
            if m3:
                st = m3.group(1).strip()
        if st and '2022' in st:
            results.append(title)

# match extracted titles to funding project names.
# Use exact match first, then fuzzy by removing extra spaces and normalizing parentheses spacing.

def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())

fund_norm = {norm(k): k for k in fund_map.keys()}
matched=[]
for title in results:
    nt = norm(title)
    if nt in fund_norm:
        matched.append(fund_norm[nt])
        continue
    # try contains match: funding name that startswith title or vice versa
    best=None
    for fn, orig in fund_norm.items():
        if fn.startswith(nt) or nt.startswith(fn):
            best=orig
            break
    if best:
        matched.append(best)

matched_unique = sorted(set(matched))

total = sum(fund_map.get(p,0.0) for p in matched_unique)

out = {
    "total_funding": int(round(total)),
    "matched_project_count": len(matched_unique),
    "projects": matched_unique
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NBSUCTIM9JLMEB37N0JQuCuN': ['Funding'], 'var_call_TdUCedLY6IGaC3oOgBBiqt7o': ['civic_docs'], 'var_call_GCrz7PZzTsfBZVJ15IQgHB5f': 'file_storage/call_GCrz7PZzTsfBZVJ15IQgHB5f.json', 'var_call_rg2So0OGkK4XssNZ4JbiVkKf': 'file_storage/call_rg2So0OGkK4XssNZ4JbiVkKf.json'}

exec(code, env_args)
