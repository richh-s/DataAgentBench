code = """import json
import re
from collections import defaultdict

# Load patents whose citations mention UNIV CALIFORNIA
citation_patents_path = locals()['var_functions.query_db:48']
with open(citation_patents_path, 'r') as f:
    citation_patents = json.load(f)

print('Loaded ' + str(len(citation_patents)) + ' patents whose citations mention UNIV CALIFORNIA')

# Process these patents to extract assignees and CPC codes
assignee_cpc_codes = defaultdict(set)
assignee_citation_count = defaultdict(int)

for patent in citation_patents[:1000]:
    patents_info = patent.get('Patents_info', '')
    
    # Skip patents assigned to UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee name
    assignee = 'Unknown'
    
    # Pattern 1: "is owned by"
    match = re.search(r'is (?:owned by|assigned to|belonging to)\s+([^,.(]+)', patents_info, re.IGNORECASE)
    if match:
        assignee = match.group(1).strip()
    
    # Pattern 2: "holds the"
    if assignee == 'Unknown':
        match = re.search(r'([A-Z][A-Z\s&\-]+?)\s+holds the', patents_info)
        if match:
            assignee = match.group(1).strip()
    
    # Pattern 3: Starting with company name
    if assignee == 'Unknown':
        match = re.search(r'^([A-Z]{2,}(?:\s+[A-Z]{2,})*)\s+', patents_info)
        if match:
            assignee = match.group(1).strip()
    
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Extract CPC codes (primary/inventive ones)
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        for cpc in cpc_list:
            if isinstance(cpc, dict) and cpc.get('inventive', False):
                code = cpc.get('code', '')
                if code:
                    assignee_cpc_codes[assignee].add(code)
    except:
        continue
    
    assignee_citation_count[assignee] += 1

print('Found ' + str(len(assignee_cpc_codes)) + ' unique assignees')
print('Top 10 assignees:')
for assignee, count in sorted(assignee_citation_count.items(), key=lambda x: x[1], reverse=True)[:10]:
    print('  ' + assignee + ': ' + str(count) + ' patents, ' + str(len(assignee_cpc_codes[assignee])) + ' CPC codes')

# Save results
results = {
    'assignee_cpc_map': {k: list(v) for k, v in assignee_cpc_codes.items()},
    'assignee_counts': dict(assignee_citation_count)
}

with open('assignee_cpc_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

print('__RESULT__:')
print(json.dumps({'assignees_found': len(assignee_cpc_codes)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}}

exec(code, env_args)
