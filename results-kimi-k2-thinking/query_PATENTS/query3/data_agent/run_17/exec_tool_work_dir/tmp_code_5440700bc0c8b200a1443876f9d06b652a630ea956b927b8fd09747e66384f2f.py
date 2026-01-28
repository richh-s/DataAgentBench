code = """import json
import re
from collections import defaultdict

# Get the file path
citation_file = locals()['var_functions.query_db:48']

# Load the patents data
with open(citation_file, 'r') as f:
    patents = json.load(f)

print('Total patents processed:', len(patents))

# Extract assignees and CPC codes
assignee_data = defaultdict(lambda: defaultdict(set))

# Process patents
for patent in patents[:500]:  # Limit for speed
    info = patent.get('Patents_info', '')
    cpc_data = patent.get('cpc', '[]')
    
    # Skip UNIV CALIFORNIA patents
    if 'UNIV CALIFORNIA' in info.upper():
        continue
    
    # Extract assignee
    assignee = None
    patterns = [
        r'is (?:owned by|assigned to|belonging to)\s+([^,.]+)',
        r'^([A-Z][A-Z\s&\-]{3,})\s+holds',
    ]
    
    for pat in patterns:
        m = re.search(pat, info, re.I)
        if m:
            assignee = m.group(1).strip()
            break
    
    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Extract CPC codes
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        for cpc in cpc_list:
            if isinstance(cpc, dict) and cpc.get('inventive', False):
                code = cpc.get('code', '')
                if code:
                    assignee_data[assignee]['cpc_codes'].add(code)
                    assignee_data[assignee]['patent_count'] += 1
    except:
        pass

# Filter assignees with CPC codes
valid_assignees = {k: v for k, v in assignee_data.items() if v['cpc_codes']}

print('Valid assignees found:', len(valid_assignees))

# Prepare results
results = []
for assignee, data in valid_assignees.items():
    results.append({
        'assignee': assignee,
        'cpc_codes': list(data['cpc_codes']),
        'patent_count': data['patent_count']
    })

# Sort by patent count
results.sort(key=lambda x: x['patent_count'], reverse=True)

print('Top results:')
for r in results[:10]:
    print('  ' + r['assignee'] + ': ' + str(r['patent_count']) + ' patents, ' + str(len(r['cpc_codes'])) + ' CPCs')

# Save
with open('candidate_assignees.json', 'w') as f:
    json.dump(results, f, indent=2)

print('__RESULT__:')
print(json.dumps({'candidates': len(results)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}, 'var_functions.execute_python:72': {'assignees': 0, 'cpc_codes': 0}}

exec(code, env_args)
