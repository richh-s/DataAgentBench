code = """import json
import re

# Load data files
uc_file = locals()['var_functions.query_db:30']
citation_file = locals()['var_functions.query_db:60']

with open(uc_file, 'r') as f:
    uc_records = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for record in uc_records:
    info = record['Patents_info']
    match = re.search(r'pub\. number\s+([A-Z]{2}-[A-Z0-9-]+)', info)
    if match:
        uc_pub_numbers.add(match.group(1))

print('UC pub numbers:', len(uc_pub_numbers))

# Load and process citation data in chunks
with open(citation_file, 'r') as f:
    all_patents = json.load(f)

print('Total patents to check:', len(all_patents))

# Find citing patents with assignees
assignee_citations = {}

for patent in all_patents:
    info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in info:
        continue
    
    # Get citations
    citation_str = patent.get('citation', '[]')
    if citation_str == '[]':
        continue
    
    try:
        citations = json.loads(citation_str)
        cites_uc = False
        
        for cite in citations:
            if cite.get('publication_number') in uc_pub_numbers:
                cites_uc = True
                break
        
        if cites_uc:
            # Extract assignee
            assignee = ''
            if 'holds the' in info:
                assignee = info.split('holds the')[0].strip()
            elif 'assigned to' in info:
                assignee = info.split('assigned to')[1].split(' and')[0].strip()
            elif 'is owned by' in info:
                assignee = info.split('is owned by')[1].split(' and')[0].strip()
            elif 'is belonging to' in info:
                assignee = info.split('is belonging to')[1].split(' and')[0].strip()
            
            if assignee:
                # Get CPC codes
                cpc_codes = []
                cpc_str = patent.get('cpc', '[]')
                if cpc_str != '[]':
                    try:
                        cpc_list = json.loads(cpc_str)
                        for cpc in cpc_list:
                            if cpc.get('inventive') and len(cpc.get('code', '')) >= 4:
                                cpc_codes.append(cpc['code'][:4])
                                break  # Take only first primary
                    except:
                        pass
                
                # Record
                if assignee not in assignee_citations:
                    assignee_citations[assignee] = {
                        'count': 0,
                        'cpc_codes': set()
                    }
                
                assignee_citations[assignee]['count'] += 1
                if cpc_codes:
                    assignee_citations[assignee]['cpc_codes'].add(cpc_codes[0])
    
    except:
        continue

print('Found', len(assignee_citations), 'assignees citing UC patents')

# Format results
results = []
for assignee, data in assignee_citations.items():
    if assignee != 'UNIV CALIFORNIA':
        results.append({
            'assignee': assignee,
            'citations': data['count'],
            'cpc_subclasses': list(data['cpc_codes'])[:5]  # Limit to 5
        })

# Sort by citation count
results.sort(key=lambda x: x['citations'], reverse=True)

output = {
    'total_assignees': len(results),
    'citing_assignees': results[:30],  # Top 30
    'uc_pub_numbers_found': len(uc_pub_numbers)
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:22': [{'total_rows': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'count': 59, 'publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'CN-100339724-C', 'US-2017145219-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'US-2021000566-A1', 'US-2006051790-A1', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-11667770-B2', 'CA-2562038-C', 'US-6750960-B2', 'US-2020025859-A1', 'EP-1212462-A1', 'US-5547866-A', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'AU-2015364602-B2', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'CN-102584712-A', 'CN-102067370-B', 'US-11546022-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'HK-1250569-A1', 'ID-23426-A', 'US-5304932-A', 'US-2018243924-A1', 'AU-6535890-A']}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:54': {'uc_publication_numbers': ['EP-4284234-A1', 'AU-6535890-A', 'IL-244029-A0', 'CN-102584712-A', 'EP-0826155-A4', 'US-2023321419-A1', 'WO-2012162563-A2', 'TW-201925402-A', 'WO-2020055916-A9', 'US-5547866-A', 'AU-2015364602-B2', 'WO-2021102420-A1', 'US-5304932-A', 'US-2021000566-A1', 'MX-2013002850-A', 'US-11667770-B2', 'AU-2003297741-A1', 'CN-102067370-B', 'CA-2550552-A1', 'US-2006292670-A1', 'US-2022074631-A1', 'CA-2562038-C', 'WO-2017214343-A1', 'WO-2010045542-A3', 'JP-2014224156-A', 'RO-70061-A', 'JP-S6163700-A', 'HK-1250569-A1', 'US-9061071-B2', 'US-2017281687-A1', 'US-2023279470-A1', 'US-2023155090-A1', 'US-6750960-B2', 'US-2006051790-A1', 'CN-103189548-A', 'AU-2010214112-B2', 'AU-2019275518-B2', 'IL-274176-A', 'WO-2024044766-A3', 'EP-1212462-A1', 'US-2020025859-A1', 'WO-2018026404-A3', 'US-11376346-B2', 'US-2023171142-A1', 'US-2021101879-A1', 'WO-2024112568-A1', 'ID-23426-A', 'AU-2007297661-A1', 'KR-20200041324-A', 'US-2019328740-A1', 'AU-2008349842-A1', 'US-2022018060-A1', 'US-11546022-B2', 'US-2018243924-A1', 'WO-2023225482-A3', 'CA-2298540-A1', 'CN-100339724-C', 'US-6767662-B2', 'US-2017145219-A1']}, 'var_functions.execute_python:58': {'uc_count': 59, 'uc_pub_numbers': ['US-11376346-B2', 'CN-102584712-A', 'US-2022018060-A1', 'US-2022074631-A1', 'ID-23426-A', 'US-6750960-B2', 'WO-2012162563-A2', 'US-11667770-B2', 'US-2021101879-A1', 'WO-2010045542-A3', 'US-6767662-B2', 'AU-6535890-A', 'US-11546022-B2', 'US-2023171142-A1', 'WO-2018026404-A3', 'CN-100339724-C', 'EP-1212462-A1', 'AU-2003297741-A1', 'MX-2013002850-A', 'US-2023279470-A1', 'US-5304932-A', 'US-9061071-B2', 'CN-102067370-B', 'US-2006292670-A1', 'WO-2020055916-A9', 'US-2019328740-A1', 'CA-2550552-A1', 'WO-2017214343-A1', 'US-2017145219-A1', 'WO-2021102420-A1', 'US-5547866-A', 'US-2020025859-A1', 'AU-2007297661-A1', 'CA-2562038-C', 'US-2023321419-A1', 'CN-103189548-A', 'RO-70061-A', 'WO-2024112568-A1', 'JP-S6163700-A', 'CA-2298540-A1', 'EP-0826155-A4', 'WO-2024044766-A3', 'TW-201925402-A', 'EP-4284234-A1', 'HK-1250569-A1', 'AU-2010214112-B2', 'US-2006051790-A1', 'AU-2008349842-A1', 'US-2021000566-A1', 'IL-274176-A', 'AU-2019275518-B2', 'US-2023155090-A1', 'US-2018243924-A1', 'AU-2015364602-B2', 'KR-20200041324-A', 'US-2017281687-A1', 'IL-244029-A0', 'WO-2023225482-A3', 'JP-2014224156-A']}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [], 'var_functions.query_db:68': [{'symbol': 'B01J2523/25', 'titleFull': 'Barium'}, {'symbol': 'B01J13/0021', 'titleFull': 'Preparation of sols containing a solid organic phase'}, {'symbol': 'B01J13/0026', 'titleFull': 'Preparation of sols containing a liquid organic phase'}, {'symbol': 'B01J13/0008', 'titleFull': 'Sols of inorganic materials in water'}, {'symbol': 'B01J13/0043', 'titleFull': 'Preparation of sols containing elemental metal'}], 'var_functions.list_db:70': ['cpc_definition'], 'var_functions.execute_python:72': {'uc_pub_numbers_count': 59, 'uc_pub_numbers_sample': ['US-9061071-B2', 'US-5547866-A', 'CN-100339724-C', 'WO-2020055916-A9', 'ID-23426-A', 'AU-2010214112-B2', 'AU-2003297741-A1', 'CA-2550552-A1', 'US-2006292670-A1', 'US-2020025859-A1']}, 'var_functions.execute_python:74': {'status': 'processing', 'uc_count': 59}}

exec(code, env_args)
