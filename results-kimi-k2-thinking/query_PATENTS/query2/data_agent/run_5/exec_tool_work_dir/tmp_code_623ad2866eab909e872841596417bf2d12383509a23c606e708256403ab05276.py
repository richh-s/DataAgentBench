code = """import json
import re
from collections import Counter, defaultdict

# Load all patents to get the full dataset
all_patents_file_path = locals()['var_functions.query_db:40']
with open(all_patents_file_path, 'r') as f:
    all_patents = json.load(f)

# Pattern matching for Germany/German connections
germany_pattern = re.compile(r'Germany|GERMANY|DEUTSCHLAND|germany|DE-|\.DE\b|Deutschland', re.IGNORECASE)
german_company_pattern = re.compile(r'\b(gmbh|GmbH|GMBH|Daimler|Siemens|Bosch|Bayer|BASF|Merck|SAP|Volkswagen|Continental|Adidas|Allianz|BMW|Henkel|Fresenius|Mercedes|Audi|Porsche|Thyssenkrupp|E\.ON|RWE|Deutsche)\b', re.IGNORECASE)

# Extract Germany-related patents with year and month information
germany_patents = []

for patent in all_patents:
    patents_info = patent['Patents_info']
    if germany_pattern.search(patents_info) or german_company_pattern.search(patents_info):
        grant_date = patent['grant_date']
        
        # Extract year and month
        year_match = re.search(r'(\d{4})', grant_date)
        month_match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', grant_date, re.IGNORECASE)
        
        if year_match and month_match:
            year = int(year_match.group(1))
            month_name = month_match.group(1)[:3].capitalize()
            month_map = {
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            month_num = month_map.get(month_name, 0)
            
            # Filter for SECOND HALF of each year (July-December)
            if month_num >= 7 and year >= 2015 and year <= 2024:  # Reasonable range
                # Parse CPC codes
                try:
                    cpc_codes = json.loads(patent['cpc'])
                    for cpc in cpc_codes:
                        code = cpc.get('code', '')
                        # Extract level 4 code
                        if '/' in code:
                            level4_code = code.split('/')[0]
                        else:
                            level4_code = code[:4]
                        
                        if len(level4_code) >= 3:
                            germany_patents.append({
                                'cpc_level4': level4_code,
                                'year': year,
                                'month': month_num,
                                'title_localized': patent['title_localized']
                            })
                except:
                    pass

# Group patents by CPC level 4 code and year
cpc_by_year = defaultdict(lambda: defaultdict(int))
for patent in germany_patents:
    cpc_by_year[patent['cpc_level4']][patent['year']] += 1

# Calculate EMA for each CPC code and find best year
results = []
smoothing_factor = 0.1

for cpc_code, year_counts in cpc_by_year.items():
    years = sorted(year_counts.keys())
    if len(years) < 2:
        continue  # Need at least 2 years for EMA
    
    # Calculate EMA for each year
    ema_values = {}
    first_year = min(years)
    initial_value = year_counts[first_year]
    
    for year in years:
        if year == first_year:
            ema_values[year] = initial_value
        else:
            prev_ema = ema_values[year-1]
            current_value = year_counts.get(year, 0)
            ema = (smoothing_factor * current_value) + ((1 - smoothing_factor) * prev_ema)
            ema_values[year] = ema
    
    # Find year with highest EMA
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    
    results.append({
        'cpc_level4_code': cpc_code,
        'best_year': best_year,
        'best_year_ema': ema_values[best_year],
        'patent_count_best_year': year_counts[best_year],
        'total_patents_all_years': sum(year_counts.values()),
        'years_active': len(years),
        'all_year_data': dict(year_counts),
        'ema_by_year': ema_values
    })

# Sort by best EMA value and get top results
top_results = sorted(results, key=lambda x: x['best_year_ema'], reverse=True)[:15]

print('__RESULT__:')
print(json.dumps(top_results, indent=2))

# Also print summary statistics
summary = {
    'total_germany_patents_second_half_all_years': len(germany_patents),
    'total_unique_cpc_level4': len(cpc_by_year),
    'cpc_codes_with_multi_year_data': len(results),
    'analysis_range_years': f"{min([p['year'] for p in germany_patents])}-{max([p['year'] for p in germany_patents])}"
}

for i, result in enumerate(top_results, 1):
    summary[f'rank_{i}'] = f"{result['cpc_level4_code']}: EMA {result['best_year_ema']:.2f} in {result['best_year']} ({result['patent_count_best_year']} patents)"

print(json.dumps(summary, indent=2))"""

env_args = {'var_functions.query_db:0': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:6': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 5, 'sample_grant_dates': ['January 23rd, 2019', '5th Jun 2019', 'dated 10th September 2019', 'Mar 19th, 2019', '10th of December, 2019']}, 'var_functions.execute_python:22': {'total_germany_2019_patents': 5}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_2019_patents': 3838}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'total_2019_germany_patents': 26}, 'var_functions.execute_python:38': {'total_germany_patents_2nd_half_2019': 382, 'unique_cpc_level4_codes': 103, 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['H04W72', 9]]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_germany_patents': 461, 'analysis_note': 'Only 2019 data available - using patent counts as activity measure', 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_germany_2019_2nd_half_patents': 461, 'total_unique_cpc_level4_codes': 137, 'top_cpc_codes_with_counts': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]], 'note': 'Since multi-year data not available, showing 2019 second half patent counts as activity measure'}}

exec(code, env_args)
