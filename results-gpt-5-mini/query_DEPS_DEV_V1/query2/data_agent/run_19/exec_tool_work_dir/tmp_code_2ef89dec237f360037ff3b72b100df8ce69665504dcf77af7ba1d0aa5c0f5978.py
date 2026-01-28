code = """import json
import pandas as pd
import re

# Load data from storage variables (file paths or lists)
def load_var(v):
    import os
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_records = load_var(var_call_8fQlnzV26oyHs3NX1K7IRmAT)
ppv_records = load_var(var_call_D32odqfMwAdE5EhCtSeBlNte)
projinfo_records = load_var(var_call_PKHML2fTt1OBtrtJ7upfMGga)

df_pkg = pd.DataFrame(pkg_records)
# Ensure columns exist
for c in ['System','Name','Version','Links']:
    if c not in df_pkg.columns:
        df_pkg[c] = None

# project_packageversion
df_ppv = pd.DataFrame(ppv_records)
for c in ['System','Name','Version','ProjectName']:
    if c not in df_ppv.columns:
        df_ppv[c] = None

# Merge on System, Name, Version
merged = pd.merge(df_pkg, df_ppv, on=['System','Name','Version'], how='inner')

# Unique projects
projects = merged['ProjectName'].dropna().unique().tolist()

# project_info df
df_info = pd.DataFrame(projinfo_records)
if 'Project_Information' not in df_info.columns:
    df_info['Project_Information'] = ''

# Function to extract forks from text
patterns = [r"([\d,]+)\s+forks",
            r"forks count of\s+([\d,]+)",
            r"forked\s+([\d,]+)\s+times",
            r"and\s+([\d,]+)\s+forks",
            r"has\s+([\d,]+)\s+forks",
            r"forks:\s*([\d,]+)"]

def extract_forks(text):
    if not isinstance(text, str):
        return None
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            val = m.group(1)
            val = val.replace(',','')
            try:
                return int(val)
            except:
                continue
    return None

# Build mapping project -> forks by searching Project_Information containing project
results = []
for p in projects:
    # Search in df_info for rows that contain the project string
    matches = df_info[df_info['Project_Information'].str.contains(str(p), na=False)]
    forks = None
    matched_text = None
    if not matches.empty:
        # Try each matched row to extract forks
        for txt in matches['Project_Information'].astype(str).tolist():
            f = extract_forks(txt)
            if f is not None:
                forks = f
                matched_text = txt
                break
        # If none extracted, still try first match to extract any number later
        if forks is None:
            # try extract any number before 'fork' even if pattern differs
            for txt in matches['Project_Information'].astype(str).tolist():
                m = re.search(r"([\d,]+)", txt)
                if m:
                    try:
                        forks = int(m.group(1).replace(',',''))
                        matched_text = txt
                        break
                    except:
                        pass
    else:
        # no direct match; try fuzzy: look for repo owner or repo name separately
        owner_repo = p.split('/')
        if len(owner_repo)==2:
            owner, repo = owner_repo
            # Try containing '/repo' or 'repo on GitHub'
            matches = df_info[df_info['Project_Information'].str.contains(str(repo), na=False)]
            if not matches.empty:
                for txt in matches['Project_Information'].astype(str).tolist():
                    if owner in txt:
                        f = extract_forks(txt)
                        if f is not None:
                            forks = f
                            matched_text = txt
                            break
    if forks is not None:
        results.append({'project': p, 'forks': forks, 'matched_text': matched_text})

# If no results found, return empty
if not results:
    out = []
else:
    # Deduplicate by project taking max forks if multiple
    df_res = pd.DataFrame(results)
    df_res = df_res.groupby('project', as_index=False).agg({'forks':'max','matched_text':'first'})
    df_res = df_res.sort_values('forks', ascending=False).head(5)
    out = df_res[['project','forks']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_uQvEBbwjJrFnDEImbGkqzuEE': 'file_storage/call_uQvEBbwjJrFnDEImbGkqzuEE.json', 'var_call_8fQlnzV26oyHs3NX1K7IRmAT': 'file_storage/call_8fQlnzV26oyHs3NX1K7IRmAT.json', 'var_call_D32odqfMwAdE5EhCtSeBlNte': 'file_storage/call_D32odqfMwAdE5EhCtSeBlNte.json', 'var_call_PKHML2fTt1OBtrtJ7upfMGga': 'file_storage/call_PKHML2fTt1OBtrtJ7upfMGga.json'}

exec(code, env_args)
