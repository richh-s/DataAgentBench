code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_1ZpCQhYra0k0tBTyDdaLHB9D)
levels = load_records(var_call_kI1p8bLG8n0M8E43T00DuOKS)

lvl5 = set(r['symbol'] for r in levels if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

# parse year from natural language dates
year_re = re.compile(r'(19|20)\d{2}')

def parse_year(s):
    if not s:
        return None
    m = year_re.search(s)
    if not m:
        return None
    return int(m.group(0))

# parse CPC codes list

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for it in arr:
            c = it.get('code') if isinstance(it, dict) else None
            if c:
                codes.append(c)
        return codes
    except Exception:
        # fallback regex for codes like A01B1/00
        return re.findall(r'\b[A-HY]\d{2}[A-Z]\d+(?:/\d+)?\b', cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # count each level-5 group code once per publication
    grp = set()
    for c in codes:
        # level-5 in provided definition set seems to be 4-char subclass like H04L, A61K, etc.
        g = c.replace(' ', '')[:4]
        if g in lvl5:
            grp.add(g)
    for g in grp:
        rows.append((g, y, 1))

df = pd.DataFrame(rows, columns=['symbol','year','n'])
if df.empty:
    out = []
else:
    annual = df.groupby(['symbol','year'], as_index=False)['n'].sum()
    # compute EMA per symbol over years
    alpha = 0.2
    out_rows = []
    for sym, g in annual.groupby('symbol'):
        g2 = g.sort_values('year').copy()
        ema = None
        for _, row in g2.iterrows():
            val = float(row['n'])
            ema = val if ema is None else alpha*val + (1-alpha)*ema
            out_rows.append((sym, int(row['year']), ema))
    ema_df = pd.DataFrame(out_rows, columns=['symbol','year','ema'])
    # for each year, find max EMA and keep ties
    ema_df['ema_rank'] = ema_df.groupby('year')['ema'].rank(method='min', ascending=False)
    top = ema_df[ema_df['ema_rank']==1].copy()
    # determine best year (max ema) for each symbol among years where it is top
    best = top.sort_values(['symbol','ema','year'], ascending=[True,False,False]).groupby('symbol', as_index=False).first()
    # filter best year 2022
    res = best[best['year']==2022]['symbol'].sort_values().unique().tolist()
    out = res

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1ZpCQhYra0k0tBTyDdaLHB9D': 'file_storage/call_1ZpCQhYra0k0tBTyDdaLHB9D.json', 'var_call_kI1p8bLG8n0M8E43T00DuOKS': 'file_storage/call_kI1p8bLG8n0M8E43T00DuOKS.json'}

exec(code, env_args)
