code = """import json
from datetime import datetime

# Get the file path from the previous query
result_file = var_functions.query_db:22
print('File path type:', type(result_file))
print('File path preview:', str(result_file)[:100])

# Read the data from the file
with open(result_file, 'r') as f:
    raw_data = json.load(f)

print('Total records:', len(raw_data))

# Process data to extract CPC codes and years
cpc_year_counts = {}
all_years = set()

for record in raw_data:
    try:
        # Parse publication date
        date_str = record['publication_date']
        # Remove ordinal suffixes
        for suffix in ['st,', 'nd,', 'rd,', 'th,']:
            date_str = date_str.replace(suffix, ',')
        date_obj = datetime.strptime(date_str.strip(), '%b %d, %Y')
        year = date_obj.year
        all_years.add(year)
        
        # Parse CPC codes
        cpc_data = json.loads(record['cpc'])
        for cpc_item in cpc_data:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                # Check if this is a level 5 code (has main group and subgroup)
                parts = code.split('/')
                if len(parts) == 2:
                    subgroup = parts[1]
                    # Level 5 codes have subgroups with at least 3 digits (e.g., 056, 244)
                    if len(subgroup) >= 3 and subgroup.isdigit():
                        # Initialize dict for this CPC code if needed
                        if code not in cpc_year_counts:
                            cpc_year_counts[code] = {}
                        # Count filings
                        cpc_year_counts[code][year] = cpc_year_counts[code].get(year, 0) + 1
    except Exception as e:
        continue

print('Unique CPC codes:', len(cpc_year_counts))
print('Year range:', min(all_years) if all_years else 'None', '-', max(all_years) if all_years else 'None')
print('Sample CPC codes:', list(cpc_year_counts.keys())[:5])

# Calculate EMA for each CPC code
alpha = 0.2
cpc_best_year = {}

for cpc_code, yearly_counts in cpc_year_counts.items():
    # Create time series for all years
    sorted_years = sorted(all_years)
    ema_values = {}
    ema = 0
    
    for year in sorted_years:
        count = yearly_counts.get(year, 0)
        ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    # Find year with highest EMA
    if ema_values:
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        if best_year == 2022:
            cpc_best_year[cpc_code] = ema_values[best_year]

# Sort by EMA value descending
cpc_best_2022 = sorted(cpc_best_year.items(), key=lambda x: x[1], reverse=True)
final_cpc_codes = [code for code, ema in cpc_best_2022[:50]]  # Top 50 with best year 2022

print('CPC codes with best year 2022:', len(final_cpc_codes))
print('\n__RESULT__:')
print(json.dumps(final_cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
