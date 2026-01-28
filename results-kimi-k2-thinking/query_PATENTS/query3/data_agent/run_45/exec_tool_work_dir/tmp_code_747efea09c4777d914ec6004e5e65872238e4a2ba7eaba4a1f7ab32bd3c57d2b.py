code = """import json
import re
from collections import defaultdict

# Load UC patents from the stored variable
uc_patents_var = locals()['var_functions.query_db:58']

# Handle both file paths and direct data
if isinstance(uc_patents_var, str):
    with open(uc_patents_var, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = uc_patents_var

print("UC Patents Count:", len(uc_patents))

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    # Multiple patterns to extract publication numbers
    patterns = [
        r'pub\. number\s+([A-Z0-9-]+)',
        r'pub\.no\.\s+([A-Z0-9-]+)',
        r'publication number\s+([A-Z0-9-]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, info, re.IGNORECASE)
        if match:
            pub_num = match.group(1).strip()
            uc_pub_numbers.add(pub_num)
            break

print("UC Publication Numbers:", len(uc_pub_numbers))
print("Sample:", list(uc_pub_numbers)[:10])

# Create a lookup of UC patents for CPC codes
uc_cpc_lookup = {}
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    cpc_str = patent.get('cpc', '[]')
    
    # Find publication number for this patent
    pub_num = None
    for pattern in patterns:
        match = re.search(pattern, info, re.IGNORECASE)
        if match:
            pub_num = match.group(1).strip()
            break
    
    if pub_num and cpc_str and cpc_str != '[]':
        try:
            cpc_list = json.loads(cpc_str)
            codes = [item.get('code') for item in cpc_list if item.get('code')]
            uc_cpc_lookup[pub_num] = codes
        except:
            uc_cpc_lookup[pub_num] = []

print("UC CPC lookup entries:", len(uc_cpc_lookup))

# Now let's get a sample of patents with citations to scan
citation_patents_var = locals()['var_functions.query_db:84']

if isinstance(citation_patents_var, str):
    # Empty result from earlier query
    citation_patents = []
else:
    citation_patents = citation_patents_var

print("Citation patents sample:", len(citation_patents))

# Since direct search didn't work, let's get patents with citations that have US or WO numbers
citation_vars = [v for k, v in locals().items() if 'var_' in k and 'query_db' in k and ('36' in k or '34' in k)]

print("Available citation sources:", len(citation_vars))

all_cite_patents = []
for var in citation_vars:
    if isinstance(var, list):
        all_cite_patents.extend(var)

print("Total patent records to scan:", len(all_cite_patents))

# Find citations to UC patents
uc_citations = []
assignee_citations = defaultdict(lambda: {'count': 0, 'uc_patents': set(), 'cpc_codes': set()})

for i, patent in enumerate(all_cite_patents):
    if i % 1000 == 0 and i > 0:
        print(f"Processed {i} patents...")
    
    citation_str = patent.get('citation', '[]')
    if not citation_str or citation_str == '[]':
        continue
    
    try:
        citations_list = json.loads(citation_str)
        for citation in citations_list:
            cited_pub = citation.get('publication_number', '')
            if cited_pub and cited_pub in uc_pub_numbers:
                # Found a citation to a UC patent!
                info = patent.get('Patents_info', '')
                
                # Extract assignee name more carefully
                assignee = None
                info_patterns = [
                    r'^([A-Z][A-Za-z\s\&\-\.\d]+?)\s+(?:holds|assigned to|owned by)',
                    r'^([A-Z][A-Za-z\s\&\-\.\d]+?)(?:\s+holds|\s+is the)',
                ]
                
                for pattern in info_patterns:
                    match = re.search(pattern, info, re.IGNORECASE)
                    if match:
                        assignee = match.group(1)
                        # Clean up
                        assignee = assignee.strip()
                        if assignee.startswith('In '):
                            assignee = assignee[3:]
                        break
                
                if assignee and 'UNIV CALIFORNIA' not in assignee.upper():
                    uc_citations.append({
                        'assignee': assignee,
                        'cited_uc_patent': cited_pub,
                        'citing_patent_info': info[:100] + "..."
                    })
                    
                    # Track assignee data
                    assignee_info = assignee_citations[assignee]
                    assignee_info['count'] += 1
                    assignee_info['uc_patents'].add(cited_pub)
                    
                    # Extract CPC codes from citing patent
                    cpc_str = patent.get('cpc', '[]')
                    if cpc_str and cpc_str != '[]':
                        try:
                            cpc_list = json.loads(cpc_str)
                            for cpc_item in cpc_list:
                                code = cpc_item.get('code')
                                if code:
                                    # Extract main subclass for grouping
                                    # e.g., C12Q from C12Q1/6883
                                    subclass_match = re.match(r'([A-Z]\d{2}[A-Z]?)', code)
                                    if subclass_match:
                                        subclass = subclass_match.group(1)
                                        assignee_info['cpc_codes'].add(subclass)
                        except:
                            pass
    except Exception as e:
        continue

print("\\n" + "="*50)
print("FINAL RESULTS:")
print(f"Total citations to UC patents from non-UC assignees: {len(uc_citations)}")
print(f"Number of unique non-UC assignees: {len(assignee_citations)}")

# Rank assignees by citation count
sorted_assignees = sorted(assignee_citations.items(), key=lambda x: x[1]['count'], reverse=True)

print("\\nTop 15 assignees citing UC patents:")
for i, (assignee, data) in enumerate(sorted_assignees[:15], 1):
    print(f"{i}. {assignee}")
    print(f"   Citations: {data['count']}, UC Patents Cited: {len(data['uc_patents'])}")
    print(f"   CPC Subclasses: {len(data['cpc_codes'])}")
    if data['cpc_codes']:
        print(f"   CPC Codes: {', '.join(sorted(data['cpc_codes'])[:5])}")
    print()

# Save results for next step
print("\\n__RESULT__:")
result = {
    'total_citations': len(uc_citations),
    'unique_assignees': len(assignee_citations),
    'top_assignees_data': [(assignee, data['count'], list(data['uc_patents']), list(data['cpc_codes'])) 
                          for assignee, data in sorted_assignees[:15]]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:70': {'uc_patents': 169, 'uc_pub_numbers': 59, 'citations_found': 1, 'unique_assignees': 1, 'top_assignees': [['The US patent application', 1, 17]]}, 'var_functions.execute_python:80': {'citations': 0, 'assignees': 0, 'top_assignees': []}, 'var_functions.query_db:82': [{'count': '87411'}], 'var_functions.query_db:84': []}

exec(code, env_args)
