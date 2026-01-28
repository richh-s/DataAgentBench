code = """import json
import re
import os
from collections import defaultdict

# Debug print available storage
print('Available storage variables:')
storage_vars = {}
for key in list(locals().keys()):
    if 'var_' in key:
        value = locals()[key]
        storage_vars[key] = type(value).__name__
        print(f'  {key}: {type(value).__name__}')

# Try to find UC patents from any storage variable
uc_patents = []
uc_key = None

for key in list(locals().keys()):
    if 'var_functions.query_db:' in key and ('44' in key or '8' in key or '14' in key):
        value = locals()[key]
        
        # Check if it's a file path or actual data
        if isinstance(value, str) and os.path.exists(value):
            # File path - load JSON
            try:
                with open(value, 'r') as f:
                    data = json.load(f)
                    if len(data) > 0 and 'UNIV CALIFORNIA' in str(data):
                        uc_patents = data
                        uc_key = key
                        break
            except:
                continue
        elif isinstance(value, list):
            # Direct list data
            if len(value) > 0 and 'UNIV CALIFORNIA' in str(value):
                uc_patents = value
                uc_key = key
                break

print('\nUC patents result:', len(uc_patents), 'records from key:', uc_key)
if uc_patents:
    print('Sample UC patent:', uc_patents[0].get('Patents_info', '')[:100])

# Find general patents for citation analysis
all_patents = []
for key in list(locals().keys()):
    if 'var_functions.query_db:' in key and ('36' in key or '34' in key or '22' in key):
        value = locals()[key]
        
        if isinstance(value, str) and os.path.exists(value):
            try:
                with open(value, 'r') as f:
                    data = json.load(f)
                    all_patents.extend(data)
            except:
                continue
        elif isinstance(value, list):
            all_patents.extend(value)

print('All patents for analysis:', len(all_patents))

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent.get('Patents_info', '')
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        uc_pub_numbers.add(match.group(1).strip())

print('Extracted UC publication numbers:', len(uc_pub_numbers))

# Find citations to UC patents
citations = []
citing_assignees = defaultdict(lambda: defaultdict(set))

for patent in all_patents:
    citation_json = patent.get('citation', '[]')
    if citation_json and citation_json != '[]':
        try:
            cite_list = json.loads(citation_json)
            for cite in cite_list:
                cited_pub = cite.get('publication_number')
                if cited_pub and cited_pub in uc_pub_numbers:
                    # Found a citation to UC patent
                    info = patent.get('Patents_info', '')
                    
                    # Extract assignee
                    assignee_match = re.match(r'^([^,]+?)\s+(holds|assigned to|owned by|is the applicant|is the assignee)', info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                        
                        # Skip UNIV CALIFORNIA self-citations
                        if 'UNIV CALIFORNIA' not in assignee.upper():
                            citations.append({
                                'citing_assignee': assignee,
                                'cited_uc_patent': cited_pub,
                                'citing_patent_info': info,
                                'cpc_data': patent.get('cpc', '[]')
                            })
                            
                            # Track which UC patents each assignee cites
                            citing_assignees[assignee]['uc_patents'].add(cited_pub)
                            
                            # Collect CPC codes for this citing patent
                            cpc_json = patent.get('cpc', '[]')
                            if cpc_json and cpc_json != '[]':
                                try:
                                    cpc_list = json.loads(cpc_json)
                                    for cpc_item in cpc_list:
                                        code = cpc_item.get('code')
                                        if code:
                                            citing_assignees[assignee]['cpc_codes'].add(code)
                                except:
                                    pass
        except:
            continue

print('Found total citations from non-UC assignees:', len(citations))
print('Unique citing assignees:', len(citing_assignees))

# Sort assignees by number of citations
top_assignees = sorted(citing_assignees.items(), key=lambda x: len(x[1]['uc_patents']), reverse=True)
print('\nTop assignees citing UC patents:')
for assignee, data in top_assignees[:10]:
    print(f'  {assignee}: {len(data["uc_patents"])} citations, {len(data["cpc_codes"])} CPC codes')

print('\n__RESULT__:')
result = {
    'uc_patents': len(uc_patents),
    'uc_publication_numbers': len(uc_pub_numbers),
    'citations_found': len(citations),
    'unique_assignees': len(citing_assignees),
    'top_assignees': [(a, len(d['uc_patents'])) for a, d in top_assignees[:10]]
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
