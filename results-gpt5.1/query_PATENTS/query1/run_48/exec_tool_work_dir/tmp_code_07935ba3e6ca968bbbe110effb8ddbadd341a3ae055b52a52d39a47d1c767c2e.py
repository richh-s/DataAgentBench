code = """import json, pandas as pd, datetime
from datetime import datetime

# load full symbol level-5 list
with open(var_call_2fHRqZjatqHmC308r8serlC2, 'r') as f:
    level5 = json.load(f)
level5_set = set(r['symbol'] for r in level5)

# load publication data
with open(var_call_xFmWjqA87UcOhM7t1cpGprRh, 'r') as f:
    pubs = json.load(f)

records = []
for r in pubs:
    date_str = r['publication_date']
    if not date_str:
        continue
    try:
        # parse like 'Aug 3rd, 2021'
        date_clean = date_str.replace('st','').replace('nd','').replace('rd','').replace('th','')
        dt = datetime.strptime(date_clean, '%b %d, %Y')
    except Exception:
        continue
    year = dt.year
    if year is None:
        continue
    cpc_str = r['cpc']
    if not cpc_str:
        continue
    try:
        cpc_list = json.loads(cpc_str)
    except Exception:
        continue
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # normalize CPC symbol form: keep as-is, but also strip spaces
        sym = code.replace(' ', '')
        # map to level-5 prefix: take up to first space or full symbol; here compare startswith any level5 symbol
        # To be efficient, check exact or prefix match where level5 symbol is prefix of sym
        for s in level5_set:
            if sym.startswith(s):
                records.append({'year': year, 'symbol': s, 'count': 1})
                break

if not records:
    result = json.dumps([])
else:
    df = pd.DataFrame(records)
    grp = df.groupby(['symbol','year'])['count'].sum().reset_index()
    # compute EMA per symbol over years
    ema_rows = []
    alpha = 0.2
    for sym, sub in grp.sort_values(['symbol','year']).groupby('symbol'):
        ema = None
        for _, row in sub.iterrows():
            y = int(row['year'])
            c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            ema_rows.append({'symbol': sym, 'year': y, 'ema': float(ema)})
    ema_df = pd.DataFrame(ema_rows)
    # find best year for each symbol
    best = ema_df.sort_values(['symbol','ema','year'], ascending=[True,False,True]).groupby('symbol').first().reset_index()
    # filter best year == 2022
    out = best[best['year']==2022]['symbol'].sort_values().tolist()
    result = json.dumps(out)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_2fHRqZjatqHmC308r8serlC2': 'file_storage/call_2fHRqZjatqHmC308r8serlC2.json', 'var_call_xFmWjqA87UcOhM7t1cpGprRh': 'file_storage/call_xFmWjqA87UcOhM7t1cpGprRh.json', 'var_call_Ki3nozq6TF64VIjKfkRoSVGR': [{'any_symbol': 'A'}], 'var_call_B47HtQKTFaqG82cTCbcPHg5E': [{'n': '277813'}]}

exec(code, env_args)
