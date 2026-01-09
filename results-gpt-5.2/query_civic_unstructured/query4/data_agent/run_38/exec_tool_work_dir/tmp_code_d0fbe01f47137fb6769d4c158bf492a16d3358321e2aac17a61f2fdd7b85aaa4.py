code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

docs = load_records(var_call_elk8iAEI5OvQ2IeaCJ45WP21)
fund = load_records(var_call_n7M6PeXEXsXyKEWGkvHR8dc6)

# Build funding map
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

spring_markers = [
    'spring 2022','spring, 2022','2022-spring','2022 spring','spring\u00a02022','spring\t2022'
]

# Extract project blocks with schedule lines
started_projects = set()

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # look for project headings and schedule lines
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    for ln in lines:
        # identify potential project name lines (heuristic): not empty, not bullet, title case-ish, and not common headers
        if ln and len(ln) < 120 and not ln.startswith(('(','cid:','Page','Agenda','To:','Prepared','Approved','Date prepared','Meeting date','Subject','RECOMMENDED','DISCUSSION','Capital Improvement','Disaster Recovery','Project Schedule','Estimated Schedule','Updates','Project Description','Project Updates')):
            # if line doesn't contain ':' and has letters and is not just a sentence
            if ':' not in ln and re.search(r'[A-Za-z]', ln) and not ln.endswith('.'):
                # many project names include 'Project' etc
                if any(k in ln for k in ['Project','Repairs','Repair','Improvements','Improvement','Plan','Facility','Park','Signals','Resurfacing','Study','Screens','Skate','Water','Drain','Slope','Bridge','Culvert','Biofilter','Backup Power','Right Turn Lane','Warning']):
                    current_project = ln
        # capture start markers like Begin Construction/Start etc
        if current_project:
            lnl = ln.lower()
            if ('begin' in lnl or 'start' in lnl) and 'construction' in lnl:
                if any(m in lnl for m in spring_markers):
                    started_projects.add(current_project)
            # sometimes schedule is 'Advertise: Spring 2022' etc; count as started? question: projects started in Spring 2022 => use begin construction.

# Join with funding
projects_with_funding = [(p, fund_map.get(p, 0)) for p in sorted(started_projects)]
count = len(started_projects)
total_funding = int(sum(a for _,a in projects_with_funding))

out = {
    'projects_started_spring_2022_count': count,
    'total_funding_amount': total_funding,
    'projects': projects_with_funding
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jbSq8uqjDy5yRsEZs6MFdCX2': ['Funding'], 'var_call_elk8iAEI5OvQ2IeaCJ45WP21': 'file_storage/call_elk8iAEI5OvQ2IeaCJ45WP21.json', 'var_call_n7M6PeXEXsXyKEWGkvHR8dc6': 'file_storage/call_n7M6PeXEXsXyKEWGkvHR8dc6.json'}

exec(code, env_args)
