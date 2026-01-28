code = """import json
import pandas as pd
import re

# Load data from storage-provided variables
with open(var_call_j7zmgKmrvsp5ybiTbCwnR7cb, 'r', encoding='utf-8') as f:
    records = json.load(f)
with open(var_call_4bS3BVr6OsBb2s0Uz8jQT2Nq, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# helper
month_tokens = ['jul', 'july', 'aug', 'august', 'sep', 'sept', 'september', 'oct', 'october', 'nov', 'november', 'dec', 'december']

def is_h2_2019(grant_date_str):
    if not grant_date_str or '2019' not in grant_date_str:
        return False
    s = grant_date_str.lower()
    return any(tok in s for tok in month_tokens)


def extract_year(date_str):
    if not date_str:
        return None
    m = re.search(r"(19|20)\d{2}", date_str)
    if m:
        return int(m.group(0))
    return None


def extract_level4(code):
    if not code:
        return None
    code = code.strip()
    m = re.match(r"^([A-Z]{1,2}\d{2})", code)
    if m:
        return m.group(1)
    return None

# Filter records for patents granted in second half 2019 and in Germany (Patents_info contains 'DE' or 'from DE' or ' DE,' )
filtered = []
for r in records:
    pi = (r.get('Patents_info') or '').upper()
    if 'DE' not in pi and 'GERMANY' not in pi:
        continue
    gdate = r.get('grant_date') or r.get('publication_date') or ''
    if not is_h2_2019(gdate):
        continue
    filtered.append(r)

# Aggregate counts by level4 and filing year
counts = {}  # {(level4): {year: count}}
for r in filtered:
    filing = r.get('filing_date') or ''
    fyear = extract_year(filing)
    if fyear is None:
        # try publication_date
        fyear = extract_year(r.get('publication_date') or '')
    # parse cpc list
    cpc_field = r.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # attempt to fix single quotes
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpcs = []
    codes = []
    for entry in cpcs:
        if isinstance(entry, dict):
            code = entry.get('code')
        else:
            # unexpected format
            code = None
        lvl4 = extract_level4(code) if code else None
        if lvl4:
            codes.append(lvl4)
    # if no codes found, skip
    if not codes:
        continue
    for lvl4 in set(codes):  # count one patent once per level4 group
        counts.setdefault(lvl4, {})
        year_counts = counts[lvl4]
        if fyear is None:
            # attribute to year 2019 if unknown
            fyear = 2019
        year_counts[fyear] = year_counts.get(fyear, 0) + 1

# Prepare CPC title mapping
title_map = {d.get('symbol'): d.get('titleFull') for d in cpc_defs}

# Compute EMA per level4 across years
results = []
for lvl4, yc in counts.items():
    # create time series sorted by year
    ys = sorted(yc.items())  # list of (year, count)
    years = [y for y, c in ys]
    counts_list = [c for y, c in ys]
    s = pd.Series(counts_list, index=years)
    # compute EMA with alpha=0.1
    ema_series = s.ewm(alpha=0.1, adjust=False).mean()
    final_ema = float(ema_series.iloc[-1])
    # best year by raw count (if tie, choose most recent year)
    max_count = max(counts_list)
    best_year_candidates = [y for y, c in ys if c == max_count]
    best_year = max(best_year_candidates)
    results.append({
        'cpc_group': lvl4,
        'titleFull': title_map.get(lvl4) if title_map.get(lvl4) is not None else '',
        'final_ema': final_ema,
        'best_year': int(best_year),
        'best_year_count': int(max_count),
        'years_counts': {str(y): int(c) for y, c in ys}
    })

# Sort by final_ema descending
results_sorted = sorted(results, key=lambda x: x['final_ema'], reverse=True)

# Output results as JSON string
out = json.dumps(results_sorted, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Z5PoZcWzzIyT7pRX8yliI678': ['publicationinfo'], 'var_call_LnfXH01f9c1yhuNBTxMGkY9g': ['cpc_definition'], 'var_call_4bS3BVr6OsBb2s0Uz8jQT2Nq': 'file_storage/call_4bS3BVr6OsBb2s0Uz8jQT2Nq.json', 'var_call_CohP5PtAbNAEX1Iv7sZ2Slt1': [], 'var_call_EBFdTEThNj63VApSkxzjv60N': 'file_storage/call_EBFdTEThNj63VApSkxzjv60N.json', 'var_call_j7zmgKmrvsp5ybiTbCwnR7cb': 'file_storage/call_j7zmgKmrvsp5ybiTbCwnR7cb.json'}

exec(code, env_args)
