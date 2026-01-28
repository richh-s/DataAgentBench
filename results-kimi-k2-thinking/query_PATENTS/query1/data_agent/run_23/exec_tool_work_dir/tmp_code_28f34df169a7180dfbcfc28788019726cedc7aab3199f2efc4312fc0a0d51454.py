code = """import json
import pandas as pd
import re

# Get file path
file_path = None
for key, value in globals().items():
    if 'query_db' in key and '26' in key:
        file_path = value
        break

# Read full data
with open(file_path, 'r') as f:
    data = json.load(f)

# Debug: Check what's in the data
print('Total records:', len(data))
print('Sample keys:', list(data[0].keys()))

# Check a few records for level 5 CPC codes
year_pattern = re.compile(r'\b(20\d{2})\b')
level5_found = []

for i in range(min(100, len(data))):  # Check first 100 records
    record = data[i]
    date_str = record.get('publication_date', '')
    year_match = year_pattern.search(date_str)
    
    if year_match:
        year = int(year_match.group(1))
        
        cpc_json = record.get('cpc', '[]')
        if cpc_json and cpc_json != '[]':
            try:
                cpc_list = json.loads(cpc_json)
                for cpc in cpc_list:
                    code = cpc.get('code', '')
                    if '/' in code:
                        base, subgroup = code.split('/')
                        if subgroup != '00':  # This is level 5
                            level5_found.append({
                                'record': i,
                                'year': year,
                                'code': code
                            })
            except:
                continue

print(f'\nLevel 5 CPC codes found in first 100 records: {len(level5_found)}')
for item in level5_found[:10]:
    print(f'  Record {item["record"]}, Year {item["year"]}: {item["code"]}')

# Now process all records systematically
records_by_year = {}
total_level5 = 0

for record in data:
    date_str = record.get('publication_date', '')
    year_match = year_pattern.search(date_str)
    
    if year_match:
        year = int(year_match.group(1))
        
        cpc_json = record.get('cpc', '[]')
        if cpc_json and cpc_json != '[]':
            try:
                cpc_list = json.loads(cpc_json)
                for cpc in cpc_list:
                    code = cpc.get('code', '')
                    if '/' in code:
                        base, subgroup = code.split('/')
                        if subgroup != '00':  # Level 5
                            if year not in records_by_year:
                                records_by_year[year] = {}
                            records_by_year[year][code] = records_by_year[year].get(code, 0) + 1
                            total_level5 += 1
            except:
                continue

print(f'\nTotal level 5 CPC records: {total_level5}')
print(f'Years with data: {sorted(records_by_year.keys())}')

# Count unique CPC codes per year
for year in sorted(records_by_year.keys()):
    print(f'Year {year}: {len(records_by_year[year])} unique level 5 codes')

# Show sample codes from 2022 if available
if 2022 in records_by_year:
    print(f'\nSample level 5 codes from 2022:')
    codes_2022 = list(records_by_year[2022].keys())[:10]
    for code in codes_2022:
        print(f'  {code}: {records_by_year[2022][code]} filings')

# Calculate EMA for all CPC codes
years = sorted(records_by_year.keys())
all_codes = set()
for year_data in records_by_year.values():
    all_codes.update(year_data.keys())

print(f'\nTotal unique level 5 CPC codes: {len(all_codes)}')

# EMA calculation
smoothing = 0.2
peak_2022_codes = []

for code in all_codes:
    ema = None
    max_ema = -1
    peak_year = None
    
    for year in years:
        count = records_by_year.get(year, {}).get(code, 0)
        if ema is None:
            ema = count
        else:
            ema = (smoothing * count) + ((1 - smoothing) * ema)
        
        if ema > max_ema:
            max_ema = ema
            peak_year = year
    
    if peak_year == 2022:
        peak_2022_codes.append((code, max_ema))

# Sort by EMA value
peak_2022_sorted = sorted(peak_2022_codes, key=lambda x: x[1], reverse=True)
final_codes = [code for code, ema in peak_2022_sorted]

print(f'\nCPC codes peaking in 2022: {len(final_codes)}')
print('Top 10:')
for code, ema in peak_2022_sorted[:10]:
    print(f'  {code}: EMA = {ema:.2f}')

result = {
    'total_cpc_codes_level5': len(all_codes),
    'codes_peaking_2022': len(final_codes),
    'cpc_codes_best_year_2022': final_codes
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}]}

exec(code, env_args)
