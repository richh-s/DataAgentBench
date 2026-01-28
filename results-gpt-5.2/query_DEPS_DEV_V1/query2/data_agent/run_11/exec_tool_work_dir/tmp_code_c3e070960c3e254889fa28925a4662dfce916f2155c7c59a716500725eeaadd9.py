code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        # assume path
        import pathlib
        p = pathlib.Path(v)
        if p.exists() and p.suffix=='.json':
            with p.open('r', encoding='utf-8') as f:
                return json.load(f)
        # fallback
        return json.loads(v)
    return v

ppv = load_records(var_call_IuAYwMo2wMfOj8TtUKynhrKs)
pkg = load_records(var_call_R8wNQRAU5G8Qt5kBBovoIdMC)
pi  = load_records(var_call_b9RPK28tm89a5M6HY0n5I7fy)

df_ppv = pd.DataFrame(ppv)
df_pkg = pd.DataFrame(pkg)

def parse_jsonish_array(s):
    if s is None:
        return []
    if isinstance(s, list):
        return s
    try:
        return json.loads(s)
    except Exception:
        # try extract quoted tokens
        return re.findall(r'"(.*?)"', str(s))

def parse_is_release(s):
    if s is None:
        return False
    if isinstance(s, dict):
        return bool(s.get('IsRelease'))
    try:
        o = json.loads(s)
        return bool(o.get('IsRelease'))
    except Exception:
        m = re.search(r'"IsRelease"\s*:\s*(true|false)', str(s), re.IGNORECASE)
        if m:
            return m.group(1).lower()=='true'
        return False

df_pkg['licenses_list'] = df_pkg['Licenses'].apply(parse_jsonish_array)
df_pkg['is_release'] = df_pkg['VersionInfo'].apply(parse_is_release)

# Filter package license MIT and release
mask_mit = df_pkg['licenses_list'].apply(lambda xs: any(str(x).upper()=='MIT' for x in xs))
df_pkg_f = df_pkg[mask_mit & df_pkg['is_release']].copy()

# Join to project mapping by (System,Name,Version)
df_join = df_pkg_f.merge(df_ppv, on=['System','Name','Version'], how='inner')

# Extract fork counts from project_info text and map by ProjectName
fork_re = re.compile(r'project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+forks\b', re.IGNORECASE)

def extract_name_forks(text):
    if not text:
        return (None, None)
    t = str(text)
    m = fork_re.search(t)
    if not m:
        return (None, None)
    proj = m.group(1).strip().rstrip('.,')
    forks = int(m.group(2).replace(',',''))
    return proj, forks

proj_rows = []
for r in pi:
    proj, forks = extract_name_forks(r.get('Project_Information'))
    if proj is not None and forks is not None:
        proj_rows.append({'ProjectName': proj, 'Forks': forks})

df_proj = pd.DataFrame(proj_rows).drop_duplicates(subset=['ProjectName'])

# Join and compute max forks per project
cand = df_join[['ProjectName']].drop_duplicates().merge(df_proj, on='ProjectName', how='inner')

top5 = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IuAYwMo2wMfOj8TtUKynhrKs': 'file_storage/call_IuAYwMo2wMfOj8TtUKynhrKs.json', 'var_call_R8wNQRAU5G8Qt5kBBovoIdMC': 'file_storage/call_R8wNQRAU5G8Qt5kBBovoIdMC.json', 'var_call_b9RPK28tm89a5M6HY0n5I7fy': 'file_storage/call_b9RPK28tm89a5M6HY0n5I7fy.json'}

exec(code, env_args)
