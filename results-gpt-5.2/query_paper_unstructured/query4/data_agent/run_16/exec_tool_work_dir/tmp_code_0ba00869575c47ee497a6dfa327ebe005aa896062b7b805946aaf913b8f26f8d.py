code = """import json, re, pandas as pd

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

papers = load_maybe_path(var_call_fZH1JE6HGdaqiEJxAXKMPqqa)
cits = load_maybe_path(var_call_SfMGEro4SDvnESWaKsJVlOAm)

df = pd.DataFrame(papers)
df['title'] = df['filename'].str.replace(r'\\.txt$', '', regex=True)

def pub_year(txt):
    if not isinstance(txt, str):
        return None
    # Prefer explicit venue header lines like CHI '16 or UbiComp '16
    m = re.search(r"\b(?:CHI|UbiComp|CSCW|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth|AH)\s*'?\s*(\d{2})\b", txt)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy<=30 else 1900+yy
    # else earliest plausible year in 2000..2026
    yrs = [int(y) for y in re.findall(r'\b(20\d{2})\b', txt)]
    yrs = [y for y in yrs if 2000 <= y <= 2026]
    return min(yrs) if yrs else None

df['pub_year'] = [pub_year(t) for t in df['text'].tolist()]

# domain physical activity: substring match
mask = df['text'].str.contains(r'(?i)physical activity', regex=True, na=False) | df['title'].str.contains(r'(?i)physical activity', regex=True, na=False)
df = df[mask & (df['pub_year']==2016)][['title']].drop_duplicates()

cdf = pd.DataFrame(cits)
cdf['total_citations'] = cdf['total_citations'].astype(int)
res = df.merge(cdf, on='title', how='left').fillna({'total_citations':0})
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8fMaorK3TSrjojq1oPQfLpMO': 'file_storage/call_8fMaorK3TSrjojq1oPQfLpMO.json', 'var_call_SfMGEro4SDvnESWaKsJVlOAm': 'file_storage/call_SfMGEro4SDvnESWaKsJVlOAm.json', 'var_call_WfAIsipV2AOM0gr51VowBVz5': [], 'var_call_fZH1JE6HGdaqiEJxAXKMPqqa': 'file_storage/call_fZH1JE6HGdaqiEJxAXKMPqqa.json'}

exec(code, env_args)
