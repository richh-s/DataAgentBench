code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_TY47ktUAW7KCosFpvygKIODd, 'r') as f:
    pkg_rows = json.load(f)
with open(var_call_VDA1TzjNoz2T347LFnSvYFzG, 'r') as f:
    ppv_rows = json.load(f)
with open(var_call_Y5W4dmMrI2zRSJ3AJ2qSeVw9, 'r') as f:
    proj_rows = json.load(f)

pkg_df = pd.DataFrame(pkg_rows)
ppv_df = pd.DataFrame(ppv_rows)
proj_df = pd.DataFrame(proj_rows)

# Merge package rows (already filtered for MIT & IsRelease true) with project_packageversion on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System', 'Name', 'Version'], how='inner')

# Get unique GitHub project names
project_names = merged['ProjectName'].dropna().unique().tolist()

# Helper to parse forks from a Project_Information text
def parse_forks(text):
    if not isinstance(text, str):
        return None
    patterns = [
        r"(\d{1,3}(?:,\d{3})*)\s+forks",
        r"forks count of\s+(\d{1,3}(?:,\d{3})*)",
        r"forked\s+(\d{1,3}(?:,\d{3})*)\s+times",
        r"has been forked\s+(\d{1,3}(?:,\d{3})*)\s+times",
        r"forks count of (\d{1,3}(?:,\d{3})*)",
        r"and\s+(\d{1,3}(?:,\d{3})*)\s+forks",
    ]
    for p in patterns:
        m = re.search(p, text)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    return None

results = []
for pname in project_names:
    # find project_info rows where Project_Information contains the project name (owner/repo)
    mask = proj_df['Project_Information'].astype(str).str.contains(pname, regex=False)
    matched = proj_df[mask]
    best_forks = None
    best_info = None
    if not matched.empty:
        # parse forks from all matched rows and take the max available
        for info in matched['Project_Information'].tolist():
            f = parse_forks(info)
            if f is not None:
                if best_forks is None or f > best_forks:
                    best_forks = f
                    best_info = info
    # If no match found or no forks parsed, try a fallback: look for just the repo name part (after '/') in Project_Information
    if best_forks is None:
        repo_fragment = pname.split('/')[-1]
        mask2 = proj_df['Project_Information'].astype(str).str.contains(repo_fragment, regex=False)
        matched2 = proj_df[mask2]
        if not matched2.empty:
            for info in matched2['Project_Information'].tolist():
                if pname in info:
                    f = parse_forks(info)
                    if f is not None:
                        if best_forks is None or f > best_forks:
                            best_forks = f
                            best_info = info
    # Final fallback: if still None, set to 0
    if best_forks is None:
        best_forks = 0
    results.append({'ProjectName': pname, 'Forks': best_forks, 'Matched_Info': best_info if best_info is not None else ''})

# Deduplicate by ProjectName (results already unique per project_name), sort by forks desc and take top 5
results_sorted = sorted(results, key=lambda x: x['Forks'], reverse=True)
top5 = results_sorted[:5]

# Prepare output (omit Matched_Info in final output to keep concise)
out = [{'ProjectName': r['ProjectName'], 'Forks': r['Forks']} for r in top5]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_TY47ktUAW7KCosFpvygKIODd': 'file_storage/call_TY47ktUAW7KCosFpvygKIODd.json', 'var_call_VDA1TzjNoz2T347LFnSvYFzG': 'file_storage/call_VDA1TzjNoz2T347LFnSvYFzG.json', 'var_call_Y5W4dmMrI2zRSJ3AJ2qSeVw9': 'file_storage/call_Y5W4dmMrI2zRSJ3AJ2qSeVw9.json'}

exec(code, env_args)
