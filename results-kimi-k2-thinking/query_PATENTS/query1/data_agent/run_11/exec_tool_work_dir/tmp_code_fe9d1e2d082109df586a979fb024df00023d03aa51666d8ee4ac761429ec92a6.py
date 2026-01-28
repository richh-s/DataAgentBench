code = """import json
from datetime import datetime

# Get the file path from the previous query
file_path = locals()['var_functions.query_db:30']
print('File path:', file_path[:100])

# Read and parse the data
with open(file_path, 'r') as f:
    data = json.load(f)

print('Total records:', len(data))

# Initialize storage for CPC codes and their counts per year
cpc_year_counts = {}
all_years = set()

# Process each record
for record in data:
    try:
        # Parse publication date
        date_str = record['publication_date']
        # Clean the date string by removing ordinal suffixes
        for suffix in ['st,', 'nd,', 'rd,', 'th,']:
            date_str = date_str.replace(suffix, ',')
        date_obj = datetime.strptime(date_str.strip(), '%b %d, %Y')
        year = date_obj.year
        all_years.add(year)
        
        # Parse CPC codes (JSON format)
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            # Filter for group codes at level 5 (format: class/subclass/main-group/subgroup)
            # Level 5 codes have BOTH main group and subgroup: XXXX/NNN
            if code and '/' in code:
                parts = code.split('/')
                if len(parts) == 2:
                    subgroup = parts[1]
                    # Level 5 subgroup codes are typically 3+ digits
                    if len(subgroup) >= 3 and subgroup.isdigit():
                        # Initialize count dict for this CPC code if needed
                        if code not in cpc_year_counts:
                            cpc_year_counts[code] = {}
                        # Increment count for this year
                        cpc_year_counts[code][year] = cpc_year_counts[code].get(year, 0) + 1
    except Exception as e:
        continue

print('Unique level 5 CPC codes found:', len(cpc_year_counts))
print('Year range:', sorted(list(all_years)))
print('Sample CPC codes:', list(cpc_year_counts.keys())[:5])

# Calculate EMA for each CPC code
alpha = 0.2
cpc_best_years = {}

for cpc_code, yearly_counts in cpc_year_counts.items():
    # Get all years sorted
    sorted_years = sorted(list(all_years))
    
    # Calculate EMA across years
    ema_values = {}
    ema = 0  # Initial EMA
    
    for year in sorted_years:
        count = yearly_counts.get(year, 0)
        ema = alpha * count + (1 - alpha) * ema
        ema_values[year] = ema
    
    # Find year with highest EMA
    if ema_values:
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        cpc_best_years[cpc_code] = {
            'best_year': best_year,
            'best_ema': ema_values[best_year]
        }

# Filter CPC codes where best year is 2022
cpc_best_2022 = [(code, info['best_ema']) for code, info in cpc_best_years.items() 
                 if info['best_year'] == 2022]

# Sort by EMA value (descending)
cpc_best_2022.sort(key=lambda x: x[1], reverse=True)

# Extract just the CPC codes
final_cpc_codes = [code for code, ema in cpc_best_2022]

print('CPC codes with best year 2022:', len(final_cpc_codes))
print('Top 10 CPC codes:', final_cpc_codes[:10])

print('\n__RESULT__:')
print(json.dumps(final_cpc_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
