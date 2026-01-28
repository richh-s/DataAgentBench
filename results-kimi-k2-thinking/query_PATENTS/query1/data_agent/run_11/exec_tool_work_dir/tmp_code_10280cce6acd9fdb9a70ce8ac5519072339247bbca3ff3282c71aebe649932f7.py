code = """import json
import pandas as pd
from datetime import datetime

# Load the full data
result_file = var_functions.query_db:5
with open(result_file, 'r') as f:
    data = json.load(f)

print(f'Total records: {len(data)}')

# Parse CPC codes and extract years
patent_records = []

for record in data:
    try:
        # Parse publication date
        pub_date_str = record['publication_date']
        # Remove ordinal suffixes
        date_clean = pub_date_str.replace('st,', ',').replace('nd,', ',').replace('rd,', ',').replace('th,', ',')
        pub_date = datetime.strptime(date_clean, '%b %d, %Y')
        year = pub_date.year
        
        # Parse CPC codes  
        cpc_list = json.loads(record['cpc'])
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code and '/' in code:
                # Check if it looks like a group code (has group/subgroup structure)
                group_part = code.split('/')[1]
                # Level 5 codes typically have 3+ digits in the subgroup
                if len(group_part) >= 3 and group_part[-2:].isdigit():
                    patent_records.append({
                        'cpc_code': code,
                        'year': year
                    })
    except:
        continue

print(f'Parsed {len(patent_records)} records with level 5 CPC codes')

# Create DataFrame
df = pd.DataFrame(patent_records)

# Count filings by CPC code and year
yearly_counts = df.groupby(['cpc_code', 'year']).size().reset_index(name='count')
print(f'Found {len(yearly_counts)} CPC-year combinations')

# Calculate EMA for each CPC code
alpha = 0.2
cpc_results = []

for cpc_code in yearly_counts['cpc_code'].unique():
    # Get counts for this CPC code
    code_counts = yearly_counts[yearly_counts['cpc_code'] == cpc_code]
    
    # Create time series (2018-2023 based on typical patent data)
    all_years = list(range(2018, 2024))
    year_to_count = dict(zip(code_counts['year'], code_counts['count']))
    
    # Calculate EMA
    ema = 0
    year_emas = {}
    
    for year in all_years:
        count = year_to_count.get(year, 0)
        ema = alpha * count + (1 - alpha) * ema
        year_emas[year] = ema
    
    # Find best year
    if year_emas:
        best_year = max(year_emas.keys(), key=lambda y: year_emas[y])
        if best_year == 2022:
            cpc_results.append({
                'cpc_code': cpc_code,
                'best_ema': year_emas[best_year]
            })

# Sort by EMA descending
cpc_results.sort(key=lambda x: x['best_ema'], reverse=True)
final_codes = [r['cpc_code'] for r in cpc_results]

print(f'Found {len(final_codes)} CPC codes with best year 2022')

# Print result in required format
print('\n__RESULT__:')
print(json.dumps(final_codes))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
