code = """import json
import re

# Direct access to the file path variable
# Based on the pattern, the variable should be named var_functions.query_db:54
var_name = 'var_functions.query_db:54'

# Check if it exists in globals
if var_name in globals():
    file_path = globals()[var_name]
    print('Accessed file path:', file_path)
else:
    print('Variable not found directly')
    # Try alternative - just use the most recent query result
    file_path = None
    for name in sorted(globals().keys(), reverse=True):
        if 'query_db' in name and isinstance(globals()[name], str):
            file_path = globals()[name]
            print('Using file path from variable:', name)
            break

if file_path is None:
    print('WARNING: File path not found')
    cpc_codes_2022 = []
else:
    # Process the data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print('Processing', len(data), 'records')
    
    # Track CPC level 5 codes by year
    year_pattern = re.compile(r'\b(20\d{2})\b')
    yearly_counts = {}
    
    for record in data:
        date_str = record.get('publication_date', '')
        year_match = year_pattern.search(date_str)
        
        if year_match:
            year = int(year_match.group(1))
            
            cpc_str = record.get('cpc', '[]')
            if cpc_str:
                try:
                    cpc_list = json.loads(cpc_str)
                    for item in cpc_list:
                        code = item.get('code', '')
                        # CPC level 5: contains '/' and subgroup not '00'
                        if '/' in code and not code.endswith('/00'):
                            key = (year, code)
                            yearly_counts[key] = yearly_counts.get(key, 0) + 1
                except:
                    continue
    
    print('Collected data for', len(yearly_counts), 'year-code combinations')
    
    # Build time series for each code
    years = sorted(set(k[0] for k in yearly_counts.keys()))
    codes = set(k[1] for k in yearly_counts.keys())
    
    print('Years:', years)
    print('Unique level-5 CPC codes:', len(codes))
    
    # Calculate EMA and find codes peaking in 2022
    smoothing = 0.2
    peak_2022 = []
    
    for code in codes:
        ema = None
        max_ema = -1
        peak_year = None
        
        for year in years:
            count = yearly_counts.get((year, code), 0)
            
            if ema is None:
                ema = count
            else:
                ema = (smoothing * count) + ((1 - smoothing) * ema)
            
            if ema > max_ema:
                max_ema = ema
                peak_year = year
        
        if peak_year == 2022:
            peak_2022.append((code, max_ema))
    
    # Sort by EMA
    peak_2022.sort(key=lambda x: x[1], reverse=True)
    cpc_codes_2022 = [code for code, ema in peak_2022]
    
    print('Codes peaking in 2022:', len(cpc_codes_2022))
    
    # Show some examples
    if peak_2022:
        print('Top 5 by EMA:')
        for code, ema in peak_2022[:5]:
            print(' ', code, 'EMA:', round(ema, 2))

# Return final result
result = {'cpc_codes': cpc_codes_2022}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
