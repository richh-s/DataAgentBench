code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

level5_syms = load_records(var_call_Taupbn2DqrklH5m7qzokADuS)
pubrecs = load_records(var_call_X9vADTpaB389uTlW5xAPk1zf)

level5_set = set(r['symbol'] for r in level5_syms if r.get('symbol'))

# Extract year from natural-language filing_date
month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    # try json
    try:
        data = json.loads(cpc_str)
        codes = []
        if isinstance(data, list):
            for it in data:
                if isinstance(it, dict) and 'code' in it:
                    codes.append(it['code'])
                elif isinstance(it, str):
                    codes.append(it)
        return codes
    except Exception:
        # fallback regex for patterns like A01B 33/00 etc
        return re.findall(r'([A-HY]\d{2}[A-Z]\s*\d+\/\d+)', cpc_str)

rows = []
for r in pubrecs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    if not codes:
        continue
    # map to level5 group code: first 4 chars (e.g., H01M) and must be in level5_set
    groups = set()
    for c in codes:
        c = c.strip().replace(' ', '')
        if len(c) >= 4:
            g = c[:4]
            if g in level5_set:
                groups.add(g)
    for g in groups:
        rows.append((g, y))

df = pd.DataFrame(rows, columns=['symbol','year'])
if df.empty:
    out = []
else:
    counts = df.value_counts(['symbol','year']).reset_index(name='filings')
    # build complete year ranges per symbol
    alpha = 0.2
    winners = []
    for sym, gdf in counts.groupby('symbol'):
        gdf = gdf.sort_values('year')
        years = list(range(int(gdf['year'].min()), int(gdf['year'].max())+1))
        s = pd.Series(0.0, index=years)
        for _, rr in gdf.iterrows():
            s.loc[int(rr['year'])] = float(rr['filings'])
        ema = s.ewm(alpha=alpha, adjust=False).mean()
        best_year = int(ema.idxmax())
        winners.append((sym, best_year, float(ema.loc[best_year])))
    win_df = pd.DataFrame(winners, columns=['symbol','best_year','best_ema'])
    out = sorted(win_df.loc[win_df['best_year']==2022, 'symbol'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Taupbn2DqrklH5m7qzokADuS': 'file_storage/call_Taupbn2DqrklH5m7qzokADuS.json', 'var_call_X9vADTpaB389uTlW5xAPk1zf': 'file_storage/call_X9vADTpaB389uTlW5xAPk1zf.json'}

exec(code, env_args)
