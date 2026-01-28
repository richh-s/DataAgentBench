code = """import json
import re
from collections import defaultdict

# Access UC patents data
uc_patents = var_functions.query_db_58

print('UC patents loaded:', len(uc_patents))

# Extract UC publication numbers more carefully
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    # Look for publication number patterns more explicitly
    patterns = [
        r'pub\. number ([A-Z0-9-]+)',
        r'pub\. number ([^\.]+)',
        r'has publication number ([A-Z0-9-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, info)
        if match:
            pub_num = match.group(1).strip()
            if '-' in pub_num:  # Valid pub number format
                uc_pub_numbers.add(pub_num)
                break

print('UC publication numbers extracted:', len(uc_pub_numbers))
print('Sample:', list(uc_pub_numbers)[:5])

# Get all available patent records from storage
all_patent_vars = []
for key in locals().keys():
    if 'var_functions.query_db' in key and ('58' not in key):
        all_patent_vars.append(locals()[key])

print('Patent data sources found:', len(all_patent_vars))

# Combine all patent records
all_patents = []
for var in all_patent_vars:
    if isinstance(var, list):
        all_patents.extend(var)

print('Total patents to scan:', len(all_patents))

# Find citations to UC patents
uc_citations = []
assignee_citations = defaultdict(lambda: {'count': 0, 'cpc_codes': set(), 'uc_patents': set()})

for i, patent in enumerate(all_patents):
    if i % 1000 == 0 and i > 0:
        print(f'Scanned {i} patents...')
    
    citation_str = patent.get('citation', '[]')
    if not citation_str or citation_str == '[]':
        continue
    
    try:
        citations_list = json.loads(citation_str)
        for citation in citations_list:
            cited_pub = citation.get('publication_number', '')
            if cited_pub and cited_pub in uc_pub_numbers:
                # Extract assignee - improved pattern
                info = patent.get('Patents_info', '')
                
                # Try different assignee extraction patterns
                assignee = None
                patterns = [
                    r'^([A-Z][A-Za-z\s\&\-\.\d]+) (?:holds|assigned to|owned by|is the assignee)',
                    r'^([A-Z][A-Za-z\s\&\-\.\d]+?)\s+holds',
                    r'^([A-Z][A-Za-z\s\&\-\.\d]+?)\s+assigned'
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, info)
                    if match:
                        assignee = match.group(1).strip()
                        # Clean up common issues
                        if assignee.startswith('In '):
                            assignee = assignee[3:]
                        if assignee.endswith(' and'):
                            assignee = assignee[:-4]
                        break
                
                if assignee and 'UNIV CALIFORNIA' not in assignee.upper():
                    uc_citations.append({
                        'assignee': assignee,
                        'cited_uc_patent': cited_pub
                    })
                    
                    assignee_data = assignee_citations[assignee]
                    assignee_data['count'] += 1
                    assignee_data['uc_patents'].add(cited_pub)
                    
                    # Extract CPC codes from citing patent
                    cpc_str = patent.get('cpc', '[]')
                    if cpc_str and cpc_str != '[]':
                        try:
                            cpc_list = json.loads(cpc_str)
                            for cpc_item in cpc_list:
                                code = cpc_item.get('code')
                                if code:
                                    # Extract main subclass (first 4 characters after letter)
                                    # e.g., from C12Q1/6883 get C12Q
                                    subclass_match = re.match(r'([A-Z]\d{2}[A-Z]?)', code)
                                    if subclass_match:
                                        assignee_data['cpc_codes'].add(subclass_match.group(1))
                        except:
                            pass
    except:
        continue

print('\\nTotal UC citations found:', len(uc_citations))
print('Unique non-UC assignees:', len(assignee_citations))

# Rank assignees by citation count
ranked_assignees = sorted(assignee_citations.items(), key=lambda x: x[1]['count'], reverse=True)

print('\\nTop assignees citing UC patents:')
for assignee, data in ranked_assignees[:15]:
    print(f"  {assignee}: {data['count']} citations, {len(data['cpc_codes'])} CPC subclasses")

print('\\n__RESULT__:')
result = {
    'total_uc_citations': len(uc_citations),
    'unique_assignees': len(assignee_citations),
    'top_assignees': [(a, d['count'], len(d['cpc_codes'])) for a, d in ranked_assignees[:10]],
    'all_assignees': list(assignee_citations.keys())
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:70': {'uc_patents': 169, 'uc_pub_numbers': 59, 'citations_found': 1, 'unique_assignees': 1, 'top_assignees': [['The US patent application', 1, 17]]}}

exec(code, env_args)
