code = """import json
import pandas as pd
import re
import os

# Load stored results (may be file paths if large)
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_pNsXIDWnuvJR9O7ceMXfXnhT)
ppv = load_var(var_call_Td50Z5i8OoYFNXwiM4t3pBcH)
proj = load_var(var_call_K08xMT0fVeRbl9Mmy6xpv87j)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_proj = pd.DataFrame(proj)

# Merge package records with project_packageversion
merged = pd.merge(df_pkg, df_ppv, on=['System','Name','Version'], how='inner')

# Prepare function to extract forks count from Project_Information text
def extract_forks(text):
    if not isinstance(text, str):
        return None
    patterns = [r'(?P<num>[\d,]+)\s*(?:forks|forked)', r'forked\s*(?P<num>[\d,]+)', r'(?P<num>[\d,]+)\s*times\s*(?:forks|forked)']
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group('num')
            if num:
                try:
                    return int(num.replace(',',''))
                except:
                    return None
    return None

# For each matched ProjectName, find corresponding project_info entry and extract forks
project_names = merged['ProjectName'].dropna().unique().tolist()
results = []
for pname in project_names:
    mask = df_proj['Project_Information'].fillna('').str.contains(pname, regex=False)
    matched = df_proj[mask]
    fork_vals = []
    for _, row in matched.iterrows():
        f = extract_forks(row.get('Project_Information', ''))
        if f is not None:
            fork_vals.append((f, row.get('Project_Information', '')))
    if fork_vals:
        fmax, info = max(fork_vals, key=lambda x: x[0])
        results.append({'ProjectName': pname, 'Forks': int(fmax), 'Project_Information': info})

# Sort and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)[:5]

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_pNsXIDWnuvJR9O7ceMXfXnhT': 'file_storage/call_pNsXIDWnuvJR9O7ceMXfXnhT.json', 'var_call_Td50Z5i8OoYFNXwiM4t3pBcH': 'file_storage/call_Td50Z5i8OoYFNXwiM4t3pBcH.json', 'var_call_K08xMT0fVeRbl9Mmy6xpv87j': 'file_storage/call_K08xMT0fVeRbl9Mmy6xpv87j.json'}

exec(code, env_args)
