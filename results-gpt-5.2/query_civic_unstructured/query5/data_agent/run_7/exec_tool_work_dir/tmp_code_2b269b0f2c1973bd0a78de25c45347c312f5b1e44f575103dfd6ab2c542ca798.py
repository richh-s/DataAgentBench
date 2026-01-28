code = """import json, re
import pandas as pd

def load_tool_result(var):
    # var can be list (already loaded) or file path string
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_tool_result(var_call_GkieIoQMVqz5qVMMds0l1Ppd)
funding = load_tool_result(var_call_mdLht1QiCpWJ3oLGa4nFNsnz)

# Extract Disaster Recovery Projects section and project names with schedules that include 2022 as start indicator.
project_starts_2022 = set()

year_pat = re.compile(r"\b2022\b")

for d in docs:
    text = d.get('text','')
    # isolate disaster section
    m = re.search(r"Disaster Recovery Projects(.*)", text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        continue
    section = m.group(1)
    # stop at next major section if present
    stop = re.search(r"\n\s*(Capital Improvement Projects|Staff has also prepared|Public Works Quarterly|Page \d+ of \d+|Agenda Item)\b", section, flags=re.IGNORECASE)
    if stop:
        section = section[:stop.start()]

    lines = [ln.strip() for ln in section.splitlines()]

    # project heading heuristic: a line with letters and not starting with bullet characters, followed later by 'Project Schedule' block
    for i, ln in enumerate(lines):
        if not ln or ln.lower().startswith(('updates','project schedule','estimated schedule','project description','discussion')):
            continue
        if any(tok in ln for tok in ['(cid:', 'Page', 'Agenda Item', 'RECOMMENDED ACTION']):
            continue
        # candidate project name lines often have no colon
        if ':' in ln:
            continue
        # Look ahead for schedule lines containing 2022 within next 25 lines
        window = "\n".join(lines[i:i+30])
        if re.search(r"Project Schedule|Estimated Schedule", window, flags=re.IGNORECASE) and year_pat.search(window):
            # require that 2022 appears on a line indicating start e.g., Begin Construction/Start/Advertise etc.
            # We'll accept any occurrence of 2022 in schedule as start year since question asks started in 2022 and docs usually list schedule milestones.
            project_starts_2022.add(ln)

# As fallback, if none found, broader heuristic: any disaster project name line that contains 2022 near it.
if not project_starts_2022:
    for d in docs:
        text = d.get('text','')
        if 'Disaster Recovery Projects' not in text:
            continue
        section = text.split('Disaster Recovery Projects',1)[1]
        for line in section.splitlines():
            if year_pat.search(line):
                # try grab previous non-empty line as project name
                # simplistic: skip
                pass

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Match funding Project_Name exactly with extracted names.
matched = fund_df[fund_df['Project_Name'].isin(sorted(project_starts_2022))]

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
