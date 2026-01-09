code = """import json, re, pandas as pd

def load_mongo(path_or_list):
    if isinstance(path_or_list, str):
        with open(path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_list

papers = load_mongo(var_call_Ym0Bfg7pQCPkJUCBjzvNtpdG)

# Heuristic: domain physical activity if text contains 'physical activity' or 'activity tracking' etc.
pa_papers = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    txt = d.get('text','')
    if re.search(r'\bphysical activity\b', txt, re.I) or re.search(r'activity\s+tracking', txt, re.I) or re.search(r'\bfitbit\b', txt, re.I):
        # publication year: look for 2016 near copyright/venue lines; simplest: require '2016' somewhere and exclude cases where only later year appears in obvious way.
        # We'll accept if regex finds ' 2016' and not exclusively in references; approximate.
        if re.search(r'\b2016\b', txt):
            pa_papers.append({'title': title})

pa_titles = sorted(set([p['title'] for p in pa_papers]))

cit = pd.DataFrame(var_call_0WGoTfn8Cmqfs3SYw26g5IUG)
if not cit.empty:
    cit['citation_count'] = cit['citation_count'].astype(int)

# total citations (all years) for those titles
if pa_titles:
    cit_f = cit[cit['title'].isin(pa_titles)]
    totals = cit_f.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    totals = pd.DataFrame(columns=['title','total_citations'])

res = totals.sort_values(['total_citations','title'], ascending=[False, True]).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps({'titles_found': pa_titles, 'result': res}, ensure_ascii=False))"""

env_args = {'var_call_Ym0Bfg7pQCPkJUCBjzvNtpdG': 'file_storage/call_Ym0Bfg7pQCPkJUCBjzvNtpdG.json', 'var_call_0WGoTfn8Cmqfs3SYw26g5IUG': 'file_storage/call_0WGoTfn8Cmqfs3SYw26g5IUG.json'}

exec(code, env_args)
