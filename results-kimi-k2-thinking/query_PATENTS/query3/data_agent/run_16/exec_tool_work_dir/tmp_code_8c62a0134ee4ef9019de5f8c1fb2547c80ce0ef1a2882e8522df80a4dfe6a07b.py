code = """import json
import re

# Load UC patent data
uc_file = locals()['var_functions.query_db:28']
with open(uc_file, 'r') as f:
    uc_patents = json.load(f)

print('UC patent count:', len(uc_patents))

# Extract UC publication numbers
uc_pub_numbers = []
for patent in uc_patents:
    info = patent['Patents_info']
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', info)
    if matches:
        uc_pub_numbers.append(matches[-1])

print('UC publication numbers extracted:', len(uc_pub_numbers))

# Load all patents with citations
all_citations = locals()['var_functions.query_db:62']
with open(all_citations, 'r') as f:
    all_patents = json.load(f)

print('Total patents to search:', len(all_patents))

# Find patents that cite UC patents
uc_set = set(uc_pub_numbers)
citing_patents_data = []

for patent in all_patents:
    citation_text = patent.get('citation', '')
    if not citation_text or citation_text == '[]':
        continue
    
    # Check if any UC patent is cited
    for uc_pub in uc_set:
        if uc_pub in citation_text:
            # Get assignee name
            info = patent['Patents_info']
            assignee = 'Unknown'
            
            # Try different patterns to extract assignee
            patterns = [
                r'^(.*?)(?:holds|hold|assigned|belongs|owned|owns|is)',
                r'(?:by|to|assigned to|owned by|belongs to)\s+(.*?)(?:\s+and has|,|\.\s)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, info, re.IGNORECASE)
                if match:
                    assignee = match.group(1).strip()
                    break
            
            # Exclude UNIV CALIFORNIA
            if 'UNIV CALIFORNIA' not in assignee.upper():
                citing_patents_data.append({
                    'citing_patent': info,
                    'assignee': assignee,
                    'cited_uc_patent': uc_pub,
                    'cpc': patent.get('cpc', '[]')
                })
            break

print('Found citing patents:', len(citing_patents_data))

# Count by assignee
assignee_counts = {}
for data in citing_patents_data:
    assignee = data['assignee']
    assignee_counts[assignee] = assignee_counts.get(assignee, 0) + 1

# Get top assignees
top_assignees = sorted(assignee_counts.items(), key=lambda x: x[1], reverse=True)
print('\nTop assignees:')
for assignee, count in top_assignees[:10]:
    print(f'  {assignee}: {count} citations')

print('\nFirst citing patent details:')
if citing_patents_data:
    first = citing_patents_data[0]
    print('Assignee:', first['assignee'])
    print('Cites UC patent:', first['cited_uc_patent'])

result = {
    'total_citing_patents': len(citing_patents_data),
    'unique_assignees': len(assignee_counts),
    'top_assignees': top_assignees[:10]
}

print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_patents': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'uc_patents_count': 169, 'uc_pub_numbers_count': 169, 'first_10_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1']}, 'var_functions.query_db:34': [], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}], 'var_functions.query_db:40': [{'Patents_info': 'In US, the application (ID US-202117502422-A) is belonging to APPLE INC and has publication no. US-2022110100-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2012039285-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-8565254-B2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015189633-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2019215098-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2019254025-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-10448389-B1",\n    "type": ""\n  }\n]', 'cpc': '[\n  {\n    "code": "H04W72/23",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L25/0204",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/0053",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/11",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/27",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04W24/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W24/08",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W72/042",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/11",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W48/16",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04W76/27",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H04L5/001",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]'}], 'var_functions.query_db:42': [], 'var_functions.query_db:44': [], 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': {'citing_patents_count': 0, 'uc_patents_count': 169}, 'var_functions.execute_python:52': {'next_step': 'Fetch all patents with citations and identify those citing UC patents', 'uc_patent_count': 169}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.execute_python:56': {'uc_patents': 169, 'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017194630-A1', 'JP-S6163700-A', 'US-2017281687-A1', 'EP-1224461-B1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'AU-2002254753-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1']}, 'var_functions.query_db:58': [], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:66': {'status': 'loaded files', 'uc_patents': 169, 'citation_sample_size': 137678}, 'var_functions.query_db:68': [], 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json'}

exec(code, env_args)
