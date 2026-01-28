code = """import json
import re
from collections import defaultdict

# Step 1: Load all patents data
print('Loading all patents data...')
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded: %s' % len(all_patents))

# Step 2: Find UNIV CALIFORNIA patents and extract publication numbers
uc_pub_numbers = set()
uc_patents = []

# Test with a sample first
print('\n=== Testing with first 100 patents ===')
for i, patent in enumerate(all_patents[:100]):
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        print('Found UC patent at index %s: %s' % (i, patents_info[:200]))
        
        # Extract publication number
        patterns = [
            r'pub\. number\s+([A-Z]{2}-[^\s,\)]+)',
            r'publication number\s+([A-Z]{2}-[^\s,\)]+)',
            r'pub\. no\.\s+([A-Z]{2}-[^\s,\)]+)',
            r'with pub\. number\s+([A-Z]{2}-[^\s,\)]+)',
            r'has pub\. number\s+([A-Z]{2}-[^\s,\)]+)'
        ]
        
        pub_num = None
        for pattern in patterns:
            match = re.search(pattern, patents_info, re.IGNORECASE)
            if match:
                pub_num = match.group(1)
                print('  Extracted pub number: %s' % pub_num)
                uc_pub_numbers.add(pub_num)
                break
        
        if not pub_num:
            print('  NO PUB NUMBER FOUND')

print('=== End test ===')
print('UC Patents in sample: %s' % len(uc_patents))
print('UC Pub numbers found: %s' % len(uc_pub_numbers))

# Now check for citations in a larger sample
print('\n=== Testing citations in larger sample ===')
uc_pub_sample = list(uc_pub_numbers)[:5] if uc_pub_numbers else ['US-11421276-B2']

found_citations = 0
test_patents = all_patents[:500]

for i, patent in enumerate(test_patents):
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue  # Skip UC patents themselves
    
    citation_data = patent.get('citation', '[]')
    if citation_data == '[]' or not citation_data:
        continue
    
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num in uc_pub_sample:
                found_citations += 1
                print('Found citation at index %s: %s' % (i, patents_info[:100]))
                print('  Cites: %s' % pub_num)
                if found_citations >= 3:
                    break
        if found_citations >= 3:
            break
    except:
        continue

print('Found %s citations in test sample' % found_citations)

result = {'uc_patents_sample': len(uc_patents), 'uc_pub_numbers': len(uc_pub_numbers), 'citations_found': found_citations}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
