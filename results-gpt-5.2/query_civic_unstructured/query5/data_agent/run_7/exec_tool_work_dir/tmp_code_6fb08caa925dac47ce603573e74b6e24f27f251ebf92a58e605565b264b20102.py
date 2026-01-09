code = """import json, re
import pandas as pd

def load_tool_result(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_tool_result(var_call_GkieIoQMVqz5qVMMds0l1Ppd)
funding = load_tool_result(var_call_mdLht1QiCpWJ3oLGa4nFNsnz)

project_starts_2022 = set()
year_pat = re.compile(r"\b2022\b")

for d in docs:
    text = d.get('text','') or ''
    m = re.search(r"Disaster Recovery Projects(.*)", text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    section = m.group(1)
    stop = re.search(r"\n\s*(Capital Improvement Projects|Staff has also prepared|Public Works Quarterly Update|\f|$)", section, flags=re.IGNORECASE)
    if stop:
        section = section[:stop.start()]

    lines = [ln.strip() for ln in section.splitlines()]

    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        if low.startswith(('updates','project schedule','estimated schedule','project description','discussion','recommended action')):
            continue
        if '(cid:' in ln or ln.startswith('Page') or 'Agenda Item' in ln:
            continue
        if ':' in ln:
            continue
        window = "\n".join(lines[i:i+30])
        if re.search(r"Project Schedule|Estimated Schedule", window, flags=re.IGNORECASE) and year_pat.search(window):
            project_starts_2022.add(ln)

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

matched = fund_df[fund_df['Project_Name'].isin(project_starts_2022)].copy()

total = int(matched['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_project_count': int(matched.shape[0]),
    'matched_projects': matched[['Project_Name','total_amount']].to_dict(orient='records'),
    'extracted_project_names_started_2022': sorted(project_starts_2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GkieIoQMVqz5qVMMds0l1Ppd': 'file_storage/call_GkieIoQMVqz5qVMMds0l1Ppd.json', 'var_call_mdLht1QiCpWJ3oLGa4nFNsnz': 'file_storage/call_mdLht1QiCpWJ3oLGa4nFNsnz.json'}

exec(code, env_args)
