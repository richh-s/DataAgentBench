code = """import json, pandas as pd, pathlib, re

def load_records(v):
    if isinstance(v, str):
        p = pathlib.Path(v)
        if p.exists() and p.suffix=='.json':
            with p.open('r', encoding='utf-8') as f:
                return json.load(f)
        return json.loads(v)
    return v

ppv = load_records(var_call_IuAYwMo2wMfOj8TtUKynhrKs)
pkg = load_records(var_call_R8wNQRAU5G8Qt5kBBovoIdMC)
df_ppv = pd.DataFrame(ppv)
df_pkg = pd.DataFrame(pkg)

# minimal parse is_release, MIT filter

def parse_is_release(s):
    if s is None:
        return False
    try:
        import json
        return bool(json.loads(s).get('IsRelease'))
    except Exception:
        m = re.search(r'"IsRelease"\s*:\s*(true|false)', str(s), re.IGNORECASE)
        return (m.group(1).lower()=='true') if m else False

def has_mit(s):
    try:
        import json
        arr = json.loads(s)
        return any(str(x).upper()=='MIT' for x in arr)
    except Exception:
        return 'MIT' in str(s)

df_pkg_f = df_pkg[df_pkg['Licenses'].apply(has_mit) & df_pkg['VersionInfo'].apply(parse_is_release)].copy()

df_join = df_pkg_f.merge(df_ppv, on=['System','Name','Version'], how='inner')

print('__RESULT__:')
print(json.dumps({'df_join_columns': df_join.columns.tolist(), 'df_join_head': df_join.head(5).to_dict(orient='records')}))"""

env_args = {'var_call_IuAYwMo2wMfOj8TtUKynhrKs': 'file_storage/call_IuAYwMo2wMfOj8TtUKynhrKs.json', 'var_call_R8wNQRAU5G8Qt5kBBovoIdMC': 'file_storage/call_R8wNQRAU5G8Qt5kBBovoIdMC.json', 'var_call_b9RPK28tm89a5M6HY0n5I7fy': 'file_storage/call_b9RPK28tm89a5M6HY0n5I7fy.json', 'var_call_VITOJlwfj36s9jmyS81xk3kV': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}}

exec(code, env_args)
