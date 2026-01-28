code = """import json
import re

# Load full patent dataset
full_data_path = locals()['var_functions.query_db:20']
with open(full_data_path, 'r') as f:
    all_patents = json.load(f)

# Rebuild the set of UC cited publications
with open(locals()['var_functions.query_db:16'], 'r') as f:
    uc_patents = json.load(f)

uc_cited_pubs = set()
for row in uc_patents:
    citation_str = row['citation']
    if citation_str and citation_str != '[]':
        try:
            citations = json.loads(citation_str)
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num:
                    uc_cited_pubs.add(pub_num)
        except:
            continue

# Find all patents that cite UC patents
citing_assignees = {}
citing_cpc_codes = {}

for i, patent in enumerate(all_patents):
    if i % 1000 == 0:
        print(f'Processing {i}/{len(all_patents)}...')
    
    citation_str = patent['citation']
    patents_info = patent['Patents_info']
    cpc_str = patent.get('cpc', '')
    
    if not citation_str or citation_str == '[]':
        continue
    
    # Parse citations
    try:
        citations = json.loads(citation_str)
        for citation in citations:
            cited_pub = citation.get('publication_number', '')
            if cited_pub in uc_cited_pubs:
                # This patent cites a UC patent
                # Extract assignee from Patents_info
                assignee_match = re.search(r'([A-Z][^,]+?) holds|([A-Z][^,]+?) is the assignee|assigned to ([A-Z][^,]+)', patents_info, re.IGNORECASE)
                if assignee_match:
                    assignee = assignee_match.group(1) or assignee_match.group(2) or assignee_match.group(3)
                    if assignee:
                        assignee = assignee.strip().upper()
                        if 'UNIV CALIFORNIA' not in assignee:
                            citing_assignees[assignee] = citing_assignees.get(assignee, 0) + 1
                            
                            # Also record CPC codes if available
                            if cpc_str and cpc_str != '[]':
                                try:
                                    cpc_codes = json.loads(cpc_str)
                                    if assignee not in citing_cpc_codes:
                                        citing_cpc_codes[assignee] = set()
                                    for cpc_entry in cpc_codes:
                                        code = cpc_entry.get('code', '')
                                        if code:
                                            citing_cpc_codes[assignee].add(code)
                                except:
                                    pass
    except:
        continue

# Save results
cpc_codes_dict = {k: list(v) for k, v in citing_cpc_codes.items()}

print('__RESULT__:')
print(json.dumps({
    'citing_assignees_count': len(citing_assignees),
    'top_assignees': dict(sorted(citing_assignees.items(), key=lambda x: x[1], reverse=True)[:20]),
    'assignee_cpc_codes': cpc_codes_dict
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 169, 'total_citations': 1308, 'sample': [{'publication_number': 'US-4599677-A', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2015129765-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'FR-3105380-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-11466906-B2', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2001053519-A1', 'source_patent': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}, 'var_functions.execute_python:10': {'total_cited_publications': 1112, 'sample_pubs': ['WO-2013025632-A1', 'US-2020023209-A1', 'US-6200265-B1', 'EP-2694154-A1', 'US-9974593-B2', 'US-5366770-A', 'US-8865406-B2', 'US-2006105322-A1', 'US-7757565-B2', 'US-2014356956-A1', 'JP-H11261169-A', 'US-2016242650-A1', 'US-2014356867-A1', 'WO-2014093712-A1', 'US-8080523-B2', 'WO-2013169802-A1', 'WO-2010144578-A2', 'EP-2515996-A2', 'US-2011281288-A1', 'US-2012065087-A1']}, 'var_functions.execute_python:12': {'message': 'Created cited_pubs.json with all cited publication numbers', 'count': 1112}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 277813, 'total_uc_cited_pubs': 1112, 'sample_uc_cited': ['US-2014170753-A1', 'US-2003222263-A1', 'FR-1447611-A', 'US-5710621-A', 'US-5019504-A', 'US-5125736-A', 'US-4911920-A', 'US-6303344-B1', 'US-9057109-B2', 'US-5532071-A']}, 'var_functions.execute_python:24': {'total_patents_loaded': 277813, 'total_uc_cited_pubs': 1112, 'sample_uc_cited': ['US-2016000590-A1', 'WO-9213961-A1', 'US-9587252-B2', 'EP-2764103-A2', 'US-6461870-B2', 'US-2005238577-A1', 'US-6492160-B1', 'EP-2928557-A2', 'US-2015291961-A1', 'US-8618096-B2']}, 'var_functions.execute_python:26': {'uc_cited_pubs_count': 1112, 'sample_cited': ['US-2005147558-A1', 'US-2011300538-A1', 'US-2013062527-A1', 'US-2012316076-A1', 'US-7135709-B1', 'US-2015240261-A1', 'US-6492160-B1', 'WO-2014039872-A1', 'US-5895223-A', 'WO-2008016345-A2']}, 'var_functions.execute_python:28': {'total_patents_to_search': 277813, 'total_uc_cited_pubs': 1112}}

exec(code, env_args)
