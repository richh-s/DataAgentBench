code = """import json
import pandas as pd
import re
from datetime import datetime
import ast

# Load the first query result (patent data from publication_database)
patent_data = locals()['var_functions.query_db:2']

# Load the second query result (CPC level 5 symbols from CPCDefinition_database)
cpc_level5_data = locals()['var_functions.query_db:3']
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

# Convert patent data to DataFrame
df_patents = pd.DataFrame(patent_data)

# Parse the publication_date to extract year
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    try:
        # Extract year from patterns like "Aug 3rd, 2021", "Oct 6th, 2020", etc.
        match = re.search(r'(\d{4})', str(date_str))
        if match:
            return int(match.group(1))
        return None
    except:
        return None

df_patents['year'] = df_patents['publication_date'].apply(extract_year)

# Parse the cpc field (JSON-like string)
def parse_cpc(cpc_str):
    if pd.isna(cpc_str):
        return []
    try:
        cpc_list = ast.literal_eval(cpc_str)
        return cpc_list
    except:
        return []

df_patents['cpc_parsed'] = df_patents['cpc'].apply(parse_cpc)

# Filter patents from 2020-2022
min_year = 2020
max_year = 2022
mask = (df_patents['year'] >= min_year) & (df_patents['year'] <= max_year)
df_filtered = df_patents[mask].copy()

# Count patents by year and CPC code
from collections import defaultdict
cpc_year_counts = {}

for _, row in df_filtered.iterrows():
    year = row['year']
    if year is None:
        continue
    
    for cpc_entry in row['cpc_parsed']:
        code = cpc_entry.get('code', '')
        if not code:
            continue
        
        # Check if this CPC code starts with any level 5 symbol
        for level5_symbol in cpc_level5_symbols:
            if code.startswith(level5_symbol):
                if year not in cpc_year_counts:
                    cpc_year_counts[year] = defaultdict(int)
                cpc_year_counts[year][level5_symbol] += 1
                break

# Convert counts to DataFrame
years = sorted(cpc_year_counts.keys())
all_cpcs = set()
for year_counts in cpc_year_counts.values():
    all_cpcs.update(year_counts.keys())

# Create DataFrame with years as columns, CPCs as rows
df_counts = pd.DataFrame(index=sorted(all_cpcs), columns=years).fillna(0)

for year in years:
    for cpc_code in cpc_year_counts[year]:
        df_counts.loc[cpc_code, year] = cpc_year_counts[year][cpc_code]

# Calculate exponential moving average (smoothing factor 0.2)
alpha = 0.2

def calculate_ema(series):
    # Calculate exponential moving average with smoothing factor 0.2
    ema = pd.Series(index=series.index, dtype=float)
    ema.iloc[0] = series.iloc[0]
    
    for i in range(1, len(series)):
        ema.iloc[i] = alpha * series.iloc[i] + (1 - alpha) * ema.iloc[i-1]
    
    return ema

# Calculate EMA for each CPC code
ema_results = {}
for cpc_code in df_counts.index:
    ema_series = calculate_ema(df_counts.loc[cpc_code])
    ema_results[cpc_code] = ema_series

df_ema = pd.DataFrame(ema_results).T

# Find the year with the highest EMA for each CPC code
best_years = {}
for cpc_code in df_ema.index:
    max_ema = df_ema.loc[cpc_code].max()
    best_year = df_ema.loc[cpc_code].idxmax()
    best_years[cpc_code] = best_year

# Filter CPC codes whose best year is 2022
result_cpcs = [cpc for cpc, year in best_years.items() if year == max_year]

# Output the result
import json as js
print('__RESULT__:')
print(js.dumps(result_cpcs))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
