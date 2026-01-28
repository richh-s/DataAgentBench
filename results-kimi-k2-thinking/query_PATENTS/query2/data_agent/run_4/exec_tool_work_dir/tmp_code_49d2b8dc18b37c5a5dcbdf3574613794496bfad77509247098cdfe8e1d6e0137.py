code = """import json
import pandas as pd
import numpy as np

# Load CPC definitions
cpc_file = var_functions.query_db:24

with open(cpc_file, 'r') as f:
    cpc_defs = json.load(f)

# Create CPC lookup
cpc_lookup = {item['symbol']: item['titleFull'] for item in cpc_defs}

# Load processed patent data from previous step
patent_file = var_functions.query_db:16

with open(patent_file, 'r') as f:
    german_patents = json.load(f)

# Process patents to get monthly data for 2019
patent_monthly = []
for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    if grant_date and '2019' in str(grant_date):
        # Check if it's second half based on month name
        date_str = str(grant_date).lower()
        second_half = any(m in date_str for m in ['jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        
        if second_half:
            # Parse CPC codes
            try:
                cpc_data = json.loads(patent.get('cpc', '[]'))
                for cpc_item in cpc_data:
                    code = cpc_item.get('code', '')
                    level4 = code.split('/')[0][:4]
                    if len(level4) >= 3:
                        # Determine month (default to July if not clear)
                        month = 7
                        for i, m in enumerate(['jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
                            if m in date_str:
                                month = 7 + i
                                break
                        
                        patent_monthly.append({
                            'cpc_level4': level4,
                            'month': month,
                            'year': 2019
                        })
            except:
                continue

# Create DataFrame
df = pd.DataFrame(patent_monthly)

# Count filings by CPC and month
df_counts = df.groupby(['cpc_level4', 'month']).size().reset_index(name='filings')

# Create complete range for second half 2019
months = [7, 8, 9, 10, 11, 12]
all_cpcs = df['cpc_level4'].unique()

# Calculate EMA for each CPC
from collections import defaultdict

def calculate_ema(values, alpha=0.1):
    """Calculate exponential moving average"""
    if not values:
        return []
    
    ema = []
    # Start with first value
    ema.append(values[0])
    
    for i in range(1, len(values)):
        ema.append(alpha * values[i] + (1 - alpha) * ema[i-1])
    
    return ema

# Process each CPC group
cpc_results = []

for cpc in all_cpcs:
    # Get filings for each month
    filings_by_month = []
    for month in months:
        count = df_counts[
            (df_counts['cpc_level4'] == cpc) & 
            (df_counts['month'] == month)
        ]['filings'].sum()
        filings_by_month.append(count)
    
    # Calculate EMA
    ema_values = calculate_ema(filings_by_month)
    
    # Find best month (highest EMA)
    best_month_idx = np.argmax(ema_values)
    best_month = months[best_month_idx]
    best_ema = ema_values[best_month_idx]
    
    # Get full title
    title = cpc_lookup.get(cpc, 'Title not found')
    
    cpc_results.append({
        'cpc_level4': cpc,
        'title_full': title,
        'best_month': best_month,
        'best_ema': round(best_ema, 2),
        'total_filings': sum(filings_by_month)
    })

# Sort by best EMA and get top 10
top_results = sorted(cpc_results, key=lambda x: x['best_ema'], reverse=True)[:10]

print("Top 10 CPC technology areas in Germany (second half 2019):")
for i, result in enumerate(top_results, 1):
    print(f"{i}. {result['cpc_level4']} - {result['title_full']}")
    print(f"   Best month: {result['best_month']}/2019, EMA: {result['best_ema']}, Total filings: {result['total_filings']}")
    print()

print("__RESULT__:")
print(json.dumps(top_results))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'total_combinations': 439, 'unique_cpc_level4': 68, 'top_cpc': [{'cpc_level4': 'B01J', 'filings': 57}, {'cpc_level4': 'C04B', 'filings': 45}, {'cpc_level4': 'B01D', 'filings': 28}, {'cpc_level4': 'H01R', 'filings': 24}, {'cpc_level4': 'H04W', 'filings': 22}, {'cpc_level4': 'G02B', 'filings': 20}, {'cpc_level4': 'B29C', 'filings': 19}, {'cpc_level4': 'F02D', 'filings': 16}, {'cpc_level4': 'H04L', 'filings': 16}, {'cpc_level4': 'F01N', 'filings': 15}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
