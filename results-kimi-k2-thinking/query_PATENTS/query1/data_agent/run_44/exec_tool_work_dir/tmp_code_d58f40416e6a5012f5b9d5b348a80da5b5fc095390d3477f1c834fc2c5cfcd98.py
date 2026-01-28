code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Get file paths
patents_file_path = locals()['var_functions.query_db:14']
level5_file_path = locals()['var_functions.query_db:6']

# Load data
with open(patents_file_path, 'r') as f:
    patents_data = json.load(f)

with open(level5_file_path, 'r') as f:
    level5_data = json.load(f)

level5_symbols = {item['symbol'] for item in level5_data}

# Process patents data
processed_data = []

for patent in patents_data:
    # Parse publication date
    date_str = patent.get('publication_date', '')
    if not date_str:
        continue
    
    # Extract year from date string
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Only consider years up to 2024 for meaningful analysis
    if year < 1900 or year > 2024:
        continue
    
    # Parse CPC codes
    cpc_str = patent.get('cpc', '')
    if not cpc_str:
        continue
    
    try:
        cpc_list = json.loads(cpc_str)
        
        for cpc_item in cpc_list:
            code = cpc_item.get('code', '')
            if not code:
                continue
            
            # Extract level 5 CPC group
            group_match = re.match(r'^([A-HY][0-9]{2}[A-Z])', code)
            if group_match:
                group_code = group_match.group(1)
                if group_code in level5_symbols:
                    processed_data.append({
                        'cpc_group': group_code,
                        'year': year
                    })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(processed_data)

# Count filings per CPC group per year
counts_by_year = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')

# Create a complete grid of all groups and years
all_groups = df['cpc_group'].unique()
all_years = sorted(df['year'].unique())

# For each group, calculate EMA and find best year
results = []
alpha = 0.2  # smoothing factor

for group in all_groups:
    group_data = counts_by_year[counts_by_year['cpc_group'] == group].sort_values('year')
    
    if len(group_data) < 2:  # Need at least 2 years for EMA
        continue
    
    # Create a complete series with all years, fill missing with 0
    complete_counts = []
    year_list = []
    data_idx = 0
    
    for year in all_years:
        if data_idx < len(group_data) and group_data.iloc[data_idx]['year'] == year:
            complete_counts.append(group_data.iloc[data_idx]['count'])
            data_idx += 1
        else:
            complete_counts.append(0)
        year_list.append(year)
    
    # Calculate EMA
    ema_values = []
    ema = complete_counts[0]  # Initialize with first value
    ema_values.append(ema)
    
    for i in range(1, len(complete_counts)):
        ema = alpha * complete_counts[i] + (1 - alpha) * ema_values[-1]
        ema_values.append(ema)
    
    # Find year with highest EMA
    max_ema_idx = np.argmax(ema_values)
    best_year = year_list[max_ema_idx]
    max_ema = ema_values[max_ema_idx]
    
    results.append({
        'cpc_group': group,
        'best_year': best_year,
        'max_ema': max_ema,
        'ema_values': ema_values,
        'years': year_list
    })

# Filter groups where best year is 2022
groups_best_2022 = [r for r in results if r['best_year'] == 2022]

print('__RESULT__:')
print(json.dumps({
    'total_level5_groups': len(all_groups),
    'groups_with_best_year_2022': len(groups_best_2022),
    'sample_results': groups_best_2022[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'level5_count': 677, 'sample_level5': ['G06D', 'C01C', 'H03G', 'A01F', 'A23F', 'G03F', 'B25D', 'D06L', 'F01C', 'C23D']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_patents': 277813, 'sample_data': [{'cpc': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/582",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01P2002/76",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1315",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0562",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/028",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/505",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0565",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0566",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/052",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01G45/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'publication_date': 'Aug 3rd, 2021'}, {'cpc': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0893",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0886",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H3/76",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2037/0873",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2007",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H3/62",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/084",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/0043",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F16H2200/2041",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'publication_date': 'Oct 6th, 2020'}]}, 'var_functions.execute_python:18': {'total_patents': 277813, 'level5_cpc_count': 677, 'sample_level5': ['A61Q', 'B25J', 'G06V', 'C08F', 'F21L', 'F22D', 'G10D', 'F26B', 'B62C', 'F04F']}, 'var_functions.execute_python:20': {'total_records': 2681344, 'unique_cpc_groups': 669, 'year_range': {'min': 1837, 'max': 2024}, 'sample_data': [{'cpc_group': 'C01B', 'year': 2021, 'full_code': 'C01B33/00'}, {'cpc_group': 'C01B', 'year': 2021, 'full_code': 'C01B35/00'}, {'cpc_group': 'H01M', 'year': 2021, 'full_code': 'H01M10/0565'}, {'cpc_group': 'H01M', 'year': 2021, 'full_code': 'H01M10/0562'}, {'cpc_group': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_group': 'H01M', 'year': 2021, 'full_code': 'H01M10/0566'}, {'cpc_group': 'H01M', 'year': 2021, 'full_code': 'H01M10/052'}, {'cpc_group': 'C01P', 'year': 2021, 'full_code': 'C01P2002/76'}, {'cpc_group': 'C01G', 'year': 2021, 'full_code': 'C01G45/006'}, {'cpc_group': 'Y02E', 'year': 2021, 'full_code': 'Y02E60/10'}]}}

exec(code, env_args)
