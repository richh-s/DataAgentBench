code = """import json, re
from collections import defaultdict

# Try to access the variable more directly
var_name = 'var_functions.query_db:17'
if var_name in globals():
    patent_result = globals()[var_name]
    print('Accessed variable successfully:', type(patent_result))
    
    # Load data
    if isinstance(patent_result, str) and '.json' in patent_result:
        with open(patent_result, 'r') as f:
            patent_data = json.load(f)
    else:
        patent_data = patent_result
    
    print('Total records:', len(patent_data))
    print('Keys in first record:', list(patent_data[0].keys()) if patent_data else 'No data')
    
    # Debug first record
    if patent_data:
        first = patent_data[0]
        print('First record CPC:', first.get('cpc', 'NONE')[:100])
        print('First record date:', first.get('publication_date', 'NONE'))
    
    print('__RESULT__:')
    print('SUCCESS')
else:
    print('Variable not found in globals')
    print('__RESULT__:')
    print('FAILURE')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:15': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
