code = """import json, re
from collections import defaultdict

# Load citation data
citation_file = locals()['var_functions.query_db:48']
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Loaded', len(patents), 'patents')

# Analyze patent info to extract assignees
assignees = defaultdict(int)
for p in patents[:200]:
    info = p.get('Patents_info', '')
    # Simple pattern: look for capitalized words at start
    parts = info.split(' holds the')
    if len(parts) > 1:
        assignee = parts[0].strip()
        assignees[assignee] += 1
    else:
        parts = info.split(' is assigned to')
        if len(parts) > 1:
            assignee = parts[1].split(',')[0].strip()
            assignees[assignee] += 1

print('Found assignees:', len(assignees))
for a, c in list(assignees.items())[:10]:
    print(a, ':', c)

# Collect CPC codes
all_cpc = set()
for p in patents[:200]:
    if 'UNIV CALIFORNIA' in p.get('Patents_info', '').upper():
        continue
    cpc_data = p.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        for cpc in cpc_list:
            if cpc.get('inventive', False):
                all_cpc.add(cpc.get('code', ''))
    except:
        pass

print('CPC codes found:', len(all_cpc))
print('Sample CPCs:', list(all_cpc)[:10])

result = {'assignees': len(assignees), 'cpc_codes': len(all_cpc)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}}

exec(code, env_args)
