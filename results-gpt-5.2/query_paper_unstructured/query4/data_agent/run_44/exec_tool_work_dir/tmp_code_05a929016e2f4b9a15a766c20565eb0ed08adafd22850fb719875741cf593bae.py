code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_Ym0Bfg7pQCPkJUCBjzvNtpdG)

pa_titles=set()
for d in papers:
    fn=d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    txt=d.get('text','') or ''
    if (re.search(r'\bphysical activity\b', txt, re.I) or re.search(r'activity\s+tracking', txt, re.I) or re.search(r'\bfitbit\b', txt, re.I)) and re.search(r'\b2016\b', txt):
        pa_titles.add(title)

pa_titles=sorted(pa_titles)

cit_raw = load_json_maybe(var_call_0WGoTfn8Cmqfs3SYw26g5IUG)
if isinstance(cit_raw, dict):
    cit_list = cit_raw.get('data', [])
else:
    cit_list = cit_raw

cit = pd.DataFrame.from_records(cit_list) if isinstance(cit_list, list) else pd.DataFrame()
if not cit.empty:
    cit['citation_count']=cit['citation_count'].astype(int)

if pa_titles and not cit.empty:
    totals=(cit[cit['title'].isin(pa_titles)]
            .groupby('title', as_index=False)['citation_count'].sum()
            .rename(columns={'citation_count':'total_citations'}))
else:
    totals=pd.DataFrame(columns=['title','total_citations'])

res=totals.sort_values(['total_citations','title'], ascending=[False,True]).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'titles_found': pa_titles, 'result': res}, ensure_ascii=False))"""

env_args = {'var_call_Ym0Bfg7pQCPkJUCBjzvNtpdG': 'file_storage/call_Ym0Bfg7pQCPkJUCBjzvNtpdG.json', 'var_call_0WGoTfn8Cmqfs3SYw26g5IUG': 'file_storage/call_0WGoTfn8Cmqfs3SYw26g5IUG.json'}

exec(code, env_args)
