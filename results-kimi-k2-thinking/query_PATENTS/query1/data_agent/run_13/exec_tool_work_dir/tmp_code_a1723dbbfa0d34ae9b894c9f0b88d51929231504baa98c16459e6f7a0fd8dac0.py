code = """import json
import pandas as pd
import re
import ast
from collections import defaultdict

# Load CPC level 5 symbols (smaller file)
cpc_file = locals()['var_functions.query_db:3']
with open(cpc_file, 'r') as f:
    cpc_level5_data = json.load(f)
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

# Initialize counters
cpc_year_counts = defaultdict(lambda: defaultdict(int))

# Process patent data in batches to avoid memory/time issues
patent_file = locals()['var_functions.query_db:2']

# First, let's see what years we have
max_records = 50000  # Limit to avoid timeout
all_years = set()

with open(patent_file, 'r') as f:
    # Load as JSON array
    data = json.load(f)
    
    # Extract years to find the range
    for record in data[:min(len(data), max_records)]:
        pub_date = record.get('publication_date', '')
        if pub_date:
            match = re.search(r'(\d{4})', str(pub_date))
            if match:
                all_years.add(int(match.group(1)))

available_years = sorted(list(all_years))
if not available_years:
    print('__RESULT__:')
    print(json.dumps([]))
    exit()

# Focus on recent years including 2022
target_years = [y for y in available_years if y >= 2020]
if 2022 not in target_years and available_years:
    target_years = available_years[-3:]  # Last 3 years

min_year = min(target_years)
max_year = max(target_years)

# Process data and count CPC groups
with open(patent_file, 'r') as f:
    data = json.load(f)
    
    for record in data[:min(len(data), max_records)]:
        pub_date = record.get('publication_date', '')
        if not pub_date:
            continue
            
        year_match = re.search(r'(\d{4})', str(pub_date))
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        if year not in target_years:
            continue
        
        cpc_str = record.get('cpc', '')
        if not cpc_str:
            continue
        
        try:
            cpc_list = ast.literal_eval(cpc_str)
        except:
            continue
        
        for cpc_entry in cpc_list:
            if not isinstance(cpc_entry, dict):
                continue
            code = cpc_entry.get('code', '')
            if not code:
                continue
            
            # Match to level 5 CPC group
            for level5_symbol in cpc_level5_symbols:
                if code.startswith(level5_symbol):
                    cpc_year_counts[year][level5_symbol] += 1
                    break

# Build DataFrame for EMA calculation
years = sorted(cpc_year_counts.keys())
all_cpcs = set()
for year_counts in cpc_year_counts.values():
    all_cpcs.update(year_counts.keys())

# Create counts DataFrame
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

# Find CPCs with best year = 2022
result_cpcs = []
for cpc in df_ema.index:
    max_ema = df_ema.loc[cpc].max()
    if max_ema > 0:
        best_year = df_ema.loc[cpc].idxmax()
        if best_year == 2022:
            result_cpcs.append((cpc, max_ema))

# Sort by EMA value (descending) - highest exponential moving averages first
result_cpcs.sort(key=lambda x: x[1], reverse=True)

# Return just the CPC codes
final_result = [cpc for cpc, ema in result_cpcs]

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
