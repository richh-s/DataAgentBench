code = """import json, re, pandas as pd

# Load large query results from files
pkg_file = var_call_w1b352T4ZFBOXox4RsKi3vR2
ppv_file = var_call_YLEC2ADWgYKLZf2WNQxlPJqU
pi_file = var_call_SIxDNQgiNh9eR3xpAi91dmBf

with open(pkg_file) as f:
    pkg = json.load(f)
with open(ppv_file) as f:
    ppv = json.load(f)
with open(pi_file) as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

pi_df = pd.DataFrame(pi)

# Extract repo name and fork count from Project_Information
repo_pattern = re.compile(r"project ([^\s/]+/[^\s]+)")
fork_pattern = re.compile(r"(\d+) forks?")

def extract_info(text):
    repo_match = repo_pattern.search(text)
    fork_match = fork_pattern.search(text)
    repo = repo_match.group(1) if repo_match else None
    forks = int(fork_match.group(1)) if fork_match else None
    return repo, forks

pi_df[['ProjectName','Forks']] = pi_df['Project_Information'].apply(lambda t: pd.Series(extract_info(t)))

# Join merged packages with project info via ProjectName
full = merged.merge(pi_df, on='ProjectName', how='inner')

# Aggregate by project (since multiple package versions may map to same project)
proj_agg = full.groupby('ProjectName', as_index=False)['Forks'].max()

# Top 5 by forks
top5 = proj_agg.sort_values('Forks', ascending=False).head(5)
result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_w1b352T4ZFBOXox4RsKi3vR2': 'file_storage/call_w1b352T4ZFBOXox4RsKi3vR2.json', 'var_call_YLEC2ADWgYKLZf2WNQxlPJqU': 'file_storage/call_YLEC2ADWgYKLZf2WNQxlPJqU.json', 'var_call_SIxDNQgiNh9eR3xpAi91dmBf': 'file_storage/call_SIxDNQgiNh9eR3xpAi91dmBf.json'}

exec(code, env_args)
