code = """import json
import pandas as pd
import numpy as np
import re

# Read the German patents data file
file_path = str(var_functions.query_db:16)
with open(file_path, 'r') as f:
    german_patents = json.load(f)

# Parse CPC codes
def extract_cpc_codes(cpc_field):
    try:
        if isinstance(cpc_field, str):
            return json.loads(cpc_field)
        return cpc_field if isinstance(cpc_field, list) else []
    except:
        return []

# Parse grant date and extract month
def extract_month(grant_date):
    if not grant_date:
        return None
    
    date_str = str(grant_date).lower()
    
    # Map month names to numbers
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    # Look for month names
    for month_name, month_num in month_map.items():
        if month_name in date_str:
            return month_num
    
    return None

# Process patents and count filings by CPC level 4 and month
cpc_month_counts = {}
monthly_totals = {}

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    
    # Check if it's in second half of 2019
    if not grant_date or '2019' not in str(grant_date):
        continue
    
    month = extract_month(grant_date)
    if not month or month < 7:  # Only second half (July-Dec)
        continue
    
    cpc_codes = extract_cpc_codes(patent.get('cpc', '[]'))
    
    for cpc_item in cpc_codes:
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        # Get level 4 CPC (first 4 characters of main class)
        level4 = code.split('/')[0][:4]
        if len(level4) < 3:
            continue
        
        # Count filings
        key = (level4, month)
        cpc_month_counts[key] = cpc_month_counts.get(key, 0) + 1
        monthly_totals[month] = monthly_totals.get(month, 0) + 1

# Build DataFrame
data = []
for (cpc, month), count in cpc_month_counts.items():
    data.append({'cpc_level4': cpc, 'month': month, 'filings': count})

df = pd.DataFrame(data)

print(f"Total CPC-month combinations: {len(df)}")
print(f"CPC groups: {df['cpc_level4'].nunique()}")
print(f"Months covered: {sorted(df['month'].unique())}")

# Calculate EMA for each CPC
def calculate_ema(series, alpha=0.1):
    return series.ewm(alpha=alpha, adjust=False).mean()

# Get all CPCs and months
cpcs = df['cpc_level4'].unique()
months = [7, 8, 9, 10, 11, 12]

cpc_results = []

for cpc in cpcs:
    # Create monthly series (July to December)
    monthly_counts = []
    for month in months:
        count = df[(df['cpc_level4'] == cpc) & (df['month'] == month)]['filings'].sum()
        monthly_counts.append(count)
    
    # Check if we have any activity (skip if all zeros)
    if sum(monthly_counts) == 0:
        continue
    
    # Calculate EMA
    series = pd.Series(monthly_counts)
    ema_values = calculate_ema(series, alpha=0.1)
    
    # Find best month (highest EMA)
    best_idx = ema_values.idxmax()
    best_month = months[best_idx]
    best_ema = ema_values.iloc[best_idx]
    
    cpc_results.append({
        'cpc_level4': cpc,
        'best_month': best_month,
        'best_ema': round(float(best_ema), 2),
        'monthly_counts': monthly_counts,
        'ema_values': [round(float(x), 2) for x in ema_values],
        'total_filings': sum(monthly_counts)
    })

# Sort by best EMA
cpc_results.sort(key=lambda x: x['best_ema'], reverse=True)

# Show top 10 results for verification
print("Top 10 CPC groups by EMA:")
for i, result in enumerate(cpc_results[:10]):
    print(f"{i+1}. {result['cpc_level4']} - Best month: {result['best_month']}, " +
          f"EMA: {result['best_ema']}, Total filings: {result['total_filings']}")
    print(f"   Monthly counts: {result['monthly_counts']}")
    print(f"   EMA values: {result['ema_values']}")
    print()

# Save results for next step
top_results = cpc_results[:20]  # Get top 20 to ensure we have enough

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'total_combinations': 439, 'unique_cpc_level4': 68, 'top_cpc': [{'cpc_level4': 'B01J', 'filings': 57}, {'cpc_level4': 'C04B', 'filings': 45}, {'cpc_level4': 'B01D', 'filings': 28}, {'cpc_level4': 'H01R', 'filings': 24}, {'cpc_level4': 'H04W', 'filings': 22}, {'cpc_level4': 'G02B', 'filings': 20}, {'cpc_level4': 'B29C', 'filings': 19}, {'cpc_level4': 'F02D', 'filings': 16}, {'cpc_level4': 'H04L', 'filings': 16}, {'cpc_level4': 'F01N', 'filings': 15}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
