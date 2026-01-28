code = """import json
import pandas as pd
import re

# Load query results from storage file paths
with open(var_call_8KxN0nFLAbi7c0aCEQ5RtEoc, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_WXS2YpZN3pXoSspY2qSoN4cw, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# Build mapping of level-4 symbol to titleFull
symbol_to_title = {rec['symbol']: rec.get('titleFull','') for rec in cpc_defs}
symbols = list(symbol_to_title.keys())
# Sort symbols by length descending to prefer longest match
symbols_sorted = sorted(symbols, key=lambda s: -len(s))

pairs = []  # (symbol, year)

year_re = re.compile(r"(19|20)\d{2}")

for rec in pubs:
    filing = rec.get('filing_date') or rec.get('grant_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # Some cpc fields might already be lists; if string, try to load
    entries = None
    if isinstance(cpc_field, list):
        entries = cpc_field
    else:
        try:
            entries = json.loads(cpc_field)
        except Exception:
            # try to cleanup and load
            try:
                cleaned = cpc_field.replace("\n", " ").strip()
                entries = json.loads(cleaned)
            except Exception:
                entries = []
    for e in entries:
        code = ''
        if isinstance(e, dict):
            code = e.get('code','')
        else:
            code = str(e)
        code = code.strip().upper()
        if not code:
            continue
        # Find matching level-4 symbol
        matched = None
        for sym in symbols_sorted:
            if code.startswith(sym):
                matched = sym
                break
        if matched:
            pairs.append((matched, year))

if not pairs:
    result = []
else:
    df = pd.DataFrame(pairs, columns=['symbol','year'])
    counts = df.groupby(['symbol','year']).size().reset_index(name='count')

    results = []
    for symbol, group in counts.groupby('symbol'):
        group = group.set_index('year').sort_index()
        miny = int(group.index.min())
        maxy = int(group.index.max())
        years = list(range(miny, maxy+1))
        counts_by_year = [int(group['count'].get(y, 0)) for y in years]
        s = pd.Series(counts_by_year, index=years)
        ema = s.ewm(alpha=0.1, adjust=False).mean()
        best_year = int(ema.idxmax())
        results.append({
            'cpc_group_code': symbol,
            'titleFull': symbol_to_title.get(symbol,'') ,
            'best_year': best_year
        })
    # sort results by cpc_group_code
    result = sorted(results, key=lambda x: x['cpc_group_code'])

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9J3kPk5xCwNnu25gsdahVGU2': 'file_storage/call_9J3kPk5xCwNnu25gsdahVGU2.json', 'var_call_WXS2YpZN3pXoSspY2qSoN4cw': 'file_storage/call_WXS2YpZN3pXoSspY2qSoN4cw.json', 'var_call_TyWkRIZH0aL2H70uKe4i5EGs': 'file_storage/call_TyWkRIZH0aL2H70uKe4i5EGs.json', 'var_call_8KxN0nFLAbi7c0aCEQ5RtEoc': 'file_storage/call_8KxN0nFLAbi7c0aCEQ5RtEoc.json'}

exec(code, env_args)
