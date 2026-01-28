code = """import json, re, pandas as pd

# load big lists
import os

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_result(var_call_VWR7ObhFYmNdM190NxiKdEif)
pkg = load_result(var_call_rkEeP9VnW5sugkENBoXV4NTb)
pi  = load_result(var_call_Y3BhuEBG2JEhAFIv5Acb6eOQ)

ppv_df = pd.DataFrame(ppv)
pkg_df = pd.DataFrame(pkg)
pi_df = pd.DataFrame(pi)

# filter packages: license contains MIT AND VersionInfo.IsRelease==true

def parse_json_field(s, default=None):
    if s is None:
        return default
    if isinstance(s, (dict,list,bool,int,float)):
        return s
    try:
        return json.loads(s)
    except Exception:
        return default

pkg_df['lic_list'] = pkg_df['Licenses'].map(lambda x: parse_json_field(x, []))
pkg_df['is_mit'] = pkg_df['lic_list'].map(lambda lst: isinstance(lst, list) and any(str(v).strip().upper()=='MIT' for v in lst))
pkg_df['vinfo'] = pkg_df['VersionInfo'].map(lambda x: parse_json_field(x, {}))
pkg_df['is_release'] = pkg_df['vinfo'].map(lambda d: isinstance(d, dict) and d.get('IsRelease') is True)

pkg_f = pkg_df[(pkg_df['System']=='NPM') & (pkg_df['is_mit']) & (pkg_df['is_release'])][['System','Name','Version']].drop_duplicates()

# join to project_packageversion
m = pkg_f.merge(ppv_df[['System','Name','Version','ProjectName','ProjectType']], on=['System','Name','Version'], how='inner')
# only github projects
m = m[m['ProjectType'].str.upper().fillna('')=='GITHUB']

# map project_info to ProjectName by extracting owner/repo from Project_Information
pattern = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

def extract_repo(text):
    if not isinstance(text, str):
        return None
    m = pattern.search(text)
    if m:
        return m.group(1)
    # fallback: maybe 'named owner/repo'
    m2 = re.search(r"named\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", text)
    return m2.group(1) if m2 else None

pi_df['ProjectName'] = pi_df['Project_Information'].map(extract_repo)

# extract forks
fork_pat = re.compile(r"([0-9][0-9,]*)\s+forks")

def extract_forks(text):
    if not isinstance(text, str):
        return None
    m = fork_pat.search(text)
    if not m:
        return None
    return int(m.group(1).replace(',',''))

pi_df['Forks'] = pi_df['Project_Information'].map(extract_forks)

# join to get forks
j = m.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='left')

# compute top 5 distinct projects by forks
j2 = j.dropna(subset=['Forks']).drop_duplicates(subset=['ProjectName'])[['ProjectName','Forks']]

top5 = j2.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_VWR7ObhFYmNdM190NxiKdEif': 'file_storage/call_VWR7ObhFYmNdM190NxiKdEif.json', 'var_call_rkEeP9VnW5sugkENBoXV4NTb': 'file_storage/call_rkEeP9VnW5sugkENBoXV4NTb.json', 'var_call_Y3BhuEBG2JEhAFIv5Acb6eOQ': 'file_storage/call_Y3BhuEBG2JEhAFIv5Acb6eOQ.json'}

exec(code, env_args)
