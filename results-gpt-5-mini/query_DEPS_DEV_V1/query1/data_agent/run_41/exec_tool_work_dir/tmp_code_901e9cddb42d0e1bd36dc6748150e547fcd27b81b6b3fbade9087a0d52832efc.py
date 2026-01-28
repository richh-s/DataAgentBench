code = """import json
import pandas as pd

# helper to load either list or filepath
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_latest = load_var(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y)
proj_pkg = load_var(var_call_CM29JjO0yMg1zMvvvwhYjq5L)
proj_info = load_var(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

df_pkg = pd.DataFrame(pkg_latest)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Merge on System, Name, Version
if not {'System','Name','Version'}.issubset(df_proj_pkg.columns):
    # ensure columns exist
    for c in ['System','Name','Version','ProjectName']:
        if c not in df_proj_pkg.columns:
            df_proj_pkg[c] = None

merged = pd.merge(df_pkg, df_proj_pkg, on=['System','Name','Version'], how='inner')

# Function to extract stars by scanning for 'stars' tokens
def extract_stars_from_text(text, repo_fullname=None):
    if not isinstance(text, str):
        return None
    txt = text
    if repo_fullname and repo_fullname not in txt:
        return None
    stars_vals = []
    key = 'stars'
    idx = txt.lower().find(key)
    start = 0
    while idx != -1:
        # find digits/comma before idx
        i = idx - 1
        # skip spaces
        while i >= 0 and txt[i] == ' ':
            i -= 1
        # collect digits and commas
        j = i
        while j >= 0 and (txt[j].isdigit() or txt[j] == ','):
            j -= 1
        num_str = txt[j+1:i+1]
        if num_str:
            try:
                val = int(num_str.replace(',', ''))
                stars_vals.append(val)
            except:
                pass
        start = idx + len(key)
        idx = txt.lower().find(key, start)
    if stars_vals:
        return stars_vals[-1]
    return None

# Precompute stars for each project_info row
proj_info_list = []
for row in df_proj_info.itertuples(index=False):
    info_text = ''
    if 'Project_Information' in df_proj_info.columns:
        info_text = getattr(row, 'Project_Information')
    stars = extract_stars_from_text(info_text)
    proj_info_list.append({'text': info_text, 'stars': stars})

# Now for each merged row, try to find matching project_info entry that contains ProjectName
results = []
for r in merged.itertuples(index=False):
    projname = getattr(r, 'ProjectName', None)
    stars = None
    if isinstance(projname, str):
        for pi in proj_info_list:
            if projname in (pi['text'] or '') and pi['stars'] is not None:
                stars = pi['stars']
                break
    if stars is None:
        # try by repo short name
        short = projname.split('/')[-1] if isinstance(projname, str) and '/' in projname else projname
        if short:
            for pi in proj_info_list:
                if short in (pi['text'] or '') and pi['stars'] is not None:
                    stars = pi['stars']
                    break
    if stars is None:
        stars = 0
    results.append({'Name': getattr(r, 'Name'), 'Version': getattr(r, 'Version'), 'ProjectName': projname, 'Stars': int(stars)})

res_df = pd.DataFrame(results)
if res_df.empty:
    top5 = []
else:
    # In case multiple entries per package name, keep latest (we already have latest) and highest stars
    res_df = res_df.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')
    top5_df = res_df.sort_values('Stars', ascending=False).head(5)
    top5 = top5_df.to_dict(orient='records')

# Prepare text answer
lines = []
for i, item in enumerate(top5, start=1):
    lines.append(f"{i}. {item['Name']} {item['Version']} — {item['Stars']} stars ({item['ProjectName']})")
answer_text = "\n".join(lines)

output = {'text': answer_text, 'records': top5}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json'}

exec(code, env_args)
