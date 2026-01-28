code = """import json

with open(var_call_BluEeKeRlnhnPiwlKGMEmLEa, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_jPItYFKSpJ9uZinUyW91jl6C, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

fund_map = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        fund_map[name] = int(amt)
    except:
        s = ''.join(ch for ch in str(amt) if ch.isdigit())
        fund_map[name] = int(s) if s else 0

projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'begin construction' in low:
            # look backwards for a non-empty candidate title
            title = None
            j = i-1
            while j >= 0:
                cand = lines[j].strip()
                if cand:
                    # filter out obvious metadata
                    cl = cand.lower()
                    if cl.startswith('project schedule') or cl.startswith('updates') or cl.startswith('page'):
                        j -= 1
                        continue
                    title = cand
                    break
                j -= 1
            if title:
                if title.lower() not in [p.lower() for p in projects]:
                    projects.append(title)

# Also check for 'begin construction: spring' mention in same line
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'spring' in low and '2022' in low:
            # find nearest title above
            title = None
            j = i-1
            while j >= 0:
                cand = lines[j].strip()
                if cand:
                    cl = cand.lower()
                    if cl.startswith('project schedule') or cl.startswith('updates') or cl.startswith('page'):
                        j -= 1
                        continue
                    title = cand
                    break
                j -= 1
            if title and title.lower() not in [p.lower() for p in projects]:
                projects.append(title)

# Clean simple decorations
cleaned = []
for p in projects:
    cp = p.replace('\ufeff','').strip()
    if cp:
        cleaned.append(cp)

# Match to funding
matched = []
unmatched = []
for p in cleaned:
    pl = p.lower()
    found = False
    for fk in fund_map:
        if not fk:
            continue
        fk_l = fk.lower()
        if fk_l == pl or pl in fk_l or fk_l in pl:
            matched.append(fk)
            found = True
            break
    if not found:
        unmatched.append(p)

total = sum(fund_map[k] for k in matched)

result = {
    'count_projects_started_spring_2022': len(cleaned),
    'total_matched_funding': total,
    'extracted_projects': cleaned,
    'matched_funding_projects': sorted(matched),
    'unmatched_projects': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cJibmufZIbpLLOJoY7hsw2Qi': ['civic_docs'], 'var_call_BluEeKeRlnhnPiwlKGMEmLEa': 'file_storage/call_BluEeKeRlnhnPiwlKGMEmLEa.json', 'var_call_jPItYFKSpJ9uZinUyW91jl6C': 'file_storage/call_jPItYFKSpJ9uZinUyW91jl6C.json'}

exec(code, env_args)
