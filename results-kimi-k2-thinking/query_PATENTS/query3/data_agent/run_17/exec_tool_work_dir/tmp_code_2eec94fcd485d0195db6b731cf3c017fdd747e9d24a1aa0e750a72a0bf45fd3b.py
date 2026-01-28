code = """import json, re
from collections import defaultdict

# Load the citation data
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Total patents loaded:', len(patents))

# Analyze patents to find those citing UNIV CALIFORNIA
assignee_counts = defaultdict(int)
assignee_cpcs = defaultdict(set)

for i, patent in enumerate(patents[:2000]):  # Process first 2000
    info = patent.get('Patents_info', '')
    
    # Skip patents assigned to UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in info.upper():
        continue
    
    # Extract assignee name
    assignee = None
    
    # Method 1: Split by common patterns
    if ' holds the ' in info:
        assignee = info.split(' holds the ')[0].strip()
    elif ' assigned to ' in info:
        parts = info.split(' assigned to ')
        if len(parts) > 1:
            assignee = parts[1].split(',')[0].strip()
    elif ' owned by ' in info:
        parts = info.split(' owned by ')
        if len(parts) > 1:
            assignee = parts[1].split(',')[0].strip()
    
    # Validate assignee
    if assignee and len(assignee) > 4 and not assignee.islower():
        # Extract CPC codes
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            cpc_codes = []
            for cpc in cpc_list:
                if isinstance(cpc, dict):
                    if cpc.get('inventive', False):
                        code = cpc.get('code', '')
                        if code:
                            cpc_codes.append(code)
            
            if cpc_codes:
                assignee_counts[assignee] += 1
                assignee_cpcs[assignee].update(cpc_codes)
        except:
            pass

# Show results
print('Assignees found:', len(assignee_counts))
print()
print('Top assignees:')
sorted_assignees = sorted(assignee_counts.items(), key=lambda x: x[1], reverse=True)
for assignee, count in sorted_assignees[:15]:
    cpc_list = list(assignee_cpcs[assignee])
    print(assignee + ': ' + str(count) + ' patents, ' + str(len(cpc_list)) + ' CPC codes')

# Get all CPC codes
all_cpc_codes = set()
for codes in assignee_cpcs.values():
    all_cpc_codes.update(codes)

print()
print('Total CPC codes to lookup:', len(all_cpc_codes))
print('Sample CPCs:', list(all_cpc_codes)[:10])

# Save data
with open('assignee_cpc_data.json', 'w') as f:
    json.dump({
        'assignee_counts': dict(assignee_counts),
        'assignee_cpcs': {k: list(v) for k, v in assignee_cpcs.items()}
    }, f, indent=2)

output = {'assignees': len(assignee_counts), 'cpc_codes': len(all_cpc_codes)}
print('\n__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.execute_python:76': {'candidates': 0}}

exec(code, env_args)
