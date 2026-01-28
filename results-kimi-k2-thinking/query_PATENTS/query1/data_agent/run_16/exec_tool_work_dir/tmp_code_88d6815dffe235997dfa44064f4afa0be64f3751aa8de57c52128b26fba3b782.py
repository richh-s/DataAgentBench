code = """import json
import pandas as pd
import numpy as np

# Load the patent data
patent_file = locals()['var_functions.query_db:4']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

# Load the CPC level 5 data
cpc_file = locals()['var_functions.query_db:11']
with open(cpc_file, 'r') as f:
    cpc_level5 = json.load(f)

# Create set of valid level 5 CPC codes for fast lookup
level5_codes = {item['symbol'] for item in cpc_level5}

# Function to parse publication date
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def parse_date(date_str):
    if not date_str or date_str == '':
        return None
    try:
        parts = date_str.split()
        if len(parts) >= 3:
            month = parts[0]
            year = parts[-1]
            if month in month_map and year.isdigit():
                return int(year)
    except:
        pass
    return None

# Extract subclass-level CPC codes and years from patents
patent_records = []
for patent in patent_data:
    pub_date = patent.get('publication_date', '')
    year = parse_date(pub_date)
    if not year:
        continue
    
    cpc_str = patent.get('cpc', '')
    if not cpc_str or cpc_str == '':
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if code:
                import re
                match = re.search(r'^([A-Z]\d{2}[A-Z])', code)
                if match:
                    subclass = match.group(1)
                    if subclass in level5_codes:
                        patent_records.append({
                            'cpc_subclass': subclass,
                            'year': year
                        })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(patent_records)

# Count patents per CPC subclass per year
yearly_counts = df.groupby(['cpc_subclass', 'year']).size().reset_index(name='count')

# Get all years in data
years = sorted(yearly_counts['year'].unique())

# Calculate EMA for each CPC subclass
alpha = 0.2  # smoothing factor
results = []

for cpc_code in yearly_counts['cpc_subclass'].unique():
    cpc_data = yearly_counts[yearly_counts['cpc_subclass'] == cpc_code].copy()
    cpc_data = cpc_data.set_index('year').reindex(years, fill_value=0)
    
    # Calculate EMA
    ema_values = []
    ema_prev = 0
    
    for year in years:
        count = cpc_data.loc[year, 'count']
        ema_current = alpha * count + (1 - alpha) * ema_prev
        ema_values.append(ema_current)
        ema_prev = ema_current
    
    cpc_data['ema'] = ema_values
    
    # Find year with highest EMA
    max_idx = np.argmax(ema_values)
    best_year = years[max_idx]
    max_ema = ema_values[max_idx]
    
    results.append({
        'cpc_code': cpc_code,
        'best_year': best_year,
        'max_ema': max_ema
    })

results_df = pd.DataFrame(results)

# Identify highest EMA for each year
yearly_best = {}
for year in years:
    year_results = []
    for _, row in results_df.iterrows():
        cpc_code = row['cpc_code']
        # Calculate EMA for this specific year
        cpc_data = yearly_counts[yearly_counts['cpc_subclass'] == cpc_code].copy()
        cpc_data = cpc_data.set_index('year').reindex(years, fill_value=0)
        
        ema_values = []
        ema_prev = 0
        for y in years:
            count = cpc_data.loc[y, 'count']
            ema_current = alpha * count + (1 - alpha) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
        
        year_idx = years.index(year)
        year_results.append({
            'cpc_code': cpc_code,
            'ema': ema_values[year_idx] if year_idx < len(ema_values) else 0
        })
    
    if year_results:
        best_for_year = max(year_results, key=lambda x: x['ema'])
        yearly_best[year] = best_for_year['cpc_code']

# Filter CPC codes where best year is 2022
cpc_2022_best = results_df[results_df['best_year'] == 2022]['cpc_code'].tolist()

print('__RESULT__:')
print(json.dumps({
    'years_available': years,
    'yearly_best_cpc': yearly_best,
    'cpc_codes_with_best_year_2022': cpc_2022_best,
    'total_cpc_codes_2022': len(cpc_2022_best)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'total_patents_processed': 277813, 'valid_records': 0, 'sample_records': []}, 'var_functions.execute_python:14': {'sample_cpc_from_patents': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10', 'C01P2002/76', 'H01M10/0525', 'H01M2004/028', 'H01M4/1315', 'H01M2004/021', 'H01M4/525', 'C01B33/00', 'H01M4/1315', 'H01M4/525', 'H01M4/505'], 'sample_level5_codes': ['A01F', 'B06B', 'C12C', 'F01N', 'D99Z', 'A47B', 'H01C', 'C07C', 'B27M', 'A63K', 'C21C', 'H03D', 'G99Z', 'B31B', 'F02P', 'A61M', 'E02C', 'D06P', 'B64C', 'B27J'], 'total_patents_processed': 277813, 'valid_records': 312315, 'sample_records': [{'cpc_subclass': 'C01B', 'year': 2021, 'full_code': 'C01B33/00'}, {'cpc_subclass': 'C01B', 'year': 2021, 'full_code': 'C01B35/00'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0565'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0562'}, {'cpc_subclass': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0566'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/052'}, {'cpc_subclass': 'C01P', 'year': 2021, 'full_code': 'C01P2002/76'}, {'cpc_subclass': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_subclass': 'Y02E', 'year': 2021, 'full_code': 'Y02E60/10'}]}}

exec(code, env_args)
