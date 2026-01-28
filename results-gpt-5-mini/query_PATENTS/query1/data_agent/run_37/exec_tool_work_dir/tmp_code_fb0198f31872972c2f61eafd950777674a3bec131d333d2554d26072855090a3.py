code = """import json
from collections import defaultdict, Counter

# Load inputs from storage file paths
with open(var_call_ntvOqoJioQfIao4fQ2Jz4C38, 'r') as f:
    cpc_defs = json.load(f)
with open(var_call_ktwux4MTTuogSRSaiwsspvpa, 'r') as f:
    pubs = json.load(f)

# Build set of level-5 CPC symbols
level5_symbols = set()
for r in cpc_defs:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym.strip().upper())

# Helper to extract year and group code
import re

year_re = re.compile(r"(\d{4})")

def extract_year(pub_date):
    if not pub_date:
        return None
    m = year_re.search(pub_date)
    if m:
        return int(m.group(1))
    return None


def extract_level5_group(code):
    if not code or len(code) < 4:
        return None
    return code[:4].upper()

# Count filings per group per year
counts = defaultdict(Counter)
for rec in pubs:
    cpc_field = rec.get('cpc')
    pub_date = rec.get('publication_date')
    year = extract_year(pub_date)
    if year is None:
        continue
    # parse cpc field which is a JSON-like string
    try:
        parsed = json.loads(cpc_field)
    except Exception:
        # skip malformed
        continue
    if not isinstance(parsed, list):
        continue
    seen_groups = set()
    for entry in parsed:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code:
            continue
        grp = extract_level5_group(code)
        if not grp:
            continue
        # Only consider groups that are in the level5_symbols
        if grp in level5_symbols:
            # Avoid double-counting same group in one publication (if duplicates in list)
            if grp in seen_groups:
                continue
            counts[grp][year] += 1
            seen_groups.add(grp)

# For each group compute EMA across years with alpha=0.2
alpha = 0.2
result_groups = []
for grp, counter in counts.items():
    if not counter:
        continue
    years = sorted(counter.keys())
    # compute ema chronologically
    ema_vals = {}
    ema = None
    for y in years:
        val = counter[y]
        if ema is None:
            ema = val
        else:
            ema = alpha * val + (1 - alpha) * ema
        ema_vals[y] = ema
    # find year with max ema
    best_year = max(ema_vals.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        result_groups.append(grp)

# Sort result
result_groups = sorted(result_groups)

import json as _json
print("__RESULT__:")
print(_json.dumps(result_groups))"""

env_args = {'var_call_ntvOqoJioQfIao4fQ2Jz4C38': 'file_storage/call_ntvOqoJioQfIao4fQ2Jz4C38.json', 'var_call_ktwux4MTTuogSRSaiwsspvpa': 'file_storage/call_ktwux4MTTuogSRSaiwsspvpa.json'}

exec(code, env_args)
