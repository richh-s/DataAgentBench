code = """import json
import pandas as pd
from datetime import datetime

# Load the full data from the previous query
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")

# Parse CPC codes and extract publication years
patent_cpc_years = []

for record in data:
    cpc_json = record['cpc']
    pub_date_str = record['publication_date']
    
    # Parse publication date to extract year
    try:
        # Handle various date formats like "Aug 3rd, 2021" or "Oct 6th, 2020"
        # Remove ordinal suffixes (st, nd, rd, th) and parse
        date_str_clean = pub_date_str.replace('st,', ',').replace('nd,', ',').replace('rd,', ',').replace('th,', ',')
        pub_date = datetime.strptime(date_str_clean, '%b %d, %Y')
        year = pub_date.year
    except:
        # Skip records with invalid dates
        continue
    
    # Parse CPC JSON
    try:
        cpc_list = json.loads(cpc_json)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                patent_cpc_years.append({
                    'cpc_code': code,
                    'year': year
                })
    except:
        # Skip records with invalid CPC JSON
        continue

print(f"Parsed {len(patent_cpc_years)} CPC code-year pairs")

# Create DataFrame
df = pd.DataFrame(patent_cpc_years)

# Get unique CPC codes and identify level 5 codes
# CPC group codes at level 5 typically have the format like A01B01/00 or H01M10/052
# They have at least 2 digits after the slash (main group and subgroup)
cpc_codes = df['cpc_code'].unique()
level_5_codes = []

for code in cpc_codes:
    # Check if it's a group code (not just a class or subclass)
    # Level 5 codes should have / and more than just the subclass level
    if '/' in code:
        # Split to get the group part
        group_part = code.split('/')[1]
        # Group codes at level 5 typically have format like "10/052" (main group/subgroup)
        # The presence of a subgroup with at least 3 digits indicates level 5
        if len(group_part) >= 3:
            level_5_codes.append(code)

print(f"Found {len(level_5_codes)} potential level 5 CPC codes")

# Filter dataframe to only level 5 codes
df_level5 = df[df['cpc_code'].isin(level_5_codes)]

# Group by year and CPC code to count filings
counts_by_year = df_level5.groupby(['cpc_code', 'year']).size().reset_index(name='count')

print(f"Counts by year and CPC code: {len(counts_by_year)} records")
print(counts_by_year.head())

# Calculate EMA for each CPC code
alpha = 0.2
cpc_emas = {}

# Get all unique CPC codes and years
codes = counts_by_year['cpc_code'].unique()
years = sorted(counts_by_year['year'].unique())

for code in codes:
    code_data = counts_by_year[counts_by_year['cpc_code'] == code]
    
    # Create a full time series with zeros for missing years
    year_counts = {year: 0 for year in years}
    for _, row in code_data.iterrows():
        year_counts[row['year']] = row['count']
    
    # Calculate EMA
    ema_values = {}
    ema = 0
    
    for year in years:
        value = year_counts[year]
        ema = alpha * value + (1 - alpha) * ema
        ema_values[year] = ema
    
    cpc_emas[code] = ema_values

# Find the best year for each CPC code (year with highest EMA)
best_years = {}
for code, ema_values in cpc_emas.items():
    if ema_values:
        best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
        best_years[code] = {
            'best_year': best_year,
            'best_ema': ema_values[best_year]
        }

# Filter for codes where best year is 2022
codes_best_2022 = [code for code, info in best_years.items() if info['best_year'] == 2022]

print(f"Found {len(codes_best_2022)} CPC codes with best year 2022")

# Verify these are level 5 codes
print("Sample codes:", codes_best_2022[:5])

# Sort by EMA value (descending) to show the highest ones first
codes_2022_with_ema = [(code, best_years[code]['best_ema']) for code in codes_best_2022]
codes_2022_with_ema.sort(key=lambda x: x[1], reverse=True)

result_codes = [code for code, _ in codes_2022_with_ema]

# Print the result
print('\n__RESULT__:')
print(json.dumps(result_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
