code = """import json
import re
from collections import defaultdict

# Load patents that cite UNIV CALIFORNIA
# These are patents whose citation field contains "UNIV CALIFORNIA"
citation_file_path = locals()['var_functions.query_db:48']
with open(citation_file_path, 'r') as f:
    citing_patents = json.load(f)

print('Total patents whose citations mention UNIV CALIFORNIA:', len(citing_patents))

# Load UC publication numbers for cross-reference
uc_pub_file = 'uc_pub_numbers.json'
with open(uc_pub_file, 'r') as f:
    uc_pub_numbers = set(json.load(f))

print('UC publication numbers loaded:', len(uc_pub_numbers))

# Extract assignees and CPC codes from patents that actually cite UC patents
assignee_cpc_codes = defaultdict(set)
assignee_citations = defaultdict(list)

# Process first 1000 patents for analysis
for patent in citing_patents[:1000]:
    patents_info = patent.get('Patents_info', '')
    citation_data = patent.get('citation', '[]')
    cpc_data = patent.get('cpc', '[]')
    
    # Skip patents that are themselves assigned to UNIV CALIFORNIA
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee
    assignee_match = re.search(r'(?:is (?:owned by|assigned to|belonging to)|holds the|belongs to)\s+([^,.(]+)', patents_info, re.IGNORECASE)
    if not assignee_match:
        continue
        
    assignee = assignee_match.group(1).strip()
    
    # Skip UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    try:
        # Check if this patent actually cites UC patents
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        
        # Collect UC citations
        uc_citations = []
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num in uc_pub_numbers:
                uc_citations.append(pub_num)
        
        if uc_citations:
            # Extract primary (inventive) CPC codes
            cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
            primary_cpcs = []
            for cpc in cpc_list:
                if isinstance(cpc, dict) and cpc.get('inventive', False):
                    code = cpc.get('code', '')
                    if code:
                        primary_cpcs.append(code)
                        assignee_cpc_codes[assignee].add(code)
            
            if primary_cpcs:
                assignee_citations[assignee].extend(uc_citations)
            
    except Exception as e:
        continue

print('Unique citing assignees found:', len(assignee_cpc_codes))
print('Sample assignees:', list(assignee_cpc_codes.keys())[:10])

# Collect all unique CPC codes
all_cpc_codes = set()
for codes in assignee_cpc_codes.values():
    all_cpc_codes.update(codes)

print('Total unique CPC codes to look up:', len(all_cpc_codes))

# Save data for CPC lookup
with open('assignee_cpc_mapping.json', 'w') as f:
    json.dump({k: list(v) for k, v in assignee_cpc_codes.items()}, f)

result = {
    'citing_assignees': len(assignee_cpc_codes),
    'total_cpc_codes': len(all_cpc_codes),
    'sample_assignees': dict(list(assignee_cpc_codes.items())[:5])
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}}

exec(code, env_args)
