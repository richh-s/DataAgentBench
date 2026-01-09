code = """import json, re
import pandas as pd

def load_json_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_json_maybe_path(var_call_xVHLNlkl7NhAAKUdKQsBsvoQ)
docs = load_json_maybe_path(var_call_6neKI2D2f3w76geKxf2wQCYH)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# Heuristic parsing: from each doc, capture Disaster Recovery Projects section and extract project names and schedules
project_info = {}

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    # take substring starting at Disaster Recovery Projects
    idx = text.find('Disaster Recovery Projects')
    sub = text[idx:]
    # stop at next major header if present
    mstop = re.search(r'\n\s*Capital Improvement Projects\b', sub)
    if mstop and mstop.start() > 0:
        sub = sub[:mstop.start()]

    # project name lines: assume non-empty lines not starting with bullets and not containing ':' and not like 'Page'
    lines = [ln.strip() for ln in sub.splitlines()]
    # find candidates: title-case lines without too many words? We'll use funding names to match directly via substring
    for pname in fund_df['Project_Name']:
        if pname in project_info:
            continue
        if pname in sub:
            # find a nearby schedule block containing Begin Construction or Start
            # extract window around first occurrence
            pos = sub.find(pname)
            window = sub[pos:pos+800]
            # look for start-ish date strings containing 2022 near 'Begin' or 'Start'
            started_2022 = False
            # common patterns
            if re.search(r'Begin\s+Construction\s*:\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            if re.search(r'Begin\s*[:\-]\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            if re.search(r'Start\s*[:\-]\s*[^\n]*2022', window, flags=re.I):
                started_2022 = True
            # also allow construction completed in 2022 but no begin; not counted
            project_info[pname] = {'disaster': True, 'started_2022': started_2022}

# Disaster projects that started in 2022
started_2022_projects = [p for p,info in project_info.items() if info.get('disaster') and info.get('started_2022')]

# Sum funding for these projects
sum_amount = fund_df[fund_df['Project_Name'].isin(started_2022_projects)]['total_amount'].sum()

out = {
    'total_funding': int(sum_amount),
    'currency': 'USD',
    'project_count': int(len(started_2022_projects)),
    'projects': started_2022_projects[:50]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xVHLNlkl7NhAAKUdKQsBsvoQ': 'file_storage/call_xVHLNlkl7NhAAKUdKQsBsvoQ.json', 'var_call_6neKI2D2f3w76geKxf2wQCYH': 'file_storage/call_6neKI2D2f3w76geKxf2wQCYH.json'}

exec(code, env_args)
