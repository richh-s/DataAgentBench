code = """import json
import re
from datetime import datetime

# Get the German patents data
results = var_functions.query_db:28

# Function to parse grant date and extract month/year
def parse_grant_date(date_str):
    if not date_str:
        return None, None
    
    date_str = str(date_str).lower()
    
    # Extract year
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None, None
    
    year = int(year_match.group(1))
    if year != 2019:
        return None, None
    
    # Extract month
    months = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    
    month = None
    for month_abbr, month_num in months.items():
        if month_abbr in date_str:
            month = month_num
            break
    
    return year, month

# Function to extract CPC level 4 code
def extract_cpc_level_4(cpc_code):
    if not cpc_code:
        return None
    try:
        # Take main part before /
        main_part = str(cpc_code).split('/')[0]
        # Remove any trailing non-alphanumeric
        clean_part = re.sub(r'[^A-Z0-9]$', '', main_part)
        return clean_part
    except:
        return None

# Process patents
filtered_patents = []
cpc_monthly_counts = {}

for patent in results:
    grant_date = patent.get('grant_date', '')
    cpc_data = patent.get('cpc', '')
    
    year, month = parse_grant_date(grant_date)
    if not year or not month or month < 7:  # Second half: July-Dec
        continue
    
    try:
        # Parse CPC JSON
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
            
        for cpc_item in cpc_list:
            cpc_code = cpc_item.get('code')
            if cpc_code:
                level_4 = extract_cpc_level_4(cpc_code)
                if level_4:
                    # Count by month and CPC level 4
                    key = (year, month, level_4)
                    cpc_monthly_counts[key] = cpc_monthly_counts.get(key, 0) + 1
                    
                    filtered_patents.append({
                        'year': year,
                        'month': month,
                        'cpc_level_4': level_4,
                        'cpc_full': cpc_code,
                        'grant_date': grant_date
                    })
    except:
        continue

print(f'Total CPC entries from German patents (second half 2019): {len(filtered_patents)}')
print(f'Unique CPC Level 4 codes: {len(set(p["cpc_level_4"] for p in filtered_patents))}')

# Group by CPC level 4 and calculate total counts
cpc_totals = {}
for _, _, cpc in cpc_monthly_counts:
    cpc_totals[cpc] = cpc_totals.get(cpc, 0) + cpc_monthly_counts[(2019, _, cpc)]

top_cpc = sorted(cpc_totals.items(), key=lambda x: x[1], reverse=True)[:10]
print('\nTop 10 CPC Level 4 codes by total filings:')
for cpc, count in top_cpc:
    print(f'  {cpc}: {count} filings')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Date parsing and CPC level 4 extraction functions ready', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'total_records': '11735'}]}

exec(code, env_args)
