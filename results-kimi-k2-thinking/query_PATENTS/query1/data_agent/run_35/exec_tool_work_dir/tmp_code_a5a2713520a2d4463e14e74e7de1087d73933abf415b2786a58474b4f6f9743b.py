code = """import json
import pandas as pd
import numpy as np
import os

# Load data
print("Loading data...")
group_matrix = pd.read_json('/tmp/group_matrix.json', orient='index')
group_matrix = group_matrix.reindex(sorted(group_matrix.columns), axis=1)
print(f"Matrix: {group_matrix.shape}")

# Calculate EMA
alpha = 0.2
ema_matrix = pd.DataFrame(index=group_matrix.index, columns=group_matrix.columns)

for group in group_matrix.index:
    values = group_matrix.loc[group].values
    ema = np.zeros(len(values))
    
    if len(values) > 0:
        ema[0] = values[0]
        for i in range(1, len(values)):
            ema[i] = alpha * values[i] + (1 - alpha) * ema[i-1]
    
    ema_matrix.loc[group] = ema

print("EMA calculated")

# Find best year for each group
best_years = {}
for group in ema_matrix.index:
    year_values = ema_matrix.loc[group]
    max_year = int(year_values.idxmax())
    max_value = float(year_values.max())
    best_years[group] = {'year': max_year, 'ema': max_value}

# Filter for best year = 2022
groups_2022 = []
for group, info in best_years.items():
    if info['year'] == 2022:
        groups_2022.append((group, info['ema']))

# Sort by EMA value
groups_2022.sort(key=lambda x: x[1], reverse=True)
print(f"Groups with best year 2022: {len(groups_2022)}")

# Extract just the group codes
group_codes = [g[0] for g in groups_2022]

# Save
with open('/tmp/best_2022_groups.json', 'w') as f:
    json.dump(group_codes, f)

result = {
    "total_groups": int(group_matrix.shape[0]),
    "best_2022_count": len(group_codes),
    "top_10": group_codes[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'records': 2141569, 'level5_symbols': 677}, 'var_functions.execute_python:22': {'groups': 667, 'years': 186}}

exec(code, env_args)
