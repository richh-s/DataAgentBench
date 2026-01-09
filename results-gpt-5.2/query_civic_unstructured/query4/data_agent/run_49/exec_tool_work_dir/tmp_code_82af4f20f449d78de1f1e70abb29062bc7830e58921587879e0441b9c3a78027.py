code = """import json, re
import pandas as pd

# load civic docs
path_docs = var_call_vqcWDfkcAaDfjGPiJi6rD5RH
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding totals by project
path_fund = var_call_dfEo8BMPVvngO0jpqpk1sgAm
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

df_fund = pd.DataFrame(fund)
if not df_fund.empty:
    df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'], errors='coerce').fillna(0).astype(int)

# extract project names whose schedule includes start in Spring 2022
# heuristic: within a section describing a project, find line 'Project Schedule'/'Estimated Schedule' and then a line containing 'Begin Construction:' and 'Spring 2022'
projects = set()

proj_header_re = re.compile(r'^\s*([A-Za-z0-9][A-Za-z0-9\-&/\',\(\)\.]*(?:\s+[A-Za-z0-9][A-Za-z0-9\-&/\',\(\)\.]*)*)\s*$')
# more permissive: capture non-empty line without bullets/labels

def norm_line(s):
    return re.sub(r'\s+', ' ', s).strip()

for d in docs:
    text = d.get('text','')
    lines = [norm_line(l) for l in text.splitlines()]
    current_project = None
    in_project_block = False
    for i,l in enumerate(lines):
        if not l:
            continue
        # detect potential project header: line not starting with common labels and not too long
        if (len(l) <= 120 and
            not l.lower().startswith(('updates:', 'project schedule', 'estimated schedule', 'project description', 'project updates', 'recommended action', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'page ', 'agenda item')) and
            not any(l.startswith(p) for p in ['(cid', '•', '-', '–', '—', '·']) and
            # avoid all-caps section headers
            not re.fullmatch(r'[A-Z\s\(\)\-\/0-9\.]+', l) and
            # avoid obvious non-project
            l not in ['Item', 'Public Works', 'Commission Meeting']):
            # if next lines include Updates or Project Description, assume header
            nxt = ' '.join(lines[i+1:i+6]).lower() if i+1 < len(lines) else ''
            if ('updates' in nxt) or ('project description' in nxt) or ('project schedule' in nxt) or ('estimated schedule' in nxt):
                current_project = l
                in_project_block = True
                continue
        if in_project_block and current_project:
            # look for begin construction spring 2022
            if 'begin construction' in l.lower() and 'spring' in l.lower() and '2022' in l:
                projects.add(current_project)
            # end block on encountering another section header
            if l.lower().startswith(('capital improvement projects', 'disaster recovery projects')):
                in_project_block = False
                current_project = None

# join with funding totals
if projects:
    df_proj = pd.DataFrame({'Project_Name': sorted(projects)})
    df_join = df_proj.merge(df_fund, on='Project_Name', how='left')
    df_join['total_amount'] = df_join['total_amount'].fillna(0).astype(int)
    count = int(len(df_join))
    total_funding = int(df_join['total_amount'].sum())
else:
    count = 0
    total_funding = 0

out = {'spring_2022_projects_count': count, 'spring_2022_total_funding': total_funding, 'projects_found': sorted(projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wh6kEpuOdcgAlJK72Hl596y6': ['Funding'], 'var_call_dfEo8BMPVvngO0jpqpk1sgAm': 'file_storage/call_dfEo8BMPVvngO0jpqpk1sgAm.json', 'var_call_vqcWDfkcAaDfjGPiJi6rD5RH': 'file_storage/call_vqcWDfkcAaDfjGPiJi6rD5RH.json'}

exec(code, env_args)
