code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_ex7rxYtLX4WRsvY4aA6SASIo)
levels = load_records(var_call_3CRdHnk9TxhKhGVkjYp9uDIW)

lvl5 = set(r['symbol'] for r in levels if r.get('symbol') is not None)

# extract year
month_map = {m.lower():i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

# parse CPC JSON-like list; dedupe codes per publication
cpc_re = re.compile(r'"code"\s*:\s*"([A-Z]\d{2}[A-Z]\d[^\"]*)"')

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    # try json
    try:
        data = json.loads(cpc_str)
        codes = []
        for it in data:
            code = it.get('code')
            if isinstance(code, str):
                codes.append(code)
        return codes
    except Exception:
        return cpc_re.findall(cpc_str)

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    if not codes:
        continue
    # normalize to group code at level 5: main group before '/'
    groups = set()
    for c in codes:
        c = c.strip()
        if '/' in c:
            grp = c.split('/')[0]
        else:
            grp = c
        groups.add(grp)
    # keep only those groups that are level5 symbols
    for g in groups:
        if g in lvl5:
            rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    # counts per year per symbol
    counts = df.groupby(['symbol','year']).size().reset_index(name='filings')
    # build complete year range per symbol
    def ema_for_symbol(sub):
        sub = sub.sort_values('year')
        years = list(range(int(sub['year'].min()), int(sub['year'].max())+1))
        m = sub.set_index('year')['filings'].to_dict()
        alpha = 0.2
        ema = None
        recs = []
        for y in years:
            x = float(m.get(y, 0))
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            recs.append((y, ema))
        # best year by EMA (if tie, choose latest year)
        best = sorted(recs, key=lambda t: (t[1], t[0]))[-1]
        return best[0], best[1]

    bests = counts.groupby('symbol').apply(lambda s: pd.Series(ema_for_symbol(s), index=['best_year','best_ema'])).reset_index()
    out = sorted(bests[bests['best_year']==2022]['symbol'].tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ex7rxYtLX4WRsvY4aA6SASIo': 'file_storage/call_ex7rxYtLX4WRsvY4aA6SASIo.json', 'var_call_3CRdHnk9TxhKhGVkjYp9uDIW': 'file_storage/call_3CRdHnk9TxhKhGVkjYp9uDIW.json'}

exec(code, env_args)
