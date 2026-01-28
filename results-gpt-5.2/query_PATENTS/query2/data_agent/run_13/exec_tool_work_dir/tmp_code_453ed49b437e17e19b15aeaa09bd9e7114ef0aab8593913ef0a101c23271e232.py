code = """import json, ast

def load_any(v):
    if isinstance(v, str):
        if v.endswith('.json'):
            with open(v,'r',encoding='utf-8') as f:
                return json.load(f)
        try:
            return json.loads(v)
        except Exception:
            # replace bare NaN tokens if present
            txt = v.replace('NaN','None').replace('nan','None')
            return ast.literal_eval(txt)
    return v

top = load_any(var_call_X1bnhUauoYlJTHlujmFfdmpn)
defs = load_any(var_call_VfAtSuHBQJhMUUezPau61QCk)

pref_map = {d['symbol']: d['titleFull'] for d in defs}
need = sorted({r['cpc4'] for r in top if r.get('cpc4')})
missing = [s for s in need if s not in pref_map]
for r in top:
    s=r['cpc4']
    r['titleFull']=pref_map.get(s) or pref_map.get(s[:3]) or pref_map.get(s[:2])

print('__RESULT__:')
print(json.dumps({'records':top,'missing_level4_titles':missing}, ensure_ascii=False))"""

env_args = {'var_call_bBfYdt6KQ8sln8ezNnwuqDD2': 'file_storage/call_bBfYdt6KQ8sln8ezNnwuqDD2.json', 'var_call_wjIpy3xP5pd73QvLuzhX5YKH': 'file_storage/call_wjIpy3xP5pd73QvLuzhX5YKH.json', 'var_call_X1bnhUauoYlJTHlujmFfdmpn': [{'year': 2007, 'cpc4': 'B41F', 'titleFull': nan, 'ema': 3.0, 'best_year': 2007, 'best_ema': 3.0}, {'year': 2008, 'cpc4': 'H01L', 'titleFull': nan, 'ema': 6.0, 'best_year': 2008, 'best_ema': 6.0}, {'year': 2011, 'cpc4': 'F16C', 'titleFull': nan, 'ema': 3.0, 'best_year': 2011, 'best_ema': 3.0}, {'year': 2012, 'cpc4': 'E02F', 'titleFull': nan, 'ema': 5.0, 'best_year': 2012, 'best_ema': 5.0}, {'year': 2014, 'cpc4': 'B63B', 'titleFull': nan, 'ema': 1.0, 'best_year': 2014, 'best_ema': 1.0}, {'year': 2015, 'cpc4': 'H04W', 'titleFull': nan, 'ema': 22.0, 'best_year': 2015, 'best_ema': 22.0}, {'year': 2016, 'cpc4': 'A61F', 'titleFull': nan, 'ema': 6.0, 'best_year': 2016, 'best_ema': 6.0}], 'var_call_VfAtSuHBQJhMUUezPau61QCk': 'file_storage/call_VfAtSuHBQJhMUUezPau61QCk.json'}

exec(code, env_args)
