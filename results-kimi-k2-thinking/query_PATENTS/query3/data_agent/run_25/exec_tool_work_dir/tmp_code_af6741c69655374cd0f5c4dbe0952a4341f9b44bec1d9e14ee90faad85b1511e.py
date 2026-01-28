code = """import json
import re

# Load the full dataset
all_data = locals()['var_functions.query_db:8']
if isinstance(all_data, str):
    with open(all_data, 'r') as f:
        all_data = json.load(f)

# Load UC data to get the list of UC publication numbers
uc_data = locals()['var_functions.query_db:30']
if isinstance(uc_data, str):
    with open(uc_data, 'r') as f:
        uc_data = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for row in uc_data:
    patents_info = row.get('Patents_info', '')
    patterns = [
        r'pub\.? number\s+([A-Z0-9-]+)',
        r'publication number\s+([A-Z0-9-]+)',
        r'publication no\.?\s+([A-Z0-9-]+)',
        r'([A-Z]{2}-[0-9]+-[A-Z][0-9]?)'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, patents_info, re.IGNORECASE)
        for match in matches:
            if any(prefix in match for prefix in ['US-', 'WO-', 'EP-', 'AU-', 'TW-', 'JP-', 'KR-', 'CA-']):
                uc_pub_numbers.add(match.strip())

print(f"UC publication numbers to search for: {len(uc_pub_numbers)}")
print(f"Sample UC pub numbers: {list(uc_pub_numbers)[:5]}")

# Now search for patents that cite these UC patents
citing_patents = []

# For debugging, let's check a smaller subset first
sample_size = min(50000, len(all_data))
print(f"Searching through {sample_size} patents...")

for i, row in enumerate(all_data[:sample_size]):
    if i % 10000 == 0:
        print(f"Processing {i}/{sample_size}...")
    
    patents_info = row.get('Patents_info', '')
    
    # Skip UNIV CALIFORNIA patents
    if re.search(r'UNIV\s+CALIFORNIA\b', patents_info, re.IGNORECASE):
        continue
    
    # Check citations
    citation_text = row.get('citation', '')
    if citation_text and citation_text.strip() != '[]':
        try:
            citations = json.loads(citation_text)
            for cite in citations:
                pub_num = cite.get('publication_number', '')
                if pub_num and pub_num in uc_pub_numbers:
                    # Found a citation to a UC patent!
                    
                    # Extract assignee
                    assignee = None
                    patterns = [
                        r'^(.*?)\s+(?:holds the US|holds the US patent|holds the US application)',
                        r'In US, the (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is(?: belonging to| assigned to| held by| owned by))? (.+?)(?: and has|,|:|\.)',
                        r'Application (?:\(.*?\) )?from US, (?:owned by|held by|assigned to|belonging to) (.+?)(?:,| with|$)',
                        r'The US (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is (?:assigned to|owned by|held by|belonging to)) (.+?)(?: and has|,|\. |$)',
                        r'Patent (?:application|filing) (?:\(.*?\) )?(?:from US, )?(?:assigned to|held by|belonging to) (.+?)(?:,| with|$)',
                        r'^(.*?)\s+holds the US patent',
                        r'^(.*?)\s+holds the US application'
                    ]
                    
                    for pattern in patterns:
                        match = re.search(pattern, patents_info, re.IGNORECASE)
                        if match:
                            assignee = match.group(1).strip()
                            # Clean up common prefixes
                            assignee = re.sub(r'^(In US, the|The US|Patent|Application)\s+', '', assignee, flags=re.IGNORECASE)
                            assignee = assignee.strip()
                            break
                    
                    if assignee and 'UNIV CALIFORNIA' not in assignee.upper():
                        citing_patents.append({
                            'citing_assignee': assignee,
                            'cited_uc_pub': pub_num,
                            'patents_info': patents_info[:200] + '...' if len(patents_info) > 200 else patents_info,
                            'cpc_data': row.get('cpc', '[]')
                        })
                        print(f"Found citation: {assignee} -> {pub_num}")
        except Exception as e:
            pass

print('__RESULT__:')
print(json.dumps({
    'patents_searched': sample_size,
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'citations_found': len(citing_patents),
    'first_few_citations': citing_patents[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'sample_patents_info': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.', 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.', 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.', 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.', 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.', 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.', 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.', 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.', 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.', 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.', 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.', 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.', 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.', 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.', 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'], 'extracted_assignees': ['PANASONIC IP MAN CO LTD', 'GLASSNER RUDOLF', 'COVESTRO LLC', 'HOMOLOGY MEDICINES INC', 'APPLETON GRP LLC', 'MEAD JOHNSON NUTRITION CO', 'WATERS TECHNOLOGIES CORP', 'MODERNATX INC', 'YOBS TECH INC', 'HONDA MOTOR CO LTD', 'INTEL CORP', 'UNIV EMORY', 'INNOLUX CORP', 'LEGACY RES AND DEVELOPMENT GROUP LLC', 'EBAY INC', 'MAHLE INT GMBH', 'RLW VIRTUAL SOLUTIONS LLC', 'BHANDARI RAJNEESH', 'TANDEM DIABETES CARE INC', 'MURATA MANUFACTURING CO']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'uc_patents_count': 169, 'uc_pub_numbers_count': 169, 'citations_from_other_assignees': 0, 'first_10_citations': []}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'uc_patents_found': 3, 'sample_uc_pubs': [{'pub_num': 'US-2022074631-A1', 'patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'cpc': '[\n  {\n    "code": "Y02B30/00",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F25B2321/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F28D15/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F25B21/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]'}, {'pub_num': 'US-11421276-B2', 'patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'cpc': '[\n  {\n    "code": "Y02A50/30",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/118",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q1/6883",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/136",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/112",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/158",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "C12Q2600/118",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}, {'pub_num': 'US-2017194630-A1', 'patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'cpc': '[\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0569",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0483",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2300/0037",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/366",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/366",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0569",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M2004/021",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0483",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0492",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0469",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/74",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/134",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/382",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/1395",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/0471",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/625",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M4/386",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01M10/0525",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/70",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02E60/10",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}]}, 'var_functions.list_db:22': ['cpc_definition'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'uc_pub_numbers': 0, 'citations_found': 0, 'sample_citations': []}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'uc_patents_found': 100, 'uc_pub_numbers_extracted': 126, 'sample_uc_pub_numbers': ['US-11667770-B2', 'US-2021101879-A1', 'US-2023314781-A1', 'US-201916401060-A', 'US-2019059638-W', 'US-2019209590-A1', 'WO-2017214343-A1', 'EP-1224461-B1', 'US-201916362297-A', 'EP-00959970-A']}}

exec(code, env_args)
