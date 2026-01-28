code = """import json
import pandas as pd
import re

# Load the large results stored in files (paths provided in the environment variables)
with open(var_call_Ww1OqiepXYb3VPVb9tBSOidL, 'r', encoding='utf-8') as f:
    pub_records = json.load(f)
with open(var_call_EDjUl9M3Vo2grncR9RDQ5K1a, 'r', encoding='utf-8') as f:
    cpc_level5_records = json.load(f)

# Extract set of level-5 symbols from cpc_definition query
level5_set = set()
for r in cpc_level5_records:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip().upper())

# Build year-group occurrences
rows = []
for rec in pub_records:
    pub_date = rec.get('publication_date')
    if not pub_date:
        continue
    m = re.search(r'(19|20)\d{2}', pub_date)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    # cpc_field is a stringified JSON list; attempt to parse
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        # if parsing fails, skip
        continue
    groups = set()
    for entry in cpc_list:
        code = entry.get('code') if isinstance(entry, dict) else None
        if not code or len(code) < 4:
            continue
        grp = code.strip().upper()[:4]
        groups.add(grp)
    for g in groups:
        rows.append({'year': year, 'group': g, 'count': 1})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows)
    # Aggregate counts per year/group
    agg = df.groupby(['group','year'], as_index=False).sum()
    # Determine full year range
    min_year = agg['year'].min()
    max_year = agg['year'].max()
    years = list(range(min_year, max_year+1))

    # Prepare DataFrame for EMA computation
    groups = sorted(agg['group'].unique())
    count_matrix = []
    for g in groups:
        row_counts = []
        grp_df = agg[agg['group']==g].set_index('year')
        for y in years:
            row_counts.append(int(grp_df['count'].get(y, 0)))
        count_matrix.append(row_counts)
    counts_df = pd.DataFrame(count_matrix, index=groups, columns=years)

    # Compute EMA with smoothing factor alpha=0.2
    ema_df = counts_df.T.ewm(alpha=0.2, adjust=False).mean().T
    # ema_df rows: groups, columns: years

    # For each group, find the year where EMA is maximum
    best_years = {}
    for g in ema_df.index:
        series = ema_df.loc[g]
        # find the year(s) with max EMA
        max_val = series.max()
        # If all zeros, skip
        if max_val <= 0:
            continue
        # choose the year where it attains max (if multiple, pick the latest year)
        # but user asked best year is 2022, so exact equality required
        best_year = int(series.idxmax())
        best_years[g] = best_year

    # Filter groups that are in level5_set and whose best year is 2022
    result = [g for g, y in best_years.items() if y == 2022 and g in level5_set]
    result = sorted(result)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ww1OqiepXYb3VPVb9tBSOidL': 'file_storage/call_Ww1OqiepXYb3VPVb9tBSOidL.json', 'var_call_EDjUl9M3Vo2grncR9RDQ5K1a': 'file_storage/call_EDjUl9M3Vo2grncR9RDQ5K1a.json'}

exec(code, env_args)
