code = """import json
import re
from collections import defaultdict

# Get UC patents directly from storage
uc_patents = locals()['var_functions.query_db:44']

print(f"Type of uc_patents: {type(uc_patents)}")
print(f"Length of uc_patents: {len(uc_patents) if hasattr(uc_patents, '__len__') else 'N/A'}")

if uc_patents and isinstance(uc_patents, list):
    print(f"First UC patent: {uc_patents[0]}")
    
    # Extract UC publication numbers
    uc_pub_numbers = set()
    for patent in uc_patents:
        info = patent.get('Patents_info', '')
        match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
        if match:
            pub_num = match.group(1).strip()
            uc_pub_numbers.add(pub_num)
        
    print(f"\nExtracted {len(uc_pub_numbers)} UC publication numbers")
    print(f"Sample: {list(uc_pub_numbers)[:5]}")
    
    # Count CPC codes per UC patent
    total_cpc_codes = 0
    for patent in uc_patents:
        cpc_data = patent.get('cpc', '[]')
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                total_cpc_codes += len(cpc_list)
            except:
                pass
    
    print(f"\nTotal CPC codes across all UC patents: {total_cpc_codes}")

print('__RESULT__:')
result = {
    'uc_patents_count': len(uc_patents) if isinstance(uc_patents, list) else 0,
    'uc_pub_numbers_count': len(uc_pub_numbers) if 'uc_pub_numbers' in locals() else 0,
    'total_cpc_codes': total_cpc_codes if 'total_cpc_codes' in locals() else 0
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}}

exec(code, env_args)
