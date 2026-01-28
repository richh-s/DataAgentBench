code = """import json
import pandas as pd
import re

# Define the variable name pattern and read the file directly
# The file path should be stored in a variable with query_db in the name
import os

# Find the correct file path by looking for it in the current directory
# or by using the stored variable approach

# Get the file path using a direct approach
# The variable name follows the pattern: var_functions.query_db:X where X is the tool call counter
file_path = None

# Try common variable patterns
possible_vars = [
    'var_functions.query_db:54',
    'var_functions.query_db:26', 
    'var_functions.query_db:30',
    'var_functions.query_db:8'
]

for var in possible_vars:
    if var in globals():
        file_path = globals()[var]
        print(f'Found variable {var}: {file_path}')
        break
    elif var in locals():
        file_path = locals()[var]
        print(f'Found variable {var}: {file_path}')
        break

if not file_path:
    # List all variables to find the right one
    print('Available variables containing query_db:')
    for key, value in globals().items():
        if 'query_db' in key and isinstance(value, str):
            print(f'  {key}: {value}')
            file_path = value
            # Take the first one that looks like a file path
            if value.endswith('.json'):
                break

if not file_path:
    print('WARNING: Could not find file path, using empty result')
    output = {'cpc_codes': []}
else:
    print('Loading data from:', file_path)
    
    # Read the data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Process data
    year_pattern = re.compile(r'\b(20\d{2})\b')
    records = []
    
    for record in data:
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
                        # Level 5: has / and subgroup not 00
                        if '/' in code:
                            base, subgroup = code.split('/')
                            if subgroup != '00':
                                records.append({'year': year, 'code': code})
                except:
                    continue
    
    # Create DataFrame
    df = pd.DataFrame(records)
    
    # Count per year per code
    yearly_counts = df.groupby(['year', 'code']).size().reset_index(name='count')
    
    # Get all years and codes
    years = sorted(yearly_counts['year'].unique())
    codes = yearly_counts['code'].unique()
    
    # Calculate EMA
    smoothing = 0.2
    peak_2022 = []
    
    for code in codes:
        code_data = yearly_counts[yearly_counts['code'] == code]
        
        # Create full timeline
        timeline = pd.DataFrame({'year': years})
        full_data = timeline.merge(code_data, on='year', how='left').fillna(0)
        
        # Calculate EMA
        ema_val = None
        max_ema = -1
        peak_year = None
        
        for _, row in full_data.iterrows():
            count = row['count']
            if ema_val is None:
                ema_val = count
            else:
                ema_val = (smoothing * count) + ((1 - smoothing) * ema_val)
            
            if ema_val > max_ema:
                max_ema = ema_val
                peak_year = row['year']
        
        if peak_year == 2022:
            peak_2022.append((code, max_ema))
    
    # Sort by EMA
    peak_2022_sorted = sorted(peak_2022, key=lambda x: x[1], reverse=True)
    final_codes = [code for code, ema in peak_2022_sorted]
    
    output = {'cpc_codes': final_codes}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'parents': '[\n  "B"\n]'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'parents': '[\n  "C"\n]'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'parents': '[\n  "D"\n]'}, {'symbol': 'F28', 'titleFull': 'HEAT EXCHANGE IN GENERAL', 'level': '4.0', 'parents': '[\n  "F"\n]'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'H', 'titleFull': 'ELECTRICITY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'Y', 'titleFull': 'GENERAL TAGGING OF NEW TECHNOLOGICAL DEVELOPMENTS; GENERAL TAGGING OF CROSS-SECTIONAL TECHNOLOGIES SPANNING OVER SEVERAL SECTIONS OF THE IPC; TECHNICAL SUBJECTS COVERED BY FORMER USPC CROSS-REFERENCE ART COLLECTIONS [XRACs] AND DIGESTS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'D', 'titleFull': 'TEXTILES; PAPER', 'level': '2.0', 'parents': '[]'}, {'symbol': 'F', 'titleFull': 'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING', 'level': '2.0', 'parents': '[]'}, {'symbol': 'E', 'titleFull': 'FIXED CONSTRUCTIONS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY', 'level': '2.0', 'parents': '[]'}, {'symbol': 'G', 'titleFull': 'PHYSICS', 'level': '2.0', 'parents': '[]'}, {'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES', 'level': '2.0', 'parents': '[]'}], 'var_functions.execute_python:24': {'total_records': 100, 'sample_keys': ['publication_date', 'cpc'], 'sample_pub_dates': ['Aug 3rd, 2021', 'Oct 6th, 2020', 'Sep 21st, 2021', '2020, April 7th', 'Mar 23rd, 2021'], 'sample_cpc_count': 38, 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'error': 'CPC data file not found'}, 'var_functions.execute_python:40': {'error': 'No CPC records found'}, 'var_functions.execute_python:46': {'analysis_complete': True, 'total_cpc_codes': 0, 'codes_with_peak_2022': 0, 'cpc_codes': []}, 'var_functions.query_db:48': [{'publication_date': 'Aug 3rd, 2021', 'cpc_sample': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Oct 6th, 2020', 'cpc_sample': '[\n  {\n    "code": "F16H47/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16H37/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}, {'publication_date': 'Sep 21st, 2021', 'cpc_sample': '[\n  {\n    "code": "B29C70/48",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C08J5/246",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code":'}, {'publication_date': '2020, April 7th', 'cpc_sample': '[\n  {\n    "code": "A61K48/0066",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12N2830/32",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "c'}, {'publication_date': 'Mar 23rd, 2021', 'cpc_sample': '[\n  {\n    "code": "H01H9/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/223",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code"'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
