code = """import json
import re

# Load UC data
cpc_codes_by_pubnum = {}
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

uc_pub_numbers_set = set()
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers_set.add(pub_num)
        
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            cpc_subclasses = set()
            for cpc_item in cpc_data:
                if isinstance(cpc_item, dict):
                    code = cpc_item.get('code', '')
                    if code:
                        subclass_match = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                        if subclass_match:
                            cpc_subclasses.add(subclass_match.group(1))
            cpc_codes_by_pubnum[pub_num] = list(cpc_subclasses)
        except:
            cpc_codes_by_pubnum[pub_num] = []

# Load citation data
citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

assignee_cpc = {}  # assignee -> {cpcSubclass: count}
total_citations = 0

print('Processing', len(citation_data), 'citation records')
print('UC patents loaded:', len(uc_pub_numbers_set))

for entry in citation_data:
    patents_info = entry.get('Patents_info', '')
    
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    assignee = None
    # Simple assignee extraction
    match = re.search(r'^([A-Z][^,\.]+?)\s+(holds|hold|owns|application|patent filing)', patents_info)
    if match:
        assignee = match.group(1).strip()
    
    if assignee and 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    if not assignee or len(assignee) > 200:
        continue
    
    # Parse citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        for citation in citations:
            if isinstance(citation, dict):
                cited_pub = citation.get('publication_number', '')
                if cited_pub:
                    cited_pub_norm = re.sub(r'\s*-\s*', '-', str(cited_pub))
                    if cited_pub_norm in uc_pub_numbers_set:
                        total_citations += 1
                        cpc_codes = cpc_codes_by_pubnum.get(cited_pub_norm, [])
                        
                        if assignee not in assignee_cpc:
                            assignee_cpc[assignee] = {}
                        
                        for cpc in cpc_codes:
                            assignee_cpc[assignee][cpc] = assignee_cpc[assignee].get(cpc, 0) + 1
    except:
        pass

print('Total UC citations found:', total_citations)
print('Unique non-UC assignees:', len(assignee_cpc))

result = {
    'total_citations': total_citations,
    'unique_assignees': len(assignee_cpc),
    'assignees': list(assignee_cpc.keys())[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}}

exec(code, env_args)
