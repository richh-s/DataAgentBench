code = """import json
import re
from collections import defaultdict

# Load data
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Total patents in citation sample:', len(patents))

# We'll process this step by step
assignee_cpc_map = defaultdict(set)
assignee_citation_count = defaultdict(int)

# Process the patents
for patent in patents:
    patents_info = patent.get('Patents_info', '')
    
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee - try multiple patterns
    assignee = None
    patterns = [
        r'is (?:owned by|assigned to|belonging to)\s+([^,.(]+)',
        r'^([A-Z][A-Z\s&\-]{3,}?)\s+holds the',
        r'^([A-Z]{2,}(?:\s+[A-Z&]{2,})+)\s+is'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            assignee = match.group(1).strip()
            break
    
    # If no match, use simple split
    if not assignee and ' holds the ' in patents_info:
        assignee = patents_info.split(' holds the ')[0].strip()
    
    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Extract CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        cpc_codes = []
        for cpc in cpc_list:
            if isinstance(cpc, dict) and cpc.get('inventive', False):
                code = cpc.get('code', '')
                if code:
                    cpc_codes.append(code)
        
        if cpc_codes:
            assignee_cpc_map[assignee].update(cpc_codes)
            assignee_citation_count[assignee] += 1
    except:
        pass

# Get all unique CPC codes
all_cpc_codes = set()
for codes in assignee_cpc_map.values():
    all_cpc_codes.update(codes)

print('Assignees found: ' + str(len(assignee_cpc_map)))
print('CPC codes to lookup: ' + str(len(all_cpc_codes)))
print('Sample CPCs: ' + str(list(all_cpc_codes)[:10]))

# Save for next step
output = {
    'assignee_cpc_map': {k: list(v) for k, v in assignee_cpc_map.items()},
    'assignee_counts': dict(assignee_citation_count),
    'total_cpc_codes': len(all_cpc_codes)
}

with open('assignee_cpc_final.json', 'w') as f:
    json.dump(output, f, indent=2)

result = {'assignees': len(assignee_cpc_map), 'cpc_codes': len(all_cpc_codes), 'sample_cpc': list(all_cpc_codes)[:10]}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}, 'var_functions.execute_python:76': {'candidates': 0}}

exec(code, env_args)
