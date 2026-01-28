code = """import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict
import numpy as np

# Load all German patents
file_path = locals()['var_functions.query_db:50']
with open(file_path, 'r') as f:
    all_patents_data = json.load(f)

# Load CPC level 4 definitions
cpc_file_path = locals()['var_functions.query_db:38']
with open(cpc_file_path, 'r') as f:
    cpc_data = json.load(f)

# Create CPC lookup for level 4
cpc_lookup = {item['symbol']: item['titleFull'] for item in cpc_data}

# Function to check if a date string is in second half of 2019
def is_second_half_2019(date_str):
    if not date_str or '2019' not in str(date_str):
        return False
    
    # Check for month names (July-December)
    second_half_months = ['July', 'August', 'September', 'October', 'November', 'December', 
                          'Jul', 'Aug', 'Sep', 'Sept', 'Oct', 'Nov', 'Dec']
    for month in second_half_months:
        if month.lower() in str(date_str).lower():
            return True
    
    # Check for numeric months 7-12 with word boundaries
    patterns = [r'\b7[\/\-\s]', r'\b8[\/\-\s]', r'\b9[\/\-\s]', r'\b10[\/\-\s]', r'\b11[\/\-\s]', r'\b12[\/\-\s]']
    for pattern in patterns:
        if re.search(pattern, str(date_str)):
            return True
    
    return False

# Helper function to extract CPC level 4 code (section + class, e.g., B04, H01)
def get_cpc_level4(code):
    """Extract level 4 CPC code: 1 letter + 2 digits"""
    if code and len(code) >= 3:
        # Pattern: letter followed by exactly 2 digits
        if re.match(r'^[A-Z]\d{2}$', code[:3]):
            return code[:3]
    return None

# Step 1: Build yearly CPC filing counts from ALL German patents
yearly_cpc_counts = defaultdict(lambda: defaultdict(int))
cpc_full_titles = {}
cpc_patent_titles_2019 = defaultdict(list)  # Store titles from 2nd half 2019

processed_patents = 0
patents_2019_second_half = 0

for patent in all_patents_data:
    # Extract grant year from grant_date
    grant_date = patent.get('grant_date', '')
    if not grant_date:
        continue
    
    # Extract year
    year_match = re.search(r'(20\d{2})', str(grant_date))
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    processed_patents += 1
    
    # Count patents from second half 2019
    if year == 2019 and is_second_half_2019(grant_date):
        patents_2019_second_half += 1
    
    # Parse CPC codes
    cpc_field = patent.get('cpc', '[]')
    if cpc_field and cpc_field != '[]':
        try:
            cpc_list = json.loads(cpc_field)
            for cpc_item in cpc_list:
                code = cpc_item.get('code', '')
                if not code:
                    continue
                    
                level4_code = get_cpc_level4(code)
                
                if level4_code:
                    # Count filings for this CPC group in this year
                    yearly_cpc_counts[year][level4_code] += 1
                    
                    # Store the full title for this CPC group
                    if level4_code not in cpc_full_titles and level4_code in cpc_lookup:
                        cpc_full_titles[level4_code] = cpc_lookup[level4_code]
                    
                    # Store patent title if it's from second half 2019
                    if year == 2019 and is_second_half_2019(grant_date):
                        title_field = patent.get('title_localized', '[]')
                        if title_field and title_field != '[]':
                            try:
                                title_list = json.loads(title_field)
                                for title_item in title_list:
                                    if title_item.get('language') == 'de':
                                        title_text = title_item.get('text', '')
                                        if title_text and len(title_text) > 10:
                                            cpc_patent_titles_2019[level4_code].append(title_text)
                                        break
                            except:
                                pass
        except Exception as e:
            continue

# Step 2: Calculate exponential moving average for each CPC group
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
        avg_raw_count = np.mean(counts)
        
        cpc_ema_results[cpc_group] = {
            'best_year': best_year,
            'max_ema': max_ema,
            'avg_raw_count': avg_raw_count,
            'ema_values': dict(zip(all_years, ema_values)),
            'raw_counts': dict(zip(all_years, counts))
        }

# Step 3: Sort by max EMA and get top results
top_cpc_groups = sorted(cpc_ema_results.items(), key=lambda x: x[1]['max_ema'], reverse=True)[:20]

# Step 4: Prepare final results with patent titles from second half 2019
results = []

for cpc_group, data in top_cpc_groups:
    best_year = int(data['best_year'])
    max_ema = float(data['max_ema'])
    avg_count = float(data['avg_raw_count'])
    
    # Get full title
    full_title = cpc_full_titles.get(cpc_group, f"CPC Group {cpc_group}")
    
    # Get a sample patent title from second half 2019 if available
    patent_title = ""
    if cpc_group in cpc_patent_titles_2019 and cpc_patent_titles_2019[cpc_group]:
        patent_title = cpc_patent_titles_2019[cpc_group][0][:200]  # Limit length
    
    results.append({
        'cpc_group_code': cpc_group,
        'full_title': full_title[:120],  # Limit length for readability
        'best_year': best_year,
        'max_ema': round(max_ema, 2),
        'avg_annual_filings': round(avg_count, 2),
        'sample_patent_title_2019': patent_title
    })

# Create summary
summary = {
    'total_patents_processed': processed_patents,
    'patents_from_2019_second_half': patents_2019_second_half,
    'years_analyzed': sorted(list(yearly_cpc_counts.keys())),
    'cpc_groups_analyzed': len(cpc_ema_results),
    'top_groups': results
}

print('__RESULT__:')
print(json.dumps(summary, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.execute_python:8': {'total_patents': 5, 'sample_keys': ['Patents_info', 'kind_code', 'application_kind', 'pct_number', 'family_id', 'title_localized', 'abstract_localized', 'claims_localized_html', 'description_localized_html', 'publication_date', 'filing_date', 'grant_date', 'priority_date', 'priority_claim', 'inventor_harmonized', 'examiner', 'uspc', 'ipc', 'cpc', 'citation', 'parent', 'child', 'entity_status', 'art_unit'], 'grant_date_sample': '14th Mar 2019', 'patents_info_sample': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'cpc_sample': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:10': 'Loaded 5 patents for initial analysis', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 50 German patents from 2019', 'var_functions.execute_python:16': 'Filtered to 50 patents granted in second half of 2019', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total German patents in 2019: 50', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.execute_python:28': 'Total German patents in 2019: 50', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'Total German patents: 11644', 'var_functions.execute_python:36': [{'cpc_group_code': 'A61', 'full_title': 'Title for A61', 'best_year': 2009, 'ema_value': 130.83892455900002, 'patent_title_2019': 'Fußplatte und Orthese'}, {'cpc_group_code': 'H01', 'full_title': 'Title for H01', 'best_year': 2024, 'ema_value': 86.75049044892519, 'patent_title_2019': 'Verfahren zur Ionenherstellung'}, {'cpc_group_code': 'Y10', 'full_title': 'Title for Y10', 'best_year': 2009, 'ema_value': 70.20029575400001, 'patent_title_2019': 'Elektronischer Schlüssel für ein Fahrzeug'}, {'cpc_group_code': 'B60', 'full_title': 'Title for B60', 'best_year': 2023, 'ema_value': 62.050278316865125, 'patent_title_2019': 'Landfahrzeug mit einem Chassis und einer Mehrzahl von daran angebrachten Eckstützeinheiten'}, {'cpc_group_code': 'H04', 'full_title': 'Title for H04', 'best_year': 2009, 'ema_value': 56.388251112000006, 'patent_title_2019': 'Sub-Frame-Zuteilung für energieeffiziente LTE'}, {'cpc_group_code': 'G01', 'full_title': 'Title for G01', 'best_year': 2006, 'ema_value': 39.21071400000001, 'patent_title_2019': 'Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor'}, {'cpc_group_code': 'C07', 'full_title': 'Title for C07', 'best_year': 2005, 'ema_value': 36.004110000000004, 'patent_title_2019': ''}, {'cpc_group_code': 'F16', 'full_title': 'Title for F16', 'best_year': 2024, 'ema_value': 33.503984011800895, 'patent_title_2019': 'Getriebevorrichtung der oszillierend innen eingreifenden Bauart'}, {'cpc_group_code': 'G11', 'full_title': 'Title for G11', 'best_year': 2001, 'ema_value': 31.6, 'patent_title_2019': ''}, {'cpc_group_code': 'G06', 'full_title': 'Title for G06', 'best_year': 2007, 'ema_value': 24.2341611, 'patent_title_2019': ''}, {'cpc_group_code': 'B31', 'full_title': 'Title for B31', 'best_year': 2000, 'ema_value': 24.0, 'patent_title_2019': ''}, {'cpc_group_code': 'B29', 'full_title': 'Title for B29', 'best_year': 2007, 'ema_value': 23.403817200000006, 'patent_title_2019': 'Blasvorrichtung zum Expandieren von Behältnissen'}, {'cpc_group_code': 'C08', 'full_title': 'Title for C08', 'best_year': 2006, 'ema_value': 20.809021, 'patent_title_2019': ''}, {'cpc_group_code': 'G09', 'full_title': 'Title for G09', 'best_year': 2000, 'ema_value': 20.0, 'patent_title_2019': ''}, {'cpc_group_code': 'F02', 'full_title': 'Title for F02', 'best_year': 2020, 'ema_value': 19.692680939948776, 'patent_title_2019': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors'}, {'cpc_group_code': 'B01', 'full_title': 'Title for B01', 'best_year': 2007, 'ema_value': 19.030197, 'patent_title_2019': ''}, {'cpc_group_code': 'B65', 'full_title': 'Title for B65', 'best_year': 2014, 'ema_value': 18.5668016292095, 'patent_title_2019': ''}, {'cpc_group_code': 'C03', 'full_title': 'Title for C03', 'best_year': 2000, 'ema_value': 17.0, 'patent_title_2019': ''}, {'cpc_group_code': 'C04', 'full_title': 'Title for C04', 'best_year': 2008, 'ema_value': 16.297189200000002, 'patent_title_2019': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken'}, {'cpc_group_code': 'C09', 'full_title': 'Title for C09', 'best_year': 2000, 'ema_value': 16.0, 'patent_title_2019': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': 'Loaded 50 patents and 137 CPC level 4 definitions', 'var_functions.execute_python:42': 'Loaded 11644 total German patents and 137 CPC level 4 definitions', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:48': 'Loaded 11644 German patents and 137 CPC level 4 definitions', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:52': 'Ready to process 11644 German patents'}

exec(code, env_args)
