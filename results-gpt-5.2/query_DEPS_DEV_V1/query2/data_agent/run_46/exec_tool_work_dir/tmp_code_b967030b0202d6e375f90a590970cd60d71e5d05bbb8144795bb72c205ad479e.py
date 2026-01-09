code = """import json, re
import pandas as pd

# Load release+MIT NPM package versions
pk_path = var_call_mLh5iXuKvQ9xpqLEXpKy9uid
pp_path = var_call_rpzcaPpvo9vKJ9QBJczmKTar
pi_path = var_call_SvGCsRHGhweCbIp9x9TEIOTK

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pk = load_records(pk_path)
pp = load_records(pp_path)
pi = load_records(pi_path)

pk_df = pd.DataFrame(pk)
pp_df = pd.DataFrame(pp)

# join to get GitHub project names for those package versions
m = pk_df.merge(pp_df, on=['System','Name','Version'], how='inner')
# unique projects
projects = pd.Series(m['ProjectName'].dropna().unique(), name='ProjectName').to_frame()

# parse project_info Project_Information strings
pi_df = pd.DataFrame(pi)
text = pi_df['Project_Information'].dropna().astype(str)

# regex to extract owner/repo and forks count
pat = re.compile(r"project\s+([^\s]+/[^\s]+).*?\b([0-9][0-9,]*)\s+forks\b", re.IGNORECASE)
rows = []
for t in text:
    mt = pat.search(t)
    if mt:
        proj = mt.group(1).strip().rstrip('.,')
        forks = int(mt.group(2).replace(',',''))
        rows.append((proj, forks))

forks_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
# if multiple entries for same project, keep max forks
forks_df = forks_df.groupby('ProjectName', as_index=False)['Forks'].max()

# filter to projects referenced by our MIT+release packages
res = projects.merge(forks_df, on='ProjectName', how='inner')
res = res.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mLh5iXuKvQ9xpqLEXpKy9uid': 'file_storage/call_mLh5iXuKvQ9xpqLEXpKy9uid.json', 'var_call_rpzcaPpvo9vKJ9QBJczmKTar': 'file_storage/call_rpzcaPpvo9vKJ9QBJczmKTar.json', 'var_call_SvGCsRHGhweCbIp9x9TEIOTK': 'file_storage/call_SvGCsRHGhweCbIp9x9TEIOTK.json'}

exec(code, env_args)
