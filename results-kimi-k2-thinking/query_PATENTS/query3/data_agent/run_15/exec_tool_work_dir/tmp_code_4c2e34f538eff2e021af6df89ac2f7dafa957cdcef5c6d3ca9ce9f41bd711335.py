code = """import json
import re

# Read the data for UNIV CALIFORNIA patents
data_path = 'var_functions.query_db:10.json'
with open(data_path, 'r') as f:
    uc_patents = json.load(f)

# Extract publication numbers from UNIV CALIFORNIA patents
uc_pub_numbers = []

for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for publication number patterns like US-2022074631-A1
    pub_num_match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-\d+-[A-Z]\d?)', patents_info, re.IGNORECASE)
    if pub_num_match:
        uc_pub_numbers.append(pub_num_match.group(1))

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'uc_pub_numbers': uc_pub_numbers[:20],  # First 20 for brevity
    'sample_patents_info': [p['Patents_info'] for p in uc_patents[:3]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'C09J9/02', 'level': '8.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "C09J9/00",\n  "C09J",\n  "C09",\n  "C"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'C09J9/02', 'synonyms': '[]', 'titleFull': 'Electrically-conducting adhesives', 'titlePart': '[\n  "Electrically-conducting adhesives"\n]'}]}

exec(code, env_args)
