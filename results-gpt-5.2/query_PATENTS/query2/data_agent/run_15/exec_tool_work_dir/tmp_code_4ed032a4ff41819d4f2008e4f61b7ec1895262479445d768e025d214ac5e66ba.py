code = """import json, re, pandas as pd
from datetime import datetime

# load records (may be file path)
rec_src = var_call_gDnNwNRtCFnzlbGJmcckEYmx
if isinstance(rec_src, str):
    with open(rec_src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = rec_src

months = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def grant_in_h2_2019(s):
    if not s:
        return False
    y = parse_year(s)
    if y != 2019:
        return False
    # check month names
    for mon in ['July','August','September','October','November','December']:
        if mon in s:
            return True
    return False

def is_germany(pinfo):
    if not pinfo:
        return False
    # country_code appears in text; use robust regex for DE token
    return bool(re.search(r'country_code\s*[:=]\s*DE\b', pinfo)) or bool(re.search(r'\bDE\b', pinfo))

def cpc_level4(code):
    if not code or '/' not in code:
        return None
    left, right = code.split('/',1)
    # main group = up to first 2 digits in right side
    m = re.match(r'(\d{1,2})', right)
    if not m:
        return None
    return f"{left}/{m.group(1)}"

def parse_title(title_localized):
    if not title_localized:
        return None
    try:
        arr = json.loads(title_localized)
        if isinstance(arr, list) and arr:
            # prefer en
            for o in arr:
                if o.get('language')=='en' and o.get('text'):
                    return o.get('text')
            return arr[0].get('text')
    except Exception:
        pass
    return title_localized

rows=[]
for r in recs:
    if not grant_in_h2_2019(r.get('grant_date')):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    title = parse_title(r.get('title_localized'))
    cpc_txt = r.get('cpc')
    try:
        cpcs = json.loads(cpc_txt) if cpc_txt else []
    except Exception:
        cpcs = []
    codes = []
    for c in cpcs:
        code = c.get('code') if isinstance(c, dict) else None
        lv4 = cpc_level4(code)
        if lv4:
            codes.append(lv4)
    # unique per patent to avoid repeats
    for lv4 in sorted(set(codes)):
        rows.append({'cpc4': lv4, 'filing_year': fy, 'title': title})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    # counts per year
    counts = df.groupby(['cpc4','filing_year']).size().reset_index(name='count')
    # compute EMA per group over years
    alpha=0.1
    res=[]
    for cpc4, g in counts.groupby('cpc4'):
        g2 = g.sort_values('filing_year')
        ema=None
        for _,row in g2.iterrows():
            x=row['count']
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            res.append({'cpc4': cpc4, 'year': int(row['filing_year']), 'ema': float(ema), 'count': int(x)})
    ema_df = pd.DataFrame(res)
    # best year per cpc4
    best = ema_df.sort_values(['cpc4','ema','year'], ascending=[True,False,True]).groupby('cpc4').head(1)
    best = best[['cpc4','year','ema']]
    # take top CPC areas by max ema
    best_top = best.sort_values('ema', ascending=False)
    out = best_top.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({'best_by_cpc4': out, 'n_patent_cpc_rows': int(len(df)), 'n_cpc4': int(df['cpc4'].nunique()) if not df.empty else 0}, ensure_ascii=False))"""

env_args = {'var_call_zTTF6hgPr56yqJylLZ3ayWfD': ['publicationinfo'], 'var_call_g21qzevV9CwhIBoT8wvFyvzk': ['cpc_definition'], 'var_call_b7r5nvohY7pKiN9t6Yv5QNXI': [], 'var_call_gDnNwNRtCFnzlbGJmcckEYmx': 'file_storage/call_gDnNwNRtCFnzlbGJmcckEYmx.json'}

exec(code, env_args)
