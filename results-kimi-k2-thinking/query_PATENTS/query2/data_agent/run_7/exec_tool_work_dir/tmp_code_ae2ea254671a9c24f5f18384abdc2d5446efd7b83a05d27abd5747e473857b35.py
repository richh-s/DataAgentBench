code = """import json
import pandas as pd
from datetime import datetime
import re

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
            '%Y %b %d'
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
import ast

def extract_cpc_codes(cpc_str):
    try:
        # The data appears to be a JSON-like string
        cpc_list = ast.literal_eval(cpc_str)
        if isinstance(cpc_list, list):
            return [item.get('code') for item in cpc_list if item.get('code')]
        return []
    except:
        return []

# Filter for German patents granted in second half of 2019
german_h2_2019_patents = []
german_patents_all = []

for rec in data:
    # Check if it's really a German patent
    patents_info_lower = rec['Patents_info'].lower()
    is_german = (
        re.search(r'DE-\d+', rec['Patents_info']) or
        'from de,' in patents_info_lower or
        re.search(r'\bde\b', patents_info_lower) or
        'germany' in patents_info_lower or
        'german' in patents_info_lower
    )
    
    if is_german:
        german_patents_all.append(rec)
        
        # Parse grant date
        grant_date = parse_grant_date(rec['grant_date'])
        if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
            cpc_codes = extract_cpc_codes(rec['cpc'])
            german_h2_2019_patents.append({
                'patent_info': rec['Patents_info'],
                'grant_date': rec['grant_date'],
                'grant_date_parsed': grant_date,
                'cpc_codes': cpc_codes
            })

print('__RESULT__:')
print(json.dumps({
    'total_german_patents': len(german_patents_all),
    'german_h2_2019_count': len(german_h2_2019_patents),
    'sample_patents': german_h2_2019_patents[:5]
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.execute_python:16': {'record_count': 5, 'first_record_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'sample_count': 10, 'sample_records': [{'patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020'}, {'patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th'}, {'patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021'}, {'patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021'}, {'patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_2019_records': 20, 'german_patents_2019': 1, 'second_half_2019_german': 0, 'sample_german_patents': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
