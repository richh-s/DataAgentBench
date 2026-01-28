code = """import json
import re
from collections import Counter

# Load all patents
all_patents_file_path = locals()['var_functions.query_db:40']
with open(all_patents_file_path, 'r') as f:
    all_patents = json.load(f)

print(f"Total patents in database: {len(all_patents)}")

# Extract all years and countries
years = []
countries = []
germany_count = 0
germany_patterns_found = []

# Pattern matching for Germany/German connections
germany_pattern = re.compile(r'Germany|GERMANY|DEUTSCHLAND|germany|DE-|\.DE\b|Deutschland', re.IGNORECASE)
german_company_pattern = re.compile(r'\b(gmbh|GmbH|GMBH|Daimler|Siemens|Bosch|Bayer|BASF|Merck|SAP|Volkswagen|Continental|Adidas|Allianz|BMW|Henkel|Fresenius|Mercedes|Audi|Porsche|Thyssenkrupp|E\.ON|RWE|Deutsche)\b', re.IGNORECASE)

for patent in all_patents:
    # Extract year
    grant_date = patent['grant_date']
    year_match = re.search(r'(\d{4})', grant_date)
    if year_match:
        years.append(int(year_match.group(1)))
    
    # Check for Germany
    patents_info = patent['Patents_info']
    if germany_pattern.search(patents_info) or german_company_pattern.search(patents_info):
        germany_count += 1
        germany_patterns_found.append(patents_info[:100])  # First 100 chars

print(f"Germany-related patents: {germany_count}")
print(f"Year range: {min(years) if years else 'None'} - {max(years) if years else 'None'}")
print(f"Unique years: {sorted(set(years))}")
print(f"Sample Germany patterns: {germany_patterns_found[:3]}")"""

env_args = {'var_functions.query_db:0': [{'grant_date': '3rd August 2021'}, {'grant_date': 'dated 6th October 2020'}, {'grant_date': '21st of September, 2021'}, {'grant_date': 'on April 7th, 2020'}, {'grant_date': 'Mar 23rd, 2021'}], 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:6': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 5, 'sample_grant_dates': ['January 23rd, 2019', '5th Jun 2019', 'dated 10th September 2019', 'Mar 19th, 2019', '10th of December, 2019']}, 'var_functions.execute_python:22': {'total_germany_2019_patents': 5}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_2019_patents': 3838}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'total_2019_germany_patents': 26}, 'var_functions.execute_python:38': {'total_germany_patents_2nd_half_2019': 382, 'unique_cpc_level4_codes': 103, 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['H04W72', 9]]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_germany_patents': 461, 'analysis_note': 'Only 2019 data available - using patent counts as activity measure', 'top_cpc_codes': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_germany_2019_2nd_half_patents': 461, 'total_unique_cpc_level4_codes': 137, 'top_cpc_codes_with_counts': [['C04B2235', 32], ['B01D2255', 19], ['B01J29', 16], ['A61M5', 14], ['H01R4', 13], ['H04W52', 12], ['C04B35', 12], ['H04L1', 10], ['H01J49', 10], ['B01J23', 10], ['F02D41', 9], ['H04W72', 9], ['B29C2049', 9], ['B01D53', 9], ['F02M59', 8], ['A61M2005', 8], ['B01J37', 8], ['B01J35', 8], ['A61F5', 6], ['B01J2229', 6]], 'note': 'Since multi-year data not available, showing 2019 second half patent counts as activity measure'}, 'var_functions.execute_python:52': {'total_germany_patents': 2858, 'unique_cpc_level4_codes': 716, 'cpc_codes_analyzed': 142, 'year_range': '2015-2024', 'top_cpc_codes_with_ema': [{'cpc_level4_code': 'H01L24', 'best_year': 2020, 'best_year_ema': 25, 'patent_count_best_year': 25, 'total_patents_all_years': 29, 'years_active': 2}, {'cpc_level4_code': 'B60G2202', 'best_year': 2015, 'best_year_ema': 17, 'patent_count_best_year': 17, 'total_patents_all_years': 20, 'years_active': 3}, {'cpc_level4_code': 'G02F1', 'best_year': 2015, 'best_year_ema': 13, 'patent_count_best_year': 13, 'total_patents_all_years': 23, 'years_active': 3}, {'cpc_level4_code': 'H01R4', 'best_year': 2019, 'best_year_ema': 13, 'patent_count_best_year': 13, 'total_patents_all_years': 14, 'years_active': 2}, {'cpc_level4_code': 'H01L2224', 'best_year': 2023, 'best_year_ema': 12.550000000000002, 'patent_count_best_year': 13, 'total_patents_all_years': 130, 'years_active': 3}, {'cpc_level4_code': 'B60L2240', 'best_year': 2018, 'best_year_ema': 12, 'patent_count_best_year': 12, 'total_patents_all_years': 14, 'years_active': 2}, {'cpc_level4_code': 'A61M5', 'best_year': 2019, 'best_year_ema': 10.94, 'patent_count_best_year': 14, 'total_patents_all_years': 40, 'years_active': 3}, {'cpc_level4_code': 'H01L29', 'best_year': 2022, 'best_year_ema': 10.914000000000001, 'patent_count_best_year': 15, 'total_patents_all_years': 58, 'years_active': 5}, {'cpc_level4_code': 'F02D41', 'best_year': 2019, 'best_year_ema': 9, 'patent_count_best_year': 9, 'total_patents_all_years': 11, 'years_active': 3}, {'cpc_level4_code': 'B60K6', 'best_year': 2018, 'best_year_ema': 8, 'patent_count_best_year': 8, 'total_patents_all_years': 15, 'years_active': 3}]}, 'var_functions.query_db:54': [], 'var_functions.query_db:56': [], 'var_functions.execute_python:60': {'summary': {'total_germany_patents_2nd_half_all_years': 0, 'total_unique_cpc_level4_codes': 0, 'cpc_codes_analyzed': 0, 'cpc_codes_with_2019_data': 0, 'year_range': 'None'}, 'top_cpc_codes_all': [], 'top_cpc_codes_with_2019_data': []}}

exec(code, env_args)
