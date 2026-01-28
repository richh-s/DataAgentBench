code = """import json
import pandas as pd
from datetime import datetime
import re
import ast

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
        # Clean date string
        date_str_clean = date_str.lower()
        date_str_clean = re.sub(r'(th|st|nd|rd|dated)\s*', '', date_str_clean)
        date_str_clean = date_str_clean.strip()
        
        # Try multiple formats
        formats = [
            '%B %d %Y',
            '%d %B %Y',
            '%B %Y',
            '%Y %B %d',
            '%Y, %B %d',
            '%Y on %b %d',
            '%Y, %b %d',
            '%d %b %Y',
            '%Y %b %d',
            '%Y on %B %d'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str_clean, fmt)
            except:
                continue
        
        # Try to extract year and month
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
    except Exception as e:
        return None

# Function to extract CPC codes from the JSON-like string
def extract_cpc_codes(cpc_str):
    codes = []
    try:
        # Try to parse as JSON/ast
        cpc_list = ast.literal_eval(cpc_str)
        if isinstance(cpc_list, list):
            for item in cpc_list:
                if isinstance(item, dict) and 'code' in item:
                    codes.append(item['code'])
        return codes
    except Exception as e:
        return []

# Process all German patents
all_german_patents = []
german_h2_2019_patents = []

has_cpc_count = 0
total_german = 0

for rec in data:
    # Check if it's a German patent
    patents_info_lower = rec['Patents_info'].lower()
    is_german = (
        re.search(r'DE-\d+', rec['Patents_info']) or
        'from de,' in patents_info_lower or
        re.search(r'\bde\b', patents_info_lower) or
        'germany' in patents_info_lower or
        'german' in patents_info_lower
    )
    
    if is_german:
        total_german += 1
        cpc_codes = extract_cpc_codes(rec['cpc'])
        if cpc_codes:
            has_cpc_count += 1
            
        all_german_patents.append({
            'patent_info': rec['Patents_info'],
            'grant_date': rec['grant_date'],
            'cpc_codes': cpc_codes,
            'cpc_count': len(cpc_codes)
        })
        
        # Check for 2019 second half
        grant_date = parse_grant_date(rec['grant_date'])
        if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
            german_h2_2019_patents.append({
                'patent_info': rec['Patents_info'],
                'grant_date': rec['grant_date'],
                'grant_date_parsed': grant_date,
                'cpc_codes': cpc_codes,
                'cpc_count': len(cpc_codes)
            })

# Get CPC codes with filings
cpc_yearly_counts = {}
for patent in all_german_patents:
    grant_date = parse_grant_date(patent['grant_date'])
    if grant_date:
        year = grant_date.year
        for cpc_code in patent['cpc_codes']:
            if cpc_code not in cpc_yearly_counts:
                cpc_yearly_counts[cpc_code] = {}
            if year not in cpc_yearly_counts[cpc_code]:
                cpc_yearly_counts[cpc_code][year] = 0
            cpc_yearly_counts[cpc_code][year] += 1

print('__RESULT__:')
print(json.dumps({
    'total_german_patents': total_german,
    'german_patents_with_cpc': has_cpc_count,
    'german_h2_2019_patents': len(german_h2_2019_patents),
    'cpc_yearly_counts_sample': {k: v for k, v in list(cpc_yearly_counts.items())[:10]}
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.execute_python:16': {'record_count': 5, 'first_record_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'sample_count': 10, 'sample_records': [{'patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020'}, {'patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th'}, {'patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021'}, {'patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021'}, {'patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_2019_records': 20, 'german_patents_2019': 1, 'second_half_2019_german': 0, 'sample_german_patents': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11735, 'german_h2_2019_count': 11, 'sample_patents': [{'patent_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'grant_date_parsed': '2019-12-24 00:00:00', 'cpc_codes': []}, {'patent_info': 'Patent filing (app. number DE-102018115363-A) from DE, belonging to SCHENCK ROTEC GMBH, with pub. number DE-102018115363-B3.', 'grant_date': '2019 on Nov 7th', 'grant_date_parsed': '2019-11-07 00:00:00', 'cpc_codes': []}, {'patent_info': 'The DE application (number DE-102008034068-A) is belonging to SEMIKRON ELEKTRONIK GMBH & CO KG and has pub. number DE-102008034068-B4.', 'grant_date': '2019, July 18th', 'grant_date_parsed': '2019-07-18 00:00:00', 'cpc_codes': []}, {'patent_info': 'DEUTSCH ZENTR LUFT & RAUMFAHRT holds the DE application (ID DE-102010001231-A), with publication no. DE-102010001231-B4.', 'grant_date': '2019 on Jul 4th', 'grant_date_parsed': '2019-07-04 00:00:00', 'cpc_codes': []}, {'patent_info': 'In DE, the patent filing (application number DE-102018124714-A) is assigned to ABBERIOR INSTRUMENTS GMBH and has publication no. DE-102018124714-B3.', 'grant_date': '2019 on Oct 17th', 'grant_date_parsed': '2019-10-17 00:00:00', 'cpc_codes': []}]}, 'var_functions.execute_python:34': {'patent_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'cpc_field_type': "<class 'str'>", 'cpc_field_sample': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]'}, 'var_functions.execute_python:36': {'german_h2_2019_patents_count': 0, 'unique_cpc_codes': 0, 'sample_patents': [], 'sample_cpc_codes': []}}

exec(code, env_args)
