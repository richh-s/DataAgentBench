code = """import json, re, pandas as pd

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

papers = load_maybe_path(var_call_8fMaorK3TSrjojq1oPQfLpMO)
cits = load_maybe_path(var_call_SfMGEro4SDvnESWaKsJVlOAm)

df_p = pd.DataFrame(papers)
df_p['title'] = df_p['filename'].str.replace(r'\\.txt$', '', regex=True)

# heuristic parse for publication year: look for 4-digit year near copyright/CHI line; choose earliest 19xx/20xx in [2000..2026]
years=[]
for txt in df_p['text'].fillna(''):
    found = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', txt)]
    found = [y for y in found if 2000 <= y <= 2026]
    years.append(min(found) if found else None)
df_p['pub_year'] = years

# domain match
mask = df_p['text'].str.contains(r'(?i)physical activity', regex=True, na=False) | df_p['title'].str.contains(r'(?i)physical activity', regex=True, na=False)
df_p = df_p[mask & (df_p['pub_year']==2016)][['title']].drop_duplicates()

# join with citations totals
cdf = pd.DataFrame(cits)
# coerce totals to int
cdf['total_citations'] = cdf['total_citations'].astype(int)
res = df_p.merge(cdf, on='title', how='left')
res = res.fillna({'total_citations':0})
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8fMaorK3TSrjojq1oPQfLpMO': 'file_storage/call_8fMaorK3TSrjojq1oPQfLpMO.json', 'var_call_SfMGEro4SDvnESWaKsJVlOAm': 'file_storage/call_SfMGEro4SDvnESWaKsJVlOAm.json'}

exec(code, env_args)
