code = """import json
import os
import pandas as pd
import re
from datetime import datetime

# Load the full data from the file
filepath = locals()['var_functions.query_db:2']
with open(filepath, 'r') as f:
    data = json.load(f)

print(f'Loaded {len(data)} records from database')

# Parse CPC codes and dates
rows = []
for record in data:
    try:
        # Parse publication date from natural language format
        pub_date_str = record['publication_date']
        # Extract year from date string (various formats like "March 15th, 2020", "Aug 3rd, 2021", "Oct 6th, 2020")
        year_match = re.search(r'(\d{4})', pub_date_str)
        if year_match:
            year = int(year_match.group(1))
        else:
            continue
            
        # Parse CPC codes from JSON string
        cpc_str = record['cpc']
        cpc_list = json.loads(cpc_str)
        
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            if code and '/' in code:  # Valid CPC format
                rows.append({
                    'cpc_code': code,
                    'year': year,
                    'inventive': cpc_entry.get('inventive', False),
                    'first': cpc_entry.get('first', False)
                })
    except:
        continue

if not rows:
    print('No valid CPC data found')
    exit()

print(f'Extracted {len(rows)} CPC entries from {len(data)} patents')

# Create dataframe and analyze CPC codes
df = pd.DataFrame(rows)
print('Year range:', df['year'].min(), 'to', df['year'].max())

# Function to extract CPC group code at different levels
def extract_cpc_level(code, level):
    """
    Extract CPC code at specified level
    Level 1: Section (A-H, Y)
    Level 2: Class (2 digits)
    Level 3: Subclass (1 letter)
    Level 4: Main group (1-3 digits before /)
    Level 5: Subgroup (digits after /)
    Example: H01M10/0562 -> 
        Level 1: H
        Level 2: H01
        Level 3: H01M
        Level 4: H01M10
        Level 5: H01M10/0562
    """
    if not code:
        return None
    
    parts = code.split('/')
    if len(parts) < 2:
        return None
        
    main_part = parts[0]  # e.g., "H01M10"
    subgroup = parts[1]   # e.g., "0562"
    
    # Section level 1
    if level == 1:
        return main_part[0] if main_part else None
    
    # Class level 2 (section + 2 digits)
    if level == 2:
        return main_part[:3] if len(main_part) >= 3 else None
    
    # Subclass level 3 (section + 2 digits + 1 letter)
    if level == 3:
        return main_part[:4] if len(main_part) >= 4 else None
    
    # Main group level 4 (full main part)
    if level == 4:
        return main_part
    
    # Subgroup level 5 (full code)
    if level == 5:
        return code
    
    return None

# Add CPC codes at level 5 (full group code)
df['cpc_level5'] = df['cpc_code'].apply(lambda x: extract_cpc_level(x, 5))

# Count patents per year for each CPC level 5 code
cpc_year_counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')

# For each CPC code, calculate exponential moving average for each year
def calculate_ema(group, alpha=0.2):
    """Calculate exponential moving average for a time series"""
    group = group.sort_values('year')
    ema_values = []
    
    # Initialize with first value
    if len(group) > 0:
        ema = group.iloc[0]['count']
        ema_values.append({'year': group.iloc[0]['year'], 'ema': ema})
        
        # Calculate EMA for subsequent years
        for idx, row in group.iloc[1:].iterrows():
            ema = alpha * row['count'] + (1 - alpha) * ema
            ema_values.append({'year': row['year'], 'ema': ema})
    
    return pd.DataFrame(ema_values)

# Calculate EMA for each CPC code
ema_results = []
for cpc_code in cpc_year_counts['cpc_level5'].unique():
    if cpc_code:
        group = cpc_year_counts[cpc_year_counts['cpc_level5'] == cpc_code]
        if len(group) > 1:  # Need at least 2 years for meaningful EMA
            ema_df = calculate_ema(group, alpha=0.2)
            ema_df['cpc_level5'] = cpc_code
            ema_results.append(ema_df)

if ema_results:
    ema_combined = pd.concat(ema_results, ignore_index=True)
    
    # Find the best year (max EMA) for each CPC code
    best_years = ema_combined.loc[ema_combined.groupby('cpc_level5')['ema'].idxmax()]
    best_years = best_years[['cpc_level5', 'year', 'ema']]
    
    # Filter for codes whose best year is 2022
    best_2022 = best_years[best_years['year'] == 2022]
    
    print(f'Found {len(best_2022)} CPC level 5 codes with best year 2022')
    
    # Sort by EMA and get top codes
    best_2022_sorted = best_2022.sort_values('ema', ascending=False)
    result = best_2022_sorted['cpc_level5'].tolist()
    
    print('__RESULT__:')
    print(json.dumps(result))
else:
    print('No EMA results calculated')
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}}

exec(code, env_args)
