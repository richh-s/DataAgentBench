code = """import json
import re
from collections import defaultdict

# Load citation patents
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Total patents loaded:', len(patents))

# Find assignees and CPC codes for patents that cite UNIV CALIFORNIA
assignee_cpc_map = defaultdict(set)
assignee_counts = defaultdict(int)

# Sample the first 200 patents for assignee extraction
for i, patent in enumerate(patents[:200]):
    patents_info = patent.get('Patents_info', '')
    
    # Skip if this is a UNIV CALIFORNIA patent itself
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee using regex patterns
    assignee = None
    
    # Pattern 1: "is owned by"
    match = re.search(r'is (?:owned by|assigned to|belonging to|held by)\s+([^,.(]+)', patents_info, re.IGNORECASE)
    if match:
        assignee = match.group(1).strip()
    
    # Pattern 2: "holds the" at the beginning
    if not assignee:
        match = re.search(r'^([A-Z][A-Z\s&\-]{3,}?)\s+holds the', patents_info)
        if match:
            assignee = match.group(1).strip()
    
    # Pattern 3: Get everything before "holds the" or "is"
    if not assignee:
        parts = patents_info.split(' holds the')
        if len(parts) > 1 and len(parts[0].strip()) > 3:
            assignee = parts[0].strip()
        else:
            parts = patents_info.split(' is ')
            if len(parts) > 0 and len(parts[0].strip()) > 3:
                # Check if this looks like an assignee name (capitalized)
                candidate = parts[0].strip()
                if re.match(r'^[A-Z]', candidate):
                    assignee = candidate
    
    if assignee and 'UNIV CALIFORNIA' not in assignee.upper():
        # Extract CPC codes
        cpc_data = patent.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            for cpc in cpc_list:
                if isinstance(cpc, dict) and cpc.get('inventive', False):
                    code = cpc.get('code', '')
                    if code:
                        assignee_cpc_map[assignee].add(code)
        except:
            pass
        
        if assignee in assignee_cpc_map and len(assignee_cpc_map[assignee]) > 0:
            assignee_counts[assignee] += 1

# Filter to only assignees that have CPC codes
valid_assignees = {k: v for k, v in assignee_cpc_map.items() if len(v) > 0}

print('Valid assignees found:', len(valid_assignees))
print('Top assignees:')
for assignee in sorted(assignee_counts, key=assignee_counts.get, reverse=True)[:10]:
    if assignee in valid_assignees:
        cpc_count = len(valid_assignees[assignee])
        patent_count = assignee_counts[assignee]
        print('  ', assignee, ':', patent_count, 'patents,', cpc_count, 'CPC codes')

# Collect all CPC codes
all_cpc_codes = set()
for codes in valid_assignees.values():
    all_cpc_codes.update(codes)

print('\nTotal CPC codes to lookup:', len(all_cpc_codes))
print('Sample CPCs:', list(all_cpc_codes)[:10])

# Save results for next step
results = {
    'assignee_cpc_map': {k: list(v) for k, v in valid_assignees.items()},
    'assignee_counts': dict(assignee_counts)
}

with open('final_assignee_cpc.json', 'w') as f:
    json.dump(results, f, indent=2)

result_summary = {
    'assignees': len(valid_assignees),
    'cpc_codes': len(all_cpc_codes)
}

print('\n__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}}

exec(code, env_args)
