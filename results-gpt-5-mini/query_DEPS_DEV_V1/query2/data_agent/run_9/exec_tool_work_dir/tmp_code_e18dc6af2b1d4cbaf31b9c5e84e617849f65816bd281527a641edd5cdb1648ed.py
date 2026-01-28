code = """import json
import pandas as pd
import re

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_pNIjHE3o9a3zDzMzhZUv0Ubj)
ppv = load_var(var_call_OZHgFr7rS1jFcpaDCTB9gmFv)
pinfo = load_var(var_call_X1oS1P9R1bSZllGgiXvtHyNr)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)

merged = pd.merge(df_pkg, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

sample_merged = merged.head(20).to_dict(orient='records')

# Projects list
projects = merged['ProjectName'].dropna().unique().tolist()
projects_sample = projects[:20]

# Parse project_info
repo_list = []
for rec in pinfo[:200]:
    pi = rec.get('Project_Information') or ''
    m = re.search(r"\b[\w.-]+/[\w.-]+\b", pi)
    repo = m.group(0) if m else None
    m2 = re.search(r"([0-9][0-9,]*)\s*(?:forks|fork)\b", pi)
    forks = int(m2.group(1).replace(',','')) if m2 else None
    repo_list.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': pi})

repo_sample = [r for r in repo_list if r['ProjectName'] is not None][:20]

# Intersection sample
intersection = list(set(projects).intersection({r['ProjectName'] for r in repo_list if r['ProjectName']}))
intersection_sample = intersection[:20]

out = {
    'merged_head': sample_merged,
    'projects_sample': projects_sample,
    'repo_sample': repo_sample,
    'intersection_sample': intersection_sample,
    'counts': {
        'num_pkg_rows': len(df_pkg),
        'num_ppv_rows': len(df_ppv),
        'num_pinfo_rows': len(df_pinfo),
        'num_projects_from_pkg': len(projects),
    }
}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_pNIjHE3o9a3zDzMzhZUv0Ubj': 'file_storage/call_pNIjHE3o9a3zDzMzhZUv0Ubj.json', 'var_call_OZHgFr7rS1jFcpaDCTB9gmFv': 'file_storage/call_OZHgFr7rS1jFcpaDCTB9gmFv.json', 'var_call_X1oS1P9R1bSZllGgiXvtHyNr': 'file_storage/call_X1oS1P9R1bSZllGgiXvtHyNr.json', 'var_call_4SAyhtKDfcKh241BBlj6wlI3': []}

exec(code, env_args)
