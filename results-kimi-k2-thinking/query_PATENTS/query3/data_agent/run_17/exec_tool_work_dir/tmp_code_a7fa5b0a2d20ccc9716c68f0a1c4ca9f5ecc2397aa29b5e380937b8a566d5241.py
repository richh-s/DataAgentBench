code = """import json, re
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded: %d' % len(all_patents))

# Step 1: Find UNIV CALIFORNIA patents and extract their publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents[:2000]:  # Limit for testing first
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        # Try multiple patterns to extract publication number
        patterns = [
            r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)',
            r'publication number\s+([A-Z]{2}-[^\s,\)]+)',
            r'pub\. no\.\s+([A-Z]{2}-[^\s,\)]+)',
            r'with pub\. number\s+([A-Z]{2}-[^\s,\)]+)',
            r'has pub\. number\s+([A-Z]{2}-[^\s,\)]+)'
        ]
        for pattern in patterns:
            match = re.search(pattern, patents_info, re.IGNORECASE)
            if match:
                pub_num = match.group(1)
                uc_pub_numbers.add(pub_num)
                break

print('UC Patents found: %d' % len(uc_patents))
print('UC Pub numbers: %d' % len(uc_pub_numbers))
print('Sample UC pub numbers: %s' % list(uc_pub_numbers)[:10])

# Step 2: Sample some citations to understand the format
print('\n' + '='*50)
print('Sampling citation formats:')
for i, patent in enumerate(all_patents[:20]):
    citation_data = patent.get('citation', '')
    patents_info = patent.get('Patents_info', '')
    if citation_data and citation_data != '[]':
        try:
            citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
            if citations and len(citations) > 0:
                print('\nPatent %d: %s' % (i, patents_info[:100]))
                print('Citations:')
                for cit in citations[:3]:
                    pub_num = cit.get('publication_number', 'N/A')
                    print('  - %s' % pub_num)
        except Exception as e:
            continue

result_summary = {
    'uc_patents': len(uc_patents),
    'uc_pub_numbers': len(uc_pub_numbers),
    'sample_uc_pub_numbers': list(uc_pub_numbers)[:10]
}

print('\n' + '='*50)
print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
