code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_IHDPGNvp1m5f0yM52i2CBGeE)

def is_pub_2016(text):
    t=text or ''
    # look for copyright or proceedings lines containing 2016, common patterns
    patterns=[r'\bCopyright\s+2016\b', r'\bCHI\s*2016\b', r'\bUbiComp\s*\'?16\b', r"\bUBICOMP\s*'16\b", r'\bCSCW\s*2016\b', r'\bDIS\s*2016\b', r'\bIUI\s*2016\b', r'\bWWW\s*2016\b', r'\b2016\s+ACM\b']
    return any(re.search(p, t, re.I) for p in patterns)

# domain physical activity based on keyword in author keywords or abstract etc.
pa_titles=set()
for d in papers:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    txt=d.get('text','')
    if re.search(r'\bphysical activity\b', txt, re.I):
        if is_pub_2016(txt):
            pa_titles.add(title)

pa_titles=sorted(pa_titles)

cit_raw=load_json_maybe(var_call_0WGoTfn8Cmqfs3SYw26g5IUG)
cit_list=cit_raw if isinstance(cit_raw, list) else cit_raw.get('data', [])
cit=pd.DataFrame.from_records(cit_list)
if not cit.empty:
    cit['citation_count']=cit['citation_count'].astype(int)

if pa_titles:
    totals=(cit[cit['title'].isin(pa_titles)].groupby('title', as_index=False)['citation_count'].sum()
            .rename(columns={'citation_count':'total_citations'}))
else:
    totals=pd.DataFrame(columns=['title','total_citations'])

res=totals.sort_values(['total_citations','title'], ascending=[False,True]).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_Ym0Bfg7pQCPkJUCBjzvNtpdG': 'file_storage/call_Ym0Bfg7pQCPkJUCBjzvNtpdG.json', 'var_call_0WGoTfn8Cmqfs3SYw26g5IUG': 'file_storage/call_0WGoTfn8Cmqfs3SYw26g5IUG.json', 'var_call_QxGSnvVsSHQ9aZlu8CsTo7Lf': {'titles_found': [], 'result': []}, 'var_call_IHDPGNvp1m5f0yM52i2CBGeE': 'file_storage/call_IHDPGNvp1m5f0yM52i2CBGeE.json'}

exec(code, env_args)
