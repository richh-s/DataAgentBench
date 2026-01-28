code = """import json

# Load the UNIV CALIFORNIA patents full data
uc_file_path = locals()['var_functions.query_db:6']
with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract all publication numbers for UNIV CALIFORNIA
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Look for publication number patterns
    import re
    pub_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if pub_match:
        uc_pub_numbers.add(pub_match.group(1))

uc_pub_count = len(uc_pub_numbers)

print('__RESULT__:')
print(json.dumps({
    'uc_publication_numbers_count': uc_pub_count,
    'sample_uc_pub_numbers': list(uc_pub_numbers)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'uc_patents_count': 114, 'sample_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A'], 'sample_cpc_codes': ['A61K38/16', 'A61K39/4611', 'B64C39/02', 'C12Q1/485', 'C12N15/1044', 'C07D409/08', 'H01M8/0232', 'C09J11/04', 'B01L2300/0883', 'C07B59/001']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
