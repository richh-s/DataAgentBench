code = """# Let me access the stored data using the correct variable names
# The storage key is var_functions.query_db:10
import json
import re
from collections import defaultdict

# Access the result from the previous query
uc_patents_data = locals().get('var_functions.query_db:10', [])

if not uc_patents_data:
    print('__RESULT__:')
    print(json.dumps({'error': 'No data found for UNIV CALIFORNIA patents'}))
else:
    # Extract UC publication numbers
    uc_pub_numbers = []
    for patent in uc_patents_data[:1000]:  # Limit for memory
        patents_info = patent.get('Patents_info', '')
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-\d+-[A-Z]\d*)', patents_info, re.IGNORECASE)
        if pub_match:
            uc_pub_numbers.append(pub_match.group(1))
    
    print('__RESULT__:')
    print(json.dumps({
        'total_uc_patents': len(uc_patents_data),
        'uc_pub_numbers_sample': uc_pub_numbers[:10],
        'success': True
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'C09J9/02', 'level': '8.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "C09J9/00",\n  "C09J",\n  "C09",\n  "C"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'C09J9/02', 'synonyms': '[]', 'titleFull': 'Electrically-conducting adhesives', 'titlePart': '[\n  "Electrically-conducting adhesives"\n]'}]}

exec(code, env_args)
