code = """import json
import re

# Load UC patents
uc_data = locals()['var_functions.query_db:12']
with open(uc_data, 'r') as f:
    uc_patents = json.load(f)

# Extract unique UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    # Look for publication number after various keywords
    for keyword in ['pub. number', 'publication number', 'has pub. number', 'with publication number']:
        if keyword in info:
            # Find the pattern after the keyword
            after_keyword = info[info.find(keyword)+len(keyword):info.find(keyword)+50]
            match = re.search(r'([A-Z]{2}-[A-Z0-9-]+)', after_keyword)
            if match:
                uc_pub_numbers.add(match.group(1))
                break

print('UC publication numbers:', len(uc_pub_numbers))
print('Sample:', sorted(list(uc_pub_numbers))[:10])

# Load all patents with citations
all_data = locals()['var_functions.query_db:32']
with open(all_data, 'r') as f:
    all_patents = json.load(f)

# Search for citations to UC patents
citations = []
assignee_cpc = {}

for patent in all_patents:
    # Check if citation field contains any UC publication number
    citation_text = patent['citation']
    if not citation_text or citation_text == '[]':
        continue
    
    found_uc = None
    for uc_pub in uc_pub_numbers:
        if uc_pub in citation_text:
            found_uc = uc_pub
            break
    
    if not found_uc:
        continue
    
    # Extract citing patent info
    info = patent['Patents_info']
    
    # Get publication number of citing patent
    citing_pub = None
    for keyword in ['pub. number', 'publication number']:
        if keyword in info:
            after_keyword = info[info.find(keyword)+len(keyword):info.find(keyword)+50]
            match = re.search(r'([A-Z]{2}-[A-Z0-9-]+)', after_keyword)
            if match:
                citing_pub = match.group(1)
                break
    
    # Extract assignee (simplified)
    assignee = None
    parts = info.split(' ')
    for i, word in enumerate(parts):
        if word in ['by', 'to'] and i+1 < len(parts):
            # Get next 3-5 words as potential assignee
            potential = ' '.join(parts[i+1:i+6])
            if 'UNIV CALIFORNIA' not in potential.upper():
                assignee = potential.split(',')[0].split(' and ')[0]
                break
    
    if not assignee:
        # Try start of string
        first_words = ' '.join(parts[:5])
        if 'UNIV CALIFORNIA' not in first_words.upper():
            assignee = first_words
    
    if assignee and 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    if not assignee:
        continue
    
    # Clean assignee
    assignee = re.sub(r'\s+', ' ', assignee).strip()
    
    # Extract CPC codes
    cpc_codes = []
    cpc_str = patent['cpc']
    if cpc_str and cpc_str != '[]':
        try:
            cpc_list = json.loads(cpc_str)
            for item in cpc_list:
                if 'code' in item:
                    cpc_codes.append(item['code'])
        except:
            pass
    
    cpc_codes = list(set(cpc_codes))
    
    # Store
    citations.append({
        'citing_pub': citing_pub,
        'cited_uc_pub': found_uc,
        'assignee': assignee,
        'cpc_codes': cpc_codes
    })
    
    if assignee not in assignee_cpc:
        assignee_cpc[assignee] = set()
    assignee_cpc[assignee].update(cpc_codes)

print('\nFound', len(citations), 'citations to UC patents')
print('Unique assignees:', len(assignee_cpc))

# Save results
with open('/tmp/citation_analysis.json', 'w') as f:
    json.dump({
        'citations': citations,
        'assignee_cpc': {k: list(v) for k, v in assignee_cpc.items()},
        'uc_pub_numbers': sorted(list(uc_pub_numbers))
    }, f)

print('__RESULT__:')
print(json.dumps({
    'citations': len(citations),
    'assignees': len(assignee_cpc),
    'top_assignees': list(assignee_cpc.keys())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:10': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}, {'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.'}, {'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.'}, {'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.'}, {'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.'}, {'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.'}, {'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'}, {'Patents_info': 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.'}, {'Patents_info': 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.'}, {'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'Patents_info': 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.'}, {'Patents_info': 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.'}], 'var_functions.execute_python:20': {'total_uc_patents': 169, 'uc_pub_numbers_count': 114, 'sample_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2']}, 'var_functions.execute_python:24': {'total_uc_patents_processed': 169, 'uc_publication_numbers_found': 114, 'sample_pub_numbers': ['US-2005234013-A1', 'US-2019328740-A1', 'US-2021101879-A1', 'AU-3353000-A', 'AU-2898989-A', 'KR-20110004413-A', 'CA-3161617-A1', 'US-2023171142-A1', 'US-11421276-B2', 'JP-2014224156-A'], 'uc_assignees': []}, 'var_functions.execute_python:26': {'uc_patents_count': 114, 'uc_publication_numbers': 114, 'sample_uc_pubs': ['JP-2005104983-A', 'HK-1250569-A1', 'WO-2024044766-A3', 'US-7745569-B2', 'WO-2023239670-A1']}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'uc_patents_count': 114, 'citing_patents_analyzed': 200, 'citations_to_uc_found': 0, 'unique_citing_assignees': 0, 'sample_citations': []}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'total_uc_patents': 169, 'total_all_patents': 137678}, 'var_functions.execute_python:36': {'citations_found': 2, 'unique_assignees': 2, 'sample_assignees': ['CALIFORNIA INST OF TECHN', 'SCHOWALTER LEO J']}, 'var_functions.execute_python:40': {'analysis': 'complete'}, 'var_functions.execute_python:44': {'citations_to_uc': 0, 'unique_assignees': 0, 'sample': []}, 'var_functions.query_db:46': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:48': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:52': {'count': 123, 'sample': ['AP-3334-A', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A']}, 'var_functions.query_db:56': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
