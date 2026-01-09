code = """import json, re, pandas as pd

path_docs = var_call_stLTAlnZKaVMrSFSE0TWNscH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_funding = var_call_f6sEqVQUCGI0kANW1XaoTmoW
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

text_all = "\n".join(d.get('text','') for d in docs)

m = re.search(r"Disaster\s+Recovery\s+Projects(?:\s*\(.*?\))?\s*\n(?P<section>.*)", text_all, flags=re.IGNORECASE|re.DOTALL)
section = m.group('section') if m else text_all

for cm in [r"Staff has also", r"Public Works Quarterly", r"RECOMMENDED ACTION"]:
    m2 = re.search(cm, section, flags=re.IGNORECASE)
    if m2:
        section = section[:m2.start()]
        break

def parse_projects_with_start(section_text):
    lines = [ln.strip() for ln in section_text.splitlines()]
    projects = []
    current = None
    for ln in lines:
        if not ln:
            continue
        if ln.startswith('(cid') or ln.startswith('•') or ln.startswith('-'):
            if current:
                current['block'] += ln + "\\n"
            continue
        is_label = bool(re.match(r"^(Updates|Project Schedule|Estimated Schedule|Project Description)\\b", ln, flags=re.IGNORECASE))
        if (not is_label) and len(ln) < 120 and (':' not in ln) and re.search(r"Project|Repairs|Repair|Improvements|Stabilization|Warning|Drain|Culvert|Bridge|Slope", ln, flags=re.IGNORECASE):
            if re.match(r"^(Design|Construction|Not Started)$", ln, flags=re.IGNORECASE):
                continue
            if current:
                projects.append(current)
            current = {'Project_Name': ln, 'block': ''}
            continue
        if current:
            current['block'] += ln + "\\n"
    if current:
        projects.append(current)

    for p in projects:
        blk = p['block']
        st = None
        mm = re.search(r"Begin\\s+Construction\\s*:\\s*([^\\n\\r]+)", blk, flags=re.IGNORECASE)
        if mm:
            st = mm.group(1).strip()
        else:
            mm = re.search(r"Start\\s*(?:Date)?\\s*:\\s*([^\\n\\r]+)", blk, flags=re.IGNORECASE)
            if mm:
                st = mm.group(1).strip()
        p['st'] = st
    return projects

proj_df = pd.DataFrame(parse_projects_with_start(section))
if proj_df.empty:
    started_2022 = proj_df
else:
    started_2022 = proj_df[proj_df['st'].fillna('').str.contains('2022', case=False, na=False)].copy()

if started_2022.empty or fund_df.empty:
    total = 0
else:
    merged = started_2022.merge(fund_df, on='Project_Name', how='left')
    total = int(merged['total_amount'].fillna(0).sum())

result = {
    'total_funding_disaster_projects_started_2022': total,
    'projects_count': int(started_2022.shape[0]) if hasattr(started_2022, 'shape') else 0,
    'projects': started_2022['Project_Name'].tolist() if (hasattr(started_2022,'empty') and (not started_2022.empty)) else []
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_stLTAlnZKaVMrSFSE0TWNscH': 'file_storage/call_stLTAlnZKaVMrSFSE0TWNscH.json', 'var_call_f6sEqVQUCGI0kANW1XaoTmoW': 'file_storage/call_f6sEqVQUCGI0kANW1XaoTmoW.json'}

exec(code, env_args)
