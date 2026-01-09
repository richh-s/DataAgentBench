code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_gLgGpdpueJPJoVfHEm7YgdpG)
levels = load_records(var_call_kjHpQtcbLwKxYtbb3n0bYP5E)

lvl5 = set(r['symbol'] for r in levels if r.get('symbol'))

month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def parse_year(s):
    if not s: return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_codes(cpc_str):
    if not cpc_str: return []
    try:
        data = json.loads(cpc_str)
        codes = []
        for e in data:
            c = e.get('code')
            if c: codes.append(c)
        return codes
    except Exception:
        # fallback: extract patterns like H01M10/0565
        return re.findall(r'\b[A-HY]\d{2}[A-Z]\d+(?:/\d+)?\b', cpc_str)

rows=[]
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None: 
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    for c in set(codes):
        grp = c.split('/')[0]  # group code e.g., H01M10
        # keep only level-5 group codes (e.g., H01M) => if grp length>4, take first 4? Actually lvl5 symbols are 4 chars like H01M
        sym = grp[:4]
        if sym in lvl5:
            rows.append((sym, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # build year range per symbol for EMA
    alpha=0.2
    res=[]
    for sym, g in counts.groupby('symbol'):
        g = g.sort_values('year')
        years = list(range(int(g['year'].min()), int(g['year'].max())+1))
        m = g.set_index('year')['filings'].to_dict()
        ema=None
        best_year=None
        best_ema=None
        for yr in years:
            x = float(m.get(yr,0))
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            if best_ema is None or ema>best_ema:
                best_ema=ema
                best_year=yr
        if best_year==2022:
            res.append(sym)
    out = sorted(set(res))

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gLgGpdpueJPJoVfHEm7YgdpG': 'file_storage/call_gLgGpdpueJPJoVfHEm7YgdpG.json', 'var_call_kjHpQtcbLwKxYtbb3n0bYP5E': 'file_storage/call_kjHpQtcbLwKxYtbb3n0bYP5E.json'}

exec(code, env_args)
