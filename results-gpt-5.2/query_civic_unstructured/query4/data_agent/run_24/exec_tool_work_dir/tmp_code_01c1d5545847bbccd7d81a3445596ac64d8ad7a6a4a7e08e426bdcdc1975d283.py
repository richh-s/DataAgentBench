code = """import json, re, pandas as pd

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json(var_call_G9FvFKVmQyBnS5piqmegy6Pu)
fund = load_json(var_call_spqE39mHBXAXiUZuGuXHx2Mw)

# Build funding map
fund_map = {}
for r in fund:
    name = r.get('Project_Name')
    amt = r.get('total_amount')
    try:
        amt = int(amt)
    except Exception:
        try:
            amt = int(float(amt))
        except Exception:
            amt = 0
    fund_map[name] = fund_map.get(name, 0) + amt

# Extract project schedule start dates from documents.
# Heuristic: project header line followed by 'Project Schedule'/'Estimated Schedule' block containing lines with ':'
# We only need projects whose schedule has a line like 'Begin Construction: Spring 2022' or 'Start ...: Spring 2022'

season_pat = re.compile(r'\bSpring\s+2022\b', re.IGNORECASE)

# candidate project names from funding table help match headers
fund_names_sorted = sorted(fund_map.keys(), key=len, reverse=True)

started_projects = set()

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # quick filter
    if 'Spring 2022' not in text and 'SPRING 2022' not in text and 'spring 2022' not in text:
        continue

    # Normalize line breaks
    lines = [ln.strip() for ln in text.splitlines()]
    # Create an index for quick lookup of exact header lines
    # We'll scan for schedule lines containing Spring 2022 and walk upwards to find nearest project name line matching funding names
    for i, ln in enumerate(lines):
        if not season_pat.search(ln):
            continue
        # Require it's a start milestone line
        if ':' not in ln:
            continue
        if not re.search(r'\b(Begin|Start|Advertise|Bid|Construction Start|NTP|Issue)\b', ln, re.IGNORECASE):
            # still might be 'Complete Design: Spring 2022' - ignore
            continue
        # We interpret 'started in Spring 2022' as project schedule start/begin construction in Spring 2022
        if not re.search(r'\b(Begin|Start)\b', ln, re.IGNORECASE):
            continue
        # Find project name above within previous 15 lines that matches a funding project name exactly
        window = lines[max(0,i-25):i]
        # also include potential bold-less headers (no bullets)
        found = None
        for back_ln in reversed(window):
            bl = back_ln.strip(' \t\u2022\u00b7\uf0b7(cid:190)(cid:131)')
            # skip empties and label lines
            if not bl or bl.lower().startswith(('project schedule','estimated schedule','updates','project description','capital improvement projects','disaster recovery projects','discussion','recommended action')):
                continue
            # direct match
            if bl in fund_map:
                found = bl
                break
        if not found:
            # try substring match against fund names for a line that looks like a project title
            for back_ln in reversed(window):
                bl = back_ln.strip(' \t\u2022\u00b7\uf0b7(cid:190)(cid:131)')
                if not bl or len(bl) < 4:
                    continue
                for nm in fund_names_sorted[:500]:  # limit for speed
                    if nm and nm in bl:
                        found = nm
                        break
                if found:
                    break
        if found:
            started_projects.add(found)

# Compute totals
count = len(started_projects)
total_funding = sum(fund_map.get(p,0) for p in started_projects)

out = {
    "projects_started_spring_2022_count": count,
    "projects_started_spring_2022_total_funding": total_funding,
    "projects": sorted(started_projects)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iPP9xubXEqIh9dJIQQcqEDq9': ['Funding'], 'var_call_G9FvFKVmQyBnS5piqmegy6Pu': 'file_storage/call_G9FvFKVmQyBnS5piqmegy6Pu.json', 'var_call_spqE39mHBXAXiUZuGuXHx2Mw': 'file_storage/call_spqE39mHBXAXiUZuGuXHx2Mw.json'}

exec(code, env_args)
