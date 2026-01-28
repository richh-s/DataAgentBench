code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

funding = load_records(var_call_J5btMduvjEydK430NNIDRHwh)
docs = load_records(var_call_fADTy4iVTLjruzvmYAydiKhY)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Parse disaster projects and their start date strings from docs
# We'll look for "Disaster Recovery Projects" section and capture lines that look like project names,
# then within the following few lines capture 'Begin Construction:' or 'Start' indicators.

disaster_projects = {}

begin_pat = re.compile(r'\b(Begin Construction|Begin construction|Start(?: Date)?|Construction Start)\s*:\s*([^\n\r]+)', re.I)

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    # take portion after the heading
    part = text.split('Disaster Recovery Projects',1)[1]
    # limit to before next major heading if exists
    cut = re.split(r'\n\s*Capital Improvement Projects|\n\s*PUBLIC WORKS|\n\s*Page \d+ of', part, maxsplit=1)[0]
    lines = [ln.strip() for ln in cut.splitlines()]
    # project name heuristic: non-empty line not starting with bullets/parentheses, and not containing ':' and not 'Updates' etc.
    current = None
    buffer = []
    for ln in lines:
        if not ln:
            continue
        # detect new project header
        if (':' not in ln) and (len(ln) < 120) and (not re.search(r'^(\(cid|\u2022|\-|\*|Page\s+\d+)', ln)) and (ln.lower() not in ['updates','project schedule','estimated schedule','project description','project updates','final design','advertise']):
            # treat as project name if it contains typical words or parentheses suffix or title case
            if re.search(r'(Project|Repairs|Repair|Improvements|Improvement|Recovery|Drain|Culvert|Bridge|Slope|Sirens|Guardrail|Warning|Fire|FEMA|CalOES)', ln, re.I):
                current = ln
                buffer = []
                if current not in disaster_projects:
                    disaster_projects[current] = []
                continue
        if current is not None:
            buffer.append(ln)
            m = begin_pat.search(ln)
            if m:
                date_str = m.group(2).strip()
                disaster_projects[current].append(date_str)

# Decide started in 2022 if any captured begin/start date contains '2022'
started_2022 = set([p for p, dates in disaster_projects.items() if any('2022' in (dt or '') for dt in dates)])

# Also include disaster projects that are explicitly FEMA/CalOES/CalJPIA in name and appear in docs with a schedule containing 2022
# Broaden: for each disaster project section, if within 10 lines of project name we see '2022'
for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    part = text.split('Disaster Recovery Projects',1)[1]
    cut = re.split(r'\n\s*Capital Improvement Projects|\n\s*PUBLIC WORKS|\n\s*Page \d+ of', part, maxsplit=1)[0]
    lines = [ln.strip() for ln in cut.splitlines()]
    for i, ln in enumerate(lines):
        if ln and (':' not in ln) and re.search(r'(FEMA|CalOES|CalJPIA)', ln, re.I):
            window = ' '.join(lines[i:i+12])
            if '2022' in window:
                started_2022.add(ln)

# Join with funding totals
fund_started = fund_df[fund_df['Project_Name'].isin(started_2022)]

total = int(fund_started['total_amount'].sum())

out = {
    'total_funding_started_2022_disaster_projects': total,
    'project_count': int(fund_started['Project_Name'].nunique()),
    'projects': fund_started.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_J5btMduvjEydK430NNIDRHwh': 'file_storage/call_J5btMduvjEydK430NNIDRHwh.json', 'var_call_fADTy4iVTLjruzvmYAydiKhY': 'file_storage/call_fADTy4iVTLjruzvmYAydiKhY.json', 'var_call_uyLAFye59CUM94oYe8ib2EVD': ['Funding'], 'var_call_9WxSALu3LBXcZdBTz3wM0G8X': ['civic_docs']}

exec(code, env_args)
