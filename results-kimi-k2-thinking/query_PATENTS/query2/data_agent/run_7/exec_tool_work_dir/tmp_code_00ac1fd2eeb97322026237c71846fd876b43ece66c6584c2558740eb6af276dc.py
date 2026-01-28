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

# Find one German patent with grant date in H2 2019 to examine CPC structure
sample_patent = None
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
        grant_date_str = rec['grant_date']
        # Check for 2019 second half
        if '2019' in grant_date_str and any(month in grant_date_str.lower() for month in ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']):
            sample_patent = rec
            break

# Examine the CPC structure
if sample_patent:
    print('__RESULT__:')
    print(json.dumps({
        'patent_info': sample_patent['Patents_info'],
        'grant_date': sample_patent['grant_date'],
        'cpc_field_type': str(type(sample_patent['cpc'])),
        'cpc_field_sample': sample_patent['cpc'][:500] if len(sample_patent['cpc']) > 500 else sample_patent['cpc']
    }, indent=2))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No sample patent found'}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}, {'symbol': 'B99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}, {'symbol': 'B29', 'level': '4.0', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL'}, {'symbol': 'B33', 'level': '4.0', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY'}, {'symbol': 'C22', 'level': '4.0', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS'}, {'symbol': 'D99', 'level': '4.0', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION'}], 'var_functions.execute_python:16': {'record_count': 5, 'first_record_keys': ['Patents_info', 'grant_date', 'cpc'], 'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'sample_count': 10, 'sample_records': [{'patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'grant_date': '30th Jun 2020'}, {'patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'grant_date': '2021 on Jan 26th'}, {'patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'grant_date': 'dated 16th February 2021'}, {'patents_info': 'In US, the patent filing (app. number US-201916560126-A) is belonging to DENSO CORP and has pub. number US-10897184-B2.', 'grant_date': 'dated 19th January 2021'}, {'patents_info': 'The US patent filing (app. number US-201916584394-A) is owned by DEPUY SYNTHES PRODUCTS INC and has publication no. US-11911287-B2.', 'grant_date': '27th Feb 2024'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_2019_records': 20, 'german_patents_2019': 1, 'second_half_2019_german': 0, 'sample_german_patents': []}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'total_german_patents': 11735, 'german_h2_2019_count': 11, 'sample_patents': [{'patent_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th', 'grant_date_parsed': '2019-12-24 00:00:00', 'cpc_codes': []}, {'patent_info': 'Patent filing (app. number DE-102018115363-A) from DE, belonging to SCHENCK ROTEC GMBH, with pub. number DE-102018115363-B3.', 'grant_date': '2019 on Nov 7th', 'grant_date_parsed': '2019-11-07 00:00:00', 'cpc_codes': []}, {'patent_info': 'The DE application (number DE-102008034068-A) is belonging to SEMIKRON ELEKTRONIK GMBH & CO KG and has pub. number DE-102008034068-B4.', 'grant_date': '2019, July 18th', 'grant_date_parsed': '2019-07-18 00:00:00', 'cpc_codes': []}, {'patent_info': 'DEUTSCH ZENTR LUFT & RAUMFAHRT holds the DE application (ID DE-102010001231-A), with publication no. DE-102010001231-B4.', 'grant_date': '2019 on Jul 4th', 'grant_date_parsed': '2019-07-04 00:00:00', 'cpc_codes': []}, {'patent_info': 'In DE, the patent filing (application number DE-102018124714-A) is assigned to ABBERIOR INSTRUMENTS GMBH and has publication no. DE-102018124714-B3.', 'grant_date': '2019 on Oct 17th', 'grant_date_parsed': '2019-10-17 00:00:00', 'cpc_codes': []}]}}

exec(code, env_args)
