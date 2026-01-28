code = """import json
import re

# Load patents whose citations mention UNIV CALIFORNIA
citation_patents_path = locals()['var_functions.query_db:48']
with open(citation_patents_path, 'r') as f:
    citation_patents = json.load(f)

print('Total patents in citation sample: ' + str(len(citation_patents)))

# Debug: Show first few patents and their Patents_info
print('\nFirst 5 patents:')
for i, patent in enumerate(citation_patents[:5]):
    print('\nPatent ' + str(i) + ':')
    print('Patents_info: ' + patent.get('Patents_info', 'N/A')[:200])
    
    # Check if it contains UNIV CALIFORNIA in Patents_info
    has_uc_info = 'UNIV CALIFORNIA' in patent.get('Patents_info', '').upper()
    print('Has UNIV CALIFORNIA in Patents_info: ' + str(has_uc_info))
    
    # Show citation
    citation_data = patent.get('citation', '')
    print('Citation length: ' + str(len(citation_data)))
    if len(citation_data) > 100:
        print('Citation preview: ' + citation_data[:100] + '...')

# Count how many are actually UNIV CALIFORNIA patents
uc_patents_in_sample = []
non_uc_patents = []

for patent in citation_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents_in_sample.append(patent)
    else:
        non_uc_patents.append(patent)

print('\nUNIV CALIFORNIA patents in sample: ' + str(len(uc_patents_in_sample)))
print('Non-UC patents in sample: ' + str(len(non_uc_patents)))

if non_uc_patents:
    print('\nFirst non-UC patent:')
    print('Patents_info: ' + non_uc_patents[0].get('Patents_info', '')[:300])
    
    # Try to extract assignee
    patents_info = non_uc_patents[0].get('Patents_info', '')
    
    # Test different patterns
    patterns = [
        r'is (?:owned by|assigned to|belonging to)\s+([^,.(]+)',
        r'([A-Z][A-Z\s&\-]{3,}?)\s+(?:holds the|is|has)',
        r'^([A-Z]{2,}(?:\s+[A-Z&]{2,})+)\s+'
    ]
    
    print('\nTesting assignee extraction patterns:')
    for j, pattern in enumerate(patterns):
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            print('Pattern ' + str(j) + ': ' + match.group(1).strip())
        else:
            print('Pattern ' + str(j) + ': No match')

result = {
    'total_patents': len(citation_patents),
    'uc_patents_in_citation_sample': len(uc_patents_in_sample),
    'non_uc_patents': len(non_uc_patents)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'status': 'completed', 'citing_assignees': 0, 'total_cpc_codes': 0}, 'var_functions.execute_python:66': {'assignees_found': 0}}

exec(code, env_args)
