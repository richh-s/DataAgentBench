code = """import json
import re
import os
from collections import defaultdict

# Load UC patents data - handle both direct data and file paths
uc_patents = []

# Check all available variables
for var_name, var_value in list(locals().items()):
    if 'query_db' in var_name and ('58' in var_name or '44' in var_name or '8' in var_name):
        if isinstance(var_value, str) and os.path.exists(var_value):
            # It's a file path
            with open(var_value, 'r') as f:
                uc_patents = json.load(f)
        elif isinstance(var_value, list):
            # It's direct data
            uc_patents = var_value
        break

print('UC patents loaded:', len(uc_patents))
if uc_patents:
    print('Sample:', uc_patents[0]['Patents_info'][:50])

# Extract UC publication numbers
uc_pub_numbers = set()
uc_cpc_map = {}

for patent in uc_patents:
    info = patent.get('Patents_info', '')
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.add(pub_num)
        
        # Store CPC codes for this UC patent
        cpc_str = patent.get('cpc', '[]')
        if cpc_str and cpc_str != '[]':
            try:
                cpc_list = json.loads(cpc_str)
                uc_cpc_map[pub_num] = [item.get('code') for item in cpc_list if item.get('code')]
            except:
                uc_cpc_map[pub_num] = []

print('UC publication numbers count:', len(uc_pub_numbers))

# Load all patents to find citations
all_patents = []

# Check available variables for patent data
for var_name, var_value in list(locals().items()):
    if 'query_db' in var_name and ('60' in var_name or '52' in var_name):
        continue  # Skip count queries
    if 'query_db' in var_name:
        if isinstance(var_value, str) and os.path.exists(var_value):
            with open(var_value, 'r') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    if 'Patents_info' in data[0]:
                        all_patents.extend(data)
        elif isinstance(var_value, list):
            if len(var_value) > 0 and isinstance(var_value[0], dict) and 'Patents_info' in var_value[0]:
                all_patents.extend(var_value)

print('Total patent records to scan:', len(all_patents))

# Find citations from non-UC assignees to UC patents
citations_found = []
assignee_data = defaultdict(lambda: {'cited_uc': set(), 'cpc_codes': set()})

for patent in all_patents:
    citation_str = patent.get('citation', '[]')
    if not citation_str or citation_str == '[]':
        continue
    
    try:
        citation_list = json.loads(citation_str)
        for citation in citation_list:
            cited_pub = citation.get('publication_number', '')
            if cited_pub and cited_pub in uc_pub_numbers:
                # This patent cites a UC patent - get assignee
                info = patent.get('Patents_info', '')
                # Simple assignee extraction - improve later
                assignee_match = re.match(r'^([A-Za-z\&\s\-\.]+)', info.strip())
                if assignee_match:
                    assignee = assignee_match.group(1).strip()
                    # Check if not UNIV CALIFORNIA
                    if 'UNIV CALIFORNIA' not in assignee.upper():
                        citations_found.append({
                            'assignee': assignee,
                            'cited_uc': cited_pub
                        })
                        assignee_data[assignee]['cited_uc'].add(cited_pub)
                        
                        # Get CPC codes from citing patent
                        cpc_str = patent.get('cpc', '[]')
                        if cpc_str and cpc_str != '[]':
                            try:
                                cpc_list = json.loads(cpc_str)
                                for cpc_item in cpc_list:
                                    code = cpc_item.get('code')
                                    if code:
                                        assignee_data[assignee]['cpc_codes'].add(code)
                            except:
                                pass
    except:
        continue

print('\\nCitations found:', len(citations_found))
print('Unique non-UC assignees:', len(assignee_data))

# Rank assignees by citation count
ranked_assignees = sorted(assignee_data.items(), key=lambda x: len(x[1]['cited_uc']), reverse=True)

print('\\nTop 10 assignees citing UC patents:')
for assignee, data in ranked_assignees[:10]:
    print(f'  {assignee}: {len(data["cited_uc"])} citations')

print('\\n__RESULT__:')
print(json.dumps({
    'uc_patents': len(uc_patents),
    'uc_pub_numbers': len(uc_pub_numbers),
    'citations_found': len(citations_found),
    'unique_assignees': len(assignee_data),
    'top_assignees': [(a, len(d['cited_uc']), len(d['cpc_codes'])) for a, d in ranked_assignees[:10]]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
