code = """import json
import re

# Load UC patents
uc_file = locals()['var_functions.query_db:14']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

print('Number of UC patents:', len(uc_patents))

# Let's examine the first few patents more carefully
for i, patent in enumerate(uc_patents[:3]):
    info = patent['Patents_info']
    print(f'\n=== Patent {i+1} ===')
    print('Patents_info:', info[:200])
    
    # Try different regex approaches
    print('Trying pattern 1:', re.findall(r'\b[A-Z]{2}-\d{4,}[A-Z0-9-]*\b', info))
    print('Trying pattern 2:', re.findall(r'[A-Z]{2}-\d+-[A-Z0-9-]+', info))
    print('Trying pattern 3:', re.findall(r'US-\d{4,}-[A-Z0-9]+', info))

# Now try a comprehensive extraction
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    # More comprehensive pattern to catch all variations
    patterns = [
        r'[A-Z]{2}-\d{4,}-[A-Z0-9]+',  # US-202117472182-A
        r'[A-Z]{2}-\d{4,}[A-Z]',        # US-202117472182A
        r'[A-Z]{2}-[A-Z0-9-]{4,}',      # More general
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, info)
        for match in matches:
            if len(match) > 8:  # Ensure it's a full patent number
                uc_pub_numbers.add(match)

result = {
    'uc_patent_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_numbers': sorted(list(uc_pub_numbers))[:15]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:12': {'sample_patent': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:24': {'count': 169, 'first_keys': ['Patents_info', 'citation']}, 'var_functions.execute_python:26': {'uc_patent_count': 169, 'uc_pub_numbers_count': 114, 'sample_uc_numbers': ['AU-2003297741-A1', 'AU-3353000-A', 'HR-P20201231-T1', 'US-2017087258-A1', 'AU-2015364602-B2', 'HK-1250569-A1', 'MX-2013002850-A', 'CA-2718348-C', 'JP-2009260386-A', 'KR-20050085437-A']}, 'var_functions.query_db:28': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}], 'var_functions.execute_python:34': {'uc_patent_count': 169, 'uc_pub_numbers_count': 187, 'sample_uc_numbers': ['AP-2011005954-A', 'AU-2001296493-A', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A1']}, 'var_functions.execute_python:38': {'count': 187, 'sample': ['US-2021000566-A1', 'AU-7724398-A', 'US-2017015812-W', 'CA-3055214-A', 'US-202117472182-A']}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:46': {'total_uc_patents': 169, 'unique_uc_pub_numbers': 114, 'sample_numbers': ['US-2019328740-A1', 'US-2019209590-A1', 'CA-2283629-C', 'US-2017087258-A1', 'IL-244029-A0', 'MX-2013002850-A', 'US-11546022-B2', 'US-2021181673-A1', 'CA-3161617-A1', 'RO-70061-A']}, 'var_functions.execute_python:52': {'total_patents_with_citations': 137678, 'uc_patent_publications': 0, 'citing_patents_count': 0}, 'var_functions.execute_python:56': {'uc_patent_count': 169, 'uc_pub_numbers_count': 187, 'sample_numbers': ['AP-2011005954-A', 'AU-2001296493-A', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A1']}, 'var_functions.execute_python:60': {'citing_patents_count': 0, 'uc_citations_count': 0, 'total_patents_checked': 137678, 'uc_publications_count': 0}, 'var_functions.query_db:62': [], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:68': {'uc_patent_count': 169, 'uc_pub_numbers_count': 0, 'sample_uc_numbers': []}}

exec(code, env_args)
