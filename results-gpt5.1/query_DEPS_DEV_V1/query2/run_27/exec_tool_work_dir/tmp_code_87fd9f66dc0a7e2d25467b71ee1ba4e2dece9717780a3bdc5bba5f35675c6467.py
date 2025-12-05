code = """import json, pandas as pd

# Load full results from files
with open(var_call_MpSXGD9nfuGWWUe7pVWriUO7, 'r') as f:
    packageinfo = json.load(f)
with open(var_call_hRlWcXTYnXJAuIHT5W72nzlN, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_rXwVuu97q74n5N5BVXRwHsqI, 'r') as f:
    proj_info = json.load(f)

pkg_df = pd.DataFrame(packageinfo)
pp_df = pd.DataFrame(proj_pkg)
pi_df = pd.DataFrame(proj_info)

merged = pkg_df.merge(pp_df, on=['System','Name','Version'], how='inner')

# Extract project name and fork count from Project_Information text
import re

def parse_project_info(text):
    # Example pattern: "The project owner/repo on GitHub ... stars, and 123 forks"
    name_match = re.search(r"project ([^\s/]+/[^\s]+)|named ([^\s/]+/[^\s,]+)|under the name ([^\s/]+/[^\s,]+)", text)
    forks_match = re.search(r"(\d+) forks", text)
    project_name = None
    if name_match:
        for group in name_match.groups():
            if group:
                project_name = group
                break
    forks = int(forks_match.group(1)) if forks_match else None
    return project_name, forks

pi_df['Parsed'] = pi_df['Project_Information'].apply(parse_project_info)
pi_df['ParsedProjectName'] = pi_df['Parsed'].apply(lambda x: x[0])
pi_df['Forks'] = pi_df['Parsed'].apply(lambda x: x[1])
pi_df = pi_df.drop(columns=['Parsed'])

# Join merged with project_info on ProjectName (from pp_df) matching ParsedProjectName
merged2 = merged.merge(pi_df, left_on='ProjectName', right_on='ParsedProjectName', how='inner')

# Aggregate by project (some may appear multiple times due to multiple package versions)
agg = merged2.groupby('ProjectName')['Forks'].max().reset_index()

# Get top 5 by forks
top5 = agg.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MpSXGD9nfuGWWUe7pVWriUO7': 'file_storage/call_MpSXGD9nfuGWWUe7pVWriUO7.json', 'var_call_hRlWcXTYnXJAuIHT5W72nzlN': 'file_storage/call_hRlWcXTYnXJAuIHT5W72nzlN.json', 'var_call_rXwVuu97q74n5N5BVXRwHsqI': 'file_storage/call_rXwVuu97q74n5N5BVXRwHsqI.json'}

exec(code, env_args)
