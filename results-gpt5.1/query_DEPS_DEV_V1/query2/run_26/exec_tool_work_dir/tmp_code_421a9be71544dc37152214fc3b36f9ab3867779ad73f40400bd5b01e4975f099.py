code = """import json, re, pandas as pd

pkg_path = var_call_iuYPATRJBBSfQN9xOpSY5lvb
map_path = var_call_myWnm6AlyvVwEoFKNjtTcNIU
proj_path = var_call_a2MBwQ0aVHPj01NHTMEdHXim

with open(pkg_path) as f:
    pkg = json.load(f)
with open(map_path) as f:
    mp = json.load(f)
with open(proj_path) as f:
    proj = json.load(f)

pkg_df = pd.DataFrame(pkg)
mp_df = pd.DataFrame(mp)
proj_df = pd.DataFrame(proj)

pkg_df = pkg_df[pkg_df['Licenses'].str.contains('"MIT"', regex=False, na=False)]

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease') if isinstance(x,str) else None)

pkg_df = pkg_df[pkg_df['IsRelease'] == True]

merged = pkg_df.merge(mp_df, on=['System','Name','Version'], how='inner')

proj_df['ProjectName'] = proj_df['Project_Information'].str.extract(r"The project ([^ ]+/[^ ]+) is hosted on GitHub|The project ([^ ]+/[^ ]+) on GitHub|The project is hosted on GitHub under the name ([^, ]+)|The project on GitHub, named ([^, ]+),|The GitHub project named ([^ ]+) ")[0]

merged = merged.merge(proj_df[['ProjectName','Project_Information']], on='ProjectName', how='inner')

def extract_forks(text):
    m = re.search(r"(\d+) forks", text)
    return int(m.group(1)) if m else None

merged['Forks'] = merged['Project_Information'].apply(lambda x: extract_forks(x))

proj_max = merged.groupby('ProjectName').agg({'Forks':'max'}).reset_index()

top5 = proj_max.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iuYPATRJBBSfQN9xOpSY5lvb': 'file_storage/call_iuYPATRJBBSfQN9xOpSY5lvb.json', 'var_call_myWnm6AlyvVwEoFKNjtTcNIU': 'file_storage/call_myWnm6AlyvVwEoFKNjtTcNIU.json', 'var_call_a2MBwQ0aVHPj01NHTMEdHXim': 'file_storage/call_a2MBwQ0aVHPj01NHTMEdHXim.json'}

exec(code, env_args)
