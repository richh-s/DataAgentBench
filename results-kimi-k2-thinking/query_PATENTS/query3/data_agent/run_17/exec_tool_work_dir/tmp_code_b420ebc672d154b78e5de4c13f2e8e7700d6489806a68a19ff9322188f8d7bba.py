code = """import json, re
from collections import defaultdict

# Load citation data
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Total patents:', len(patents))

# Extract assignees and CPC codes
assignee_counts = defaultdict(int)
assignee_cpcs = defaultdict(set)
processed = 0

for patent in patents:
    info = patent.get('Patents_info', 'N/A')
    cpc_data = patent.get('cpc', '[]')
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in info.upper():
        continue
    
    # Extract assignee
    assignee = None
    if ' holds' in info:
        assignee = info.split(' holds')[0].strip().split(',')[0]
    elif ' assigned to ' in info:
        assignee = info.split(' assigned to ')[1].split(',')[0].strip()
    elif ' owned by ' in info:
        assignee = info.split(' owned by ')[1].split(',')[0].strip()
    
    if not assignee or len(assignee) < 5 or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        primary_cpcs = []
        for cpc in cpc_list:
            if isinstance(cpc, dict):
                if cpc.get('inventive', False):
                    code = cpc.get('code', '')
                    if code:
                        primary_cpcs.append(code)
        
        if primary_cpcs:
            assignee_cpcs[assignee].update(primary_cpcs)
            assignee_counts[assignee] += 1
            processed += 1
    except:
        pass

print('Processed:', processed)
print('Unique assignees:', len(assignee_counts))

# Get all CPC codes
all_codes = set()
for codes in assignee_cpcs.values():
    all_codes.update(codes)

print('Total CPC codes:', len(all_codes))

# Top assignees
print('\nTop assignees:')
for assignee, count in sorted(assignee_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    if assignee in assignee_cpcs:
        print(assignee, ':', count, 'patents,', len(assignee_cpcs[assignee]), 'CPC codes')

result = {'assignees': len(assignee_counts), 'cpc_codes': len(all_codes)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.execute_python:76': {'candidates': 0}}

exec(code, env_args)
