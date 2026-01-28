code = """import json
import pandas as pd
import re
from datetime import datetime

# Load publication data
pub_file = locals()['var_functions.query_db:0']
print('Loading publications from:', pub_file)
with open(pub_file, 'r') as f:
    publications = json.load(f)

# Load CPC sample data  
cpc_file = locals()['var_functions.query_db:6']
print('Loading CPC data from:', cpc_file)
with open(cpc_file, 'r') as f:
    cpc_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'pub_count': len(publications),
    'cpc_count': len(cpc_data),
    'sample_pub_cpc': publications[0].get('cpc', '')[:200] if publications else 'No data',
    'sample_grant_date': publications[0].get('grant_date', '') if publications else 'No data'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/108', 'synonyms': '[]', 'titleFull': 'Swine', 'titlePart': '[\n  "Swine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/105', 'synonyms': '[]', 'titleFull': 'Murine', 'titlePart': '[\n  "Murine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/101', 'synonyms': '[]', 'titleFull': 'Bovine', 'titlePart': '[\n  "Bovine"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/107', 'synonyms': '[]', 'titleFull': 'Rabbit', 'titlePart': '[\n  "Rabbit"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'True', 'childGroups': '[]', 'children': '[]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'CPCONLY', 'level': '9.0', 'limitingReferences': '[]', 'notAllocatable': 'False', 'parents': '[\n  "A01K2227/10",\n  "A01K2227/00",\n  "A01K",\n  "A01",\n  "A"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'A01K2227/103', 'synonyms': '[]', 'titleFull': 'Ovine', 'titlePart': '[\n  "Ovine"\n]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8th, 2019'}, {'grant_date': '8th April 2019'}, {'grant_date': '2019, May 30th'}, {'grant_date': '22nd May 2019'}, {'grant_date': '2019 on Nov 14th'}], 'var_functions.execute_python:18': {'var_functions.query_db:0': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:0.json'}, 'var_functions.query_db:6': {'type': "<class 'str'>", 'length': 38, 'preview': 'file_storage/functions.query_db:6.json'}, 'var_functions.query_db:8': {'type': "<class 'list'>", 'length': 10, 'preview': "[{'grant_date': '14th Mar 2019'}, {'grant_date': 'Mar 19th, 2019'}, {'grant_date': 'Mar 12th, 2019'}, {'grant_date': '2019 on Jul 12th'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': 'July 8t"}}}

exec(code, env_args)
