code = """import json
import re
import os
from collections import defaultdict

# Access storage variables
uc_patents = []
all_patents = []

# Try to find UC patents
for key, val in list(locals().items()):
    if 'query_db' in key and ('44' in key or '8' in key or '14' in key):
        if isinstance(val, list):
            uc_patents = val
        elif isinstance(val, str) and os.path.exists(val):
            uc_patents = json.load(open(val))

# Try to find all patents
for key, val in list(locals().items()):
    if 'query_db' in key and ('36' in key or '34' in key or '22' in key):
        if isinstance(val, list):
            all_patents.extend(val)
        elif isinstance(val, str) and os.path.exists(val):
            all_patents.extend(json.load(open(val)))

print('UC patents count:', len(uc_patents))
print('All patents count:', len(all_patents))

# Extract UC publication numbers and CPC codes
uc_pub_numbers = set()
uc_cpc_data = {}

for p in uc_patents:
    info = p.get('Patents_info', '')
    m = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if m:
        pub_num = m.group(1).strip()
        uc_pub_numbers.add(pub_num)
        
        cpc_json = p.get('cpc', '[]')
        if cpc_json and cpc_json != '[]':
            try:
                cpc_list = json.loads(cpc_json)
                uc_cpc_data[pub_num] = [item.get('code') for item in cpc_list if item.get('code')]
            except:
                uc_cpc_data[pub_num] = []

print('UC publication numbers:', len(uc_pub_numbers))

# Find non-UC citations
citations = []
assignee_data = defaultdict(lambda: defaultdict(set))

for p in all_patents:
    cite_json = p.get('citation', '[]')
    if not cite_json or cite_json == '[]':
        continue
    
    try:
        for cite in json.loads(cite_json):
            cited_pub = cite.get('publication_number')
            if cited_pub and cited_pub in uc_pub_numbers:
                info = p.get('Patents_info', '')
                m = re.match(r'^[A-Za-z\s\&\-\.]+', info)
                if m:
                    assignee = m.group(0).strip()
                    if 'UNIV CALIFORNIA' not in assignee.upper():
                        citations.append({'assignee': assignee, 'cited': cited_pub})
                        assignee_data[assignee]['cited'].add(cited_pub)
                        
                        cpc_json = p.get('cpc', '[]')
                        if cpc_json and cpc_json != '[]':
                            for item in json.loads(cpc_json):
                                if item.get('code'):
                                    assignee_data[assignee]['cpc'].add(item['code'])
    except:
        pass

print('Non-UC citations found:', len(citations))
print('Unique non-UC assignees:', len(assignee_data))

# Rank assignees by citation count
sorted_assignees = sorted(assignee_data.items(), key=lambda x: len(x[1]['cited']), reverse=True)

print('\nTop assignees citing UC patents:')
for assignee, data in sorted_assignees[:15]:
    print(f'  {assignee}: {len(data["cited"])} citations, {len(data["cpc"])} CPC codes')

print('\\n__RESULT__:')
result = {
    'citations': len(citations),
    'assignees': len(assignee_data),
    'top_assignees': [(a, len(d['cited']), len(d['cpc'])) for a, d in sorted_assignees[:10]]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
