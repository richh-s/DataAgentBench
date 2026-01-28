code = """import json
import re
from collections import defaultdict

# Get UNIV CALIFORNIA patents from storage
uc_patents = locals()['var_functions.query_db:58']
print('UC patents loaded:', len(uc_patents))

# Extract UC publication numbers
uc_pub_numbers = set()
uc_cpc_lookup = {}

for patent in uc_patents:
    info = patent.get('Patents_info', '')
    # Extract publication number
    match = re.search(r'pub\\.?\\s*number\\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes for this UC patent
        cpc_str = patent.get('cpc', '[]')
        if cpc_str and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                codes = [item.get('code') for item in cpc_list if item.get('code')]
                uc_cpc_lookup[pub_num] = codes
            except:
                uc_cpc_lookup[pub_num] = []

print('UC publication numbers:', len(uc_pub_numbers))

# Get all available patent records
all_patents = []
for key, val in locals().items():
    if 'query_db' in key and '58' not in key:
        if isinstance(val, list):
            all_patents.extend(val)

print('All patents to scan:', len(all_patents))

# Find citations
uc_citations = []
assignee_data = defaultdict(lambda: {'cited': set(), 'cpc_codes': set()})

for patent in all_patents:
    citation_str = patent.get('citation', '[]')
    if citation_str and citation_str != '[]':
        try:
            for cite in json.loads(citation_str):
                cited_pub = cite.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    info = patent.get('Patents_info', '')
                    assignee_match = re.match(r'^([A-Za-z\\&\\s\\-\\.]+)', info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                        if 'UNIV CALIFORNIA' not in assignee.upper():
                            uc_citations.append({'assignee': assignee, 'cited': cited_pub})
                            assignee_data[assignee]['cited'].add(cited_pub)
                            
                            cpc_str = patent.get('cpc', '[]')
                            if cpc_str and cpc_str != '[]':
                                for cpc in json.loads(cpc_str):
                                    if cpc.get('code'):
                                        assignee_data[assignee]['cpc_codes'].add(cpc['code'])
        except:
            continue

print('Citations found:', len(uc_citations))
print('Unique assignees:', len(assignee_data))

# Rank assignees
ranked = sorted(assignee_data.items(), key=lambda x: len(x[1]['cited']), reverse=True)

print('\\nTop assignees:')
for assignee, data in ranked[:10]:
    print(f'  {assignee}: {len(data["cited"])} citations, {len(data["cpc_codes"])} CPCs')

print('\\n__RESULT__:')
result = {
    'citations': len(uc_citations),
    'assignees': len(assignee_data),
    'top_assignees': [(a, len(d['cited']), len(d['cpc_codes'])) for a, d in ranked[:10]]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:70': {'uc_patents': 169, 'uc_pub_numbers': 59, 'citations_found': 1, 'unique_assignees': 1, 'top_assignees': [['The US patent application', 1, 17]]}}

exec(code, env_args)
