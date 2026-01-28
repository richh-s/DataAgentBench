code = """import json, re
import pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_dGtesJIXNNNsfONCBsfnBBgu)
funding = load_maybe_path(var_call_GDGSfAI3qBmWEhKepTKF28OD)

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Minimal name pattern: line starts with uppercase/number and length>=4
name_pat = re.compile(r"^([A-Z0-9][A-Za-z0-9/&\-\'\.,\(\) ]{3,})$")

spring2022_pat = re.compile(r"Spring\s+2022|2022\s*[-/]\s*Spring", re.IGNORECASE)
begin_pat = re.compile(r"\b(Begin|Start|Started)\b", re.IGNORECASE)

projects_spring2022 = set()

for d in docs:
    lines = [(ln or '').strip() for ln in (d.get('text','') or '').splitlines()]
    for i, ln in enumerate(lines):
        if not ln or ln.startswith('(') or ln.lower().startswith('page ') or 'Agenda Item' in ln:
            continue
        m = name_pat.match(ln)
        if not m:
            continue
        name = m.group(1).strip()
        window = "\n".join(lines[i:i+18])
        if spring2022_pat.search(window) and begin_pat.search(window):
            projects_spring2022.add(name)

fund_total = sum(int(fund_map.get(p, 0)) for p in projects_spring2022)

result = {
    'projects_started_spring_2022_count': int(len(projects_spring2022)),
    'total_funding_usd': int(fund_total)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dGtesJIXNNNsfONCBsfnBBgu': 'file_storage/call_dGtesJIXNNNsfONCBsfnBBgu.json', 'var_call_GDGSfAI3qBmWEhKepTKF28OD': 'file_storage/call_GDGSfAI3qBmWEhKepTKF28OD.json'}

exec(code, env_args)
