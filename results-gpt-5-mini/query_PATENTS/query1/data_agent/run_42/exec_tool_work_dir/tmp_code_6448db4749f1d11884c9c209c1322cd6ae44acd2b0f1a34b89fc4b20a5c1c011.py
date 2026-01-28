code = """import json
import re
import pandas as pd

# Load the query results from storage variables
pubs_var = var_call_wtmmWwn0WWan2n9Gyyf3RdAz
lvl5_var = var_call_vB2RFMdZHKCnZdt7bOiALVwe

# If the storage entries are file paths (strings), load JSON from file
if isinstance(pubs_var, str):
    with open(pubs_var, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pubs_var

if isinstance(lvl5_var, str):
    with open(lvl5_var, 'r', encoding='utf-8') as f:
        lvl5 = json.load(f)
else:
    lvl5 = lvl5_var

# Extract valid level-5 group symbols
valid_groups = set()
for r in lvl5:
    sym = r.get('symbol')
    if sym:
        valid_groups.add(sym.strip().upper())

# Helper to extract year from filing_date text
year_re = re.compile(r"(19|20)\d{2}")

# Count occurrences per (group, year)
counts = {}
min_year = None
max_year = None

for rec in pubs:
    filing = rec.get('filing_date')
    if not filing:
        continue
    m = year_re.search(filing)
    if not m:
        continue
    year = int(m.group(0))
    if min_year is None or year < min_year:
        min_year = year
    if max_year is None or year > max_year:
        max_year = year

    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field may be a JSON string or already parsed list
    cpc_list = None
    if isinstance(cpc_field, str):
        try:
            cpc_list = json.loads(cpc_field)
        except Exception:
            try:
                import ast
                cpc_list = ast.literal_eval(cpc_field)
            except Exception:
                cpc_list = None
    elif isinstance(cpc_field, list):
        cpc_list = cpc_field

    if not cpc_list:
        continue

    for entry in cpc_list:
        # entry may be dict with 'code'
        code = None
        if isinstance(entry, dict):
            code = entry.get('code')
        elif isinstance(entry, str):
            code = entry
        if not code or len(code) < 4:
            continue
        group = code[:4].upper()
        if group in valid_groups:
            counts.setdefault((group, year), 0)
            counts[(group, year)] += 1

# If no counts found, output empty list
if not counts:
    result = []
else:
    all_years = list(range(min_year, max_year + 1))
    # Build DataFrame: rows groups, columns years
    groups = sorted({g for (g, y) in counts.keys()})
    df = pd.DataFrame(0, index=groups, columns=all_years, dtype=float)
    for (g, y), cnt in counts.items():
        df.at[g, y] = cnt

    # Compute EMA per group across years with alpha=0.2
    best_year_for_group = {}
    for g in df.index:
        series = df.loc[g]
        # ensure sorted by year
        series = series.sort_index()
        ema = series.ewm(alpha=0.2, adjust=False).mean()
        # get year with highest EMA
        max_year = int(ema.idxmax())
        best_year_for_group[g] = max_year

    # Select groups whose best year is 2022
    result = [g for g, y in best_year_for_group.items() if y == 2022]
    result.sort()

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wtmmWwn0WWan2n9Gyyf3RdAz': 'file_storage/call_wtmmWwn0WWan2n9Gyyf3RdAz.json', 'var_call_vB2RFMdZHKCnZdt7bOiALVwe': 'file_storage/call_vB2RFMdZHKCnZdt7bOiALVwe.json'}

exec(code, env_args)
