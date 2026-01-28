code = """import json
import re

# Load all UNIV CALIFORNIA patents
uc_file = locals()['var_functions.query_db:30']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

# Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent['Patents_info']
    # Extract publication number
    patterns = [
        r'(?:pub\.|publication|pub\s+no|publication\s+no|pub\s+number|has\s+publication\s+no|has\s+pub\.|with\s+pub\.)\s+(?:[A-Z]+-)?([A-Z]{2}-\d+-[A-Z]\d*)',
        r'publication\s+number\s+([A-Z]{2}-\d+-[A-Z]\d*)',
        r'pub\.\s+number\s+([A-Z]{2}-\d+-[A-Z]\d*)'
    ]
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            pub_num = match.group(1)
            uc_pub_numbers.add(pub_num)
            break

print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print("Sample:", list(uc_pub_numbers)[:10])

# Create a query to find patents citing these publication numbers
# Since we can't load all data at once, let's create a search pattern
search_patterns = []
for pub_num in list(uc_pub_numbers)[:10]:  # Start with sample
    search_patterns.append(f"%{pub_num}%")

result = {
    'uc_pub_numbers': list(uc_pub_numbers),
    'sample_search_patterns': search_patterns
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_pub_to_cpc': {}, 'uc_pub_numbers': []}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'uc_pub_count': 54, 'citation_count': 0, 'citations': []}, 'var_functions.query_db:44': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}]}

exec(code, env_args)
