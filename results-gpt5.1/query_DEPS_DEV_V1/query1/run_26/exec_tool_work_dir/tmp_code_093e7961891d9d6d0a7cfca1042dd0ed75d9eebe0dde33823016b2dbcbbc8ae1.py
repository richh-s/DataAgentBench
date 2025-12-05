code = """import json, re, pandas as pd

ppv_file = var_call_z5bj9hrb9L2sl10uM2L3bbd0
info_file = var_call_6TrqMWXj0c1phKEIHGFu84gb

with open(ppv_file) as f:
    ppv = json.load(f)
with open(info_file) as f:
    info = json.load(f)

ppv_df = pd.DataFrame(ppv)
info_df = pd.DataFrame(info)

# extract repo name and stars from Project_Information
pat = re.compile(r"project ([^\s]+/[^\s]+).*?stars?,?\s+([0-9,]+)")

repos = []
stars = []
for txt in info_df['Project_Information']:
    m = pat.search(txt)
    if m:
        repos.append(m.group(1))
        stars.append(int(m.group(2).replace(',', '')))
    else:
        repos.append(None)
        stars.append(None)

info_df['ProjectName'] = repos
info_df['Stars'] = stars
info_df = info_df.dropna(subset=['ProjectName','Stars'])

# latest version per (System,Name) from ppv_df joined with packageinfo isn't strictly needed for stars; assume mapping any version ok, but we need latest per Name
# infer latest by max Version string within each Name; lexicographic approximation
latest_ppv = ppv_df.sort_values('Version').groupby(['System','Name']).tail(1)
latest_npm_ppv = latest_ppv[latest_ppv['System']=='NPM']

merged = latest_npm_ppv.merge(info_df[['ProjectName','Stars']], on='ProjectName', how='inner')

top5 = merged.sort_values('Stars', ascending=False).drop_duplicates('Name').head(5)

result = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MEaQ8Er8fplu6LkGdZVD9PA7': 'file_storage/call_MEaQ8Er8fplu6LkGdZVD9PA7.json', 'var_call_z5bj9hrb9L2sl10uM2L3bbd0': 'file_storage/call_z5bj9hrb9L2sl10uM2L3bbd0.json', 'var_call_tWMelHuUtYNLeD7hjuhbhXqg': {'proj_names_sample': ['djplaner/trimester-date', 'substack/jsonify', '947418354/boot-style', 'richmccartney/design-system-monorepo', 'mathe42/vite-plugin-serviceworker', 'substack/tty-browserify', 'docume/ntary', 'dynamicpunch/my-card', 'dwmt/catamaran', 'ebizltd/ebiz-kit'], 'count': 7853}, 'var_call_6TrqMWXj0c1phKEIHGFu84gb': 'file_storage/call_6TrqMWXj0c1phKEIHGFu84gb.json'}

exec(code, env_args)
