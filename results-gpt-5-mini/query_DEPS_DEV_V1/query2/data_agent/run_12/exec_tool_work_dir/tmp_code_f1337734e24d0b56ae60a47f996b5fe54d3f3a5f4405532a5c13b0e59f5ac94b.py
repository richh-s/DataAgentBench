code = """import json
import pandas as pd
import re

# Load query results from storage variables
# These variables may be file paths (strings) or already-loaded lists

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_records = load_var(var_call_k2GvuirEQwVVbKXBMSH81K0z)
projpkg_records = load_var(var_call_uLXKwspKQgyXQptE4QoOqyJD)
projinfo_records = load_var(var_call_80S2KDcLbrtNeZ810ZKjujWm)

# Create DataFrames
df_pkg = pd.DataFrame(pkg_records)
df_projpkg = pd.DataFrame(projpkg_records)
df_projinfo = pd.DataFrame(projinfo_records)

# Ensure relevant columns exist
for col in ['System','Name','Version']:
    if col not in df_pkg.columns:
        df_pkg[col] = None
    if col not in df_projpkg.columns:
        df_projpkg[col] = None

# Inner join on System, Name, Version
merged = pd.merge(df_pkg[['System','Name','Version']], df_projpkg[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Unique project names
project_names = merged['ProjectName'].dropna().unique().tolist()

# Helper to extract forks from Project_Information text
def extract_forks(text):
    if not isinstance(text, str):
        return None
    patterns = [
        r"([\d,]+)\s+forks",
        r"forked\s+([\d,]+)\s+times",
        r"forks count of\s+([\d,]+)",
        r"has been forked\s+([\d,]+)\s+times",
        r"forked\s+([\d,]+)",
        r"([\d,]+)\s+fork",
    ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1).replace(',','')
            try:
                return int(num)
            except:
                continue
    return None

# Build mapping from project info texts for faster search
projinfo_texts = df_projinfo['Project_Information'].fillna('').astype(str).tolist()

results = []
for pname in project_names:
    matches = []
    for txt in projinfo_texts:
        if pname in txt:
            forks = extract_forks(txt)
            matches.append((forks, txt))
    # If no direct substring match, try matching by repo name part after '/'
    if not matches:
        # try matching by repo part only
        if '/' in pname:
            owner, repo = pname.split('/',1)
            for txt in projinfo_texts:
                if repo in txt:
                    forks = extract_forks(txt)
                    matches.append((forks, txt))
    # choose best match: the one with non-None forks; if multiple, take max forks
    forks_vals = [m[0] for m in matches if m[0] is not None]
    forks_val = None
    if forks_vals:
        forks_val = max(forks_vals)
    else:
        # if no forks found but matches exist, try to extract any number near the repo
        if matches:
            # try extract from first match
            forks_val = extract_forks(matches[0][1])
    if forks_val is not None:
        results.append({'ProjectName': pname, 'Forks': forks_val})

# Deduplicate by ProjectName (already unique) and sort
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)

top5 = results_sorted[:5]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_9R3g3CSK9PMdDDZnqTMoFtLe': ['packageinfo'], 'var_call_XBZHoUhec2X4vshXjj10M7PR': ['project_info', 'project_packageversion'], 'var_call_k2GvuirEQwVVbKXBMSH81K0z': 'file_storage/call_k2GvuirEQwVVbKXBMSH81K0z.json', 'var_call_uLXKwspKQgyXQptE4QoOqyJD': 'file_storage/call_uLXKwspKQgyXQptE4QoOqyJD.json', 'var_call_80S2KDcLbrtNeZ810ZKjujWm': 'file_storage/call_80S2KDcLbrtNeZ810ZKjujWm.json'}

exec(code, env_args)
