code = """import json
import re
from collections import defaultdict

# Access UC patents directly from storage variables
uc_patents = var_functions.query_db_58

print('UC patents loaded:', len(uc_patents))
print('Sample:', uc_patents[0]['Patents_info'][:100] if uc_patents else 'None')

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1).strip())

print('UC publication numbers:', len(uc_pub_numbers))
print('Sample:', list(uc_pub_numbers)[:5])

# Now look for citations - we need a broader search
# Let's check available storage for all patents
available_keys = [k for k in locals().keys() if 'var_' in k]
print('\nAvailable storage keys:', len(available_keys))

# Find all patent records
all_patents = []
for key in available_keys:
    try:
        data = locals()[key]
        if isinstance(data, list) and len(data) > 0:
            # Check if this looks like patent data
            if isinstance(data[0], dict) and 'Patents_info' in data[0]:
                all_patents.extend(data)
    except:
        continue

print('Total patent records found:', len(all_patents))

# Find citations to UC patents
citations = []
citing_assignees = defaultdict(lambda: {'cited_uc': set(), 'cpc_codes': set()})

for patent in all_patents[:10000]:  # Process subset first
    citation_data = patent.get('citation', '[]')
    if citation_data and citation_data != '[]':
        try:
            citations_list = json.loads(citation_data)
            for cite in citations_list:
                cited_pub = cite.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # Extract assignee
                    info = patent['Patents_info']
                    assignee_match = re.match(r'^[A-Za-z\&\s\-\.]+', info)
                    if assignee_match:
                        assignee = assignee_match.group(0).strip()
                        if 'UNIV CALIFORNIA' not in assignee.upper():
                            citations.append({
                                'assignee': assignee,
                                'cited_uc': cited_pub
                            })
                            citing_assignees[assignee]['cited_uc'].add(cited_pub)
                            
                            # Get CPC codes from citing patent
                            cpc_data = patent.get('cpc', '[]')
                            if cpc_data and cpc_data != '[]':
                                try:
                                    cpc_list = json.loads(cpc_data)
                                    for cpc in cpc_list:
                                        if cpc.get('code'):
                                            citing_assignees[assignee]['cpc_codes'].add(cpc['code'])
                                except:
                                    pass
        except:
            continue

print('\\nProcessing complete:')
print('Total citations found:', len(citations))
print('Unique citing assignees:', len(citing_assignees))

# Rank assignees
sorted_assignees = sorted(citing_assignees.items(), key=lambda x: len(x[1]['cited_uc']), reverse=True)
print('\\nTop assignees:')
for assignee, data in sorted_assignees[:10]:
    print(f'  {assignee}: {len(data["cited_uc"])} citations, {len(data["cpc_codes"])} CPC codes')

print('\\n__RESULT__:')
print(json.dumps({
    'citations': len(citations),
    'assignees': len(citing_assignees),
    'top_ten': [(a, len(d['cited_uc'])) for a, d in sorted_assignees[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
