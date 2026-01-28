code = """import json
import re

# Access the full results from previous queries
results_univ_california = var_functions['query_db:12']
results_publications = var_functions['query_db:8']
results_citations = var_functions['query_db:6']

# Load the data if they're file paths
if isinstance(results_univ_california, str) and results_univ_california.endswith('.json'):
    with open(results_univ_california, 'r') as f:
        univ_california_data = json.load(f)
else:
    univ_california_data = results_univ_california

if isinstance(results_publications, str) and results_publications.endswith('.json'):
    with open(results_publications, 'r') as f:
        publications_data = json.load(f)
else:
    publications_data = results_publications

if isinstance(results_citations, str) and results_citations.endswith('.json'):
    with open(results_citations, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = results_citations

# Let's understand the data structure better
print('UNIV CALIFORNIA records:', len(univ_california_data))
sample = json.dumps(univ_california_data[0], indent=2)
print('Sample record:', sample[:500])
print('\n' + '='*80 + '\n')

print('Publications records:', len(publications_data))
sample = json.dumps(publications_data[0], indent=2)
print('Sample record:', sample[:500])
print('\n' + '='*80 + '\n')

print('Citations records:', len(citations_data))
sample = json.dumps(citations_data[0], indent=2)
print('Sample record:', sample[:500])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
