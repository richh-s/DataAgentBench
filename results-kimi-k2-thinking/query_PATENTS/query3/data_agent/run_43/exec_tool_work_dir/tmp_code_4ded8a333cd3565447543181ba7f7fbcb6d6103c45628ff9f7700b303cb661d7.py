code = """import json
import re

# Get UC patents data
file_path = locals()['var_functions.query_db:14']
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    # Look for publication number patterns
    patterns = [
        r'(?:pub\. number|publication number|has pub\. number|has publication number|pub\. number|number) ([A-Z]{2}-[A-Z0-9-]+)',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, info, re.IGNORECASE)
        for match in matches:
            if '-' in match and len(match) > 6:
                uc_pub_numbers.add(match)

# More general pattern too
for patent in uc_patents:
    info = patent['Patents_info']
    matches = re.findall(r'\b([A-Z]{2}-\d{4,}[A-Z0-9-]*)\b', info)
    for match in matches:
        uc_pub_numbers.add(match)

# Save UC publication numbers
with open('/tmp/uc_pub_numbers.json', 'w') as f:
    json.dump(list(uc_pub_numbers), f)

result = {
    'uc_patent_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_uc_numbers': sorted(list(uc_pub_numbers))[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:12': {'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:24': {'count': 169, 'first_keys': ['Patents_info', 'citation']}, 'var_functions.execute_python:26': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_numbers': ['AU-2003297741-A1', 'AU-3353000-A', 'HR-P20201231-T1', 'US-2017087258-A1', 'AU-2015364602-B2', 'HK-1250569-A1', 'MX-2013002850-A', 'CA-2718348-C', 'JP-2009260386-A', 'KR-20050085437-A']}, 'var_functions.query_db:28': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}]}

exec(code, env_args)
