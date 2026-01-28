code = """import json, os, sys

# Read the UC California data file
uc_file_path = 'var_functions.query_db:50'

if os.path.exists(uc_file_path):
    with open(uc_file_path, 'r') as f:
        uc_data = json.load(f)
    
    print('Loaded UNIV CALIFORNIA patents:', len(uc_data))
    
    # Show first record structure
    if uc_data:
        first_rec = uc_data[0]
        print('First record keys:', list(first_rec.keys()))
        print('Sample Patents_info:', first_rec.get('Patents_info', '')[:100])
        print('Has citation:', bool(first_rec.get('citation')))
    
    # Initialize collections
    cpc_codes = set()
    cited_patents = set()
    
    # Process records
    for i, rec in enumerate(uc_data[:100]):
        # Extract CPC codes
        cpc_str = rec.get('cpc', '')
        if cpc_str and len(cpc_str) > 2:
            try:
                # Use eval safely
                cpc_list = eval(cpc_str, {"__builtins__": {}}, {})
                if isinstance(cpc_list, list):
                    for cpc in cpc_list:
                        if isinstance(cpc, dict) and 'code' in cpc:
                            cpc_codes.add(cpc['code'])
            except Exception as e:
                print(f'Error parsing CPC in record {i}: {str(e)[:50]}')
    
    print('Unique CPC codes found:', len(cpc_codes))
    print('Sample CPC codes:', sorted(list(cpc_codes))[:10])
    
    result = {
        'uc_patents': len(uc_data),
        'cpc_codes_count': len(cpc_codes),
        'sample_cpc': sorted(list(cpc_codes))[:10]
    }
    
    print('\n__RESULT__:')
    print(json.dumps(result))
else:
    print('File not found')
    print('\n__RESULT__:')
    print(json.dumps({'error': 'file_not_found'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:20': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.query_db:22': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': [{'total': '277813'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:38': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
