code = """import json
import os
import re
from collections import defaultdict
from datetime import datetime

# Get the file path from previous query result - avoid f-strings to prevent syntax errors
result_key = 'var_functions.query_db:36'
print("Looking for key:", result_key)

# Check if it's available in globals
if result_key in globals():
    result_file = globals()[result_key]
    print("Found result file path:", result_file)
else:
    print("Key not found in globals. Available keys:", [k for k in globals().keys() if 'query_db' in str(k)])
    result_file = None

if result_file and os.path.exists(result_file):
    try:
        with open(result_file, 'r') as f:
            patents_data = json.load(f)
        
        print("Successfully loaded data. Total records:", len(patents_data))
        
        # Check first record structure
        if patents_data:
            first = patents_data[0]
            print("First record keys:", list(first.keys()))
            print("Sample Patents_info:", str(first.get('Patents_info', ''))[:100])
            print("Sample grant_date:", str(first.get('grant_date', ''))[:50])
        
        # Process data
        cpc_year_counts = defaultdict(lambda: defaultdict(int))
        
        for patent in patents_data:
            patents_info = patent.get('Patents_info', '')
            grant_date = patent.get('grant_date', '')
            
            # Extract year from grant_date
            year_match = re.search(r'(\d{4})', grant_date)
            if not year_match:
                continue
            year = int(year_match.group(1))
            
            # Parse CPC codes
            cpc_data = patent.get('cpc', '[]')
            try:
                cpc_codes = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            except:
                continue
            
            if not isinstance(cpc_codes, list):
                continue
            
            # Count CPC level 4 codes
            for cpc_entry in cpc_codes:
                if not isinstance(cpc_entry, dict):
                    continue
                
                cpc_code = cpc_entry.get('code', '')
                if not cpc_code or len(cpc_code) < 4:
                    continue
                
                # Find slash to separate main group
                slash_pos = cpc_code.find('/')
                if slash_pos > 0:
                    main_group = cpc_code[:slash_pos]
                    # Level 4 is first 4 characters of main group
                    if len(main_group) >= 4:
                        level4_code = main_group[:4]
                        cpc_year_counts[level4_code][year] += 1
        
        print("Processed CPC data. Unique level 4 groups:", len(cpc_year_counts))
        print("Year range:", min([min(years.keys()) for years in cpc_year_counts.values()]), 
              "to", max([max(years.keys()) for years in cpc_year_counts.values()]))
        
        # Save to file
        output_data = {code: dict(years) for code, years in cpc_year_counts.items()}
        with open('cpc_filing_by_year.json', 'w') as f:
            json.dump(output_data, f)
        
        result = {
            'status': 'success',
            'cpc_groups': len(cpc_year_counts),
            'total_patents': len(patents_data),
            'year_range': {
                'min': min([min(years.keys()) for years in cpc_year_counts.values()]),
                'max': max([max(years.keys()) for years in cpc_year_counts.values()])
            }
        }
        
    except Exception as e:
        print("Error processing file:", e)
        import traceback
        traceback.print_exc()
        result = {'status': 'error', 'message': str(e)}
else:
    print("Result file not accessible")
    result = {'status': 'error', 'message': 'Result file not found'}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'status': 'success', 'cpc_groups': 11, 'total_patents': 6, 'sample_groups': ['B41F', 'B66C', 'E02F', 'B60S', 'F02D']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
