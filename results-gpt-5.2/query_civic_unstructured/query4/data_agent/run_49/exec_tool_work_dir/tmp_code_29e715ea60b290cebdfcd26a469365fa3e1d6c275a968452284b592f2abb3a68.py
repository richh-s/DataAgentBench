code = """import json, re
import pandas as pd

path_docs = var_call_vqcWDfkcAaDfjGPiJi6rD5RH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_dfEo8BMPVvngO0jpqpk1sgAm
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_fund = pd.DataFrame(fund)
if not df_fund.empty:
    df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'], errors='coerce').fillna(0).astype(int)


def norm_line(s):
    return re.sub(r'\s+', ' ', s).strip()

projects = set()

for d in docs:
    text = d.get('text', '') or ''
    lines = [norm_line(l) for l in text.splitlines()]
    current_project = None
    in_block = False
    for i, l in enumerate(lines):
        if not l:
            continue

        low = l.lower()
        # candidate header line (project name)
        if (len(l) <= 120 and
            not low.startswith(('updates:', 'project schedule', 'estimated schedule', 'project description', 'project updates',
                                'recommended action', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared',
                                'meeting date', 'subject', 'page ', 'agenda item')) and
            not l.startswith(('(cid', '•', '-', '–', '—', '·')) and
            not re.fullmatch(r'[A-Z\s\(\)\-\/0-9\.]+', l)):
            nxt = ' '.join(lines[i+1:i+6]).lower() if i+1 < len(lines) else ''
            if ('updates' in nxt) or ('project description' in nxt) or ('project schedule' in nxt) or ('estimated schedule' in nxt):
                current_project = l
                in_block = True
                continue

        if in_block and current_project:
            if ('begin construction' in low) and ('spring' in low) and ('2022' in low):
                projects.add(current_project)

            # stop block when a new major section starts
            if low.startswith(('capital improvement projects', 'disaster recovery projects')):
                in_block = False
                current_project = None

if projects:
    df_proj = pd.DataFrame({'Project_Name': sorted(projects)})
    df_join = df_proj.merge(df_fund, on='Project_Name', how='left')
    df_join['total_amount'] = df_join['total_amount'].fillna(0).astype(int)
    count = int(len(df_join))
    total_funding = int(df_join['total_amount'].sum())
else:
    count = 0
    total_funding = 0

out = {
    'spring_2022_projects_count': count,
    'spring_2022_total_funding': total_funding,
    'projects_found': sorted(projects)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wh6kEpuOdcgAlJK72Hl596y6': ['Funding'], 'var_call_dfEo8BMPVvngO0jpqpk1sgAm': 'file_storage/call_dfEo8BMPVvngO0jpqpk1sgAm.json', 'var_call_vqcWDfkcAaDfjGPiJi6rD5RH': 'file_storage/call_vqcWDfkcAaDfjGPiJi6rD5RH.json'}

exec(code, env_args)
