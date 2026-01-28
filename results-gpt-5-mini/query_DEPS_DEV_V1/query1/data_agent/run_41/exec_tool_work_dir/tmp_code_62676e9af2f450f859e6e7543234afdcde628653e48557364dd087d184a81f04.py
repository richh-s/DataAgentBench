code = """import json
import re
import pandas as pd

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

# Merge
if {'System','Name','Version'}.issubset(df_proj_pkg.columns):
    merged = pd.merge(df_pkg, df_proj_pkg, on=['System','Name','Version'], how='inner')
else:
    merged = pd.DataFrame()

# regex to find number before 'stars'
stars_re = re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE)

# build list of project_info texts
proj_texts = []
if 'Project_Information' in df_proj_info.columns:
    for row in df_proj_info['Project_Information'].astype(str):
        m = stars_re.findall(row)
        stars = None
        if m:
            try:
                stars = int(m[-1].replace(',', ''))
            except:
                stars = None
        proj_texts.append({'text': row, 'stars': stars})

results = []
if not merged.empty:
    for _, r in merged.iterrows():
        pname = r.get('ProjectName')
        stars = None
        if isinstance(pname, str):
            for pi in proj_texts:
                if pname in (pi['text'] or '') and pi['stars'] is not None:
                    stars = pi['stars']
                    break
        if stars is None and isinstance(pname, str):
            short = pname.split('/')[-1]
            for pi in proj_texts:
                if short and short in (pi['text'] or '') and pi['stars'] is not None:
                    stars = pi['stars']
                    break
        if stars is None:
            stars = 0
        results.append({'Name': r.get('Name'), 'Version': r.get('Version'), 'ProjectName': pname, 'Stars': int(stars)})

res = []
if results:
    df = pd.DataFrame(results)
    # remove duplicates keeping highest stars
    df = df.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates(subset=['Name'], keep='first')
    top5 = df.sort_values('Stars', ascending=False).head(5)
    res = top5.to_dict(orient='records')

# prepare text
lines = []
i = 1
for item in res:
    lines.append(str(i) + '. ' + str(item['Name']) + ' ' + str(item['Version']) + ' — ' + str(item['Stars']) + ' stars (' + str(item['ProjectName']) + ')')
    i += 1
answer_text = '\n'.join(lines)
output = {'text': answer_text, 'records': res}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json'}

exec(code, env_args)
