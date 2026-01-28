code = """import json
import pandas as pd
import re

# Load data from storage variables; they may be file paths (strings) or lists

def load_var(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg_records = load_var(var_call_8WoVjcIam0sUV5vlZh7J9GYr)
ppv_records = load_var(var_call_rDqdevglZHDEVsu1aJD5pCM2)
pinfo_records = load_var(var_call_r4Unr19zwNmLVIqnH17p8eJp)

pkg_df = pd.DataFrame(pkg_records)
ppv_df = pd.DataFrame(ppv_records)
pinfo_df = pd.DataFrame(pinfo_records)

# Ensure relevant columns exist
pkg_df = pkg_df[["System","Name","Version"]].drop_duplicates()
ppv_df = ppv_df[["System","Name","Version","ProjectName"]]

# Merge to get ProjectName for the filtered MIT release packages
merged = pd.merge(pkg_df, ppv_df, on=["System","Name","Version"] , how='inner')

project_names = merged['ProjectName'].dropna().unique().tolist()

# Helper to extract forks from Project_Information text

def extract_forks(text):
    if not isinstance(text, str):
        return None
    t = text
    # common pattern: number before 'forks'
    m = re.search(r'([\d,]+)\s+forks', t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # pattern: 'forks count of X'
    m = re.search(r'forks count of\s*[:]?\s*([\d,]+)', t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # pattern: 'been forked X times' or 'forked X times'
    m = re.search(r'forked\s+([\d,]+)\s+times', t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    m = re.search(r'been forked\s+([\d,]+)', t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # pattern: 'has been forked X times' covered above; fallback: digits followed by 'fork'
    m = re.search(r'([\d,]+)\s+fork', t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    return None

results = []

for pname in project_names:
    # find rows in project_info where Project_Information contains the project repo path
    mask = pinfo_df['Project_Information'].astype(str).str.contains(pname, case=False, na=False)
    matched = pinfo_df[mask]
    best_forks = None
    best_row_text = None
    if not matched.empty:
        for txt in matched['Project_Information'].astype(str):
            f = extract_forks(txt)
            if f is not None:
                if best_forks is None or f > best_forks:
                    best_forks = f
                    best_row_text = txt
    # If no direct match by Project_Information, also try matching by ProjectName owner or repo separately
    if best_forks is None:
        # try splitting owner and repo
        if '/' in pname:
            owner, repo = pname.split('/',1)
            # search by repo only
            mask2 = pinfo_df['Project_Information'].astype(str).str.contains(repo, case=False, na=False)
            matched2 = pinfo_df[mask2]
            if not matched2.empty:
                for txt in matched2['Project_Information'].astype(str):
                    f = extract_forks(txt)
                    if f is not None:
                        if best_forks is None or f > best_forks:
                            best_forks = f
                            best_row_text = txt
    if best_forks is not None:
        results.append({
            'ProjectName': pname,
            'Forks': best_forks,
            'Project_Information': best_row_text
        })

# Deduplicate by ProjectName (should already be unique) and sort
results_unique = {r['ProjectName']: r for r in results}.values()
results_sorted = sorted(results_unique, key=lambda x: x['Forks'], reverse=True)

top5 = results_sorted[:5]

# Prepare JSON-serializable output
out = []
for r in top5:
    out.append({'ProjectName': r['ProjectName'], 'Forks': int(r['Forks']), 'Project_Information': r['Project_Information']})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_PCVhi9BuL61ZIm1snvHInJdA': ['packageinfo'], 'var_call_Ld29gzcb6Svm3IAFgpFZZuuT': ['project_info', 'project_packageversion'], 'var_call_8WoVjcIam0sUV5vlZh7J9GYr': 'file_storage/call_8WoVjcIam0sUV5vlZh7J9GYr.json', 'var_call_rDqdevglZHDEVsu1aJD5pCM2': 'file_storage/call_rDqdevglZHDEVsu1aJD5pCM2.json', 'var_call_r4Unr19zwNmLVIqnH17p8eJp': 'file_storage/call_r4Unr19zwNmLVIqnH17p8eJp.json'}

exec(code, env_args)
