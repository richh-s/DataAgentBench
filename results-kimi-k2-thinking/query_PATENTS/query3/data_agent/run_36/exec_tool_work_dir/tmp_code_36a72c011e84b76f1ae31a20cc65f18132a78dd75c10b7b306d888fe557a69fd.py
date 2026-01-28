code = """import json
import pandas as pd
from collections import defaultdict
import re

# Load the results from previous queries
# Access the variables from the storage

# First, get UNIV CALIFORNIA patents
uc_patents_key = 'var_functions.query_db:14'
uc_patents_data = locals().get(uc_patents_key)

uc_patents = []
if isinstance(uc_patents_data, str) and uc_patents_data.endswith('.json'):
    with open(uc_patents_data, 'r') as f:
        uc_patents = json.load(f)
elif isinstance(uc_patents_data, list):
    uc_patents = uc_patents_data

# Get all patents
all_patents_key = 'var_functions.query_db:12'
all_patents_data = locals().get(all_patents_key)

all_patents = []
if isinstance(all_patents_data, str) and all_patents_data.endswith('.json'):
    with open(all_patents_data, 'r') as f:
        all_patents = json.load(f)
elif isinstance(all_patents_data, list):
    all_patents = all_patents_data

print(f"Found {len(uc_patents)} UNIV CALIFORNIA patents")
print(f"Found {len(all_patents)} total patents")

# Extract publication numbers for UNIV CALIFORNIA patents
uc_pub_numbers = set()

for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for publication number patterns
    pub_num_match = re.search(r'(?:pub\. number|publication number)\s+([A-Z]{2}-[A-Z0-9]+-[A-Z0-9]+)', patents_info, re.IGNORECASE)
    if pub_num_match:
        pub_num = pub_num_match.group(1)
        uc_pub_numbers.add(pub_num)

print(f"Extracted {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print(f"Sample: {list(uc_pub_numbers)[:5]}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
