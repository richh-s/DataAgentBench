code = """import json
import re

# Step 1: Load all patent data
all_data = locals()['var_functions.query_db:8']
if isinstance(all_data, str):
    with open(all_data, 'r') as f:
        all_data = json.load(f)

print(f"Total patents loaded: {len(all_data)}")

# Step 2: Extract UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
uc_patterns = [
    r'UNIV CALIFORNIA\b',
    r'\bUNIV CALIFORNIA(?!-)',
    r'^(UNIV CALIFORNIA)\b'
]

for row in all_data:
    patents_info = row.get('Patents_info', '')
    # Check if this is a UNIV CALIFORNIA patent
    if re.search(r'UNIV\s+CALIFORNIA\b', patents_info, re.IGNORECASE):
        # Extract publication number
        pub_match = re.search(r'(?:pub\.? number|publication number|publication no\.?)\s+([A-Z0-9-]+)', patents_info, re.IGNORECASE)
        if pub_match:
            pub_num = pub_match.group(1)
            uc_pub_numbers.add(pub_num)
        else:
            # Try alternate pattern: pub. number US-2017194630-A1 format
            pub_match2 = re.search(r'([A-Z]{2}-[0-9]+-[A-Z][0-9]?)', patents_info)
            if pub_match2:
                uc_pub_numbers.add(pub_match2.group(1))

print(f"Found {len(uc_pub_numbers)} UNIV CALIFORNIA publication numbers")
print("Sample UC pub numbers:", list(uc_pub_numbers)[:5])

# Step 3: Find patents that cite UNIV CALIFORNIA patents
citing_patents = []

for i, row in enumerate(all_data):
    if i % 10000 == 0:
        print(f"Processing patent {i}...")
    
    patents_info = row.get('Patents_info', '')
    
    # Skip patents assigned to UNIV CALIFORNIA
    if re.search(r'UNIV\s+CALIFORNIA\b', patents_info, re.IGNORECASE):
        continue
    
    # Check citations
    citation_text = row.get('citation', '[]')
    if citation_text and citation_text.strip() != '[]':
        try:
            citations = json.loads(citation_text)
            for cite in citations:
                pub_num = cite.get('publication_number', '')
                if pub_num and pub_num in uc_pub_numbers:
                    # Extract assignee
                    assignee = None
                    patterns = [
                        r'^(.*?) holds the US',
                        r'In US, the (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is(?: belonging to| assigned to| held by| owned by))? (.+?)(?: and has|,|:)',
                        r'Application (?:\(.*?\) )?from US, (?:owned by|held by|assigned to|belonging to) (.+?)(?:,| with|$)',
                        r'The US (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is (?:assigned to|owned by|held by|belonging to)) (.+?)(?: and has|,|\. )',
                        r'Patent (?:application|filing) (?:\(.*?\) )?(?:from US, )?(?:assigned to|held by|belonging to) (.+?)(?:,| with|$)'
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, patents_info, re.IGNORECASE)
                        if match:
                            assignee = match.group(1).strip()
                            break
                    
                    if assignee and 'UNIV CALIFORNIA' not in assignee.upper():
                        citing_patents.append({
                            'citing_assignee': assignee,
                            'cited_pub_number': pub_num,
                            'cpc_data': row.get('cpc', '[]')
                        })
        except:
            pass

# Remove duplicates
unique_citations = {}
for cite in citing_patents:
    key = (cite['citing_assignee'], cite['cited_pub_number'])
    if key not in unique_citations:
        unique_citations[key] = cite

result = list(unique_citations.values())

print('__RESULT__:')
print(json.dumps({
    'uc_pub_numbers': len(uc_pub_numbers),
    'citations_found': len(result),
    'sample_citations': result[:10]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.', 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.', 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.', 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.', 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.', 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.', 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.', 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.', 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.', 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.', 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.', 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'], 'extracted_assignees': ['PANASONIC IP MAN CO LTD', 'GLASSNER RUDOLF', 'COVESTRO LLC', 'HOMOLOGY MEDICINES INC', 'APPLETON GRP LLC', 'MEAD JOHNSON NUTRITION CO', 'WATERS TECHNOLOGIES CORP', 'MODERNATX INC', 'YOBS TECH INC', 'HONDA MOTOR CO LTD', 'INTEL CORP', 'UNIV EMORY', 'INNOLUX CORP', 'LEGACY RES AND DEVELOPMENT GROUP LLC', 'EBAY INC', 'MAHLE INT GMBH', 'RLW VIRTUAL SOLUTIONS LLC', 'BHANDARI RAJNEESH', 'TANDEM DIABETES CARE INC', 'MURATA MANUFACTURING CO']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'uc_patents_count': 169, 'uc_pub_numbers_count': 169, 'citations_from_other_assignees': 0, 'first_10_citations': []}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_patents_found': 3, 'sample_uc_pubs': [{'pub_num': 'US-2022074631-A1', 'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'pub_num': 'US-11421276-B2', 'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'cpc': '[\n  {\n    "code": "Y02A50/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/118",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/118",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'pub_num': 'US-2017194630-A1', 'patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'cpc': '[\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0569",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0483",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2300/0037",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/366",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/366",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0569",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0483",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0492",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/74",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}, 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
