code = """import json
import re
from collections import defaultdict

# Load data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Loaded ' + str(len(all_patents)) + ' patents')

# Find UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        # Extract pub number
        match = re.search(r'pub\. number\s+([A-Z]{2}-[^\s,]+)', patents_info)
        if match:
            uc_pub_numbers.add(match.group(1))

print('Found ' + str(len(uc_pub_numbers)) + ' UC pub numbers')

# Find citing patents and extract assignees/CPCs
assignee_cpc = defaultdict(set)
for patent in all_patents[:10000]:  # Process subset for speed
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Check citations
    citation_data = patent.get('citation', '[]')
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        cites_uc = False
        for citation in citations:
            if citation.get('publication_number', '') in uc_pub_numbers:
                cites_uc = True
                break
        
        if cites_uc:
            # Get assignee
            assignee_match = re.search(r'([A-Z][A-Z\s&]+?)\s+(?:holds|is|has)', patents_info)
            if assignee_match:
                assignee = assignee_match.group(1).strip()
            else:
                assignee = 'Unknown'
            
            if 'UNIV CALIFORNIA' not in assignee.upper():
                # Get CPC codes
                cpc_data = patent.get('cpc', '[]')
                cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                for cpc in cpc_list:
                    if isinstance(cpc, dict) and cpc.get('inventive', False):
                        code = cpc.get('code', '')
                        if code:
                            assignee_cpc[assignee].add(code)
    except:
        continue

print('Assignees found: ' + str(len(assignee_cpc)))
print('Sample: ' + str(list(assignee_cpc.keys())[:5]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}}

exec(code, env_args)
