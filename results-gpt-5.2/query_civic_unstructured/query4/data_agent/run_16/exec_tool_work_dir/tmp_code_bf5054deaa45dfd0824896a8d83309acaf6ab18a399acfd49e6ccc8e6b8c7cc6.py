code = """import json, re
import pandas as pd

# Load civic docs
path_docs = var_call_DnvX5ZNdhPWMsNARXybySijh
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding aggregated by project
path_fund = var_call_DU4fgVvJATGr32z2TP0P3lAc
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name'].strip(): float(r['total_amount']) for r in fund}

spring_2022_projects = set()

# Heuristic parser for agenda-style project blocks
for d in docs:
    text = d.get('text','')
    if 'Project Schedule' not in text and 'Estimated Schedule' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    in_schedule = False
    for ln in lines:
        if not ln:
            continue
        # detect project header lines (avoid bullets, page, agenda labels)
        if not ln.startswith(('(cid', 'Page ', 'Agenda ', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Capital Improvement Projects', 'Disaster Recovery Projects')):
            # likely project name: line with no colon and not too long
            if (':' not in ln) and (len(ln) <= 120) and (not ln.startswith(('Updates','Project','Complete','Advertise','Begin','Final','Estimated','City will','Staff'))):
                # Exclude generic headings
                if ln not in ('Item','4.B.','Public Works','Commission Meeting','Agenda Report'):
                    current_project = ln
                    in_schedule = False
                    continue
        if 'Project Schedule' in ln or 'Estimated Schedule' in ln:
            in_schedule = True
            continue
        if in_schedule and current_project:
            # capture begin construction line
            if re.search(r'Begin\s+Construction', ln, re.I):
                if re.search(r'\bSpring\s+2022\b', ln, re.I) or re.search(r'\bSpring\s*2022\b', ln, re.I):
                    spring_2022_projects.add(current_project)

# Sum funding for matched projects
matched = [p for p in spring_2022_projects if p in fund_map]
missing = [p for p in spring_2022_projects if p not in fund_map]

total_funding = sum(fund_map[p] for p in matched)

result = {
    "spring_2022_project_count": len(spring_2022_projects),
    "spring_2022_total_funding": int(total_funding),
    "projects": sorted(spring_2022_projects),
    "funding_matched_count": len(matched),
    "funding_missing_projects": sorted(missing)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DnvX5ZNdhPWMsNARXybySijh': 'file_storage/call_DnvX5ZNdhPWMsNARXybySijh.json', 'var_call_DU4fgVvJATGr32z2TP0P3lAc': 'file_storage/call_DU4fgVvJATGr32z2TP0P3lAc.json'}

exec(code, env_args)
