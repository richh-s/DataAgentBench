code = """import json
import pandas as pd
import re
import ast
from collections import defaultdict

# Load full patent dataset
patent_file = locals()['var_functions.query_db:2']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Load CPC level 5 symbols
cpc_file = locals()['var_functions.query_db:3']
with open(cpc_file, 'r') as f:
    cpc_level5_data = json.load(f)
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

# Convert to DataFrame
df_patents = pd.DataFrame(patent_data)

# Extract year
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    match = re.search(r'(\d{4})', str(date_str))
    return int(match.group(1)) if match else None

df_patents['year'] = df_patents['publication_date'].apply(extract_year)

# Parse CPC codes
def parse_cpc(cpc_str):
    if pd.isna(cpc_str):
        return []
    try:
        return ast.literal_eval(cpc_str)
    except:
        return []

df_patents['cpc_parsed'] = df_patents['cpc'].apply(parse_cpc)

# Get available years and filter to recent years
available_years = sorted([y for y in df_patents['year'].unique() if y is not None])
year_range = available_years[-3:] if len(available_years) >= 3 else available_years

min_year = min(year_range)
max_year = max(year_range)

# Filter data
mask = (df_patents['year'] >= min_year) & (df_patents['year'] <= max_year)
df_filtered = df_patents[mask].copy()

# Count patents by CPC group level 5 and year
cpc_year_counts = {}

for _, row in df_filtered.iterrows():
    year = row['year']
    if year is None:
        continue
    
    for cpc_entry in row['cpc_parsed']:
        if not isinstance(cpc_entry, dict):
            continue
        code = cpc_entry.get('code', '')
        if not code:
            continue
        
        # Match to level 5 CPC group
        for level5_symbol in cpc_level5_symbols:
            if code.startswith(level5_symbol):
                if year not in cpc_year_counts:
                    cpc_year_counts[year] = defaultdict(int)
                cpc_year_counts[year][level5_symbol] += 1
                break

# Prepare data for EMA calculation
years = sorted(cpc_year_counts.keys())
all_cpcs = set()
for year_counts in cpc_year_counts.values():
    all_cpcs.update(year_counts.keys())

# Create DataFrame
df_counts = pd.DataFrame(index=sorted(all_cpcs), columns=years).fillna(0)
for year in years:
    for cpc_code in cpc_year_counts[year]:
        df_counts.loc[cpc_code, year] = cpc_year_counts[year][cpc_code]

# Calculate EMA (α = 0.2)
alpha = 0.2

def calculate_ema(series):
    if len(series) == 0:
        return series
    ema = pd.Series(index=series.index, dtype=float)
    ema.iloc[0] = series.iloc[0]
    for i in range(1, len(series)):
        ema.iloc[i] = alpha * series.iloc[i] + (1 - alpha) * ema.iloc[i-1]
    return ema

# Calculate EMA for each CPC
df_ema = pd.DataFrame(index=df_counts.index, columns=df_counts.columns)
for cpc in df_counts.index:
    df_ema.loc[cpc] = calculate_ema(df_counts.loc[cpc])

# Find CPCs with best year = max_year (2022 or latest year)
best_year_2022 = []
for cpc in df_ema.index:
    max_ema = df_ema.loc[cpc].max()
    if max_ema > 0:  # Only consider CPCs with actual data
        best_year = df_ema.loc[cpc].idxmax()
        if best_year == max_year:
            best_year_2022.append(cpc)

# Sort by EMA value (descending) to get "highest" first
ema_values_2022 = {cpc: df_ema.loc[cpc, max_year] for cpc in best_year_2022}
sorted_cpcs = sorted(ema_values_2022.items(), key=lambda x: x[1], reverse=True)
result_cpcs = [cpc for cpc, ema in sorted_cpcs]

print('__RESULT__:')
print(json.dumps(result_cpcs))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
