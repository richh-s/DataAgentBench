code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        import pathlib
        p = pathlib.Path(v)
        return json.loads(p.read_text(encoding='utf-8'))
    return v

pub = load_records(var_call_20k8zF9SkAKnR8sxAFvtxbUL)

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def is_h2_2019(grant):
    if not grant or '2019' not in grant:
        return False
    g = grant.lower()
    months = ['jul','aug','sep','oct','nov','dec']
    return any(m in g for m in months)

def get_country(pinfo):
    if not pinfo:
        return None
    m = re.search(r'Application\s*\([^)]*from\s+([A-Z]{2})', pinfo)
    if m:
        return m.group(1)
    m = re.search(r'\bfrom\s+([A-Z]{2})\b', pinfo)
    if m:
        return m.group(1)
    return None

def extract_lvl4(code):
    if not code:
        return None
    # take part before '/' then keep first 3 chars (section+class+subclass)
    pre = code.split('/')[0]
    pre = pre.strip()
    return pre[:3] if len(pre)>=3 else pre

rows=[]
for r in pub:
    if not is_h2_2019(r.get('grant_date')):
        continue
    if get_country(r.get('Patents_info'))!='DE':
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw,str) else (cpc_raw or [])
    except Exception:
        cpcs=[]
    codes=[]
    for c in cpcs:
        code = c.get('code') if isinstance(c,dict) else None
        lvl4 = extract_lvl4(code)
        if lvl4:
            codes.append(lvl4)
    for lvl4 in set(codes):
        rows.append({'lvl4':lvl4,'filing_year':fy})

df=pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    counts=df.groupby(['lvl4','filing_year']).size().reset_index(name='n')
    # build EMA per lvl4 sorted by year
    alpha=0.1
    best=[]
    for lvl4, g in counts.groupby('lvl4'):
        g=g.sort_values('filing_year')
        ema=None
        best_year=None
        best_ema=None
        for _,row in g.iterrows():
            n=row['n']
            ema = n if ema is None else alpha*n + (1-alpha)*ema
            if best_ema is None or ema>best_ema:
                best_ema=ema
                best_year=int(row['filing_year'])
        best.append({'lvl4':lvl4,'best_year':best_year,'best_ema':float(best_ema)})
    best_df=pd.DataFrame(best).sort_values('best_ema',ascending=False)
    # join titles
    cpcdef=load_records(var_call_aq7NOAmHU97i0X0Cr8Kmle32)
    def_df=pd.DataFrame(cpcdef).rename(columns={'symbol':'lvl4','titleFull':'titleFull'})
    merged=best_df.merge(def_df,on='lvl4',how='left')
    out=merged[['titleFull','lvl4','best_year','best_ema']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VSzlvifVG1SzqRZ5JvZKZmjj': [], 'var_call_kLkvFRTyLKeX15BZ7XeNwYst': [], 'var_call_20k8zF9SkAKnR8sxAFvtxbUL': 'file_storage/call_20k8zF9SkAKnR8sxAFvtxbUL.json', 'var_call_gNId7NZE3UpTVmIkkcVZgPYT': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0', 'status': 'published'}], 'var_call_6LW7JesvOKVJZneUYd6Ubwgc': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'status': 'published'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'status': 'published'}], 'var_call_aq7NOAmHU97i0X0Cr8Kmle32': 'file_storage/call_aq7NOAmHU97i0X0Cr8Kmle32.json'}

exec(code, env_args)
