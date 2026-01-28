code = """import json
import pandas as pd
import re

with open(var_call_K8WichaIoLyvFp4xd4Pf9vzG, 'r') as f:
    pkg_data = json.load(f)
with open(var_call_VTyoyOJxDeDqfOsSd5OyZYqZ, 'r') as f:
    ppv_data = json.load(f)
with open(var_call_wEWgMh0lZ5twsDGs3rZo8JAC, 'r') as f:
    projinfo_data = json.load(f)

pkg_df = pd.DataFrame(pkg_data)
ppv_df = pd.DataFrame(ppv_data)
proj_df = pd.DataFrame(projinfo_data)

def parse_json_field(x):
    try:
        return json.loads(x)
    except Exception:
        try:
            return json.loads(x.replace("'", '"'))
        except Exception:
            return None

def is_release(vinfo_str):
    v = parse_json_field(vinfo_str)
    if isinstance(v, dict):
        return v.get('IsRelease') is True
    return False

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(is_release)

def licenses_contain_mit(lic_str):
    arr = parse_json_field(lic_str)
    if isinstance(arr, list):
        for x in arr:
            try:
                if str(x).strip().lower() == 'mit':
                    return True
            except:
                continue
        return False
    if isinstance(lic_str, str):
        return 'mit' in lic_str.lower()
    return False

pkg_df['HasMIT'] = pkg_df['Licenses'].apply(licenses_contain_mit)
filtered_pkg = pkg_df[(pkg_df['IsRelease']) & (pkg_df['HasMIT'])][['System','Name','Version']].drop_duplicates()

merged = pd.merge(filtered_pkg, ppv_df, on=['System','Name','Version'], how='inner')
merged = merged[merged['ProjectType'].str.upper() == 'GITHUB']

project_names = merged['ProjectName'].dropna().unique().tolist()

results = []
for pname in project_names:
    # find project_info rows where Project_Information mentions the repo path
    mask = proj_df['Project_Information'].notna() & proj_df['Project_Information'].str.contains(pname, regex=False)
    matches = proj_df[mask]
    best_forks = None
    best_info = None
    if not matches.empty:
        for _, row in matches.iterrows():
            text = str(row['Project_Information'])
            # try common patterns to extract forks
            m = re.search(r"([0-9,]+)\s+forks?", text, flags=re.IGNORECASE)
            if m:
                f = int(m.group(1).replace(',', ''))
            else:
                m2 = re.search(r"forks?[^0-9]*([0-9,]+)", text, flags=re.IGNORECASE)
                if m2:
                    f = int(m2.group(1).replace(',', ''))
                else:
                    f = 0
            if (best_forks is None) or (f > best_forks):
                best_forks = f
                best_info = text
    results.append({'ProjectName': pname, 'Forks': best_forks, 'Project_Information': best_info})

res_df = pd.DataFrame(results)
if res_df.empty:
    out = []
else:
    res_df['Forks_sort'] = res_df['Forks'].fillna(0).astype(int)
    res_df = res_df.sort_values('Forks_sort', ascending=False).drop_duplicates('ProjectName')
    top5 = res_df.head(5)[['ProjectName','Forks','Project_Information']]
    out = []
    for _, r in top5.iterrows():
        out.append({'ProjectName': r['ProjectName'], 'Forks': int(r['Forks']) if (r['Forks'] is not None) else None, 'Project_Information': r['Project_Information']})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_K8WichaIoLyvFp4xd4Pf9vzG': 'file_storage/call_K8WichaIoLyvFp4xd4Pf9vzG.json', 'var_call_VTyoyOJxDeDqfOsSd5OyZYqZ': 'file_storage/call_VTyoyOJxDeDqfOsSd5OyZYqZ.json', 'var_call_wEWgMh0lZ5twsDGs3rZo8JAC': 'file_storage/call_wEWgMh0lZ5twsDGs3rZo8JAC.json'}

exec(code, env_args)
