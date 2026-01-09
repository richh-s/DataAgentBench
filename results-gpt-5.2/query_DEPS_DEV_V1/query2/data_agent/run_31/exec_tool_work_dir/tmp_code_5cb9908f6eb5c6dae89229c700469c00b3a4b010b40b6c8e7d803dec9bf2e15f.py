code = """import json, re, pandas as pd

pkg_src = var_call_jLy7JGZwP2NxlPUqI4o3a6UQ
if isinstance(pkg_src, str):
    pkg_rows = json.load(open(pkg_src, 'r', encoding='utf-8'))
else:
    pkg_rows = pkg_src

ppv_src = var_call_Qt4xwKcVxVYT5mt6Xxcs6nc4
if isinstance(ppv_src, str):
    ppv_rows = json.load(open(ppv_src, 'r', encoding='utf-8'))
else:
    ppv_rows = ppv_src

pi_src = var_call_w01sOkyWD7NxphfAyErI99iw
if isinstance(pi_src, str):
    pi_rows = json.load(open(pi_src, 'r', encoding='utf-8'))
else:
    pi_rows = pi_src

pkg_df = pd.DataFrame(pkg_rows)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv_rows)[['System','Name','Version','ProjectName']]

j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(j['ProjectName'].dropna().drop_duplicates().tolist())

pi_df = pd.DataFrame(pi_rows)

fork_re = re.compile(r"\b([0-9][0-9,]*)\s+forks\b", re.IGNORECASE)
proj_re = re.compile(r"\bproject\s+([^\s,]+/[^\s,]+)")

def parse_info(s):
    if not isinstance(s, str):
        return (None, None)
    mproj = proj_re.search(s)
    proj = mproj.group(1) if mproj else None
    mf = fork_re.search(s)
    forks = int(mf.group(1).replace(',','')) if mf else None
    return (proj, forks)

parsed = pi_df['Project_Information'].apply(parse_info)
pi_df['ProjectName'] = parsed.apply(lambda x: x[0])
pi_df['Forks'] = parsed.apply(lambda x: x[1])

rel = pi_df[pi_df['ProjectName'].isin(projects)].dropna(subset=['ProjectName','Forks']).copy()
agg = rel.groupby('ProjectName', as_index=False)['Forks'].max()

pkg_example = j[['ProjectName','Name']].drop_duplicates().groupby('ProjectName', as_index=False).first()
agg = agg.merge(pkg_example, on='ProjectName', how='left')

agg = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

lines = [str(i+1)+'. '+row.ProjectName+' (NPM: '+str(row.Name)+'): '+str(int(row.Forks))+' forks' for i, row in agg.reset_index(drop=True).iterrows()]
out = '\n'.join(lines)

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_jLy7JGZwP2NxlPUqI4o3a6UQ': 'file_storage/call_jLy7JGZwP2NxlPUqI4o3a6UQ.json', 'var_call_Qt4xwKcVxVYT5mt6Xxcs6nc4': 'file_storage/call_Qt4xwKcVxVYT5mt6Xxcs6nc4.json', 'var_call_w01sOkyWD7NxphfAyErI99iw': 'file_storage/call_w01sOkyWD7NxphfAyErI99iw.json', 'var_call_yae5Xf1Ze3zQyWBaG4RG5Cnj': [{'ProjectName': 'dataminingsupply/dms-io'}, {'ProjectName': 'isacvale/fc'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}, {'ProjectName': 'laihaojie/jie'}], 'var_call_vOSpA7yxgw8IrU7kMKdIqboc': [{'column_name': 'Project_Information', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Licenses', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Homepage', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OSSFuzz', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}]}

exec(code, env_args)
