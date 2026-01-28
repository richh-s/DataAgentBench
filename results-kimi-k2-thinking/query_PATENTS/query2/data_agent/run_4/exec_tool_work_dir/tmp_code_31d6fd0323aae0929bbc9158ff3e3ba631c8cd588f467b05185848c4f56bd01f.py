code = """import json
import pandas as pd
import numpy as np
import re

# Read the German patents data
with open('/tmp/tmp_query_db_16.json', 'r') as f:
    german_patents = json.load(f)

# Parse CPC codes
def extract_cpc_codes(cpc_field):
    try:
        if isinstance(cpc_field, str):
            return json.loads(cpc_field)
        return cpc_field if isinstance(cpc_field, list) else []
    except:
        return []

# Extract month from grant date
def extract_month(grant_date):
    if not grant_date:
        return None
    
    date_str = str(grant_date).lower()
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    for month_name, month_num in month_map.items():
        if month_name in date_str:
            return month_num
    
    return None

# Count filings by CPC level 4 and month
cpc_month_data = []

for patent in german_patents:
    grant_date = patent.get('grant_date', '')
    
    if not grant_date or '2019' not in str(grant_date):
        continue
    
    month = extract_month(grant_date)
    if not month or month < 7:
        continue
    
    cpc_codes = extract_cpc_codes(patent.get('cpc', '[]'))
    
    for cpc_item in cpc_codes:
        code = cpc_item.get('code', '')
        if not code:
            continue
        
        level4 = code.split('/')[0][:4]
        if len(level4) < 3:
            continue
        
        cpc_month_data.append({
            'cpc_level4': level4,
            'month': month
        })

# Create DataFrame and count
df = pd.DataFrame(cpc_month_data)
print(f"Total records: {len(df)}")
print(f"Unique CPC groups: {df['cpc_level4'].nunique()}")
print(f"Date range: months {sorted(df['month'].unique())}")

# Count filings per CPC per month
df_counts = df.groupby(['cpc_level4', 'month']).size().reset_index(name='filings')

# Calculate EMA for each CPC (July-December)
months = [7, 8, 9, 10, 11, 12]
alpha = 0.1

cpc_groups = df['cpc_level4'].unique()
results = []

for cpc in cpc_groups:
    monthly_filings = []
    for month in months:
        count = df_counts[
            (df_counts['cpc_level4'] == cpc) & 
            (df_counts['month'] == month)
        ]['filings'].sum()
        monthly_filings.append(count)
    
    total_filings = sum(monthly_filings)
    if total_filings == 0:
        continue
    
    # Calculate EMA
    ema = []
    current_ema = monthly_filings[0]
    ema.append(current_ema)
    
    for i in range(1, len(monthly_filings)):
        current_ema = alpha * monthly_filings[i] + (1 - alpha) * current_ema
        ema.append(current_ema)
    
    # Find best month
    best_idx = np.argmax(ema)
    best_month = months[best_idx]
    
    results.append({
        'cpc_level4': cpc,
        'best_month': best_month,
        'best_ema': round(ema[best_idx], 2),
        'total_filings': total_filings,
        'monthly_counts': monthly_filings,
        'ema_values': [round(x, 2) for x in ema]
    })

# Sort by best EMA
results.sort(key=lambda x: x['best_ema'], reverse=True)

print(f"Processed {len(results)} CPC groups")
print("Top 10 by EMA:")
for i, r in enumerate(results[:10]):
    print(f"{i+1}. {r['cpc_level4']} - Month {r['best_month']}, EMA: {r['best_ema']}")

print("__RESULT__:")
print(json.dumps(results[:15]))  # Return top 15"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['cpc_definition'], 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'total_combinations': 439, 'unique_cpc_level4': 68, 'top_cpc': [{'cpc_level4': 'B01J', 'filings': 57}, {'cpc_level4': 'C04B', 'filings': 45}, {'cpc_level4': 'B01D', 'filings': 28}, {'cpc_level4': 'H01R', 'filings': 24}, {'cpc_level4': 'H04W', 'filings': 22}, {'cpc_level4': 'G02B', 'filings': 20}, {'cpc_level4': 'B29C', 'filings': 19}, {'cpc_level4': 'F02D', 'filings': 16}, {'cpc_level4': 'H04L', 'filings': 16}, {'cpc_level4': 'F01N', 'filings': 15}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
