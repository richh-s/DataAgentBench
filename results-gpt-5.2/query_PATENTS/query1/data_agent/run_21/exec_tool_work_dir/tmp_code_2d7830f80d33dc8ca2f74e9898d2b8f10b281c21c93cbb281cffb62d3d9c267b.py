code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pub = load_records(var_call_zSKD24osnh7UtFsVccO2NC9q)
level5 = load_records(var_call_VLtXqT1Lb48BT47rZEWqDqLG)

level5_set = set(r['symbol'] for r in level5 if r.get('symbol'))

month_map = {m.lower(): i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'], start=1)}

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def extract_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for e in arr if isinstance(arr, list) else []:
            code = e.get('code') if isinstance(e, dict) else None
            if code:
                code = code.strip()
                grp = code.split('/')[0]
                if grp in level5_set:
                    codes.append(grp)
        return list(set(codes))
    except Exception:
        # fallback regex
        found = re.findall(r'"code"\s*:\s*"([A-Z]\\d{2}[A-Z]\d*(?:/\\d+)?)"', cpc_str)
        codes = []
        for code in found:
            grp = code.split('/')[0]
            if grp in level5_set:
                codes.append(grp)
        return list(set(codes))

rows = []
for r in pub:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    codes = extract_codes(r.get('cpc'))
    for c in codes:
        rows.append((y,c))

if not rows:
    out = []
else:
    df = pd.DataFrame(rows, columns=['year','cpc5'])
    counts = df.groupby(['cpc5','year']).size().reset_index(name='filings')

    # compute EMA per cpc5 over sorted years
    alpha = 0.2
    best = []
    for cpc5, g in counts.groupby('cpc5'):
        g2 = g.sort_values('year').copy()
        ema = None
        emas = []
        for _, row in g2.iterrows():
            x = float(row['filings'])
            ema = x if ema is None else alpha*x + (1-alpha)*ema
            emas.append(ema)
        g2['ema'] = emas
        # best year by ema, tie -> latest year
        max_ema = g2['ema'].max()
        best_year = int(g2.loc[g2['ema']==max_ema,'year'].max())
        best.append((cpc5, best_year, float(max_ema)))

    best_df = pd.DataFrame(best, columns=['cpc5','best_year','best_ema'])
    out = sorted(best_df[best_df['best_year']==2022]['cpc5'].unique().tolist())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSKD24osnh7UtFsVccO2NC9q': 'file_storage/call_zSKD24osnh7UtFsVccO2NC9q.json', 'var_call_VLtXqT1Lb48BT47rZEWqDqLG': 'file_storage/call_VLtXqT1Lb48BT47rZEWqDqLG.json'}

exec(code, env_args)
