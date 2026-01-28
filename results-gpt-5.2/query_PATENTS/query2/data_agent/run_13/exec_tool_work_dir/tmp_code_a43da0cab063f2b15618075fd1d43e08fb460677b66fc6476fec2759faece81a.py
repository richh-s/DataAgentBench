code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

top = var_call_X1bnhUauoYlJTHlujmFfdmpn
if isinstance(top, str):
    top = json.loads(top)

defs = load_records(var_call_VfAtSuHBQJhMUUezPau61QCk)
df_defs = pd.DataFrame(defs)
# some symbols might include deeper like B41F; ensure present
sym_set = set(df_defs['symbol'].astype(str))
need = sorted({r['cpc4'] for r in top if r.get('cpc4')})
missing = [s for s in need if s not in sym_set]

# fetch missing from DB? can't here; just output missing list and also map by prefix if available
# try mapping by first 3 (class without subclass) e.g., B41 from B41F
pref_map = dict(zip(df_defs['symbol'].astype(str), df_defs['titleFull']))
for r in top:
    s = r['cpc4']
    title = pref_map.get(s)
    if title is None:
        title = pref_map.get(s[:3]) or pref_map.get(s[:2])
    r['titleFull'] = title

print('__RESULT__:')
print(json.dumps({'records':top,'missing_level4_titles':missing}, ensure_ascii=False))"""

env_args = {'var_call_bBfYdt6KQ8sln8ezNnwuqDD2': 'file_storage/call_bBfYdt6KQ8sln8ezNnwuqDD2.json', 'var_call_wjIpy3xP5pd73QvLuzhX5YKH': 'file_storage/call_wjIpy3xP5pd73QvLuzhX5YKH.json', 'var_call_X1bnhUauoYlJTHlujmFfdmpn': [{'year': 2007, 'cpc4': 'B41F', 'titleFull': nan, 'ema': 3.0, 'best_year': 2007, 'best_ema': 3.0}, {'year': 2008, 'cpc4': 'H01L', 'titleFull': nan, 'ema': 6.0, 'best_year': 2008, 'best_ema': 6.0}, {'year': 2011, 'cpc4': 'F16C', 'titleFull': nan, 'ema': 3.0, 'best_year': 2011, 'best_ema': 3.0}, {'year': 2012, 'cpc4': 'E02F', 'titleFull': nan, 'ema': 5.0, 'best_year': 2012, 'best_ema': 5.0}, {'year': 2014, 'cpc4': 'B63B', 'titleFull': nan, 'ema': 1.0, 'best_year': 2014, 'best_ema': 1.0}, {'year': 2015, 'cpc4': 'H04W', 'titleFull': nan, 'ema': 22.0, 'best_year': 2015, 'best_ema': 22.0}, {'year': 2016, 'cpc4': 'A61F', 'titleFull': nan, 'ema': 6.0, 'best_year': 2016, 'best_ema': 6.0}], 'var_call_VfAtSuHBQJhMUUezPau61QCk': 'file_storage/call_VfAtSuHBQJhMUUezPau61QCk.json'}

exec(code, env_args)
