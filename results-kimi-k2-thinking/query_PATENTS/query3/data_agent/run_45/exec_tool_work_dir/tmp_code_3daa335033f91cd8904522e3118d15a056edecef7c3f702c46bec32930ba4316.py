code = """import json
import re
from collections import defaultdict

# Debug: check what variables are available
available_vars = [k for k in locals().keys() if 'var_' in k]
print('Available variables containing "var_":', available_vars)

# Try to access UC patents
try:
    uc_patents = var_functions.query_db:58
    print('Successfully accessed UC patents directly')
    print('UC patents count:', len(uc_patents))
except:
    print('Direct access failed, trying alternative approach')
    uc_patents = None

# If direct access failed, find UC patents in available variables
if uc_patents is None:
    for key in available_vars:
        try:
            data = locals()[key]
            if isinstance(data, list) and len(data) > 0:
                if 'UNIV CALIFORNIA' in str(data[0]):
                    uc_patents = data
                    print(f'Found UC patents in {key}: {len(data)} records')
                    break
        except:
            continue

if uc_patents is None:
    print('ERROR: Could not find UC patents')
    print('\\n__RESULT__:')
    print(json.dumps({'error': 'No UC patents found'}))
else:
    # Extract UC publication numbers
    uc_pub_numbers = set()
    for patent in uc_patents:
        info = patent.get('Patents_info', '')
        
        # Multiple patterns to extract pub number
        patterns = [
            r'pub\.?\s*number\s+([A-Z0-9-]+)',
            r'pub\. number\s+([^\.]+)',
            r'has publication number\s+([A-Z0-9-]+)',
            r'with pub\. number\s+([A-Z0-9-]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, info)
            if match:
                pub_num = match.group(1).strip()
                if '-' in pub_num and len(pub_num) > 5:  # Basic validation
                    uc_pub_numbers.add(pub_num)
                    break
    
    print('UC publication numbers extracted:', len(uc_pub_numbers))
    print('Sample numbers:', list(uc_pub_numbers)[:5])
    
    # Store CPC codes for UC patents
    uc_cpc_codes = {}
    total_cpc_codes = 0
    for patent in uc_patents:
        info = patent.get('Patents_info', '')
        cpc_str = patent.get('cpc', '[]')
        if cpc_str and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                codes = [item.get('code') for item in cpc_list if item.get('code')]
                # Store by publication number if we can extract it
                for pattern in patterns:
                    match = re.search(pattern, info)
                    if match:
                        pub_num = match.group(1).strip()
                        uc_cpc_codes[pub_num] = codes
                        break
                total_cpc_codes += len(codes)
            except:
                pass
    
    print(f'Total CPC codes for UC patents: {total_cpc_codes}')
    
    print('\\n__RESULT__:')
    result = {
        'uc_patents_count': len(uc_patents),
        'uc_pub_numbers_count': len(uc_pub_numbers),
        'uc_cpc_codes_total': total_cpc_codes,
        'sample_uc_pub_numbers': list(uc_pub_numbers)[:5]
    }
    print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:70': {'uc_patents': 169, 'uc_pub_numbers': 59, 'citations_found': 1, 'unique_assignees': 1, 'top_assignees': [['The US patent application', 1, 17]]}}

exec(code, env_args)
