code = """import json
import re
from collections import defaultdict

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
            if month_num >= 7 and year >= 2015 and year <= 2024:
                # Parse CPC codes
                try:
                    cpc_codes = json.loads(patent['cpc'])
                    for cpc in cpc_codes:
                        code = cpc.get('code', '')
                        # Extract level 4 code - take first 4 characters or section/class
                        if len(code) >= 4:
                            level4_code = code[:4]
                        else:
                            level4_code = code
                        
                        if len(level4_code) >= 3:  # Minimum length for meaningful CPC code
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

# Get year range
if germany_patents:
    all_years = sorted(set(p['year'] for p in germany_patents))
else:
    all_years = []

# Calculate EMA for each CPC code (level 4 only) and find best year
results = []
smoothing_factor = 0.1

for cpc_code, year_counts in cpc_by_year.items():
    years = sorted(year_counts.keys())
    if len(years) < 2:
        continue  # Need at least 2 years for meaningful EMA
    
    # Calculate EMA for each year
    ema_values = {}
    
    for i, year in enumerate(years):
        if i == 0:
            ema_values[year] = float(year_counts[year])
        else:
            prev_year = years[i-1]
            prev_ema = ema_values[prev_year]
            current_value = year_counts[year]
            ema = (smoothing_factor * current_value) + ((1 - smoothing_factor) * prev_ema)
            ema_values[year] = ema
    
    # Find year with highest EMA
    best_year = max(ema_values.keys(), key=lambda y: ema_values[y])
    
    # Check if 2019 is in the dataset for this CPC code and get 2019 second half count
    patents_2019_2nd_half = year_counts.get(2019, 0)
    
    results.append({
        'cpc_level4_code': cpc_code,
        'best_year': best_year,
        'best_year_ema': round(ema_values[best_year], 2),
        'patent_count_best_year': year_counts[best_year],
        'total_patents_all_years': sum(year_counts.values()),
        'years_active': len(years),
        'patents_in_2019_second_half': patents_2019_2nd_half,
        'year_by_year_counts': dict(year_counts),
        'ema_by_year': {str(year): round(ema, 2) for year, ema in ema_values.items()}
    })

# Sort by best EMA value and get top results
top_results = sorted(results, key=lambda x: x['best_year_ema'], reverse=True)[:10]

# Get results with 2019 data and sort by EMA
top_results_2019 = sorted([r for r in results if r['patents_in_2019_second_half'] > 0], 
                         key=lambda x: x['best_year_ema'], reverse=True)[:10]

print('__RESULT__:')
print(json.dumps({
    'summary': {
        'total_germany_patents_2nd_half_all_years': len(germany_patents),
        'total_unique_cpc_level4_codes': len(cpc_by_year),
        'cpc_codes_analyzed': len(results),
        'cpc_codes_with_2019_data': len([r for r in results if r['patents_in_2019_second_half'] > 0]),
        'year_range': f"{min(all_years)}-{max(all_years)}" if all_years else "None"
    },
    'top_cpc_codes_all': top_results,
    'top_cpc_codes_with_2019_data': top_results_2019
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:6': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 5, 'sample_grant_dates': ['January 23rd, 2019', '5th Jun 2019', 'dated 10th September 2019', 'Mar 19th, 2019', '10th of December, 2019']}, 'var_functions.execute_python:22': {'total_germany_2019_patents': 5}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_2019_patents': 3838}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'total_2019_germany_patents': 26}, 'var_functions.execute_python:38': {'total_germany_patents_2nd_half_2019': 382, 'unique_cpc_level4_codes': 103, 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['H04W72', 9]]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_germany_patents': 461, 'analysis_note': 'Only 2019 data available - using patent counts as activity measure', 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_germany_2019_2nd_half_patents': 461, 'total_unique_cpc_level4_codes': 137, 'top_cpc_codes_with_counts': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]], 'note': 'Since multi-year data not available, showing 2019 second half patent counts as activity measure'}, 'var_functions.execute_python:52': {'total_germany_patents': 2858, 'unique_cpc_level4_codes': 716, 'cpc_codes_analyzed': 142, 'year_range': '2015-2024', 'top_cpc_codes_with_ema': [{'cpc_level4_code': 'H01L24', 'best_year': 2020, 'best_year_ema': 25, 'patent_count_best_year': 25, 'total_patents_all_years': 29, 'years_active': 2}, {'cpc_level4_code': 'B60G2202', 'best_year': 2015, 'best_year_ema': 17, 'patent_count_best_year': 17, 'total_patents_all_years': 20, 'years_active': 3}, {'cpc_level4_code': 'G02F1', 'best_year': 2015, 'best_year_ema': 13, 'patent_count_best_year': 13, 'total_patents_all_years': 23, 'years_active': 3}, {'cpc_level4_code': 'H01R4', 'best_year': 2019, 'best_year_ema': 13, 'patent_count_best_year': 13, 'total_patents_all_years': 14, 'years_active': 2}, {'cpc_level4_code': 'H01L2224', 'best_year': 2023, 'best_year_ema': 12.550000000000002, 'patent_count_best_year': 13, 'total_patents_all_years': 130, 'years_active': 3}, {'cpc_level4_code': 'B60L2240', 'best_year': 2018, 'best_year_ema': 12, 'patent_count_best_year': 12, 'total_patents_all_years': 14, 'years_active': 2}, {'cpc_level4_code': 'A61M5', 'best_year': 2019, 'best_year_ema': 10.94, 'patent_count_best_year': 14, 'total_patents_all_years': 40, 'years_active': 3}, {'cpc_level4_code': 'H01L29', 'best_year': 2022, 'best_year_ema': 10.914000000000001, 'patent_count_best_year': 15, 'total_patents_all_years': 58, 'years_active': 5}, {'cpc_level4_code': 'F02D41', 'best_year': 2019, 'best_year_ema': 9, 'patent_count_best_year': 9, 'total_patents_all_years': 11, 'years_active': 3}, {'cpc_level4_code': 'B60K6', 'best_year': 2018, 'best_year_ema': 8, 'patent_count_best_year': 8, 'total_patents_all_years': 15, 'years_active': 3}]}, 'var_functions.query_db:54': [], 'var_functions.query_db:56': [], 'var_functions.execute_python:60': {'summary': {'total_germany_patents_2nd_half_all_years': 0, 'total_unique_cpc_level4_codes': 0, 'cpc_codes_analyzed': 0, 'cpc_codes_with_2019_data': 0, 'year_range': 'None'}, 'top_cpc_codes_all': [], 'top_cpc_codes_with_2019_data': []}, 'var_functions.query_db:66': [{'symbol': 'H01L2224/37294', 'titleFull': 'Material of the matrix with a principal constituent of the material being a liquid not provided for in groups H01L2224/372\xa0-\xa0H01L2224/37291'}, {'symbol': 'H01L2224/37295', 'titleFull': 'Material of the matrix with a principal constituent of the material being a gas not provided for in groups H01L2224/372\xa0-\xa0H01L2224/37291'}, {'symbol': 'H01L2224/37286', 'titleFull': 'Material of the matrix with a principal constituent of the material being a non metallic, non metalloid inorganic material'}, {'symbol': 'H01L2224/372', 'titleFull': 'Material of the matrix with a principal constituent of the material being a metal or a metalloid, e.g. boron [B], silicon [Si], germanium [Ge], arsenic [As], antimony [Sb], tellurium [Te] and polonium [Po], and alloys thereof'}, {'symbol': 'H01L2224/3729', 'titleFull': 'Material of the matrix with a principal constituent of the material being a polymer, e.g. polyester, phenolic based polymer, epoxy'}, {'symbol': 'H01L2224/37299', 'titleFull': 'Base material'}, {'symbol': 'H01L2224/37499', 'titleFull': 'Shape or distribution of the fillers'}, {'symbol': 'H01L2224/37399', 'titleFull': 'Coating material'}, {'symbol': 'H01L2224/37614', 'titleFull': 'Thallium [Tl] as principal constituent'}, {'symbol': 'H01L2224/37605', 'titleFull': 'Gallium [Ga] as principal constituent'}]}

exec(code, env_args)
