code = """import json
import re
import pandas as pd

# Load data from storage variables (file paths or lists)
def load_storage(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg_records = load_storage(var_call_o8SLiWMJRsK4fxvg0qTkAttS)
proj_pkg_records = load_storage(var_call_QJ6pMCoB4Vqsr1UsqErqSWhX)
proj_info_records = load_storage(var_call_NZ9pmDspDGoJDZYipDOKURGz)

# DataFrames
df_pkg = pd.DataFrame(pkg_records)
df_proj_pkg = pd.DataFrame(proj_pkg_records)
df_proj_info = pd.DataFrame(proj_info_records)

# Parse VersionInfo JSON-like strings to extract IsRelease and Ordinal
import math

def parse_versioninfo(v):
    if not isinstance(v, str) or not v.strip():
        return (None, None)
    try:
        j = json.loads(v)
        isrel = j.get('IsRelease')
        ordn = j.get('Ordinal')
        return (isrel, ordn)
    except Exception:
        # attempt crude parse
        isrel = None
        ordn = None
        if 'IsRelease' in v:
            m = re.search(r'"IsRelease"\s*:\s*(true|false)', v, re.IGNORECASE)
            if m:
                isrel = True if m.group(1).lower()=='true' else False
        m2 = re.search(r'"Ordinal"\s*:\s*(\d+)', v)
        if m2:
            ordn = int(m2.group(1))
        return (isrel, ordn)

# Apply only to NPM
if 'System' in df_pkg.columns:
    df_pkg = df_pkg[df_pkg['System']=='NPM'].copy()
else:
    df_pkg = df_pkg.copy()

isrels = []
ordinals = []
for vi in df_pkg.get('VersionInfo', []):
    isr, ordn = parse_versioninfo(vi)
    isrels.append(isr)
    ordinals.append(ordn if ordn is not None else -1)

df_pkg['IsRelease'] = isrels
df_pkg['Ordinal'] = ordinals

# Keep only releases
df_releases = df_pkg[df_pkg['IsRelease']==True].copy()

# For each Name, select row with max Ordinal. If Ordinal missing, fallback to max UpstreamPublishedAt
result_rows = []
for name, group in df_releases.groupby('Name'):
    # prefer max Ordinal
    g = group.copy()
    if g['Ordinal'].isnull().all() or (g['Ordinal']<=0).all():
        # fallback: use UpstreamPublishedAt
        try:
            g['UpstreamPublishedAt'] = pd.to_numeric(g['UpstreamPublishedAt'], errors='coerce')
            row = g.loc[g['UpstreamPublishedAt'].idxmax()]
        except Exception:
            row = g.iloc[-1]
    else:
        row = g.loc[g['Ordinal'].idxmax()]
    result_rows.append({'Name': row['Name'], 'Version': row['Version']})

df_latest = pd.DataFrame(result_rows)

# Build mapping from (System,Name,Version) to list of ProjectName
mapping = {}
for rec in proj_pkg_records:
    if rec.get('System')!='NPM':
        continue
    key = (rec.get('System'), rec.get('Name'), rec.get('Version'))
    mapping.setdefault(key, []).append(rec.get('ProjectName'))

# Preprocess project_info: extract stars for each Project_Information entry
# We'll also create a map from project_name -> stars by searching for project_name substring
projinfo_list = proj_info_records

# Precompute for each project_info entry the stars extracted (first match of number before 'star')
projinfo_stars = []
star_pattern = re.compile(r'([0-9,]+)\s+stars', re.IGNORECASE)
for rec in projinfo_list:
    pi = rec.get('Project_Information','') or ''
    m = star_pattern.search(pi)
    if m:
        stars = int(m.group(1).replace(',',''))
    else:
        stars = None
    projinfo_stars.append({'Project_Information': pi, 'Stars': stars})

# For faster lookup, for each project_name, find best matching stars among project_info entries that contain it
package_results = []
for _, lr in df_latest.iterrows():
    name = lr['Name']
    version = lr['Version']
    key = ('NPM', name, version)
    project_names = mapping.get(key, [])
    best = None
    best_proj = None
    for pn in project_names:
        if not pn:
            continue
        # search project_info entries containing pn
        pn_found = False
        best_for_pn = None
        for entry in projinfo_stars:
            if pn in entry['Project_Information']:
                pn_found = True
                if entry['Stars'] is not None:
                    if best_for_pn is None or entry['Stars']>best_for_pn:
                        best_for_pn = entry['Stars']
        # if found star for this project name, consider
        if pn_found and best_for_pn is not None:
            if best is None or best_for_pn>best:
                best = best_for_pn
                best_proj = pn
    if best is not None:
        package_results.append({'Name': name, 'Version': version, 'ProjectName': best_proj, 'Stars': int(best)})

# Sort and take top 5
package_results_sorted = sorted(package_results, key=lambda x: x['Stars'], reverse=True)
top5 = package_results_sorted[:5]

# Prepare result
import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_WbGLcZzdT8CLDlsy3ZN9r1YE': ['packageinfo'], 'var_call_IPjb4Ef28jMWwbXZFPr1KLzY': ['project_info', 'project_packageversion'], 'var_call_o8SLiWMJRsK4fxvg0qTkAttS': 'file_storage/call_o8SLiWMJRsK4fxvg0qTkAttS.json', 'var_call_QJ6pMCoB4Vqsr1UsqErqSWhX': 'file_storage/call_QJ6pMCoB4Vqsr1UsqErqSWhX.json', 'var_call_NZ9pmDspDGoJDZYipDOKURGz': 'file_storage/call_NZ9pmDspDGoJDZYipDOKURGz.json'}

exec(code, env_args)
