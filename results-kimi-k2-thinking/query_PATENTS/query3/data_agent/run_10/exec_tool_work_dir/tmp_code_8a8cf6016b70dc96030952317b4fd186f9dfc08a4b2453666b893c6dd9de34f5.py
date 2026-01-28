code = """import json
import os

# Get the file path from the storage variable
result_file = var_functions.query_db:30

# Read the data
with open(result_file, 'r') as f:
    uc_patents = json.load(f)

print('Total UC patents with citations:', len(uc_patents))

# Process the data to extract UC publication numbers and their citations
uc_data = []
for record in uc_patents:
    patents_info = record['Patents_info']
    citation_str = record['citation']
    
    # Extract UC publication number
    import re
    pub_match = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z-]+)', patents_info)
    uc_pub_num = pub_match.group(1) if pub_match else None
    
    # Parse citations
    try:
        citations = json.loads(citation_str)
    except:
        citations = []
    
    uc_data.append({
        'uc_pub_num': uc_pub_num,
        'citations': citations
    })

# Count total citations
total_citations = sum(len(r['citations']) for r in uc_data if r['citations'])
print('Total citations found across all UC patents:', total_citations)
print('First few UC patents and their citations:')
for i in range(min(3, len(uc_data))):
    record = uc_data[i]
    print(f'{i+1}. UC Patent {record["uc_pub_num"]} has {len(record["citations"])} citations')
    for j, cite in enumerate(record['citations'][:3]):
        pub_num = cite.get('publication_number', 'N/A')
        print(f'   - Citation {j+1}: {pub_num}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total': '169'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
