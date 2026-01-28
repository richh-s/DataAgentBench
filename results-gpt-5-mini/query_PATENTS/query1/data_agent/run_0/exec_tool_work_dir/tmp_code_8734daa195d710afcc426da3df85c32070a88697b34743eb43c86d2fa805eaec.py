code = """import json
import re
import pandas as pd

# Load data from storage paths
with open(var_call_rjgYm0vc3wJr83WwATICSDhx, 'r') as f:
    level5_records = json.load(f)
with open(var_call_WvbFYp6A4UZpiwK3dOkmRhMH, 'r') as f:
    publications = json.load(f)

level5_symbols = set()
for r in level5_records:
    sym = r.get('symbol')
    if sym:
        level5_symbols.add(sym)

# Aggregate counts per group per year
group_year_counts = {}
for rec in publications:
    fd = rec.get('filing_date') or ''
    years_found = re.findall(r"(\d{4})", fd)
    if not years_found:
        continue
    year = int(years_found[-1])
    cpc_field = rec.get('cpc', '[]')
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        # If already a list or unparsable, skip
        if isinstance(cpc_field, list):
            cpcs = cpc_field
        else:
            continue
    groups_in_rec = set()
    for entry in cpcs:
        code = None
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, str):
            code = entry
        if not code or not isinstance(code, str):
            continue
        m = re.match(r'^([A-Z]\d{2}[A-Z])', code)
        if m:
            groups_in_rec.add(m.group(1))
    for g in groups_in_rec:
        group_year_counts.setdefault(g, {})
        group_year_counts[g][year] = group_year_counts[g].get(year, 0) + 1

# Determine global year range
all_years = set()
for counts in group_year_counts.values():
    all_years.update(counts.keys())
if not all_years:
    result = []
else:
    min_y, max_y = min(all_years), max(all_years)
    years = list(range(min_y, max_y + 1))

    result = []
    for g, counts in group_year_counts.items():
        if g not in level5_symbols:
            continue
        series = pd.Series([counts.get(y, 0) for y in years], index=years)
        ema = series.ewm(alpha=0.2, adjust=False).mean()
        best_year = int(ema.idxmax())
        if best_year == 2022:
            result.append(g)

# Sort result for consistency
result = sorted(result)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DRtsE5tXs9Verfup7KIiCbTJ': ['publicationinfo'], 'var_call_3C4ifW8sGUX2BRgMEHnLKXZl': ['cpc_definition'], 'var_call_rjgYm0vc3wJr83WwATICSDhx': 'file_storage/call_rjgYm0vc3wJr83WwATICSDhx.json', 'var_call_WvbFYp6A4UZpiwK3dOkmRhMH': 'file_storage/call_WvbFYp6A4UZpiwK3dOkmRhMH.json'}

exec(code, env_args)
