code = """import json, re
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Step 1: Find UNIV CALIFORNIA patents and extract their publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents[:500]:  # Limit for testing
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        print('UC Patent:', patents_info[:200])
        # Extract publication number
        match = re.search(r'(?:pub\. number|publication number|pub\. no\.|with pub\. number|has pub\. number)\s+([A-Z]{2}-[^\s,\)]+)', patents_info)
        if match:
            pub_num = match.group(1)
            print('  Extracted pub number:', pub_num)
            uc_pub_numbers.add(pub_num)
        else:
            print('  NO PUB NUMBER FOUND')

print('\nUC Patents found:', len(uc_patents))
print('UC Pub numbers:', len(uc_pub_numbers))

# Step 2: Check some random citations to see patterns
print('\nChecking random citation patterns:')
sample_patents = all_patents[100:110]
for patent in sample_patents:
    citation_data = patent.get('citation', '[]')
    patents_info = patent.get('Patents_info', '')
    if citation_data != '[]':
        print('\nSample patent:', patents_info[:100])
        try:
            citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
            if citations and len(citations) > 0:
                print('Sample citations:')
                for i, citation in enumerate(citations[:3]):
                    print('  ', citation.get('publication_number', ''))
        except:
            pass
        break"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}}

exec(code, env_args)
