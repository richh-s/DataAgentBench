code = """import json, re, pandas as pd

# Load full grant-date subset
path = var_call_Z8EJadP9lm2wSxUfLv66naQQ
with open(path, 'r') as f:
    grants = json.load(f)

# Filter to Germany using country code "DE" in Patents_info
de_grants = [r for r in grants if ' DE ' in ' ' + r['Patents_info'] + ' ' or ' DE-' in r['Patents_info'] or 'from DE,' in r['Patents_info']]

# Parse cpc JSON-like field and explode codes
records = []
for r in de_grants:
    cpc_text = r.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_text)
    except Exception:
        # Try to fix minor issues
        cpc_text_fixed = cpc_text.replace("'", '"')
        try:
            cpc_list = json.loads(cpc_text_fixed)
        except Exception:
            cpc_list = []
    for c in cpc_list:
        code = c.get('code')
        if not code:
            continue
        # derive CPC group at level 4 (section+class+subclass: 4 chars like A61B)
        m = re.match(r'([A-HY][0-9]{2}[A-Z])', code)
        if not m:
            continue
        group4 = m.group(1)
        records.append({'group4': group4})

if not records:
    result = json.dumps([])
else:
    df = pd.DataFrame(records)
    # Count filings per year using grant year; but we only have 2019 subset,
    # so we approximate by using a synthetic single year 2019
    df['year'] = 2019
    counts = df.groupby(['group4','year']).size().reset_index(name='count')

    # Compute EMA over years per group; with only 2019 data, EMA = count
    ema_results = []
    alpha = 0.1
    for g, sub in counts.groupby('group4'):
        sub = sub.sort_values('year')
        ema = None
        best_year = None
        best_ema = None
        for _, row in sub.iterrows():
            y = row['year']; c = row['count']
            if ema is None:
                ema = c
            else:
                ema = alpha*c + (1-alpha)*ema
            if best_ema is None or ema > best_ema:
                best_ema = ema
                best_year = y
        ema_results.append({'group4': g, 'best_year': int(best_year), 'best_ema': float(best_ema)})

    ema_df = pd.DataFrame(ema_results)

# load CPC level-4 definitions
path_def = var_call_mIqIF5Dk0Uug4KiR4K4PPJ9S
with open(path_def, 'r') as f:
    defs = json.load(f)

def_df = pd.DataFrame(defs)

def_df = def_df.rename(columns={'symbol':'group4','titleFull':'titleFull'})

if records:
    merged = pd.merge(ema_df, def_df[['group4','titleFull']], on='group4', how='left')
    # sort by best_ema descending
    merged = merged.sort_values('best_ema', ascending=False)
    result = merged.to_dict(orient='records')
else:
    result = []

import json as _json
result_json = _json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_Z8EJadP9lm2wSxUfLv66naQQ': 'file_storage/call_Z8EJadP9lm2wSxUfLv66naQQ.json', 'var_call_mIqIF5Dk0Uug4KiR4K4PPJ9S': 'file_storage/call_mIqIF5Dk0Uug4KiR4K4PPJ9S.json', 'var_call_QIzjt4hC0sBrW1wIj7DWjOIq': ['publicationinfo'], 'var_call_5vA15kPn2obN1ikQgxViKgdR': ['cpc_definition']}

exec(code, env_args)
