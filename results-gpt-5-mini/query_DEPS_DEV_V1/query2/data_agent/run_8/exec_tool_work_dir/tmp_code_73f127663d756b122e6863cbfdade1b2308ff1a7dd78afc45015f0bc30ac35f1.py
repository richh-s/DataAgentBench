code = """import json, re, pandas as pd

# Load results from previous queries (they may be file paths or lists)
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

pkg_records = load_var(var_call_YepJmbqhJlm6sOJV4plzB9Cu)
ppv_records = load_var(var_call_3L0fs4aWe436WNLRJ7OLFFjY)
pinfo_records = load_var(var_call_T7F79VNCepZEyjgNWmbMZmd5)

pkg_df = pd.DataFrame(pkg_records)
ppv_df = pd.DataFrame(ppv_records)
pinfo_df = pd.DataFrame(pinfo_records)

# Normalize column names
pkg_df = pkg_df.rename(columns={c: c for c in pkg_df.columns})
ppv_df = ppv_df.rename(columns={c: c for c in ppv_df.columns})

# Merge on System, Name, Version
merge_cols = ['System', 'Name', 'Version']
merged = pd.merge(pkg_df[merge_cols], ppv_df[['System','Name','Version','ProjectName']], on=merge_cols)

# Unique project names
project_names = merged['ProjectName'].dropna().unique().tolist()

# Prepare project_info texts
pinfo_df['pi_lower'] = pinfo_df['Project_Information'].fillna('').str.lower()

# regex patterns to extract forks
patterns = [re.compile(r"(\d[\d,]*)\s+forks"),
            re.compile(r"forked\s+(\d[\d,]*)"),
            re.compile(r"forks count of\s+(\d[\d,]*)"),
            re.compile(r"forks\D*(\d[\d,]*)")]

def extract_forks(text):
    if not text:
        return None
    for pat in patterns:
        m = pat.search(text)
        if m:
            num = m.group(1).replace(',', '')
            try:
                return int(num)
            except:
                continue
    return None

# Build mapping from project_name to forks
results = []
for pn in project_names:
    pn_lower = pn.lower()
    # find rows in pinfo where the project_name appears
    matches = pinfo_df[pinfo_df['pi_lower'].str.contains(pn_lower, na=False)]
    forks_vals = []
    for _, row in matches.iterrows():
        f = extract_forks(row['Project_Information'])
        if f is not None:
            forks_vals.append(f)
    # If no direct match found, try matching just repo part (after slash)
    if len(forks_vals) == 0 and '/' in pn_lower:
        repo_only = pn_lower.split('/',1)[1]
        matches2 = pinfo_df[pinfo_df['pi_lower'].str.contains(repo_only, na=False)]
        for _, row in matches2.iterrows():
            f = extract_forks(row['Project_Information'])
            if f is not None:
                forks_vals.append(f)
    forks = max(forks_vals) if forks_vals else 0
    results.append({'ProjectName': pn, 'Forks': int(forks)})

# Deduplicate by ProjectName (should be unique already), then sort
results_df = pd.DataFrame(results).drop_duplicates(subset=['ProjectName'])
results_df = results_df.sort_values(by='Forks', ascending=False)

top5 = results_df.head(5).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_YepJmbqhJlm6sOJV4plzB9Cu': 'file_storage/call_YepJmbqhJlm6sOJV4plzB9Cu.json', 'var_call_3L0fs4aWe436WNLRJ7OLFFjY': 'file_storage/call_3L0fs4aWe436WNLRJ7OLFFjY.json', 'var_call_T7F79VNCepZEyjgNWmbMZmd5': 'file_storage/call_T7F79VNCepZEyjgNWmbMZmd5.json'}

exec(code, env_args)
