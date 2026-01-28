code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

latest_df = pd.DataFrame(load_records(var_call_g1fm6eUvyVnnJpURKPCqQdKj))
ppv_df = pd.DataFrame(load_records(var_call_ARjOrtyN7tkr12WKKpms1n3O))
pi = load_records(var_call_wflmjMBsRVXEHklUWMBHxqGH)

merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

repo_re = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
stars_re = re.compile(r"([0-9,]+)\s+stars")

rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m_repo = repo_re.search(txt)
    m_stars = stars_re.search(txt)
    if m_repo and m_stars:
        rows.append({'ProjectName': m_repo.group(0), 'Stars': int(m_stars.group(1).replace(',',''))})

stars_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(stars_df, on='ProjectName', how='left').dropna(subset=['Stars'])

best = merged2.sort_values(['System','Name','Stars'], ascending=[True, True, False]).drop_duplicates(subset=['System','Name'])
top5 = best.sort_values('Stars', ascending=False).head(5)

out = top5[['Name','Version','ProjectName','Stars']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json', 'var_call_IBrNSDvMfnv3jfKQamNJ8heQ': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'ncols': 4, 'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_0xhBUaBnto81g7HSpNr1oQWV': {'merged_cols': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}]}, 'var_call_g8YLSokAr1uGRucKV2PWspX9': {'stars_cols': [], 'stars_head': []}, 'var_call_W5eDliJIn8iwgaSg9uCYTMxv': {'count_repo': 0, 'count_stars': 0, 'count_both': 0, 'examples': []}, 'var_call_dLutFnTAI5w0fQ13s9y8ZrFO': [{'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}, {'Project_Information': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.'}, {'Project_Information': 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.'}, {'Project_Information': 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.'}, {'Project_Information': 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'}], 'var_call_aflEVGnPrGq769S4qkBMetEy': {'repo': None, 'stars': None}, 'var_call_oU9pE2qTpvkC8ReiyCE1GsdY': {'matches': ['leaflet/leaflet'], 'stars': ['38715 stars']}}

exec(code, env_args)
