code = """import json
import pandas as pd
from collections import defaultdict

# Load the results from previous queries
# File paths are stored in variables, let's read them

# First, let's read the data about UNIV CALIFORNIA patents
uc_file = var_functions.query_db:14
if isinstance(uc_file, str) and uc_file.endswith('.json'):
    with open(uc_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = uc_file if isinstance(uc_file, list) else []

# Now let's get all patents data
all_file = var_functions.query_db:12
if isinstance(all_file, str) and all_file.endswith('.json'):
    with open(all_file, 'r') as f:
        all_patents = json.load(f)
else:
    all_patents = all_file if isinstance(all_file, list) else []

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")
print(f"Found {len(all_patents)} total patents")

# Let's extract publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = set()
uc_assignees = defaultdict(list)

for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Extract publication number from patents_info
    import re
    # Look for patterns like "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', patents_info, re.IGNORECASE)
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        uc_pub_numbers.add(pub_num)
        uc_assignees[pub_num].append('UNIV CALIFORNIA')

print(f"Extracted {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print(f"Sample: {list(uc_pub_numbers)[:5]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
