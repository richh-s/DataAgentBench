code = """# Get all patents that cite UNIV CALIFORNIA patents and their assignees/CPC data
import json
import re
from collections import defaultdict

# Get the file paths from storage
all_patents_file = locals()['var_functions.query_db:24']

# Load all patents at once
with open(all_patents_file, 'r') as f:
    all_patents = json.load(f)

uc_pub_numbers = set()
assignee_citations = defaultdict(list)

# Extract UNIV CALIFORNIA publication numbers
for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        # Extract the publication number
        match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-[^\s,]+)', patents_info, re.IGNORECASE)
        if match:
            uc_pub_numbers.add(match.group(1))

print('Found', len(uc_pub_numbers), 'UNIV CALIFORNIA patent numbers')
print('Sample:', list(uc_pub_numbers)[:5])

# Find patents that cite UC patents
for patent in all_patents[:100000]:  # Limit for speed
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    citation_data = patent.get('citation', '[]')
    if citation_data == '[]' or not citation_data:
        continue
    
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num and pub_num in uc_pub_numbers:
                # Extract assignee
                assignee_match = re.search(r'(?:is (?:owned by|assigned to|belonging to)|holds the|belongs to)\s+([^,.(]+)', patents_info, re.IGNORECASE)
                if assignee_match:
                    assignee = assignee_match.group(1).strip()
                    if 'UNIV CALIFORNIA' not in assignee.upper():
                        # Get CPC codes for this patent
                        cpc_data = patent.get('cpc', '[]')
                        try:
                            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                            primary_cpcs = [cpc.get('code') for cpc in cpc_list if isinstance(cpc, dict) and cpc.get('inventive', False)]
                            if primary_cpcs:
                                assignee_citations[assignee].extend(primary_cpcs)
                        except:
                            pass
                break
    except:
        continue

# Collect all CPC codes to lookup
all_cpc_codes = set()
for codes in assignee_citations.values():
    all_cpc_codes.update(codes)

print('Citing assignees found:', len(assignee_citations))
print('CPC codes to lookup:', len(all_cpc_codes))

# Get top assignees
sorted_assignees = sorted(assignee_citations.items(), key=lambda x: len(x[1]), reverse=True)
print('\nTop assignees:')
for i, (assignee, cpcs) in enumerate(sorted_assignees[:10]):
    print(assignee + ': ' + str(len(cpcs)) + ' citations')

# Save for CPC lookup
results = {
    'assignee_cpc_map': {k: list(v) for k, v in assignee_citations.items()},
    'total_cpc_codes': len(all_cpc_codes)
}

with open('assignee_cpc.json', 'w') as f:
    json.dump(results, f, indent=2)

print('\n__RESULT__:')
print(json.dumps({'assignees': len(assignee_citations), 'cpc_codes': len(all_cpc_codes)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.execute_python:76': {'candidates': 0}, 'var_functions.query_db:86': [{'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201916362297-A) is assigned to UNIV CALIFORNIA and has publication no. US-11248107-B2.'}, {'Patents_info': 'The IL patent application (no. IL-14014099-A) is assigned to UNIV CALIFORNIA and has publication no. IL-140140-A0.'}, {'Patents_info': 'The US application (number US-202017021925-A) is assigned to UNIV CALIFORNIA and has pub. number US-2021000566-A1.'}, {'Patents_info': 'The PT application (number PT-14764430-T) is assigned to UNIV CALIFORNIA and has publication number PT-2970346-T.'}, {'Patents_info': 'The US patent application (no. US-37750473-A) is assigned to UNIV CALIFORNIA and has publication no. US-3842373-A.'}, {'Patents_info': 'The US patent filing (application number US-202117791452-A) is assigned to UNIV CALIFORNIA and has pub. number US-2023321419-A1.'}, {'Patents_info': 'In KR, the application (number KR-20087016723-A) is assigned to UNIV CALIFORNIA and has publication no. KR-20080078049-A.'}, {'Patents_info': 'The CA patent application (number CA-2562038-A) is assigned to UNIV CALIFORNIA and has pub. number CA-2562038-C.'}, {'Patents_info': 'In BR, the patent application (no. BR-112021021092-A) is assigned to UNIV CALIFORNIA and has publication no. BR-112021021092-A8.'}, {'Patents_info': 'The US patent application (ID US-74211203-A) is assigned to UNIV CALIFORNIA and has publication no. US-2005136639-A1.'}, {'Patents_info': 'In US, the patent filing (application no. US-202016988179-A) is assigned to UNIV CALIFORNIA and has publication number US-2021039104-A1.'}, {'Patents_info': 'The WO patent application (number US-2023073050-W) is assigned to UNIV CALIFORNIA and has publication no. WO-2024050335-A2.'}, {'Patents_info': 'In WO, the application (ID US-2018018836-W) is assigned to UNIV CALIFORNIA and has publication no. WO-2018152537-A1.'}, {'Patents_info': 'In JP, the patent filing (app. number JP-2014180140-A) is assigned to UNIV CALIFORNIA and has pub. number JP-2014224156-A.'}, {'Patents_info': 'In US, the patent filing (application number US-70199003-A) is assigned to UNIV CALIFORNIA and has publication number US-2004115131-A1.'}, {'Patents_info': 'The US patent filing (application number US-91189497-A) is assigned to UNIV CALIFORNIA and has publication no. US-6030830-A.'}, {'Patents_info': 'In WO, the application (ID US-2018053351-W) is assigned to UNIV CALIFORNIA and has publication number WO-2019067860-A1.'}, {'Patents_info': 'The PE application (no. PE-2012000906-A) is assigned to UNIV CALIFORNIA and has publication number PE-20130764-A1.'}, {'Patents_info': 'In US, the patent application (number US-201515514092-A) is assigned to UNIV CALIFORNIA and has publication no. US-2017294981-A1.'}, {'Patents_info': 'In CN, the application (ID CN-201210027378-A) is assigned to UNIV CALIFORNIA and has pub. number CN-102584712-A.'}, {'Patents_info': 'In CA, the application (ID CA-2278751-A) is assigned to UNIV CALIFORNIA and has publication no. CA-2278751-A1.'}, {'Patents_info': 'The US patent filing (application no. US-202117798325-A) is assigned to UNIV CALIFORNIA and has pub. number US-2023155090-A1.'}, {'Patents_info': 'In US, the application (number US-202218054917-A) is assigned to UNIV CALIFORNIA and has publication no. US-2023340506-A1.'}], 'var_functions.query_db:88': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}, {'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.'}, {'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.'}, {'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.'}, {'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.'}, {'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.'}, {'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'}, {'Patents_info': 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.'}, {'Patents_info': 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.'}, {'Patents_info': 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.'}, {'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'Patents_info': 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.'}, {'Patents_info': 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.'}, {'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.'}, {'Patents_info': 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US application (no. US-8864206-A), with publication number US-2009031436-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent filing (application number AU-2005269556-A), with publication number AU-2005269556-A1.'}, {'Patents_info': 'The US patent filing (application no. US-201916362297-A) is assigned to UNIV CALIFORNIA and has publication no. US-11248107-B2.'}, {'Patents_info': 'Patent filing (application no. US-2019021660-W) from WO, assigned to UNIV CALIFORNIA, with publication number WO-2019173834-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent filing (app. number US-201715422925-A), with pub. number US-2017145219-A1.'}, {'Patents_info': 'The US patent filing (application no. US-201815950106-A) is held by UNIV CALIFORNIA and has publication no. US-2018304537-A1.'}, {'Patents_info': 'In US, the application (ID US-202016883515-A) is owned by UNIV CALIFORNIA and has publication number US-2021002329-A1.'}, {'Patents_info': 'The KR application (number KR-20207004898-A) is belonging to UNIV CALIFORNIA and has pub. number KR-20200041324-A.'}, {'Patents_info': 'In CN, the application (no. CN-201180052574-A) is belonging to UNIV CALIFORNIA and has pub. number CN-103189548-A.'}, {'Patents_info': 'The CA application (no. CA-2298540-A) is held by UNIV CALIFORNIA and has pub. number CA-2298540-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU application (number AU-2001296493-A), with publication no. AU-2001296493-B2.'}, {'Patents_info': 'In AU, the application (ID AU-2008329628-A) is belonging to UNIV CALIFORNIA and has publication no. AU-2008329628-B2.'}, {'Patents_info': 'Application (no. US-201916401060-A) from US, assigned to UNIV CALIFORNIA, with publication no. US-10765865-B2.'}, {'Patents_info': 'In JP, the application (ID JP-2004321293-A) is belonging to UNIV CALIFORNIA and has publication number JP-2005104983-A.'}, {'Patents_info': 'The IL patent application (no. IL-14014099-A) is assigned to UNIV CALIFORNIA and has publication no. IL-140140-A0.'}, {'Patents_info': 'The US application (number US-202017021925-A) is assigned to UNIV CALIFORNIA and has pub. number US-2021000566-A1.'}, {'Patents_info': 'In US, the patent application (ID US-17323505-A) is held by UNIV CALIFORNIA and has pub. number US-2006051790-A1.'}, {'Patents_info': 'Patent filing (app. number KR-20207010098-A) from KR, belonging to UNIV CALIFORNIA, with publication no. KR-20200084864-A.'}, {'Patents_info': 'The PT application (number PT-14764430-T) is assigned to UNIV CALIFORNIA and has publication number PT-2970346-T.'}], 'var_functions.execute_python:92': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.query_db:94': [], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json'}

exec(code, env_args)
