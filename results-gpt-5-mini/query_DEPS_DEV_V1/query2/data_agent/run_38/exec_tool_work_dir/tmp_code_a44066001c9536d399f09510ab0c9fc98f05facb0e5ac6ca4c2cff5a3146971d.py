code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_K8WichaIoLyvFp4xd4Pf9vzG, 'r') as f:
    pkg_data = json.load(f)
with open(var_call_VTyoyOJxDeDqfOsSd5OyZYqZ, 'r') as f:
    ppv_data = json.load(f)
with open(var_call_wEWgMh0lZ5twsDGs3rZo8JAC, 'r') as f:
    projinfo_data = json.load(f)

pkg_df = pd.DataFrame(pkg_data)
ppv_df = pd.DataFrame(ppv_data)
proj_df = pd.DataFrame(projinfo_data)

# Helper to parse JSON-like fields safely
def parse_json_field(x):
    try:
        return json.loads(x)
    except Exception:
        # try single quotes fix
        try:
            return json.loads(x.replace("'", '"'))
        except Exception:
            return None

# Filter package rows: ensure IsRelease true and Licenses contains MIT
def is_release(vinfo_str):
    v = parse_json_field(vinfo_str)
    if isinstance(v, dict):
        return v.get('IsRelease') is True
    return False

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(is_release)

def licenses_contain_mit(lic_str):
    arr = parse_json_field(lic_str)
    if isinstance(arr, list):
        return any(str(x).strip().lower() == 'mit' for x in arr)
    # fallback search
    return isinstance(lic_str, str) and 'mit' in lic_str.lower()

pkg_df['HasMIT'] = pkg_df['Licenses'].apply(licenses_contain_mit)

filtered_pkg = pkg_df[(pkg_df['IsRelease']) & (pkg_df['HasMIT'])][['System','Name','Version']].drop_duplicates()

# Merge with project_packageversion on System, Name, Version
merged = pd.merge(filtered_pkg, ppv_df, on=['System','Name','Version'], how='inner')

# Keep only GitHub projects
merged = merged[merged['ProjectType'].str.upper()=='GITHUB']

# Get unique ProjectName values
project_names = merged['ProjectName'].dropna().unique().tolist()

# For each project_name, find matching project_info row(s) where Project_Information contains the project_name
results = []
for pname in project_names:
    # find rows where Project_Information contains pname
    mask = proj_df['Project_Information'].notna() & proj_df['Project_Information'].str.contains(pname, regex=False)
    matches = proj_df[mask]
    forks = None
    info_text = None
    if not matches.empty:
        # take first match (or the one with largest extracted forks)
        best_forks = -1
        best_info = None
        for _, row in matches.iterrows():
            text = str(row['Project_Information'])
            # attempt to extract forks number with several regex patterns
            f = None
            patterns = [r'forks?[^0-9\n]*?([0-9,]+)', r'forked[^0-9\n]*?([0-9,]+)', r'([0-9,]+)\s+forks?']
            for pat in patterns:
                m = re.search(pat, text, flags=re.IGNORECASE)
                if m:
                    try:
                        f = int(m.group(1).replace(',',''))
                        break
                    except:
                        continue
            if f is None:
                # try to find any number near 'stars' and 'forks' pattern; as fallback set 0
                f = 0
            if f > best_forks:
                best_forks = f
                best_info = text
        forks = best_forks if best_forks>=0 else None
        info_text = best_info
    else:
        forks = None
        info_text = None
    results.append({'ProjectName': pname, 'Forks': forks, 'Project_Information': info_text})

# Convert to DataFrame and get top 5 by forks (treat None as 0)
res_df = pd.DataFrame(results)
res_df['Forks_sort'] = res_df['Forks'].fillna(0).astype(int)
res_df = res_df.sort_values('Forks_sort', ascending=False).drop_duplicates('ProjectName')

top5 = res_df.head(5)[['ProjectName','Forks','Project_Information']]

# Prepare JSON-serializable output
out = []
for _, r in top5.iterrows():
    out.append({'ProjectName': r['ProjectName'], 'Forks': int(r['Forks']) if (r['Forks'] is not None) else None, 'Project_Information': r['Project_Information']})

result_json = json.dumps(out)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_K8WichaIoLyvFp4xd4Pf9vzG': 'file_storage/call_K8WichaIoLyvFp4xd4Pf9vzG.json', 'var_call_VTyoyOJxDeDqfOsSd5OyZYqZ': 'file_storage/call_VTyoyOJxDeDqfOsSd5OyZYqZ.json', 'var_call_wEWgMh0lZ5twsDGs3rZo8JAC': 'file_storage/call_wEWgMh0lZ5twsDGs3rZo8JAC.json'}

exec(code, env_args)
