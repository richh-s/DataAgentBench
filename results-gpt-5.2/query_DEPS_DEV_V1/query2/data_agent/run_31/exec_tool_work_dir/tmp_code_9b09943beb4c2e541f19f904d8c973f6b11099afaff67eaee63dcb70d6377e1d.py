code = """import json, re, pandas as pd

# Load package rows (may be file path)
pkg_src = var_call_jLy7JGZwP2NxlPUqI4o3a6UQ
if isinstance(pkg_src, str):
    with open(pkg_src, 'r', encoding='utf-8') as f:
        pkg_rows = json.load(f)
else:
    pkg_rows = pkg_src

ppv_src = var_call_Qt4xwKcVxVYT5mt6Xxcs6nc4
if isinstance(ppv_src, str):
    with open(ppv_src, 'r', encoding='utf-8') as f:
        ppv_rows = json.load(f)
else:
    ppv_rows = ppv_src

pi_src = var_call_w01sOkyWD7NxphfAyErI99iw
if isinstance(pi_src, str):
    with open(pi_src, 'r', encoding='utf-8') as f:
        pi_rows = json.load(f)
else:
    pi_rows = pi_src

pkg_df = pd.DataFrame(pkg_rows)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv_rows)[['System','Name','Version','ProjectName']]

# inner join packages that are NPM+MIT+IsRelease with github-mapped package versions
j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# unique projects
projects = j['ProjectName'].dropna().drop_duplicates().tolist()

# Build project_info DF with parsed fork count
pi_df = pd.DataFrame(pi_rows)

fork_re = re.compile(r"\b([0-9][0-9,]*)\s+forks\b", re.IGNORECASE)
proj_re = re.compile(r"\bproject\s+([^\s,]+/[^\s,]+)")

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    mproj = proj_re.search(s)
    proj = mproj.group(1) if mproj else None
    mf = fork_re.search(s)
    forks = int(mf.group(1).replace(',','')) if mf else None
    return proj, forks

parsed = pi_df['Project_Information'].apply(parse_info)
pi_df['ProjectName'] = parsed.apply(lambda x: x[0])
pi_df['Forks'] = parsed.apply(lambda x: x[1])

# Filter to relevant projects and max forks per project
rel = pi_df[pi_df['ProjectName'].isin(projects)].copy()
rel = rel.dropna(subset=['ProjectName','Forks'])
agg = rel.groupby('ProjectName', as_index=False)['Forks'].max()

# Join back to one example package name (optional) - pick first
pkg_example = j[['ProjectName','Name']].drop_duplicates().groupby('ProjectName', as_index=False).first()
agg = agg.merge(pkg_example, on='ProjectName', how='left')

# Top 5 by forks
agg = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result_lines = []
for _, r in agg.iterrows():
    result_lines.append(f"{r['ProjectName']} (NPM: {r['Name']}): {int(r['Forks'])} forks")

out = "\n".join(result_lines)
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jLy7JGZwP2NxlPUqI4o3a6UQ': 'file_storage/call_jLy7JGZwP2NxlPUqI4o3a6UQ.json', 'var_call_Qt4xwKcVxVYT5mt6Xxcs6nc4': 'file_storage/call_Qt4xwKcVxVYT5mt6Xxcs6nc4.json', 'var_call_w01sOkyWD7NxphfAyErI99iw': 'file_storage/call_w01sOkyWD7NxphfAyErI99iw.json', 'var_call_yae5Xf1Ze3zQyWBaG4RG5Cnj': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}], 'var_call_vOSpA7yxgw8IrU7kMKdIqboc': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}]}

exec(code, env_args)
