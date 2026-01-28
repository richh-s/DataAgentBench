code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np

# Read German patents data
file_path = locals()['var_functions.query_db:30']
with open(file_path, 'r') as f:
    patents_data = json.load(f)

# Read CPC definitions
cpc_file_path = locals()['var_functions.query_db:26']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

# Create CPC lookup
cpc_lookup = {item['symbol']: item['titleFull'] for item in cpc_data}

# Function to check if a date string is in second half of 2019
def is_second_half_2019(date_str):
    if not date_str:
        return False
    
    # Check for month names
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December', 'Jul', 'Aug', 'Sep', 'Sept', 'Oct', 'Nov', 'Dec']
    for month in second_half_months:
        if month.lower() in date_str.lower():
            return True
    
    # Check for numeric months 7-12
    patterns = [r'\b7\b', r'\b8\b', r'\b9\b', r'\b10\b', r'\b11\b', r'\b12\b']
    for pattern in patterns:
        if re.search(pattern, date_str) and '2019' in date_str:
            return True
    
    return False

# Helper function to extract CPC level 4 code
def get_cpc_level4(code):
    # Level 4 codes are like B04, B23, B30 (section + class)
    # They consist of 1 letter + 2 digits
    if len(code) >= 3:
        return code[:3]
    return None

# Step 1: Extract CPC groups and filings by year from all German patents
yearly_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_full_titles = {}
cpc_patent_titles = defaultdict(list)

for patent in patents_data:
    # Extract grant year from grant_date
    grant_date = patent.get('grant_date', '')
    if not grant_date:
        continue
    
    # Extract year
    year_match = re.search(r'(20\d{2})', grant_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Parse CPC codes
    cpc_field = patent.get('cpc', '[]')
    if cpc_field and cpc_field != '[]':
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                level4_code = get_cpc_level4(code)
                
                if level4_code:
                    # Count filings for this CPC group in this year
                    yearly_cpc_counts[year][level4_code] += 1
                    
                    # Store the full title for this CPC group
                    if level4_code not in cpc_full_titles:
                        cpc_full_titles[level4_code] = cpc_lookup.get(level4_code, f"Title for {level4_code}")
                    
                    # Store patent title if it's from second half 2019
                    if year == 2019 and is_second_half_2019(grant_date):
                        title_field = patent.get('title_localized', '[]')
                        if title_field and title_field != '[]':
                            try:
                                title_list = json.loads(title_field)
                                for title_item in title_list:
                                    if title_item.get('language') == 'de':
                                        cpc_patent_titles[level4_code].append(title_item.get('text', ''))
                                        break
                            except:
                                pass
        except:
            pass

# Step 2: Calculate exponential moving average for each CPC group
# We need to have data for all years, then apply EMA
all_years = sorted(yearly_cpc_counts.keys())
smoothing_factor = 0.1
cpc_ema_results = {}

for cpc_group in set([cpc for year_counts in yearly_cpc_counts.values() for cpc in year_counts.keys()]):
    # Get counts for all years for this CPC group
    counts = []
    for year in all_years:
        counts.append(yearly_cpc_counts[year].get(cpc_group, 0))
    
    # Calculate EMA
    ema_values = []
    if counts:
        ema = counts[0]  # Initialize with first value
        ema_values.append(ema)
        
        for i in range(1, len(counts)):
            ema = smoothing_factor * counts[i] + (1 - smoothing_factor) * ema
            ema_values.append(ema)
    
    # Find year with highest EMA
    if ema_values:
        max_ema_idx = np.argmax(ema_values)
        best_year = all_years[max_ema_idx]
        max_ema = ema_values[max_ema_idx]
        
        cpc_ema_results[cpc_group] = {
            'best_year': best_year,
            'max_ema': max_ema,
            'ema_values': dict(zip(all_years, ema_values)),
            'raw_counts': dict(zip(all_years, counts))
        }

# Step 3: Sort by max EMA and get top results
top_cpc_groups = sorted(cpc_ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)[:20]

# Step 4: Prepare final results
results = []

for cpc_group, data in top_cpc_groups:
    best_year = data['best_year']
    max_ema = data['max_ema']
    
    # Get full title
    full_title = cpc_full_titles.get(cpc_group, f"Title for {cpc_group}")
    
    # Get a sample patent title from second half 2019 if available
    patent_title = ""
    if cpc_group in cpc_patent_titles and cpc_patent_titles[cpc_group]:
        patent_title = cpc_patent_titles[cpc_group][0]  # Take first title
    
    results.append({
        'cpc_group_code': cpc_group,
        'full_title': full_title,
        'best_year': int(best_year),
        'ema_value': float(max_ema),
        'patent_title_2019': patent_title
    })

print('__RESULT__:')
print(json.dumps(results, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.execute_python:8': {'total_patents': 5, 'sample_keys': ['Patents_info', 'kind_code', 'application_kind', 'pct_number', 'family_id', 'title_localized', 'abstract_localized', 'claims_localized_html', 'description_localized_html', 'publication_date', 'filing_date', 'grant_date', 'priority_date', 'priority_claim', 'inventor_harmonized', 'examiner', 'uspc', 'ipc', 'cpc', 'citation', 'parent', 'child', 'entity_status', 'art_unit'], 'grant_date_sample': '14th Mar 2019', 'patents_info_sample': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc_sample': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:10': 'Loaded 5 patents for initial analysis', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 50 German patents from 2019', 'var_functions.execute_python:16': 'Filtered to 50 patents granted in second half of 2019', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total German patents in 2019: 50', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.execute_python:28': 'Total German patents in 2019: 50', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'Total German patents: 11644'}

exec(code, env_args)
