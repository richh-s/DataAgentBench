code = """import json
import os
import re
from collections import defaultdict
from datetime import datetime

# Get the file path from previous query result
result_key = 'var_functions.query_db:32'
if result_key not in globals():
    print(f"ERROR: {result_key} not found in globals")
    print('Available globals:', [k for k in globals().keys() if 'query_db' in k])
    result = {'status': 'error', 'message': f'{result_key} not found'}
else:
    result_file = globals()[result_key]
    print(f"Loading data from: {result_file}")
    
    try:
        with open(result_file, 'r') as f:
            patents_data = json.load(f)
        
        print(f"Successfully loaded {len(patents_data)} records")
        
        # Process data to extract CPC groups and filing years
        cpc_year_counts = defaultdict(lambda: defaultdict(int))
        
        for patent in patents_data:
            # Extract grant year (all should be 2019 from our query)
            grant_date = patent.get('grant_date', '')
            grant_year = 2019  # We filtered for 2019
            
            # Parse CPC codes
            cpc_data = patent.get('cpc', '[]')
            try:
                cpc_codes = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            except:
                continue
            
            if not isinstance(cpc_codes, list):
                continue
            
            # Count each CPC code
            for cpc_entry in cpc_codes:
                if not isinstance(cpc_entry, dict):
                    continue
                
                cpc_code = cpc_entry.get('code', '')
                if not cpc_code:
                    continue
                
                # Extract the group code (first 4 characters + first digit of subclass = level 4)
                # Format: Section (1 char) + Class (2 digits) + Subclass (1 letter) + Group (1-3 digits)
                # Level 4 is the main group (e.g., G06F from G06F9/45533)
                
                if len(cpc_code) >= 4:
                    section = cpc_code[0]  # e.g., 'G'
                    class_num = cpc_code[1:3]  # e.g., '06'
                    subclass = cpc_code[3]  # e.g., 'F'
                    
                    # Find the group part (after '/')
                    group_start = cpc_code.find('/')
                    if group_start > 0:
                        # Main group is everything before '/'
                        main_group = cpc_code[:group_start]
                        
                        # Level 4 group code is section+class+subclass+first group digit
                        if len(main_group) >= 4:
                            level4_code = main_group[:4]
                            cpc_year_counts[level4_code][grant_year] += 1
        
        print(f"Found {len(cpc_year_counts)} unique CPC level 4 groups")
        
        # Save processed data
        with open('cpc_filing_counts.json', 'w') as f:
            json.dump(dict(cpc_year_counts), f)
        
        result = {
            'status': 'success', 
            'cpc_groups': len(cpc_year_counts),
            'total_patents': len(patents_data),
            'sample_groups': list(cpc_year_counts.keys())[:5]
        }
        
    except Exception as e:
        print(f"Error processing data: {e}")
        import traceback
        traceback.print_exc()
        result = {'status': 'error', 'message': str(e)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Patents_info': 'Patent application (number DE-10317286-A) from DE, belonging to NICOLAY VERWALTUNGS GMBH, with publication no. DE-10317286-B3.', 'grant_date': 'dated 7th October 2004'}, {'Patents_info': 'MIELE & CIE holds the DE patent filing (app. number DE-102005018015-A), with publication number DE-102005018015-B3.', 'grant_date': '2006 on Apr 27th'}, {'Patents_info': 'UHLMANN PAC SYSTEME GMBH & CO holds the DE patent filing (app. number DE-102006022262-A), with publication number DE-102006022262-B3.', 'grant_date': 'Nov 29th, 2007'}, {'Patents_info': 'The DE patent filing (application no. DE-102007030491-A) is belonging to HEINRICH GEORG GMBH MASCHINENF and has pub. number DE-102007030491-B3.', 'grant_date': '2009, January 29th'}, {'Patents_info': 'In DE, the patent filing (application no. DE-102009032362-A) is owned by MARTOR KG and has pub. number DE-102009032362-B3.', 'grant_date': '17th Jun 2010'}, {'Patents_info': 'Patent application (no. DE-102015114819-A) from DE, held by ROCKWELL COLLINS DEUTSCHLAND GMBH, with pub. number DE-102015114819-B3.', 'grant_date': 'on December 22nd, 2016'}, {'Patents_info': 'MITUTOYO CORP holds the DE patent filing (app. number DE-10037981-A), with pub. number DE-10037981-B4.', 'grant_date': '19th of October, 2017'}, {'Patents_info': 'The DE patent application (no. DE-10052167-A) is held by YAMATO SEWING MACHINE MFG and has pub. number DE-10052167-B4.', 'grant_date': '23rd Jun 2005'}, {'Patents_info': 'Application (no. DE-10127786-A) from DE, belonging to KRAHFORST JUERGEN, with pub. number DE-10127786-B4.', 'grant_date': 'November 10th, 2005'}, {'Patents_info': 'In DE, the patent application (no. DE-10130631-A) is owned by SCHNEIDER SIEGHARD and has publication number DE-10130631-B4.', 'grant_date': '28th of October, 2010'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:18': {'status': 'check_complete'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.execute_python:28': {'status': 'error', 'message': 'Could not find result file'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
