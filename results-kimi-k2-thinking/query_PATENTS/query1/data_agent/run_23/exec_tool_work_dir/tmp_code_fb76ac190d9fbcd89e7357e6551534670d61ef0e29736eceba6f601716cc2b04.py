code = """import json
import pandas as pd
import re

# Get the file path
keys = list(globals().keys())
file_path = None
for key in keys:
    if 'query_db' in key and '26' in key:
        file_path = globals()[key]
        break

# Read full data
with open(file_path, 'r') as f:
    data = json.load(f)

print('Data loaded successfully')
print('Total records:', len(data))

# Process records to extract CPC level 5 codes by year
year_pattern = re.compile(r'\b(20\d{2})\b')
records_by_year = {}
cpc_count = 0

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
                        if subgroup != '00':  # Level 5 code
                            if year not in records_by_year:
                                records_by_year[year] = {}
                            if code not in records_by_year[year]:
                                records_by_year[year][code] = 0
                            records_by_year[year][code] += 1
                            cpc_count += 1
            except:
                continue

print('Years found:', sorted(records_by_year.keys()))
print('Total CPC level 5 records:', cpc_count)

# Calculate EMA for each CPC code
years = sorted(records_by_year.keys())
all_cpc_codes = set()
for year_data in records_by_year.values():
    all_cpc_codes.update(year_data.keys())

print('Total unique level 5 CPC codes:', len(all_cpc_codes))

# Calculate exponential moving average
smoothing = 0.2
results_2022 = []

for cpc in all_cpc_codes:
    ema_val = None
    max_ema = -1
    max_year = None
    
    for year in years:
        count = records_by_year.get(year, {}).get(cpc, 0)
        
        if ema_val is None:
            ema_val = count
        else:
            ema_val = (smoothing * count) + ((1 - smoothing) * ema_val)
        
        if ema_val > max_ema:
            max_ema = ema_val
            max_year = year
    
    if max_year == 2022:
        results_2022.append((cpc, max_ema))

# Sort by EMA value
results_2022_sorted = sorted(results_2022, key=lambda x: x[1], reverse=True)
pcp_codes_final = [code for code, ema in results_2022_sorted]

output = {
    'analysis_complete': True,
    'total_cpc_codes': len(all_cpc_codes),
    'codes_with_peak_2022': len(pcp_codes_final),
    'cpc_codes': pcp_codes_final
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}}

exec(code, env_args)
