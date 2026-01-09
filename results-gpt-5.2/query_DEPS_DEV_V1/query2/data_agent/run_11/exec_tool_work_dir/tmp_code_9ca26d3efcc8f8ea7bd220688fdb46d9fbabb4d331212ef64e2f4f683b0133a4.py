code = """import json, re, pandas as pd, pathlib

def load_records(v):
    if isinstance(v, str):
        p = pathlib.Path(v)
        if p.exists() and p.suffix=='.json':
            with p.open('r', encoding='utf-8') as f:
                return json.load(f)
        return json.loads(v)
    return v

pkg = load_records(var_call_R8wNQRAU5G8Qt5kBBovoIdMC)
ppv = load_records(var_call_IuAYwMo2wMfOj8TtUKynhrKs)
pi2 = load_records(var_call_JVc1SSLN0ENZNxTUMkpZhkmL)

df_ppv = pd.DataFrame(ppv)
df_pkg = pd.DataFrame(pkg)

def parse_is_release(s):
    if s is None:
        return False
    try:
        return bool(json.loads(s).get('IsRelease'))
    except Exception:
        m = re.search(r'"IsRelease"\s*:\s*(true|false)', str(s), re.IGNORECASE)
        return (m.group(1).lower()=='true') if m else False

def has_mit(s):
    try:
        arr = json.loads(s)
        return any(str(x).upper()=='MIT' for x in arr)
    except Exception:
        return bool(re.search(r'\bMIT\b', str(s), re.IGNORECASE))

df_pkg_f = df_pkg[df_pkg['Licenses'].apply(has_mit) & df_pkg['VersionInfo'].apply(parse_is_release)].copy()
df_join = df_pkg_f.merge(df_ppv, on=['System','Name','Version'], how='inner')

# parse project info: handle both 'X forks' and 'forks count of X'
re1 = re.compile(r'project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+forks\b', re.IGNORECASE)
re2 = re.compile(r'project\s+([^\s]+/[^\s]+).*?forks\s+count\s+of\s+([0-9][0-9,]*)', re.IGNORECASE)

def parse_row(text):
    t = str(text)
    m = re1.search(t)
    if m:
        return m.group(1).strip().rstrip('.,'), int(m.group(2).replace(',',''))
    m = re2.search(t)
    if m:
        return m.group(1).strip().rstrip('.,'), int(m.group(2).replace(',',''))
    # also 'has been forked 12 times'
    m = re.search(r'name\s+([^\s]+/[^\s]+).*?forked\s+([0-9][0-9,]*)\s+times', t, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip('.,'), int(m.group(2).replace(',',''))
    return None

proj_rows=[]
for r in pi2:
    got = parse_row(r.get('Project_Information'))
    if got:
        proj, forks = got
        proj_rows.append({'ProjectName': proj, 'Forks': forks})

df_proj = pd.DataFrame(proj_rows).drop_duplicates(subset=['ProjectName'])

cand = df_join[['ProjectName']].drop_duplicates().merge(df_proj, on='ProjectName', how='inner')
top5 = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

lines=[]
for i, r in enumerate(top5.to_dict(orient='records'), start=1):
    lines.append(str(i)+'. '+r['ProjectName']+' - '+str(r['Forks'])+' forks')

answer = "\n".join(lines) if lines else "No matching projects found."
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_IuAYwMo2wMfOj8TtUKynhrKs': 'file_storage/call_IuAYwMo2wMfOj8TtUKynhrKs.json', 'var_call_R8wNQRAU5G8Qt5kBBovoIdMC': 'file_storage/call_R8wNQRAU5G8Qt5kBBovoIdMC.json', 'var_call_b9RPK28tm89a5M6HY0n5I7fy': 'file_storage/call_b9RPK28tm89a5M6HY0n5I7fy.json', 'var_call_VITOJlwfj36s9jmyS81xk3kV': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_pKvq1o7wOg4f8iVpZt3LTxdn': {'df_join_columns': ['System', 'Name', 'Version', 'Licenses', 'VersionInfo', 'ProjectName'], 'df_join_head': [{'System': 'NPM', 'Name': '@discue/ui-components', 'Version': '0.13.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 12\n}', 'ProjectName': 'discue/ui-components'}, {'System': 'NPM', 'Name': '@dvcol/web-extension-utils', 'Version': '1.1.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 7\n}', 'ProjectName': 'dvcol/web-extension-utils'}, {'System': 'NPM', 'Name': '@eclipsejs/cli', 'Version': '1.0.0', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 13\n}', 'ProjectName': 'dlesage25/eclipse-cli'}, {'System': 'NPM', 'Name': '@ebot7/edem-react', 'Version': '0.18.8', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 55\n}', 'ProjectName': 'ebot7/edem'}, {'System': 'NPM', 'Name': '@e4a/irmaseal-wasm-bindings', 'Version': '0.0.1', 'Licenses': '[\n  "MIT"\n]', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 1\n}', 'ProjectName': 'encryption4all/irmaseal'}]}, 'var_call_by8PgZcZMowwlluRaSf7w09r': {'df_proj_cols': [], 'df_proj_head': [], 'count': 0}, 'var_call_JVc1SSLN0ENZNxTUMkpZhkmL': 'file_storage/call_JVc1SSLN0ENZNxTUMkpZhkmL.json'}

exec(code, env_args)
