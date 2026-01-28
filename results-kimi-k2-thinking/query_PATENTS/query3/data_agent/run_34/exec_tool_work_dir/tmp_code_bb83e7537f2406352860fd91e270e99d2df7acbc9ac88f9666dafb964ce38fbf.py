code = """import json
import re

# Load the citations data that we found
citing_patents_path = locals()['var_functions.query_db:92']
with open(citing_patents_path, 'r') as f:
    citing_patents_raw = json.load(f)

print('Citing patents found: ' + str(len(citing_patents_raw)))

# Load UC patents data to get their CPC codes
uc_path = locals()['var_functions.query_db:38']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

# Build UC map: publication number -> CPC codes (normalized to uppercase)
uc_cpc_map = {}
uc_pub_numbers_upper = set()

for patent in uc_data:
    patents_info = patent['Patents_info']
    pub_match = re.search(r'pub[^\\w]*number[^\\w]*([A-Z]{2}-[^-]+-[A-Z][0-9])', patents_info, re.IGNORECASE)
    if pub_match:
        pub_num = pub_match.group(1).upper()
        uc_pub_numbers_upper.add(pub_num)
        
        try:
            cpc_data = json.loads(patent['cpc'])
            cpc_codes = list(set([cpc['code'] for cpc in cpc_data if 'code' in cpc]))
            uc_cpc_map[pub_num] = cpc_codes
        except:
            uc_cpc_map[pub_num] = []

print('UC patents loaded: ' + str(len(uc_cpc_map)))
print('Sample UC patent: ' + list(uc_cpc_map.keys())[0])

# Load CPC definitions
cpc_def_path = locals()['var_functions.query_db:28']
with open(cpc_def_path, 'r') as f:
    cpc_defs = json.load(f)

cpc_title_map = {item['symbol']: item['titleFull'] for item in cpc_defs}
print('CPC titles loaded: ' + str(len(cpc_title_map)))

# Process citing patents to find UC citations and extract assignees
assignee_cpc_relationships = []  # List of (assignee, cpc_code, cpc_title)
unique_assignees = set()

for patent in citing_patents_raw:
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in patent['Patents_info']:
        continue
    
    if not patent['citation'] or patent['citation'] == '[]':
        continue
    
    try:
        citations = json.loads(patent['citation'])
        
        # Extract assignee from this patent
        assignee_match = re.search(r'^([A-Z][A-Z0-9\\s&/.-]+?)\\s+(holds?|hold|is|owns|assigned|owned|belonging)', 
                                   patent['Patents_info'], re.IGNORECASE)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
        else:
            # Alternative pattern
            assignee_match2 = re.search(r'\\bis assigned to\\s+([A-Z][A-Z0-9\\s&/.-]+?)\\s', 
                                       patent['Patents_info'], re.IGNORECASE)
            if assignee_match2:
                assignee = assignee_match2.group(1).strip()
            else:
                continue  # Can't extract assignee
        
        # Check each citation to see if it cites a UC patent
        for citation in citations:
            cited_pub_num = citation.get('publication_number', '').upper()
            if cited_pub_num and cited_pub_num in uc_pub_numbers_upper:
                # This patent cites a UC patent!
                # Get the CPC codes of the cited UC patent
                cpc_codes = uc_cpc_map.get(cited_pub_num, [])
                
                for cpc_code in cpc_codes:
                    cpc_title = cpc_title_map.get(cpc_code, 'Title not found')
                    assignee_cpc_relationships.append({
                        'citing_assignee': assignee,
                        'cited_uc_patent': cited_pub_num,
                        'cpc_subclass': cpc_code,
                        'cpc_title_full': cpc_title
                    })
                    unique_assignees.add(assignee)
    except Exception as e:
        continue

print('Citing relationships found: ' + str(len(assignee_cpc_relationships)))
print('Unique assignees: ' + str(len(unique_assignees)))

if assignee_cpc_relationships:
    print('Sample results:')
    for i, record in enumerate(assignee_cpc_relationships[:10]):
        print(str(i+1) + '. ' + record['citing_assignee'] + ' cites ' + 
              record['cited_uc_patent'] + ' with CPC ' + record['cpc_subclass'])

# Group by assignee to prepare final answer
assignee_cpc_summary = {}
for record in assignee_cpc_relationships:
    assignee = record['citing_assignee']
    if assignee not in assignee_cpc_summary:
        assignee_cpc_summary[assignee] = []
    
    cpc_info = {
        'cpc_subclass': record['cpc_subclass'],
        'cpc_title': record['cpc_title_full']
    }
    
    # Avoid duplicates
    if cpc_info not in assignee_cpc_summary[assignee]:
        assignee_cpc_summary[assignee].append(cpc_info)

# Build final results
final_answer = []
for assignee, cpc_list in assignee_cpc_summary.items():
    for cpc_info in cpc_list:
        final_answer.append({
            'citing_assignee': assignee,
            'cpc_subclass': cpc_info['cpc_subclass'],
            'cpc_title': cpc_info['cpc_title']
        })

print('Final answer records: ' + str(len(final_answer)))

# Sort by assignee name for presentation
final_answer.sort(key=lambda x: x['citing_assignee'])

output = {
    'citing_assignees_excluding_uc_count': len(assignee_cpc_summary),
    'total_cpc_relationships': len(final_answer),
    'results': final_answer[:100]  # Limit to first 100 for display
}

print('__RESULT__:')
print(json.dumps(output, default=str))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'total': '169'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': {'status': 'success', 'count': 87}, 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'uc_patents_count': 87, 'uc_pub_numbers_count': 26, 'uc_pub_numbers': ['WO-2021102420-A1', 'US-11546022-B2', 'US-6767662-B2', 'US-6750960-B2', 'US-2006292670-A1', 'WO-2018026404-A3', 'AU-2019275518-B2', 'WO-2024112568-A1', 'US-2022074631-A1', 'WO-2012162563-A2', 'WO-2024044766-A3', 'WO-2023225482-A3', 'WO-2017214343-A1', 'US-2018243924-A1', 'US-2017145219-A1', 'US-11376346-B2', 'US-2017281687-A1', 'EP-0826155-A4', 'US-2006051790-A1', 'AU-2010214112-B2', 'EP-1212462-A1', 'US-9061071-B2', 'WO-2010045542-A3', 'US-11667770-B2', 'AU-2015364602-B2', 'US-2019328740-A1'], 'uc_cpc_sample': {'US-2022074631-A1': ['Y02B30/00', 'F25B2321/001', 'F25B21/00', 'F28D15/00', 'F25B21/00', 'F25B2321/001', 'F25B2321/001', 'F28D15/00', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08', 'A61D7/04', 'A61K31/025', 'A61K31/357', 'A61P43/00', 'A61P25/20', 'A61K31/045', 'A61K31/02', 'A61P23/00', 'A61K9/007', 'A61K31/341', 'A61M16/01', 'A61D7/04', 'A61K31/351', 'A61K31/351', 'A61K31/34', 'A61K31/08', 'A61K31/025', 'A61P43/00', 'A61K31/02', 'A61K31/045', 'A61P11/00', 'A61K31/357', 'A61P23/00', 'A61P25/20', 'A61M16/01', 'A61K31/357', 'A61P11/00', 'A61K9/007', 'A61K31/025', 'A61K31/015', 'A61K31/341', 'A61K31/025', 'A61K31/045', 'A61K31/341', 'A61K31/351', 'A61K31/357', 'A61K31/08', 'A61K9/007', 'A61P23/00', 'A61K31/34', 'A61K31/015'], 'US-2017281687-A1': ['A61K31/52', 'A61K2035/124', 'A61K31/522', 'A61K35/28', 'A61K35/28', 'A61K31/522', 'C12N2510/00', 'A61K2035/124', 'A61K31/52', 'A61K2035/124', 'A61K35/28']}}, 'var_functions.query_db:34': [{'count': '277644'}], 'var_functions.execute_python:36': {'uc_patents_count': 26, 'sample': {'US-2022074631-A1': ['Y02B30/00', 'F25B2321/001', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/08'], 'US-2017281687-A1': ['A61K31/52', 'A61K2035/124', 'A61K31/522']}}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [], 'var_functions.execute_python:42': {'uc_patents_total': 169, 'uc_pub_numbers': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F28D15/00', 'Y02B30/00', 'F25B2321/001'], 'AU-2019275518-B2': ['A61K31/045', 'A61M16/01', 'A61K9/007'], 'US-2017281687-A1': ['A61K2035/124', 'A61K35/28', 'A61K31/522']}}, 'var_functions.query_db:44': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}], 'var_functions.execute_python:45': {'uc_pub_count': 43, 'sample_pattern': "'%CA-2298540-A1%' OR citation LIKE '%US-9061071-B2%' OR citation LIKE '%WO-2012162563-A2%' OR citati"}, 'var_functions.execute_python:48': {'uc_patents_count': 43, 'query_conditions': 43, 'query_preview': "SELECT Patents_info, citation FROM publicationinfo WHERE citation LIKE '%US-2022074631-A1%' OR citation LIKE '%AU-2019275518-B2%' OR citation LIKE '%US-2017281687-A1%' OR citation LIKE '%US-9061071-B2"}, 'var_functions.query_db:50': [], 'var_functions.execute_python:52': {'uc_patents_count': 43, 'uc_pub_numbers': ['US-11376346-B2', 'WO-2024044766-A3', 'US-2023279470-A1', 'US-2023155090-A1', 'AU-2008349842-A1', 'US-6767662-B2', 'AU-2019275518-B2', 'CA-2298540-A1', 'US-2020025859-A1', 'US-2018243924-A1']}, 'var_functions.execute_python:54': {'patterns': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1'], 'count': 43}, 'var_functions.execute_python:56': {'uc_patents_count': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B21/00', 'Y02B30/00', 'F28D15/00'], 'AU-2019275518-B2': ['A61P23/00', 'A61K31/015', 'A61K31/08'], 'US-2017281687-A1': ['A61K31/52', 'C12N2510/00', 'A61K2035/124']}, 'uc_pub_numbers_sample': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1']}, 'var_functions.execute_python:58': {'cpc_definitions_count': 260808, 'cpc_title_map_size': 260808, 'sample_titles': {'A01K2227/108': 'Swine', 'A01K2227/105': 'Murine', 'A01K2227/101': 'Bovine'}}, 'var_functions.execute_python:60': {'status': 'ready_to_query', 'uc_patents_count': 43, 'uc_pub_numbers': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1', 'US-2021000566-A1', 'US-2006051790-A1', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-11667770-B2', 'US-6750960-B2', 'US-2020025859-A1', 'EP-1212462-A1', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'AU-2015364602-B2', 'IL-244029-A0', 'AU-2010214112-B2', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'US-11546022-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'HK-1250569-A1', 'US-2018243924-A1']}, 'var_functions.execute_python:64': {'uc_patents': 43, 'cpc_defs': 260808, 'sample_codes': {'US-2022074631-A1': ['F28D15/00', 'F25B21/00'], 'AU-2019275518-B2': ['A61P23/00', 'A61K31/02'], 'US-2017281687-A1': ['A61K2035/124', 'C12N2510/00']}}, 'var_functions.execute_python:68': {'loaded': True, 'sample_size': 1}, 'var_functions.execute_python:70': {'uc_patents_count': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F28D15/00', 'F25B2321/001', 'F25B21/00'], 'AU-2019275518-B2': ['A61K31/351', 'A61K31/341', 'A61K31/34']}, 'cpc_titles_sample': {'F25B21/00': 'Machines, plants or systems, using electric or magnetic effe', 'A61K31/357': 'Heterocyclic compounds having oxygen as the only ring hetero'}}, 'var_functions.execute_python:72': {'uc_patents_count': 43, 'sample_cpc': ['F25B21/00', 'Y02B30/00', 'F28D15/00', 'F25B2321/001'], 'cpc_titles_sample': {'F28D15/00': 'Heat-exchange apparatus with the intermediate heat', 'F25B21/00': 'Machines, plants or systems, using electric or mag'}, 'patterns': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1']}, 'var_functions.execute_python:74': {'uc_patents': 43, 'sample_uc': {'US-2022074631-A1': ['F25B21/00', 'F28D15/00', 'Y02B30/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/34', 'A61K31/015']}, 'sample_cpc_titles': {'F25B21/00': 'Machines, plants or systems, using electric or magnetic effe', 'A61K31/357': 'Heterocyclic compounds having oxygen as the only ring hetero'}}, 'var_functions.query_db:77': [], 'var_functions.query_db:78': [], 'var_functions.execute_python:82': {'uc_patents_count': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B2321/001', 'F25B21/00', 'F28D15/00'], 'AU-2019275518-B2': ['A61K31/025', 'A61D7/04', 'A61P43/00'], 'US-2017281687-A1': ['A61K35/28', 'C12N2510/00', 'A61K2035/124']}, 'cpc_titles_sample': {'F25B21/00': 'Machines, plants or systems, using electric or mag', 'A61K31/357': 'Heterocyclic compounds having oxygen as the only r'}, 'uc_pub_numbers_sample': ['US-2022074631-A1', 'AU-2019275518-B2', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'US-2017145219-A1', 'CA-2298540-A1']}, 'var_functions.query_db:84': [], 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json', 'var_functions.execute_python:90': {'uc_patents_analyzed': 43, 'sample_uc_cpc': {'US-2022074631-A1': ['F25B21/00', 'F25B2321/001', 'Y02B30/00'], 'AU-2019275518-B2': ['A61K31/357', 'A61K31/08', 'A61D7/04']}, 'citing_assignees_count': 0, 'final_results_count': 0, 'sample_results': []}, 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
