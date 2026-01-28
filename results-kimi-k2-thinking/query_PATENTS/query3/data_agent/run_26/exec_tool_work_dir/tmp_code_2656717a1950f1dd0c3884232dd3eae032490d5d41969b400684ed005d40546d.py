code = """import json
import re

# First, let's extract all UNIV CALIFORNIA publication numbers
uc_file = locals()['var_functions.query_db:6']
if isinstance(uc_file, str) and uc_file.endswith('.json'):
    with open(uc_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = uc_file

uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Find publication numbers (format: CC-NNNNNNN-XXX)
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', patents_info)
    for match in matches:
        uc_pub_numbers.add(match)

# Get first 20 UC publication numbers for testing
uc_sample = list(uc_pub_numbers)[:20]

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_patents),
    'total_uc_publication_numbers': len(uc_pub_numbers),
    'sample_uc_publications': uc_sample
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA', 'var_functions.execute_python:10': 'Found 1112 unique cited publication numbers', 'var_functions.query_db:12': [], 'var_functions.execute_python:14': 'Found 114 UNIV CALIFORNIA publication numbers', 'var_functions.execute_python:16': ['US-70199003-A', 'AU-2007297661-A', 'WO-2012158833-A3', 'US-2018053351-W', 'AU-2004253879-A1', 'KR-20107024636-A', 'WO-2023239670-A1', 'US-2017145219-A1', 'EP-07753965-A', 'RO-7944874-A'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total patents in database: 277813', 'var_functions.execute_python:22': 'UC publication numbers sample: "CA-2718348-C", "HK-18104296-A", "AU-2019275518-B2", "CA-3027364-A", "US-2018053351-W", "IL-24402916-A", "AU-2007297661-A1", "US-2022016812-W", "CN-201280035828-A", "US-2017281687-A1"...', 'var_functions.execute_python:24': 'Total UC publication numbers: 329, divided into 7 chunks', 'var_functions.execute_python:26': "Sample UC publication numbers to check: ['AU-2019275518-A', 'US-202117472182-A', 'US-201916454755-A']", 'var_functions.query_db:28': [], 'var_functions.execute_python:30': 'Loaded 277813 patents. Searching for citations to 329 UC patents...', 'var_functions.execute_python:32': 'Found 0 patents that cite UNIV CALIFORNIA patents', 'var_functions.execute_python:36': 'UC publication numbers: 329', 'var_functions.execute_python:38': {'total_uc_pubs': 10, 'samples': [{'info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'pub_nums': ['US-202117472182-A', 'US-2022074631-A1']}, {'info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'pub_nums': ['TW-107142982-A', 'TW-201925402-A']}, {'info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'pub_nums': ['US-201916454755-A', 'US-11421276-B2']}, {'info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'pub_nums': ['AU-2019275518-A', 'AU-2019275518-B2']}, {'info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'pub_nums': ['US-201515313510-A', 'US-2017194630-A1']}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': 'Full database file path: file_storage/functions.query_db:18.json'}

exec(code, env_args)
