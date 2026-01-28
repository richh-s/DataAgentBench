code = """import json, re
import pandas as pd

# Load only 2022 filings
with open(var_call_uGL7yfBy0gxazcXZk4Qu4Dvm, 'r') as f:
    pubs2022 = json.load(f)

# Also load level5 symbols
with open(var_call_HGBQbuxNdnnzD4ENXdiFYLWw, 'r') as f:
    level5_rows = json.load(f)

level5_set = set()
for r in level5_rows:
    sym = r.get('symbol')
    if sym:
        level5_set.add(sym.strip().upper())

rows = []
for rec in pubs2022:
    filing = rec.get('filing_date')
    if not filing or not isinstance(filing, str):
        continue
    m = re.search(r'(\d{4})', filing)
    if not m:
        continue
    year = int(m.group(1))
    if year != 2022:
        continue
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    if not isinstance(cpcs, list):
        continue
    for entry in cpcs:
        if not isinstance(entry, dict):
            continue
        code = entry.get('code')
        if not code or not isinstance(code, str):
            continue
        code = code.strip().upper()
        group = code[:4]
        if group in level5_set:
            rows.append({'group': group, 'year': year})

# Count occurrences per group in 2022
if not rows:
    result = []
else:
    df2022 = pd.DataFrame(rows)
    counts2022 = df2022.groupby('group').size().to_dict()
    # For each group found in 2022, we need to compute EMA across years and see if best year is 2022
    # So we'll load all publication filings for groups present in 2022 from full dataset

# Load full publications (but to avoid timeouts, query only groups in counts2022)
groups_in_2022 = sorted(counts2022.keys()) if rows else []

# If no groups, return empty
if not groups_in_2022:
    result = []
else:
    # Query full DB for filing_date and cpc for rows where cpc contains any of these groups
    # We'll fetch all rows and parse — but to limit size, we'll read original large file (var_call_DHxRw7whb1bB1OxlQkXmpnLJ)
    with open(var_call_DHxRw7whb1bB1OxlQkXmpnLJ, 'r') as f:
        all_pubs = json.load(f)
    rows_all = []
    for rec in all_pubs:
        filing = rec.get('filing_date')
        if not filing or not isinstance(filing, str):
            continue
        m = re.search(r'(\d{4})', filing)
        if not m:
            continue
        year = int(m.group(1))
        cpc_field = rec.get('cpc')
        if not cpc_field:
            continue
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            try:
                cpcs = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                continue
        if not isinstance(cpcs, list):
            continue
        present_groups = set()
        for entry in cpcs:
            if not isinstance(entry, dict):
                continue
            code = entry.get('code')
            if not code or not isinstance(code, str):
                continue
            code = code.strip().upper()
            group = code[:4]
            if group in groups_in_2022:
                present_groups.add(group)
        for g in present_groups:
            rows_all.append({'group': g, 'year': year})
    if not rows_all:
        result = []
    else:
        df_all = pd.DataFrame(rows_all)
        min_year = int(df_all['year'].min())
        max_year = int(df_all['year'].max())
        years = list(range(min_year, max_year+1))
        winners = []
        import numpy as np
        for g in groups_in_2022:
            sub = df_all[df_all['group']==g]
            counts = sub.groupby('year').size().reindex(years, fill_value=0).sort_index()
            ema = counts.ewm(alpha=0.2, adjust=False).mean()
            max_ema = float(ema.max())
            years_with_max = [int(y) for y,v in zip(counts.index, ema) if np.isclose(v, max_ema)]
            if 2022 in years_with_max:
                winners.append(g)
        result = sorted(winners)

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DHxRw7whb1bB1OxlQkXmpnLJ': 'file_storage/call_DHxRw7whb1bB1OxlQkXmpnLJ.json', 'var_call_HGBQbuxNdnnzD4ENXdiFYLWw': 'file_storage/call_HGBQbuxNdnnzD4ENXdiFYLWw.json', 'var_call_uGL7yfBy0gxazcXZk4Qu4Dvm': 'file_storage/call_uGL7yfBy0gxazcXZk4Qu4Dvm.json'}

exec(code, env_args)
