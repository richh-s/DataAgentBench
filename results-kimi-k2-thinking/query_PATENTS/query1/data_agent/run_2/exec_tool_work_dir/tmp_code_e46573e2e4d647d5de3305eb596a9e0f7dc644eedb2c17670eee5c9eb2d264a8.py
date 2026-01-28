code = """import json
import pandas as pd
import re
from collections import defaultdict

# Access the full dataset filepath
filepath = locals()['var_functions.query_db:32']

# Load the data
with open(filepath, 'r') as f:
    raw_data = json.load(f)

print(f'Total records loaded: {len(raw_data):,}')

# Process data: extract CPC codes and years
records = []
year_range = set()

for record in raw_data:
    try:
        # Extract year from publication_date
        pub_date = record.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            year_range.add(year)
            
            # Parse CPC codes
            cpc_str = record.get('cpc', '[]')
            cpc_list = json.loads(cpc_str)
            
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:  # Valid CPC format with subgroup
                    # Level 5 is the full CPC code
                    records.append({
                        'cpc_level5': code,
                        'year': year
                    })
    except Exception as e:
        continue

print(f'Processed {len(records)} CPC entries')
print(f'Year range: {min(year_range)} - {max(year_range)}')

# Create DataFrame
df = pd.DataFrame(records)

# Group by CPC level 5 and year to get patent counts
counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
print(f'Number of CPC-year combinations: {len(counts):,}')
print(f'Number of unique CPC level 5 codes: {counts["cpc_level5"].nunique():,}')

# Calculate EMA for each CPC code
alpha = 0.2
ema_results = []

for cpc_code in counts['cpc_level5'].unique():
    if not cpc_code:
        continue
        
    # Get all years for this CPC code
    group = counts[counts['cpc_level5'] == cpc_code].copy()
    
    # Need at least 2 years to calculate meaningful EMA
    if len(group) < 2:
        continue
    
    # Sort by year
    group = group.sort_values('year')
    
    # Initialize EMA with first value
    ema = group.iloc[0]['count']
    first_year = group.iloc[0]['year']
    
    # Store first EMA value
    ema_results.append({
        'cpc_level5': cpc_code,
        'year': first_year,
        'ema': ema,
        'count': group.iloc[0]['count']
    })
    
    # Calculate EMA for subsequent years
    for _, row in group.iloc[1:].iterrows():
        ema = alpha * row['count'] + (1 - alpha) * ema
        ema_results.append({
            'cpc_level5': cpc_code,
            'year': row['year'],
            'ema': round(ema, 2),
            'count': row['count']
        })

ema_df = pd.DataFrame(ema_results)
print(f'EMA calculations completed for {ema_df["cpc_level5"].nunique()} CPC codes')

# Find the year with maximum EMA for each CPC code
# Use idxmax to find the index of maximum EMA for each CPC code
best_years_idx = ema_df.groupby('cpc_level5')['ema'].idxmax()
best_years = ema_df.loc[best_years_idx]

print(f'Found best years for {len(best_years)} CPC codes')

# Filter for codes where best year is 2022
best_2022 = best_years[best_years['year'] == 2022]

print(f'CPC codes with best year 2022: {len(best_2022)}')

# Sort by EMA value (descending) to get highest EMA codes first
if not best_2022.empty:
    best_2022_sorted = best_2022.sort_values('ema', ascending=False)
    result_codes = best_2022_sorted['cpc_level5'].tolist()
    
    print(f'Top 10 CPC codes with best year 2022:')
    for i, code in enumerate(result_codes[:10], 1):
        ema_val = best_2022_sorted.iloc[i-1]['ema']
        print(f"  {i}. {code} (EMA: {ema_val})")
else:
    result_codes = []
    print('No CPC codes found with best year 2022')

print('__RESULT__:')
print(json.dumps(result_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': ['A61K9/06', 'A61K45/06', 'G06N3/08', 'G06N20/00', 'G02B6/3897', 'A61K31/675', 'C07D471/04', 'C07D401/14', 'A61K47/60', 'H04L69/326', 'A61B5/7267', 'G06T2207/10024', 'G06T7/90', 'A61P29/00', 'A61P35/00', 'A61P43/00', 'A61P3/10', 'A61P31/14', 'A61P25/16', 'A61P25/28', 'G06F3/011', 'A61P3/04', 'A61K47/26', 'A61P9/12', 'A61P9/10', 'A61P1/00', 'A61K31/606', 'A61K47/02', 'H01M10/613', 'G02F1/294', 'A61P9/04', 'A61P11/06', 'A61K9/2059', 'A61P3/00', 'A61P17/00', 'A61P25/20', 'A61P15/10', 'A61P25/06', 'A61P25/14', 'A61P13/12', 'A61P15/00', 'A61P13/10', 'A61P15/08', 'A61K47/12', 'A61K9/4866', 'A61P11/16', 'A61P13/00', 'A61P27/16', 'A61P25/30', 'A61P25/22', 'A61P25/24', 'A61P7/02', 'A61P37/06', 'A61P3/06', 'A61P9/02', 'H04J11/0079', 'A61P9/06', 'A61P9/00', 'C08G18/7671', 'H04N7/185', 'H04N23/51', 'H04W88/18', 'B60W2556/50'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
