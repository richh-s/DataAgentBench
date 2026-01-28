code = """import json
import re
from collections import defaultdict

# Load the citation data
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Loaded', len(patents), 'patents')

# Look at the first few records more carefully
for i in range(5):
    if i < len(patents):
        print('\n--- Patent', i, '---')
        info = patents[i].get('Patents_info', 'N/A')
        print('Info:', info)

# Let's try a very simple approach - just extract words before certain patterns
assignee_counts = defaultdict(int)
assignee_cpcs = defaultdict(set)

# Process a larger sample
for patent in patents[:1000]:  # First 1000
    info = patent.get('Patents_info', '')
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in info.upper():
        continue
    
    # Very simple assignee extraction: get text before common verbs
    assignee = None
    
    # Try multiple patterns
    if ' holds the ' in info:
        assignee = info.split(' holds the ')[0].strip()
    elif ' is assigned to ' in info:
        assignee = info.split(' is assigned to ')[1].split(',')[0].strip()
    elif ' is owned by ' in info:
        assignee = info.split(' is owned by ')[1].split(',')[0].strip()
    
    # Only accept reasonable assignee names (not too short, starts with capital)
    if assignee and len(assignee) > 5 and assignee[0].isupper() and 'UNIV CALIFORNIA' not in assignee.upper():
        # Extract CPC codes
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            cpc_codes = []
            for cpc in cpc_list:
                if isinstance(cpc, dict):
                    code = cpc.get('code', '')
                    if code and cpc.get('inventive', False):
                        cpc_codes.append(code)
            
            if cpc_codes:  # Only count if there are CPC codes
                assignee_counts[assignee] += 1
                assignee_cpcs[assignee].update(cpc_codes)
        except:
            pass

print('\nUnique assignees with CPC codes:', len(assignee_counts))

# Sort by count
top_assignees = sorted(assignee_counts.items(), key=lambda x: x[1], reverse=True)
print('\nTop assignees:')
for assignee, count in top_assignees[:15]:
    cpc_list = list(assignee_cpcs[assignee])
    print(f'  {assignee}: {count} patents, {len(cpc_list)} CPC codes')

# Get all CPC codes
all_cpc_codes = set()
for codes in assignee_cpcs.values():
    all_cpc_codes.update(codes)

print('\nTotal CPC codes to look up:', len(all_cpc_codes))
print('Sample CPC codes:', list(all_cpc_codes)[:10])

# Save for next step
results = {
    'assignee_counts': dict(assignee_counts),
    'assignee_cpcs': {k: list(v) for k, v in assignee_cpcs.items()}
}

with open('top_citing_assignees.json', 'w') as f:
    json.dump(results, f, indent=2)

print('\n__RESULT__:')
print(json.dumps({'assignees': len(assignee_counts), 'cpc_codes': len(all_cpc_codes)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.execute_python:76': {'candidates': 0}}

exec(code, env_args)
