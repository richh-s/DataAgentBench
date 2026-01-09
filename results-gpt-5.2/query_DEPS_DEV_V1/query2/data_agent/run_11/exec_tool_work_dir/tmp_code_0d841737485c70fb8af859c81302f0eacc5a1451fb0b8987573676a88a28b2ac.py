code = """import json, re, pandas as pd, pathlib

def load_records(v):
    if isinstance(v, str):
        p = pathlib.Path(v)
        if p.exists() and p.suffix=='.json':
            with p.open('r', encoding='utf-8') as f:
                return json.load(f)
        return json.loads(v)
    return v

pi  = load_records(var_call_b9RPK28tm89a5M6HY0n5I7fy)
proj_rows=[]
fork_re = re.compile(r'project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+forks\b', re.IGNORECASE)
for r in pi:
    m = fork_re.search(str(r.get('Project_Information')))
    if m:
        proj = m.group(1).strip().rstrip('.,')
        forks = int(m.group(2).replace(',',''))
        proj_rows.append({'ProjectName': proj, 'Forks': forks})

df_proj = pd.DataFrame(proj_rows)
print('__RESULT__:')
print(json.dumps({'df_proj_cols': df_proj.columns.tolist(), 'df_proj_head': df_proj.head(5).to_dict(orient='records'), 'count': len(df_proj)}))"""

env_args = {'var_call_IuAYwMo2wMfOj8TtUKynhrKs': 'file_storage/call_IuAYwMo2wMfOj8TtUKynhrKs.json', 'var_call_R8wNQRAU5G8Qt5kBBovoIdMC': 'file_storage/call_R8wNQRAU5G8Qt5kBBovoIdMC.json', 'var_call_b9RPK28tm89a5M6HY0n5I7fy': 'file_storage/call_b9RPK28tm89a5M6HY0n5I7fy.json', 'var_call_VITOJlwfj36s9jmyS81xk3kV': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_pKvq1o7wOg4f8iVpZt3LTxdn': {'df_join_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectName'], 'df_join_head': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'ProjectName': 'discue/ui-components'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'ProjectName': 'dvcol/web-extension-utils'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'ProjectName': 'dlesage25/eclipse-cli'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}', 'ProjectName': 'ebot7/edem'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'ProjectName': 'encryption4all/irmaseal'}]}}

exec(code, env_args)
