code = """import json, pandas as pd, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

cit = load_json_maybe(var_call_hcnHLgqGIlOnchZOmx6RhUpg)
files = load_json_maybe(var_call_ncmzi9YMBC2QrkTRZHn0voEK)

df_cit = pd.DataFrame(cit)
# coerce totals to int
if not df_cit.empty:
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)

# heuristic: physical activity domain papers usually have keywords in title
pa_pat = re.compile(r"(?i)(physical activity|activity track|fitness|step|steps|wearable|running|sedentary|exercise)")
pa_titles = []
for rec in files:
    fn = rec.get('filename','')
    title = re.sub(r"(?i)\\.txt$","",fn)
    if pa_pat.search(title):
        pa_titles.append(title)

# heuristic for published in 2016: use title known 2016? not available; approximate by citation table earliest year? can't.
# Since year extraction from docs is required, but docs text not returned. We will proceed by querying docs for these candidate titles and parse year/domain.
print('__RESULT__:')
print(json.dumps({'candidate_titles': pa_titles[:200], 'candidate_count': len(pa_titles)}))"""

env_args = {'var_call_ia5jYj489eBJUeMzScw2xf5n': [], 'var_call_hcnHLgqGIlOnchZOmx6RhUpg': 'file_storage/call_hcnHLgqGIlOnchZOmx6RhUpg.json', 'var_call_ncmzi9YMBC2QrkTRZHn0voEK': 'file_storage/call_ncmzi9YMBC2QrkTRZHn0voEK.json'}

exec(code, env_args)
