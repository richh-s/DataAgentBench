code = """import json
import pandas as pd
import numpy as np
import os

# Load the pivot table
group_matrix = pd.read_json('/tmp/group_matrix.json', orient='index')
print(f"Loaded matrix: {group_matrix.shape[0]} groups x {group_matrix.shape[1]} years")
print("Year range:", group_matrix.columns.min(), "to", group_matrix.columns.max())

# Sort columns by year
group_matrix = group_matrix.reindex(sorted(group_matrix.columns), axis=1)
print("Sorted year range:", group_matrix.columns.min(), "to", group_matrix.columns.max())

# Calculate EMA for each group
# EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
alpha = 0.2

# Initialize EMA matrix
ema_matrix = pd.DataFrame(index=group_matrix.index, columns=group_matrix.columns)

# For each group (row), calculate EMA across years
for group in group_matrix.index:
    values = group_matrix.loc[group].values
    ema = np.zeros_like(values, dtype=float)
    
    # First EMA = first value (common initialization)
    ema[0] = values[0]
    
    # Calculate EMA for subsequent years
    for i in range(1, len(values)):
        ema[i] = alpha * values[i] + (1 - alpha) * ema[i-1]
    
    ema_matrix.loc[group] = ema

print("EMA calculation completed")
print("Sample EMA values for first group:")
print(ema_matrix.iloc[0].head())

# For each group, find the year with highest EMA
best_years = {}
for group in ema_matrix.index:
    max_ema_idx = ema_matrix.loc[group].idxmax()
    max_ema_value = ema_matrix.loc[group].max()
    best_years[group] = {'year': int(max_ema_idx), 'ema_value': float(max_ema_value)}

print(f"\nBest years calculated for {len(best_years)} groups")
print("Sample best years:", list(best_years.items())[:5])

# Filter groups whose best year is 2022
groups_2022 = {group: info for group, info in best_years.items() if info['year'] == 2022}

print(f"\nGroups with best year = 2022: {len(groups_2022)}")

# Sort by EMA value descending to get top areas
groups_2022_sorted = sorted(groups_2022.items(), key=lambda x: x[1]['ema_value'], reverse=True)

print("\nTop 10 groups with best year 2022:")
for i, (group, info) in enumerate(groups_2022_sorted[:10]):
    print(f"{i+1}. {group}: EMA = {info['ema_value']:.2f}")

# Save results
result_codes = [group for group, info in groups_2022_sorted]

with open('/tmp/groups_best_2022.json', 'w') as f:
    json.dump(result_codes, f)

output = {
    "total_groups": len(group_matrix.index),
    "groups_best_2022": len(result_codes),
    "top_10": result_codes[:10] if result_codes else []
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'records': 2141569, 'level5_symbols': 677}, 'var_functions.execute_python:22': {'groups': 667, 'years': 186}}

exec(code, env_args)
