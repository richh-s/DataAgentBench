code = """import json
import pandas as pd
import re

# Debug: Print available variables
var_names = [name for name in globals().keys() if 'query_db' in name]
print('Available query_db variables:', var_names)

# Get the file path
file_path = None
for key, value in globals().items():
    if 'query_db' in key and '26' in key:
        file_path = value
        break

if not file_path:
    print('File path not found!')
else:
    print('Found file path:', file_path)
    
    # Read sample data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f'\nTotal records: {len(data)}')
    
    if data:
        sample = data[0]
        print(f'\nSample record:')
        print(f'  publication_date: {sample.get("publication_date")}')
        print(f'  cpc type: {type(sample.get("cpc"))}')
        cpc_sample = sample.get('cpc', '')
        if cpc_sample:
            cpc_parsed = json.loads(cpc_sample)
            print(f'  Number of CPC codes: {len(cpc_parsed)}')
            print(f'  First few codes: {[c.get("code") for c in cpc_parsed[:5]]}')
    
    # Process all records
    year_pattern = re.compile(r'\b(20\d{2})\b')
    records_by_year = {}
    
    for i, record in enumerate(data):
        date_str = record.get('publication_date', '')
        year_match = year_pattern.search(date_str)
        
        if year_match:
            year = int(year_match.group(1))
            
            cpc_json = record.get('cpc', '[]')
            if cpc_json:
                try:
                    cpc_list = json.loads(cpc_json)
                    for cpc in cpc_list:
                        code = cpc.get('code', '')
                        # Look for level 5 codes (contain / and subgroup not 00)
                        if '/' in code:
                            base, subgroup = code.split('/')
                            if subgroup != '00':  # Level 5
                                if year not in records_by_year:
                                    records_by_year[year] = {}
                                if code not in records_by_year[year]:
                                    records_by_year[year][code] = 0
                                records_by_year[year][code] += 1
                except:
                    continue
    
    print(f'\nYears found: {sorted(records_by_year.keys())}')
    
    if 2022 in records_by_year:
        print(f'Number of level 5 CPC codes in 2022: {len(records_by_year[2022])}')
        top_2022 = sorted(records_by_year[2022].items(), key=lambda x: x[1], reverse=True)[:10]
        print('Top 10 CPC codes in 2022:')
        for code, count in top_2022:
            print(f'  {code}: {count}')
    
    # Calculate EMA for a few CPC codes as demonstration
    years = sorted(records_by_year.keys())
    results_2022 = []
    
    # Get all CPC codes for analysis
    all_cpc_codes = set()
    for year_data in records_by_year.values():
        all_cpc_codes.update(year_data.keys())
    
    print(f'\nTotal unique level 5 CPC codes: {len(all_cpc_codes)}')
    
    # Simple EMA calculation
    smoothing = 0.2
    
    for cpc in list(all_cpc_codes)[:2000]:  # Test with subset
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
    
    # Sort and get final list
    results_2022_sorted = sorted(results_2022, key=lambda x: x[1], reverse=True)
    final_codes = [code for code, _ in results_2022_sorted]
    
    output = {
        'years_with_data': years,
        'total_level5_codes': len(all_cpc_codes),
        'codes_peaking_2022': len(final_codes),
        'cpc_codes': final_codes
    }
    
    print(f'\nCPC codes with peak EMA in 2022: {len(final_codes)}')
    print('__RESULT__:')
    print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}}

exec(code, env_args)
