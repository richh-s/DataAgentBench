code = """import json
import pandas as pd
from datetime import datetime
import re
from collections import defaultdict

# Access the German patents query result
query_result = locals()['var_functions.query_db:30']

if isinstance(query_result, str) and query_result.endswith('.json'):
    with open(query_result, 'r') as f:
        data = json.load(f)
else:
    data = query_result

# Function to parse grant dates
def parse_grant_date(date_str):
    if not date_str:
        return None
    try:
        date_str_clean = date_str.lower()
        date_str_clean = re.sub(r'(th|st|nd|rd|dated)\s*', '', date_str_clean)
        date_str_clean = date_str_clean.strip()
        
        formats = [
            '%B %d %Y', '%d %B %Y', '%B %Y', '%Y %B %d', '%Y, %B %d',
            '%Y on %b %d', '%Y, %b %d', '%d %b %Y', '%Y %b %d', '%Y on %B %d'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str_clean, fmt)
            except:
                continue
        
        # Extract year and month
        year_match = re.search(r'\b(201\d|202\d)\b', date_str_clean)
        if year_match:
            year = int(year_match.group(1))
            month_match = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', date_str_clean)
            if month_match:
                month_str = month_match.group(1)
                month_map = {
                    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
                }
                month = month_map.get(month_str, 1)
                return datetime(year, month, 1)
        
        return None
    except:
        return None

# Function to extract CPC codes from JSON string
def extract_cpc_codes(cpc_str):
    codes = []
    try:
        if not cpc_str or not cpc_str.strip():
            return codes
        cpc_list = json.loads(cpc_str)
        if isinstance(cpc_list, list):
            for item in cpc_list:
                if isinstance(item, dict) and 'code' in item:
                    codes.append(item['code'])
        return codes
    except Exception as e:
        return []

# Function to get CPC at level 4 (first 4 characters of the main group)
def get_cpc_level_4(cpc_code):
    if not cpc_code:
        return None
    # CPC codes are like "B41F21/102", level 4 is the group: first 4 chars before /
    parts = cpc_code.split('/')
    if len(parts) >= 1:
        main_part = parts[0]
        if len(main_part) >= 4:
            return main_part[:4]  # e.g., "B41F"
    return None

# Collect all German patents with their CPC codes
german_patents_data = []

for rec in data:
    patents_info_lower = rec['Patents_info'].lower()
    is_german = (
        re.search(r'DE-\d+', rec['Patents_info']) or
        'from de,' in patents_info_lower or
        re.search(r'\bde\b', patents_info_lower) or
        'germany' in patents_info_lower or
        'german' in patents_info_lower
    )
    
    if is_german:
        grant_date = parse_grant_date(rec['grant_date'])
        if grant_date:
            cpc_codes = extract_cpc_codes(rec['cpc'])
            if cpc_codes:  # Only include if there are CPC codes
                cpc_level_4_codes = [get_cpc_level_4(code) for code in cpc_codes if get_cpc_level_4(code)]
                
                german_patents_data.append({
                    'patent_info': rec['Patents_info'],
                    'grant_date': rec['grant_date'],
                    'grant_date_parsed': grant_date,
                    'year': grant_date.year,
                    'month': grant_date.month,
                    'cpc_level_4_codes': cpc_level_4_codes
                })

# Filter for 2019 second half patents
german_h2_2019 = [p for p in german_patents_data if p['year'] == 2019 and p['month'] >= 7]

# Count monthly filings by CPC level 4 for 2019
cpc_monthly_counts = defaultdict(lambda: defaultdict(int))

for patent in german_h2_2019:
    year = patent['year']
    month = patent['month']
    for cpc_level_4 in patent['cpc_level_4_codes']:
        cpc_monthly_counts[cpc_level_4][month] += 1

# Calculate exponential moving average (EMA) for each CPC level 4
def calculate_ema(monthly_counts, smoothing_factor=0.1):
    if not monthly_counts:
        return {}
    
    # Sort by month
    sorted_months = sorted(monthly_counts.items())
    ema_dict = {}
    ema_prev = None
    
    for month, count in sorted_months:
        if ema_prev is None:
            ema_prev = count  # First value is the count itself
        else:
            ema_prev = (smoothing_factor * count) + ((1 - smoothing_factor) * ema_prev)
        ema_dict[month] = ema_prev
    
    return ema_dict, ema_prev, sorted_months[-1][0] if sorted_months else None

cpc_ema_results = {}
for cpc_level_4, monthly_counts in cpc_monthly_counts.items():
    ema_dict, final_ema, best_month = calculate_ema(monthly_counts, 0.1)
    cpc_ema_results[cpc_level_4] = {
        'ema_by_month': ema_dict,
        'best_month': best_month,
        'best_ema': final_ema,
        'total_filings': sum(monthly_counts.values())
    }

# Sort by best EMA value
top_cpc_by_ema = sorted(cpc_ema_results.items(), key=lambda x: x[1]['best_ema'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'german_h2_2019_patents': len(german_h2_2019),
    'unique_cpc_level4_codes': len(cpc_monthly_counts),
    'top_cpc_by_ema': top_cpc_by_ema[:15],
    'cpc_monthly_counts_sample': dict(list(cpc_monthly_counts.items())[:5])
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.execute_python:16': {'record_count': 5, 'first_record_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'sample_count': 10, 'sample_records': [{'patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020'}, {'patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th'}, {'patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021'}, {'patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021'}, {'patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_2019_records': 20, 'german_patents_2019': 1, 'second_half_2019_german': 0, 'sample_german_patents': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11735, 'german_h2_2019_count': 11, 'sample_patents': [{'patent_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'grant_date_parsed': '2019-12-24 00:00:00', 'cpc_codes': []}, {'patent_info': 'Patent filing (app. number DE-102018115363-A) from DE, belonging to SCHENCK ROTEC GMBH, with pub. number DE-102018115363-B3.', 'grant_date': '2019 on Nov 7th', 'grant_date_parsed': '2019-11-07 00:00:00', 'cpc_codes': []}, {'patent_info': 'The DE application (number DE-102008034068-A) is belonging to SEMIKRON ELEKTRONIK GMBH & CO KG and has pub. number DE-102008034068-B4.', 'grant_date': '2019, July 18th', 'grant_date_parsed': '2019-07-18 00:00:00', 'cpc_codes': []}, {'patent_info': 'DEUTSCH ZENTR LUFT & RAUMFAHRT holds the DE application (ID DE-102010001231-A), with publication no. DE-102010001231-B4.', 'grant_date': '2019 on Jul 4th', 'grant_date_parsed': '2019-07-04 00:00:00', 'cpc_codes': []}, {'patent_info': 'In DE, the patent filing (application number DE-102018124714-A) is assigned to ABBERIOR INSTRUMENTS GMBH and has publication no. DE-102018124714-B3.', 'grant_date': '2019 on Oct 17th', 'grant_date_parsed': '2019-10-17 00:00:00', 'cpc_codes': []}]}, 'var_functions.execute_python:34': {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc_field_type': "<class 'str'>", 'cpc_field_sample': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:36': {'german_h2_2019_patents_count': 0, 'unique_cpc_codes': 0, 'sample_patents': [], 'sample_cpc_codes': []}, 'var_functions.execute_python:38': {'total_german_patents': 11735, 'german_patents_with_cpc': 0, 'german_h2_2019_patents': 11, 'cpc_yearly_counts_sample': {}}, 'var_functions.execute_python:40': {'patent_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004', 'cpc_type': "<class 'str'>", 'cpc_length': 564, 'cpc_start': '[\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10S439/909",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    ', 'cpc_is_empty': False}, 'var_functions.execute_python:42': {'success': False, 'error': 'malformed node or string on line 4: <ast.Name object at 0x76aaf9c76690>'}, 'var_functions.execute_python:44': {'all_german_2019_patents': 20, 'german_h2_2019_patents': 11, 'unique_cpc_level4_codes': 34, 'top_cpc_ema': [['F16H', {'ema_by_month': {'5': 20}, 'best_month': 5, 'best_ema': 20}], ['H01R', {'ema_by_month': {'9': 18}, 'best_month': 9, 'best_ema': 18}], ['B60Q', {'ema_by_month': {'5': 16}, 'best_month': 5, 'best_ema': 16}], ['B60L', {'ema_by_month': {'5': 16}, 'best_month': 5, 'best_ema': 16}], ['G01R', {'ema_by_month': {'3': 13}, 'best_month': 3, 'best_ema': 13}], ['B60K', {'ema_by_month': {'5': 9, '8': 8.299999999999999}, 'best_month': 5, 'best_ema': 9}], ['G02B', {'ema_by_month': {'10': 8}, 'best_month': 10, 'best_ema': 8}], ['F02D', {'ema_by_month': {'10': 8}, 'best_month': 10, 'best_ema': 8}], ['G06V', {'ema_by_month': {'5': 7}, 'best_month': 5, 'best_ema': 7}], ['B60W', {'ema_by_month': {'5': 6, '6': 6.2}, 'best_month': 6, 'best_ema': 6.2}]], 'sample_patent': {'patent_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'grant_date_parsed': '2019-12-24 00:00:00', 'cpc_codes': ['F16C33/4676', 'F16C33/4682', 'F16C33/4635'], 'cpc_level_4_codes': ['F16C', 'F16C', 'F16C']}}, 'var_functions.execute_python:46': {'german_h2_2019_cpc_level4_codes': 20, 'sample_cpc_level4': ['H04L', 'F01D', 'B62D', 'F16F', 'B60K', 'G02B', 'Y02T', 'H01R', 'H03L', 'G01M', 'F16D', 'F04D', 'G01N', 'H01L', 'G08B', 'F05D', 'G01L', 'F16C', 'F02D', 'B60N']}, 'var_functions.query_db:48': [], 'var_functions.query_db:50': [{'symbol': 'B60K', 'titleFull': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'level': '5.0'}, {'symbol': 'B62D', 'titleFull': 'MOTOR VEHICLES; TRAILERS', 'level': '5.0'}, {'symbol': 'F01D', 'titleFull': 'NON-POSITIVE DISPLACEMENT MACHINES OR ENGINES, e.g. STEAM TURBINES', 'level': '5.0'}, {'symbol': 'F16F', 'titleFull': 'SPRINGS; SHOCK-ABSORBERS; MEANS FOR DAMPING VIBRATION', 'level': '5.0'}, {'symbol': 'H04L', 'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION', 'level': '5.0'}]}

exec(code, env_args)
