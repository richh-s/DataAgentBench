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

# Define regex patterns without embedded newlines in the Python code string
begin_pat = re.compile(r'\b(Begin Construction|Begin construction|Start(?: Date)?|Construction Start)\s*:\s*([^\n\r]+)', re.I)
cut_pat = re.compile(r'\n\s*Capital Improvement Projects|\n\s*PUBLIC WORKS|\n\s*Page \d+ of')
header_bad_pat = re.compile(r'^\(cid|^Page\s+\d+', re.I)
header_good_kw_pat = re.compile(r'(Project|Repairs|Repair|Improvements|Improvement|Recovery|Drain|Culvert|Bridge|Slope|Sirens|Guardrail|Warning|Fire|FEMA|CalOES|CalJPIA)', re.I)

# Extract disaster projects and any begin/start date strings

disaster_projects = {}

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    part = text.split('Disaster Recovery Projects', 1)[1]
    cut = cut_pat.split(part, 1)[0]
    lines = [ln.strip() for ln in cut.splitlines()]
    current = None
    for ln in lines:
        if not ln:
            continue
        if (':' not in ln) and (len(ln) < 140) and (not header_bad_pat.search(ln)):
            if header_good_kw_pat.search(ln) and (ln.lower() not in ['updates','project schedule','estimated schedule','project description','project updates']):
                current = ln
                disaster_projects.setdefault(current, [])
                continue
        if current is not None:
            m = begin_pat.search(ln)
            if m:
                disaster_projects[current].append(m.group(2).strip())

started_2022 = set(p for p, dates in disaster_projects.items() if any('2022' in (dt or '') for dt in dates))

for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    part = text.split('Disaster Recovery Projects', 1)[1]
    cut = cut_pat.split(part, 1)[0]
    lines = [ln.strip() for ln in cut.splitlines()]
    for i, ln in enumerate(lines):
        if ln and (':' not in ln) and re.search(r'(FEMA|CalOES|CalJPIA)', ln, re.I):
            window = ' '.join(lines[i:i+12])
            if '2022' in window:
                started_2022.add(ln)

fund_started = fund_df[fund_df['Project_Name'].isin(started_2022)].copy()

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
