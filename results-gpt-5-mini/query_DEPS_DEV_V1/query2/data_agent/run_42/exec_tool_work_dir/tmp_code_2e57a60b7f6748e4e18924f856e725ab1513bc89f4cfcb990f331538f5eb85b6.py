code = """import json
import pandas as pd
import re

# Load storage
def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkgs = load(var_call_q8IhPYIbKTQcSErterjq4d5n)
ppv = load(var_call_EPqBtSQnfGDAjiONyg2HTIYm)
pinfo = load(var_call_TIeUihCrO14cUJE95FPxLJkg)

df_pkgs = pd.DataFrame(pkgs)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)

merged = df_pkgs.merge(df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
project_names = merged['ProjectName'].dropna().unique().tolist()

# Prepare forks extraction regex
fork_patterns = [
    re.compile(r"([0-9][0-9,]*)\s*forks", re.IGNORECASE),
    re.compile(r"forks count of\s*([0-9][0-9,]*)", re.IGNORECASE),
    re.compile(r"and\s*([0-9][0-9,]*)\s*forks", re.IGNORECASE),
    re.compile(r"forked\s*([0-9][0-9,]*)\s*times", re.IGNORECASE),
]

def extract_forks(s):
    if not isinstance(s, str):
        return None
    for pat in fork_patterns:
        m = pat.search(s)
        if m:
            num = m.group(1).replace(',','')
            try:
                return int(num)
            except:
                continue
    return None

# For each project_name, find matching project_info rows where Project_Information contains project_name and Licenses contains MIT
repo_forks = {}
for repo in project_names:
    # escape repo for substring search
    matches = df_pinfo[df_pinfo['Project_Information'].str.contains(repo, na=False)]
    if matches.empty:
        continue
    # filter by MIT in Licenses
    matches_mit = matches[matches['Licenses'].astype(str).str.contains('MIT', na=False)]
    if matches_mit.empty:
        continue
    # extract forks
    max_forks = None
    for _, row in matches_mit.iterrows():
        forks = extract_forks(row['Project_Information'])
        if forks is not None:
            if max_forks is None or forks > max_forks:
                max_forks = forks
    if max_forks is not None:
        repo_forks[repo] = max_forks

result_list = [{'ProjectName': k, 'Forks': v} for k, v in repo_forks.items()]
result_list = sorted(result_list, key=lambda x: x['Forks'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_call_q8IhPYIbKTQcSErterjq4d5n': 'file_storage/call_q8IhPYIbKTQcSErterjq4d5n.json', 'var_call_EPqBtSQnfGDAjiONyg2HTIYm': 'file_storage/call_EPqBtSQnfGDAjiONyg2HTIYm.json', 'var_call_TIeUihCrO14cUJE95FPxLJkg': 'file_storage/call_TIeUihCrO14cUJE95FPxLJkg.json', 'var_call_jteWDGzy5cf1c2DqKHQMQT9y': []}

exec(code, env_args)
