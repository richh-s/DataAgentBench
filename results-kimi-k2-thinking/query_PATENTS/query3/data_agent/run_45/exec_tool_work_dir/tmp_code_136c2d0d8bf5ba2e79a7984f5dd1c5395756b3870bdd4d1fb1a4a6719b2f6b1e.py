code = """import json
import re
import os
from collections import defaultdict

# Get UC patents from storage
uc_patents = []
for key, value in list(locals().items()):
    if 'query_db' in key and ('44' in key or '8' in key):
        if isinstance(value, list):
            uc_patents = value
            break
        elif isinstance(value, str) and os.path.exists(value):
            with open(value, 'r') as f:
                uc_patents = json.load(f)
                break

# Get all patents for citation analysis  
all_patents = []
for key, value in list(locals().items()):
    if 'query_db' in key and ('36' in key or '34' in key or '22' in key):
        if isinstance(value, list):
            all_patents.extend(value)
        elif isinstance(value, str) and os.path.exists(value):
            with open(value, 'r') as f:
                all_patents.extend(json.load(f))

print('UC patents:', len(uc_patents))
print('All patents:', len(all_patents))

# Extract UC publication numbers
uc_pub_numbers = set()
uc_cpc_lookup = {}

for patent in uc_patents:
    info = patent.get('Patents_info', '')
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes for this UC patent
        cpc_data = patent.get('cpc', '[]')
        if cpc_data and cpc_data != '[]':
            try:
                cpc_list = json.loads(cpc_data)
                uc_cpc_lookup[pub_num] = [item.get('code') for item in cpc_list if item.get('code')]
            except:
                uc_cpc_lookup[pub_num] = []

print('UC publication numbers:', len(uc_pub_numbers))
print('Sample:', list(uc_pub_numbers)[:3])

# Find citations from non-UC assignees
citations = []
assignee_info = defaultdict(lambda: defaultdict(set))

for patent in all_patents:
    cite_data = patent.get('citation', '[]')
    if not cite_data or cite_data == '[]':
        continue
    
    try:
        citations_list = json.loads(cite_data)
        for cite in citations_list:
            cited_pub = cite.get('publication_number')
            if cited_pub and cited_pub in uc_pub_numbers:
                # Extract assignee
                info = patent.get('Patents_info', '')
                assignee_match = re.match(r'^[A-Za-z\s\&\-]+', info)
                if assignee_match:
                    assignee = assignee_match.group(0).strip()
                    
                    # Exclude UNIV CALIFORNIA self-citations
                    if 'UNIV CALIFORNIA' not in assignee.upper():
                        citations.append({
                            'assignee': assignee,
                            'cited_uc_patent': cited_pub,
                            'cpc_data': patent.get('cpc', '[]')
                        })
                        
                        assignee_info[assignee]['uc_patents'].add(cited_pub)
                        
                        # Add CPC codes from citing patent
                        cpc_json = patent.get('cpc', '[]')
                        if cpc_json and cpc_json != '[]':
                            try:
                                cpc_list = json.loads(cpc_json)
                                for item in cpc_list:
                                    if item.get('code'):
                                        assignee_info[assignee]['cpc_codes'].add(item['code'])
                            except:
                                pass
    except:
        continue

print('Non-UC citations found:', len(citations))
print('Unique non-UC assignees:', len(assignee_info))

# Sort by number of citations
sorted_assignees = sorted(assignee_info.items(), key=lambda x: len(x[1]['uc_patents']), reverse=True)
print('\nTop assignees:')
for assignee, data in sorted_assignees[:10]:
    print(f'  {assignee}: {len(data["uc_patents"])} citations, {len(data["cpc_codes"])} CPCs')

print('\n__RESULT__:')
result = {
    'citations_count': len(citations),
    'assignees_count': len(assignee_info),
    'citing_assignees': list(assignee_info.keys())[:20]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
