code = """import json
import re
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded:', len(all_patents))

# Find UNIV CALIFORNIA patents and extract publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents[:1000]:  # Process first 1000 for speed
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        # Extract publication number
        patterns = [r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)', 
                   r'publication number\s+([A-Z]{2}-[^\s,\)]+)',
                   r'with pub\. number\s+([A-Z]{2}-[^\s,\)]+)',
                   r'has pub\. number\s+([A-Z]{2}-[^\s,\)]+)']
        
        for pattern in patterns:
            match = re.search(pattern, patents_info, re.IGNORECASE)
            if match:
                uc_pub_numbers.add(match.group(1))
                break

print('UC patents found in sample:', len(uc_patents))
print('UC publication numbers:', len(uc_pub_numbers))
print('Sample UC pubs:', list(uc_pub_numbers)[:5])

# Find patents that cite UNIV CALIFORNIA patents
citing_assignees = defaultdict(set)
citation_count = 0

for patent in all_patents[:5000]:  # Check first 5000 patents
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    citation_data = patent.get('citation', '[]')
    if citation_data == '[]':
        continue
    
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        cites_uc = False
        for citation in citations:
            if citation.get('publication_number', '') in uc_pub_numbers:
                cites_uc = True
                citation_count += 1
                break
        
        if cites_uc:
            # Extract assignee
            match = re.search(r'is (?:owned by|assigned to|belonging to)\s+([^,.]+)', patents_info)
            if match:
                assignee = match.group(1).strip()
                if 'UNIV CALIFORNIA' not in assignee.upper():
                    # Get CPC codes
                    cpc_data = patent.get('cpc', '[]')
                    cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                    for cpc in cpc_list:
                        if cpc.get('inventive', False):
                            code = cpc.get('code', '')
                            if code:
                                citing_assignees[assignee].add(code)
    except:
        continue

print('Citations to UC found:', citation_count)
print('Unique citing assignees:', len(citing_assignees))
print('Sample assignees:')
for i, (assignee, cpcs) in enumerate(list(citing_assignees.items())[:5]):
    print('  ' + assignee + ': ' + str(list(cpcs)[:3]))

# Prepare result
result = {'citation_count': citation_count, 
          'assignee_count': len(citing_assignees),
          'assignees': dict(list(citing_assignees.items())[:10])}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
