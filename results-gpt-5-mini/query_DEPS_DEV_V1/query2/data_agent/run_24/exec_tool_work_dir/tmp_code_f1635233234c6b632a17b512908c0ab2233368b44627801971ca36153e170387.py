code = """import json
import pandas as pd
import re

# Load data: variables may be lists or file paths

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

pkg_rows = load_var(var_call_BZcjSy0XAwWM9yFmLVezWteR)
proj_pkg_rows = load_var(var_call_efOjKxIMfLz6hlrn6bSm7eCn)
proj_info_rows = load_var(var_call_cJuQVYSgPun4hBzOXnyxrgjj)

df_pkg = pd.DataFrame(pkg_rows)
df_proj_pkg = pd.DataFrame(proj_pkg_rows)
df_proj_info = pd.DataFrame(proj_info_rows)

# Ensure expected columns
for df,name in [(df_pkg,'pkg'),(df_proj_pkg,'proj_pkg'),(df_proj_info,'proj_info')]:
    if df.empty:
        pass

# Merge package rows with project_packageversion on System, Name, Version
merged = pd.merge(df_pkg, df_proj_pkg, on=['System','Name','Version'], how='inner')

# Get unique ProjectName values
project_names = merged['ProjectName'].dropna().unique().tolist()

# Prepare project_info search
# Filter project_info entries that have MIT in Licenses
def has_mit(licenses_str):
    if not isinstance(licenses_str, str):
        return False
    return 'MIT' in licenses_str

df_proj_info['HasMIT'] = df_proj_info['Licenses'].apply(has_mit)

# Function to extract forks from Project_Information text
num_re = re.compile(r"(\d{1,3}(?:,\d{3})*)\s+forks", flags=re.IGNORECASE)

def extract_forks(text):
    if not isinstance(text, str):
        return None
    m = num_re.search(text)
    if m:
        num = m.group(1).replace(',','')
        try:
            return int(num)
        except:
            return None
    # try alternate patterns like 'forks count of 123' or 'forks count: 123'
    m2 = re.search(r"forks(?: count)?(?: of|:)?\s*(\d{1,3}(?:,\d{3})*)", text, flags=re.IGNORECASE)
    if m2:
        num = m2.group(1).replace(',','')
        try:
            return int(num)
        except:
            return None
    return None

# Build mapping from project_name to forks where project_info HasMIT and Project_Information contains project_name
results = {}
for pn in project_names:
    # find proj_info rows where Project_Information contains pn and HasMIT True
    mask = df_proj_info['Project_Information'].astype(str).str.contains(pn, na=False)
    candidates = df_proj_info[mask & df_proj_info['HasMIT']]
    # If none, also consider entries where Project_Information contains just the repo name without owner? skip for now
    if candidates.empty:
        continue
    # Extract forks for each candidate
    max_forks = None
    selected_info = None
    for idx, row in candidates.iterrows():
        forks = extract_forks(row.get('Project_Information'))
        if forks is None:
            continue
        if (max_forks is None) or (forks > max_forks):
            max_forks = forks
            selected_info = row.get('Project_Information')
    if max_forks is not None:
        results[pn] = {'ProjectName': pn, 'Forks': max_forks, 'Project_Information': selected_info}

# If results less than 5, we might need to attempt matching by repo suffix (repo name only)
if len(results) < 5:
    # Build map from repo (owner/repo -> repo) and try matching by '/repo' ending
    proj_name_to_repo = {pn: pn.split('/')[-1] for pn in project_names}
    for pn, repo in proj_name_to_repo.items():
        if pn in results:
            continue
        mask = df_proj_info['Project_Information'].astype(str).str.contains('/' + repo + '\b', na=False)
        candidates = df_proj_info[mask & df_proj_info['HasMIT']]
        if candidates.empty:
            continue
        max_forks = None
        selected_info = None
        for idx, row in candidates.iterrows():
            forks = extract_forks(row.get('Project_Information'))
            if forks is None:
                continue
            if (max_forks is None) or (forks > max_forks):
                max_forks = forks
                selected_info = row.get('Project_Information')
        if max_forks is not None:
            results[pn] = {'ProjectName': pn, 'Forks': max_forks, 'Project_Information': selected_info}

# Prepare final list sorted by Forks desc
final_list = sorted(results.values(), key=lambda x: x['Forks'], reverse=True)
final_top5 = final_list[:5]

# Simplify output to ProjectName and Forks
out = [{'ProjectName': r['ProjectName'], 'Forks': r['Forks'], 'Project_Information': r['Project_Information']} for r in final_top5]

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_sbFCvRLxICwGvUhG1LCnlXqm': ['packageinfo'], 'var_call_xbZCtfHq1EXF20t2B1woGj8n': ['project_info', 'project_packageversion'], 'var_call_BZcjSy0XAwWM9yFmLVezWteR': 'file_storage/call_BZcjSy0XAwWM9yFmLVezWteR.json', 'var_call_efOjKxIMfLz6hlrn6bSm7eCn': 'file_storage/call_efOjKxIMfLz6hlrn6bSm7eCn.json', 'var_call_cJuQVYSgPun4hBzOXnyxrgjj': 'file_storage/call_cJuQVYSgPun4hBzOXnyxrgjj.json'}

exec(code, env_args)
