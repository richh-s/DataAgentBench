code = """import json
import pandas as pd
from datetime import datetime
import re

# Access the 2019 grants query result
query_result = locals()['var_functions.query_db:24']

if isinstance(query_result, str) and query_result.endswith('.json'):
    with open(query_result, 'r') as f:
        data = json.load(f)
else:
    data = query_result

# Find German patents in 2019
german_patterns = [
    r'DE-\d+',
    r'from DE[,\s]',
    r'\bDE\b',
    r'Germany',
    r'German'
]

german_patents = []
for rec in data:
    patents_info_lower = rec['Patents_info'].lower()
    if (re.search(r'de-\d+', rec['Patents_info'], re.IGNORECASE) or 
        'from de' in patents_info_lower or
        re.search(r'\bde\b', rec['Patents_info'].lower()) or
        'germany' in patents_info_lower or
        'german' in patents_info_lower):
        german_patents.append(rec)

# Parse grant dates and filter for second half of 2019
def parse_grant_date(date_str):
    if not date_str:
        return None
    try:
        # Handle various date formats
        date_str_clean = date_str.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '').replace('dated', '').strip()
        
        # Try multiple formats
        formats = [
            '%B %d, %Y',
            '%d %B %Y',
            '%B %dst, %Y',
            '%B %dnd, %Y',
            '%B %drd, %Y',
            '%B %dth, %Y',
            '%d %b %Y',
            '%Y on %b %d',
            '%Y, %b %d',
            '%Y, %B %d',
            '%Y on %B %d',
            '%Y %b %d',
            '%Y %B %d'
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str_clean, fmt)
            except:
                continue
        return None
    except:
        return None

second_half_2019_german = []
for rec in german_patents:
    grant_date = parse_grant_date(rec['grant_date'])
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        second_half_2019_german.append({
            'patent_info': rec['Patents_info'],
            'grant_date': rec['grant_date'],
            'grant_date_parsed': grant_date,
            'cpc': rec['cpc']
        })

print('__RESULT__:')
print(json.dumps({
    'total_2019_records': len(data),
    'german_patents_2019': len(german_patents),
    'second_half_2019_german': len(second_half_2019_german),
    'sample_german_patents': second_half_2019_german[:3]
}, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.execute_python:16': {'record_count': 5, 'first_record_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'sample_count': 10, 'sample_records': [{'patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020'}, {'patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th'}, {'patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021'}, {'patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021'}, {'patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
