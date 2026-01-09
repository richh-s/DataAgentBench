code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

papers = load_json_maybe(var_call_4VYaIeVEDqzm0Z0t4SP4ttKp)
citations = load_json_maybe(var_call_TWhcQoF9rfbZrwClgmm2gLiO)

rows = []
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if 'empirical' not in text.lower():
        continue
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    pub_year = min(years) if years else None
    if pub_year is None or pub_year <= 2016:
        continue
    rows.append({'title': title, 'pub_year': pub_year})

papers_df = pd.DataFrame(rows)
if not papers_df.empty:
    papers_df = papers_df.drop_duplicates('title')
else:
    papers_df = pd.DataFrame(columns=['title','pub_year'])

cit_df = pd.DataFrame(citations)
# normalize/ensure columns
if 'title' not in cit_df.columns:
    cit_df['title'] = []
if 'total_citations' not in cit_df.columns:
    cit_df['total_citations'] = []

cit_df = cit_df[['title','total_citations']].copy()
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_O05e4rUsZ2q39PV166J8Xky7': 'file_storage/call_O05e4rUsZ2q39PV166J8Xky7.json', 'var_call_TWhcQoF9rfbZrwClgmm2gLiO': 'file_storage/call_TWhcQoF9rfbZrwClgmm2gLiO.json', 'var_call_4VYaIeVEDqzm0Z0t4SP4ttKp': 'file_storage/call_4VYaIeVEDqzm0Z0t4SP4ttKp.json', 'var_call_DvcNafxlXRkDBbEebAwe6teh': {'first_record': {'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, 'keys': ['title', 'total_citations']}}

exec(code, env_args)
