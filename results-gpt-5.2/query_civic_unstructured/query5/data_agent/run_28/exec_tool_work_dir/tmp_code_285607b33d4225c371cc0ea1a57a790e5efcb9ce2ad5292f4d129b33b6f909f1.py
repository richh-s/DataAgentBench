code = """import json, re
import pandas as pd

# funding
with open(var_call_E3A3KNZAloQm34K4K1JvVvyY,'r') as f:
    funding = json.load(f)
df_f = pd.DataFrame(funding)
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# docs with Disaster Projects
with open(var_call_tvobrBCauIeEF7HgXhjZu1Qp,'r') as f:
    docs = json.load(f)

begin_pat = re.compile(r'^(Begin Construction|Begin Design|Award Contract and Begin Construction):\s*(.*)$', re.I)
header_pat = re.compile(r'^Disaster Projects', re.I)
section_end_pat = re.compile(r'^Capital Improvement Projects', re.I)

projects_started_2022 = set()

for d in docs:
    lines = [ln.rstrip() for ln in d.get('text','').splitlines()]
    in_disaster = False
    current = None
    for ln in lines:
        s = ln.strip()
        if header_pat.search(s):
            in_disaster = True
            current = None
            continue
        if in_disaster and section_end_pat.search(s):
            in_disaster = False
            current = None
            continue
        if not in_disaster:
            continue
        # skip empty and bullets
        if not s or s.startswith('(cid'):
            continue
        m = begin_pat.match(s)
        if m and current:
            if '2022' in m.group(2):
                projects_started_2022.add(current)
            continue
        # identify title: line with no colon, not common labels
        if ':' not in s and not re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)\b', s, re.I):
            if len(s) < 120 and not re.match(r'^(Page\s+\d+\s+of\s+\d+|Agenda Item)', s):
                current = s

# join
matched = df_f[df_f['Project_Name'].isin(projects_started_2022)].groupby('Project_Name', as_index=False)['Amount'].sum()

total = int(matched['Amount'].sum()) if not matched.empty else 0

out = {
    'total_funding_amount_usd': total,
    'projects_started_2022': sorted(projects_started_2022),
    'matched_projects': matched.sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cguj2JY470StqtvTJdpADgC5': ['Funding'], 'var_call_E3A3KNZAloQm34K4K1JvVvyY': 'file_storage/call_E3A3KNZAloQm34K4K1JvVvyY.json', 'var_call_JESPpTsMF7CJnZLezqHiSbmp': 'file_storage/call_JESPpTsMF7CJnZLezqHiSbmp.json', 'var_call_jtmPqoYIzrjKo9fcalJWNbHi': {'total_funding_amount_usd': 0, 'num_disaster_projects_started_2022_with_funding_match': 0, 'matched_projects': [], 'extracted_disaster_projects_started_2022': [], 'num_extracted_disaster_projects_started_2022': 0}, 'var_call_tvobrBCauIeEF7HgXhjZu1Qp': 'file_storage/call_tvobrBCauIeEF7HgXhjZu1Qp.json'}

exec(code, env_args)
