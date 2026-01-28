code = """import json
import pandas as pd
import numpy as np

# Load data
patent_file = locals()['var_functions.query_db:4']
with open(patent_file, 'r') as f:
    patent_data = json.load(f)

cpc_file = locals()['var_functions.query_db:11']
with open(cpc_file, 'r') as f:
    cpc_level5 = json.load(f)

level5_codes = {item['symbol'] for item in cpc_level5}

# Parse dates
month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

def parse_date(date_str):
    if not date_str:
        return None
    try:
        parts = date_str.split()
        if len(parts) >= 3 and parts[0] in month_map and parts[-1].isdigit():
            return int(parts[-1])
    except:
        pass
    return None

# Extract records
records = []
for patent in patent_data:
    year = parse_date(patent.get('publication_date', ''))
    if not year:
        continue
    
    cpc_str = patent.get('cpc', '')
    if not cpc_str:
        continue
    
    try:
        for cpc_item in json.loads(cpc_str):
            code = cpc_item.get('code', '')
            if code:
                import re
                match = re.search(r'^([A-Z]\d{2}[A-Z])', code)
                if match:
                    subclass = match.group(1)
                    if subclass in level5_codes:
                        records.append((subclass, year))
    except:
        pass

# Create DataFrame
df = pd.DataFrame(records, columns=['subclass', 'year'])
if df.empty:
    print('__RESULT__:')
    print(json.dumps({'codes_best_in_2022': []}))
else:
    yearly_counts = df.groupby(['subclass', 'year']).size().reset_index(name='count')
    all_years = sorted(yearly_counts['year'].unique())
    
    # Calculate EMA
    alpha = 0.2
    ema_data = {}
    
    for subclass in yearly_counts['subclass'].unique():
        data = yearly_counts[yearly_counts['subclass'] == subclass].set_index('year').reindex(all_years, fill_value=0)
        ema = []
        ema_prev = 0
        
        for year in all_years:
            count = int(data.loc[year, 'count'])
            ema_prev = alpha * count + (1 - alpha) * ema_prev
            ema.append(float(ema_prev))  # Convert to float
        
        ema_data[subclass] = ema
    
    # Find codes that peaked in 2022
    codes_best_in_2022 = []
    if 2022 in all_years:
        year_idx = all_years.index(2022)
        for subclass, ema_values in ema_data.items():
            if len(ema_values) > year_idx:
                max_val = max(ema_values[:year_idx + 1])
                if ema_values[year_idx] == max_val and ema_values[year_idx] > 0:
                    codes_best_in_2022.append(subclass)
    
    print('__RESULT__:')
    print(json.dumps({
        'years': [int(y) for y in all_years],
        'codes_best_in_2022': sorted(codes_best_in_2022)
    }))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:12': {'total_patents_processed': 277813, 'valid_records': 0, 'sample_records': []}, 'var_functions.execute_python:14': {'sample_cpc_from_patents': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'C01G45/006', 'Y02E60/10', 'C01P2002/76', 'H01M10/0525', 'H01M2004/028', 'H01M4/1315', 'H01M2004/021', 'H01M4/525', 'C01B33/00', 'H01M4/1315', 'H01M4/525', 'H01M4/505'], 'sample_level5_codes': ['A01F', 'B06B', 'C12C', 'F01N', 'D99Z', 'A47B', 'H01C', 'C07C', 'B27M', 'A63K', 'C21C', 'H03D', 'G99Z', 'B31B', 'F02P', 'A61M', 'E02C', 'D06P', 'B64C', 'B27J'], 'total_patents_processed': 277813, 'valid_records': 312315, 'sample_records': [{'cpc_subclass': 'C01B', 'year': 2021, 'full_code': 'C01B33/00'}, {'cpc_subclass': 'C01B', 'year': 2021, 'full_code': 'C01B35/00'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0565'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0562'}, {'cpc_subclass': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/0566'}, {'cpc_subclass': 'H01M', 'year': 2021, 'full_code': 'H01M10/052'}, {'cpc_subclass': 'C01P', 'year': 2021, 'full_code': 'C01P2002/76'}, {'cpc_subclass': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_subclass': 'Y02E', 'year': 2021, 'full_code': 'Y02E60/10'}]}}

exec(code, env_args)
