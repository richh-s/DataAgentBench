code = """import json, re
import pandas as pd

# Load publications (may be a file path)
pubs = var_call_A1LyblK29yXwwoOIAwPiQmE3
if isinstance(pubs, str):
    with open(pubs, 'r', encoding='utf-8') as f:
        pubs = json.load(f)

# Load cpc definitions level 4 (file path)
defs = var_call_AGHCVaYHUo4BSqCbUjNOghMS
if isinstance(defs, str):
    with open(defs, 'r', encoding='utf-8') as f:
        defs = json.load(f)

def parse_year_filing(s):
    if not s:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_grant_second_half_2019(s):
    if not s or '2019' not in s:
        return False
    s_low = s.lower()
    months = ['july','august','september','october','november','december']
    return any(mon in s_low for mon in months)

def is_germany(pi):
    # try explicit country_code if present
    return '"country_code"' in pi and '"DE"' in pi

def cpc_codes_level4(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
    except Exception:
        return []
    codes = []
    for o in arr:
        code = o.get('code')
        if not code or '/' not in code:
            continue
        # level 4 here interpreted as CPC subclass (e.g., A61M) = first 4 chars of symbol
        codes.append(code[:4])
    return list(dict.fromkeys(codes))

rows = []
for r in pubs:
    if not parse_grant_second_half_2019(r.get('grant_date')):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fy = parse_year_filing(r.get('filing_date'))
    if fy is None:
        continue
    for g in cpc_codes_level4(r.get('cpc')):
        rows.append({'group4': g, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    counts = df.groupby(['group4','filing_year']).size().reset_index(name='filings')

    # compute EMA per group over years ascending
    alpha = 0.1
    def ema_best(sub):
        sub = sub.sort_values('filing_year')
        ema = None
        emas = []
        for _, rr in sub.iterrows():
            x = rr['filings']
            if ema is None:
                ema = x
            else:
                ema = alpha*x + (1-alpha)*ema
            emas.append(ema)
        sub = sub.copy()
        sub['ema'] = emas
        # best year: max ema; tie -> earliest year
        best = sub.sort_values(['ema','filing_year'], ascending=[False, True]).iloc[0]
        return pd.Series({'best_year': int(best['filing_year']), 'best_ema': float(best['ema'])})

    bests = counts.groupby('group4', as_index=False).apply(ema_best)

    # map titles from definitions: symbol exactly group4
    defdf = pd.DataFrame(defs)
    defdf['symbol'] = defdf['symbol'].astype(str)
    title_map = defdf.set_index('symbol')['titleFull'].to_dict() if not defdf.empty else {}
    bests['titleFull'] = bests['group4'].map(title_map)

    # highest ema groups
    bests = bests.sort_values(['best_ema','group4'], ascending=[False, True])
    out = bests[['titleFull','group4','best_year','best_ema']].rename(columns={'group4':'cpc_group_code'}).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_dHJEdralsnODmE40vsnyidQo': [], 'var_call_PcGoGfDSLd6nNsY4i6zIss2T': [], 'var_call_A1LyblK29yXwwoOIAwPiQmE3': 'file_storage/call_A1LyblK29yXwwoOIAwPiQmE3.json', 'var_call_AGHCVaYHUo4BSqCbUjNOghMS': 'file_storage/call_AGHCVaYHUo4BSqCbUjNOghMS.json'}

exec(code, env_args)
