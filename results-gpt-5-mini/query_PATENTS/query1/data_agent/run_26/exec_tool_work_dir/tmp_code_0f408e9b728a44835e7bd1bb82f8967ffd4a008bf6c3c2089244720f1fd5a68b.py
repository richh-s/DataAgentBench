code = """import json
import re
from collections import defaultdict

# Load data from previous tool calls (file paths stored in variables)
with open(var_call_WKopyzRgmzrmo4rPLGhzwJWo, 'r', encoding='utf-8') as f:
    pubs = json.load(f)
with open(var_call_PK5ydIC28KvFy8Ojk78FJi8i, 'r', encoding='utf-8') as f:
    lvl5 = json.load(f)

level5_set = set()
for r in lvl5:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.upper())

# helper to extract year
year_re = re.compile(r'(19|20)\d{2}')

# counts per code per year
counts = defaultdict(lambda: defaultdict(int))
all_years = set()

for rec in pubs:
    filing = rec.get('filing_date') or ''
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    all_years.add(year)
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # fallback: try to eval-ish by replacing single quotes
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpc_list = []
    codes_in_rec = set()
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        code = code.strip().upper()
        if len(code) >= 4:
            lvl5_code = code[:4]
            codes_in_rec.add(lvl5_code)
    for code in codes_in_rec:
        counts[code][year] += 1

if not all_years:
    result = []
else:
    years = sorted(all_years)
    alpha = 0.2
    best_year_by_code = {}
    for code, year_dict in counts.items():
        # Only consider codes that are in level5_set
        if code not in level5_set:
            continue
        # build counts list in years order
        cnts = [year_dict.get(y, 0) for y in years]
        # compute EMA
        ema_vals = []
        if cnts:
            ema = cnts[0]
            ema_vals.append(ema)
            for c in cnts[1:]:
                ema = alpha * c + (1 - alpha) * ema
                ema_vals.append(ema)
            # find year of max ema (if multiple, take earliest year)
            max_idx = max(range(len(ema_vals)), key=lambda i: (ema_vals[i], -i))
            best_year = years[max_idx]
            best_year_by_code[code] = {
                'best_year': best_year,
                'max_ema': ema_vals[max_idx]
            }
    # select codes whose best_year is 2022
    selected = [code for code, info in best_year_by_code.items() if info['best_year'] == 2022]
    selected = sorted(selected)
    result = selected

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WKopyzRgmzrmo4rPLGhzwJWo': 'file_storage/call_WKopyzRgmzrmo4rPLGhzwJWo.json', 'var_call_PK5ydIC28KvFy8Ojk78FJi8i': 'file_storage/call_PK5ydIC28KvFy8Ojk78FJi8i.json'}

exec(code, env_args)
