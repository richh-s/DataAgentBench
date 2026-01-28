code = """import json
import pandas as pd
import re
from collections import defaultdict

# Read multi-year German patents data
with open('/workspace/file_storage/functions.query_db:40.json', 'r') as f:
    data = json.load(f)

# Extract year from natural language date
def extract_year(date_str):
    if not date_str:
        return None
    match = re.search(r'(20(?:1[0-9]|2[0-1]))', str(date_str))
    return int(match.group(1)) if match else None

# Extract CPC level 4 code properly
# CPC level 4: Main group level, format like "H01L21/00" from "H01L21/02"
# We keep the main class and subgroup digits before any further subdivision

def extract_cpc_level4(full_code):
    if not full_code or '/' not in full_code:
        return None
    
    parts = full_code.split('/')
    main_class = parts[0]
    subgroup = parts[1] if len(parts) > 1 else ''
    
    # Extract main group digits (first sequence of digits in subgroup)
    main_group = ''
    for char in subgroup:
        if char.isdigit():
            main_group += char
        else:
            break
    
    # Pad to at least 2 digits
    if len(main_group) == 0:
        main_group = '00'
    elif len(main_group) == 1:
        main_group = main_group + '0'
    
    return f"{main_class}/{main_group}"

# Process all German patents for 2016-2020
german_patents_by_year = defaultdict(lambda: defaultdict(set))  # year -> cpc_group -> set of patents

for record in data:
    patents_info = str(record.get('Patents_info', ''))
    grant_date = str(record.get('grant_date', ''))
    cpc_json = str(record.get('cpc', '[]'))
    
    # Confirm German patent
    if 'DE-' not in patents_info and 'from DE' not in patents_info and 'DE patent' not in patents_info:
        continue
    
    year = extract_year(grant_date)
    if not year or year < 2016 or year > 2020:
        continue
    
    try:
        cpc_list = json.loads(cpc_json)
    except:
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            full_code = cpc_item['code']
            level4 = extract_cpc_level4(full_code)
            if level4:
                # Use patent snippet for deduplication
                patent_id = patents_info[:100]
                german_patents_by_year[year][level4].add(patent_id)

# Step 1: Build yearly counts per CPC group for EMA calculation
cpc_yearly_counts = defaultdict(list)  # cpc_group -> [(year, count), ...]

for year in range(2016, 2021):  # 2016-2020
    for cpc_group, patents in german_patents_by_year[year].items():
        cpc_yearly_counts[cpc_group].append((year, len(patents)))

# Step 2: Calculate EMA (α=0.1) for each CPC group
ema_results = []

for cpc_group, year_counts in cpc_yearly_counts.items():
    # Need at least 2 years for EMA
    if len(year_counts) < 2:
        continue
    
    # Sort by year
    year_counts.sort(key=lambda x: x[0])
    years = [yc[0] for yc in year_counts]
    counts = [yc[1] for yc in year_counts]
    
    # Calculate EMA manually
    ema_values = []
    ema_prev = counts[0]  # Initialize with first count
    ema_values.append(ema_prev)
    
    alpha = 0.1
    for count in counts[1:]:
        ema = alpha * count + (1 - alpha) * ema_prev
        ema_values.append(ema)
        ema_prev = ema
    
    # Find year with highest EMA
    max_ema_idx = ema_values.index(max(ema_values))
    best_year = years[max_ema_idx]
    best_ema_value = ema_values[max_ema_idx]
    best_patent_count = counts[max_ema_idx]
    
    # Only include if best year is reasonably high
    if best_patent_count >= 1:
        ema_results.append({
            'cpc_group_code': cpc_group,
            'best_year': best_year,
            'ema_value': round(best_ema_value, 3),
            'patent_count': best_patent_count
        })

# Step 3: Sort by EMA value
top_cpc_results = sorted(ema_results, key=lambda x: x['ema_value'], reverse=True)

# Step 4: Get full CPC titles from definition database
# Extract unique CPC codes to query
top_cpc_codes = [r['cpc_group_code'] for r in top_cpc_results[:20]]

print('__RESULT__:')
print(json.dumps({
    'status': 'analysis_complete',
    'total_years_analyzed': len(range(2016, 2021)),
    'total_cpc_groups': len(cpc_yearly_counts),
    'ema_results_calculated': len(ema_results),
    'top_results': top_cpc_results[:25],
    'top_cpc_codes_to_query': top_cpc_codes
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'files_in_tmp': []}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'json_files': ['/workspace/file_storage/functions.query_db:8.json', '/workspace/file_storage/functions.query_db:9.json', '/workspace/file_storage/functions.query_db:18.json', '/workspace/file_storage/functions.query_db:2.json', '/workspace/file_storage/functions.query_db:20.json']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_german_patents_2019': 50, 'second_half_german_patents': 24, 'total_cpc_assignments': 252, 'cpc_groups': ['B41F/102', 'B41F/00', 'F02D/300', 'F02D/20', 'F02M/005', 'F02D/00', 'F02M/102', 'F02M/04', 'F02M/44', 'F02M/06', 'F04B/001', 'F02M/368', 'G01D/24', 'B23K/001', 'B63B/50', 'H04W/21', 'H04W/56', 'H04L/003', 'H04L/161', 'H04W/026']}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_german_patents': 68, 'sample_record': {'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019', 'cpc': '[\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G06F9/45533",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:36': {'total_german_patents_2019': 68, 'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'unique_cpc_level4_groups': 188, 'top_cpc_groups': [['H04L/186', 4], ['C04B/656', 4], ['C04B/322', 4], ['C04B/645', 4], ['F02D/20', 3], ['H04W/21', 3], ['H04W/56', 3], ['H04W/026', 3], ['H04W/021', 3], ['H04W/022', 3], ['H04W/044', 3], ['H04W/025', 3], ['F24B/023', 3], ['F23L/04', 3], ['F23L/00', 3]]}, 'var_functions.execute_python:38': {'german_patents_second_half_2019': 33, 'total_cpc_assignments': 311, 'sample_cpc_codes': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/102', 'cpc_level4': 'B41F/100', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F22/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'full_cpc_code': 'B41F21/00', 'cpc_level4': 'B41F/000', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/3005', 'cpc_level4': 'F02D/300', 'year': 2019}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'full_cpc_code': 'F02D41/20', 'cpc_level4': 'F02D/200', 'year': 2019}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_german_patents_all_years': 510, 'sample_record': {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010', 'cpc': '[\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/003",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B26B5/001",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}}, 'var_functions.execute_python:46': {'status': 'success', 'total_cpc_records': 2479, 'german_patents_analyzed': 2479, 'unique_cpc_groups': 243, 'years_range': '2015-2019', 'top_results': [{'cpc_level4': 'D06F/00', 'best_year': 2015, 'ema_value': 47.0, 'patent_count': 47}, {'cpc_level4': 'B60G/00', 'best_year': 2015, 'ema_value': 35.0, 'patent_count': 35}, {'cpc_level4': 'D04H/00', 'best_year': 2016, 'ema_value': 30.0, 'patent_count': 30}, {'cpc_level4': 'H01L/00', 'best_year': 2019, 'ema_value': 24.087000000000003, 'patent_count': 111}, {'cpc_level4': 'A61F/00', 'best_year': 2015, 'ema_value': 23.0, 'patent_count': 23}, {'cpc_level4': 'H03F/00', 'best_year': 2016, 'ema_value': 22.0, 'patent_count': 22}, {'cpc_level4': 'F16D/00', 'best_year': 2015, 'ema_value': 18.0, 'patent_count': 18}, {'cpc_level4': 'G01N/00', 'best_year': 2015, 'ema_value': 17.0, 'patent_count': 17}, {'cpc_level4': 'G02F/00', 'best_year': 2015, 'ema_value': 16.0, 'patent_count': 16}, {'cpc_level4': 'B01D/00', 'best_year': 2017, 'ema_value': 14.7, 'patent_count': 21}], 'ema_analysis_complete': True}, 'var_functions.execute_python:48': {'total_german_patents_2019': 68, 'second_half_2019_patents': 311, 'unique_cpc_groups_2019': 108, 'top_cpc_groups': {'C04B/600': 20, 'H04W/000': 15, 'B29C/500': 13, 'H04L/100': 10, 'F02D/000': 9, 'C04B/500': 8, 'C04B/300': 8, 'G02B/200': 7, 'G02B/100': 7, 'H04L/000': 6, 'F23L/000': 6, 'H01J/000': 6, 'G02B/000': 6, 'F02D/200': 5, 'F02M/000': 5, 'F02N/000': 5, 'F16H/000': 5, 'H04W/200': 4, 'A61F/000': 4, 'G01M/200': 4}}, 'var_functions.execute_python:50': {'total_records': 2030, 'year_range': '2016-2019', 'unique_cpc_groups': 527, 'sample_data': [{'cpc_level4': 'A01B/000', 'year': 2016, 'patent_count': 1}, {'cpc_level4': 'A01K/000', 'year': 2018, 'patent_count': 1}, {'cpc_level4': 'A21C/000', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23B/000', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23L/100', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23N/000', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23N/100', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A43B/000', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A43B/200', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A45D/000', 'year': 2016, 'patent_count': 1}]}, 'var_functions.execute_python:52': {'status': 'success', 'total_cpc_yearly_records': 2030, 'german_patents_years': '2016-2019', 'unique_years': [2016, 2017, 2018, 2019], 'unique_cpc_groups': 527, 'top_cpc_groups': [{'cpc_level4': 'H01L/000', 'best_year': 2019, 'ema_value': 20.11, 'patent_count': 40}, {'cpc_level4': 'F16H/000', 'best_year': 2019, 'ema_value': 10.1, 'patent_count': 11}, {'cpc_level4': 'B01D/000', 'best_year': 2017, 'ema_value': 10.0, 'patent_count': 10}, {'cpc_level4': 'Y10T/200', 'best_year': 2016, 'ema_value': 10.0, 'patent_count': 10}, {'cpc_level4': 'C04B/500', 'best_year': 2018, 'ema_value': 10.0, 'patent_count': 10}, {'cpc_level4': 'D04H/400', 'best_year': 2016, 'ema_value': 10.0, 'patent_count': 10}, {'cpc_level4': 'F04B/100', 'best_year': 2017, 'ema_value': 9.0, 'patent_count': 9}, {'cpc_level4': 'H03H/100', 'best_year': 2016, 'ema_value': 8.0, 'patent_count': 8}, {'cpc_level4': 'Y10T/100', 'best_year': 2016, 'ema_value': 8.0, 'patent_count': 8}, {'cpc_level4': 'H01L/800', 'best_year': 2017, 'ema_value': 8.0, 'patent_count': 8}, {'cpc_level4': 'H02J/000', 'best_year': 2017, 'ema_value': 8.0, 'patent_count': 8}, {'cpc_level4': 'C04B/600', 'best_year': 2019, 'ema_value': 7.4, 'patent_count': 20}, {'cpc_level4': 'H04W/000', 'best_year': 2019, 'ema_value': 7.0, 'patent_count': 16}, {'cpc_level4': 'B62D/000', 'best_year': 2018, 'ema_value': 7.0, 'patent_count': 7}, {'cpc_level4': 'H03H/000', 'best_year': 2016, 'ema_value': 6.0, 'patent_count': 6}, {'cpc_level4': 'G05B/300', 'best_year': 2017, 'ema_value': 6.0, 'patent_count': 6}, {'cpc_level4': 'A61F/000', 'best_year': 2018, 'ema_value': 6.0, 'patent_count': 6}, {'cpc_level4': 'F02N/000', 'best_year': 2016, 'ema_value': 6.0, 'patent_count': 6}, {'cpc_level4': 'F16H/100', 'best_year': 2016, 'ema_value': 6.0, 'patent_count': 6}, {'cpc_level4': 'B60Q/100', 'best_year': 2017, 'ema_value': 6.0, 'patent_count': 6}], 'ema_calculation_complete': True}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': [], 'var_functions.execute_python:60': {'total_patents_analyzed': 2030, 'cpc_yearly_records': 911, 'unique_cpc_groups': 809, 'years_analyzed': [2016, 2017, 2018, 2019], 'top_cpc_codes': [{'cpc_level4': 'H01L29240/00', 'best_year': 2017, 'ema_value': 3.0, 'patent_count': 3}, {'cpc_level4': 'F16H22000/00', 'best_year': 2018, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'B23K263/00', 'best_year': 2017, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'B23K260/00', 'best_year': 2017, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'G05B194/00', 'best_year': 2017, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'G05B22193/00', 'best_year': 2017, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'F16K310/00', 'best_year': 2016, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'H01L29241/00', 'best_year': 2018, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'B60R160/00', 'best_year': 2016, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'H01L297/00', 'best_year': 2017, 'ema_value': 2.0, 'patent_count': 2}, {'cpc_level4': 'Y10T294/00', 'best_year': 2018, 'ema_value': 1.3, 'patent_count': 4}, {'cpc_level4': 'F02D412/00', 'best_year': 2019, 'ema_value': 1.2000000000000002, 'patent_count': 3}, {'cpc_level4': 'Y02T101/00', 'best_year': 2019, 'ema_value': 1.1900000000000002, 'patent_count': 2}, {'cpc_level4': 'Y02T107/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'B60W100/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'B60K64/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'B60W101/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'Y02T106/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'G01R333/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'H01L234/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'H01L233/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'H02J70/00', 'best_year': 2019, 'ema_value': 1.1, 'patent_count': 2}, {'cpc_level4': 'B60R212/00', 'best_year': 2017, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60L22404/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60K63/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60L22405/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60W200/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60L152/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'B60K65/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}, {'cpc_level4': 'F16H22002/00', 'best_year': 2018, 'ema_value': 1.0, 'patent_count': 1}]}, 'var_functions.execute_python:62': {'total_patent_cpc_assignments': 2030, 'years_analyzed': [2016, 2017, 2018, 2019], 'unique_cpc_level4_groups': 788, 'sample_cpc_codes': [{'cpc_level4': 'B64G/128', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/336', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/336', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'B64G/128', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/232', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/232', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'B64G/128', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'B64G/128', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/190', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}, {'cpc_level4': 'F16C/320', 'year': 2016, 'patent_id': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with '}], 'yearly_counts_sample': [{'cpc_level4': 'A01B/590', 'year': 2016, 'patent_count': 1}, {'cpc_level4': 'A01K/102', 'year': 2018, 'patent_count': 1}, {'cpc_level4': 'A01K/103', 'year': 2018, 'patent_count': 1}, {'cpc_level4': 'A21C/900', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23B/700', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23L/318', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23N/120', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23N/121', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A23N/170', 'year': 2019, 'patent_count': 1}, {'cpc_level4': 'A43B/132', 'year': 2019, 'patent_count': 1}], 'ready_for_ema': True}, 'var_functions.execute_python:64': {'german_second_half_2019_patents': 313, 'unique_cpc_level4_groups': 190, 'sample_patents': [{'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc_level4': 'B41F/102', 'full_cpc_code': 'B41F21/102'}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc_level4': 'B41F/00', 'full_cpc_code': 'B41F22/00'}, {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc_level4': 'B41F/00', 'full_cpc_code': 'B41F21/00'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc_level4': 'F02D/300', 'full_cpc_code': 'F02D41/3005'}, {'patent_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'cpc_level4': 'F02D/20', 'full_cpc_code': 'F02D41/20'}], 'sample_cpc_groups': ['F05D/12', 'C04B/543', 'H04W/026', 'B60W/194', 'G07C/009', 'F23L/04', 'B29C/561', 'B64D/062', 'F02P/00', 'H01J/043']}, 'var_functions.query_db:66': [], 'var_functions.execute_python:70': {'status': 'no_results', 'message': 'No EMA results calculated'}}

exec(code, env_args)
