code = """import json
import re
import pandas as pd

# Load data from storage variables (could be file paths or actual lists)
def load_var(v):
    if isinstance(v, str):
        # assume it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_latest = load_var(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y)
proj_pkg = load_var(var_call_CM29JjO0yMg1zMvvvwhYjq5L)
proj_info = load_var(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

df_pkg = pd.DataFrame(pkg_latest)
df_pkgver = pd.DataFrame(proj_pkg)
df_proj = pd.DataFrame(proj_info)

# Ensure columns exist
for c in ['System','Name','Version','ProjectName']:
    if c not in df_pkgver.columns:
        df_pkgver[c] = None

# Merge latest package records with project_packageversion
merged = pd.merge(df_pkg, df_pkgver, on=['System','Name','Version'], how='inner')

# Function to extract stars from Project_Information text
stars_re = re.compile(r"(\d[\d,]*)\s+stars", re.IGNORECASE)

def extract_stars(text, projname):
    if not isinstance(text, str):
        return None
    # only consider entries that mention the project name
    if projname not in text:
        return None
    matches = stars_re.findall(text)
    if not matches:
        return None
    # take the last match (most likely the stars count)
    s = matches[-1].replace(',', '')
    try:
        return int(s)
    except:
        return None

# For faster lookup, attempt to parse stars for all project_info entries
proj_info_stars = []
for row in df_proj.itertuples(index=False):
    info_text = row.Project_Information if 'Project_Information' in df_proj.columns else ''
    # try to extract owner/repo from the text: pattern 'The project owner/repo'
    # but we'll not rely on that; store text and parsed stars if any
    m = stars_re.findall(info_text)
    stars = None
    if m:
        stars = int(m[-1].replace(',', ''))
    proj_info_stars.append({'text': info_text, 'stars': stars})

# Now map merged rows to stars by searching project_info entries that contain the ProjectName
results = []
for r in merged.itertuples(index=False):
    projname = r.ProjectName
    stars = None
    if isinstance(projname, str):
        for pi in proj_info_stars:
            if projname in (pi['text'] or ''):
                if pi['stars'] is not None:
                    stars = pi['stars']
                    break
    if stars is None:
        # try a broader search: find any numeric 'X stars' in any project_info that also contains the repo last part
        # e.g., if projname is owner/repo, search for '/repo' or ' repo'
        short = projname.split('/')[-1] if isinstance(projname, str) else ''
        for pi in proj_info_stars:
            if short and short in (pi['text'] or '') and pi['stars'] is not None:
                stars = pi['stars']
                break
    if stars is None:
        stars = 0
    results.append({'Name': r.Name, 'Version': r.Version, 'ProjectName': r.ProjectName, 'Stars': int(stars)})

# Deduplicate by Name just in case (we already selected latest versions, but there may be duplicates)
# Keep the one with highest Stars per Name
res_df = pd.DataFrame(results)
if res_df.empty:
    top5 = []
else:
    res_df = res_df.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')
    top5_df = res_df.sort_values('Stars', ascending=False).head(5)
    top5 = top5_df.to_dict(orient='records')

# Build plain-text answer
lines = []
for i, item in enumerate(top5, start=1):
    lines.append(f"{i}. {item['Name']} {item['Version']} — {item['Stars']} stars ({item['ProjectName']})")
answer_text = "\n".join(lines)

output = {'text': answer_text, 'records': top5}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json'}

exec(code, env_args)
