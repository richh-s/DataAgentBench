code = """import json
import pandas as pd
import re
from collections import defaultdict

# The query results are stored in files -- open them
with open(locals()['var_functions.query_db:2'], 'r') as f:
    patent_data = json.load(f)

with open(locals()['var_functions.query_db:3'], 'r') as f:
    cpc_level5_data = json.load(f)

cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

# Convert patent data to DataFrame
df_patents = pd.DataFrame(patent_data)

# Extract year from publication_date
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    match = re.search(r'(\d{4})', str(date_str))
    return int(match.group(1)) if match else None

df_patents['year'] = df_patents['publication_date'].apply(extract_year)

# Parse CPC codes (JSON-like string to list)
import ast

def parse_cpc(cpc_str):
    if pd.isna(cpc_str):
        return []
    try:
        return ast.literal_eval(cpc_str)
    except:
        return []

df_patents['cpc_parsed'] = df_patents['cpc'].apply(parse_cpc)

# Filter to reasonable year range (let's use available years)
available_years = sorted([y for y in df_patents['year'].unique() if y is not None])
if len(available_years) >= 3:
    # Use the last 3 years of data
    year_range = available_years[-3:]
elif len(available_years) >= 2:
    year_range = available_years[-2:]
else:
    year_range = available_years

min_year = min(year_range)
max_year = max(year_range)

mask = (df_patents['year'] >= min_year) & (df_patents['year'] <= max_year)
df_filtered = df_patents[mask].copy()

# Count patents by year and CPC group (level 5)
cpc_year_counts = {}

for _, row in df_filtered.iterrows():
    year = row['year']
    if year is None:
        continue
    
    for cpc_entry in row['cpc_parsed']:
        code = cpc_entry.get('code', '') if isinstance(cpc_entry, dict) else ''
        if not code:
            continue
        
        # Find matching level 5 CPC group
        for level5_symbol in cpc_level5_symbols:
            if code.startswith(level5_symbol):
                if year not in cpc_year_counts:
                    cpc_year_counts[year] = defaultdict(int)
                cpc_year_counts[year][level5_symbol] += 1
                break

# Build counts DataFrame
years = sorted(cpc_year_counts.keys())
all_cpcs = set()
for year_counts in cpc_year_counts.values():
    all_cpcs.update(year_counts.keys())

df_counts = pd.DataFrame(index=sorted(all_cpcs), columns=years).fillna(0)

for year in years:
    for cpc_code in cpc_year_counts[year]:
        df_counts.loc[cpc_code, year] = cpc_year_counts[year][cpc_code]

# Calculate exponential moving average (α = 0.2)
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

# Find best year for each CPC
best_years = {}
for cpc in df_ema.index:
    max_ema = df_ema.loc[cpc].max()
    best_year = df_ema.loc[cpc].idxmax()
    best_years[cpc] = (best_year, max_ema)

# Sort by EMA value to find "highest" EMA
top_cpcs = sorted(best_years.items(), key=lambda x: x[1][1], reverse=True)

# Filter those with best year = 2022
result_cpcs = [
    cpc for cpc, (year, ema) in top_cpcs 
    if year == 2022 and ema > 0
]

print('__RESULT__:')
print(json.dumps(result_cpcs))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
