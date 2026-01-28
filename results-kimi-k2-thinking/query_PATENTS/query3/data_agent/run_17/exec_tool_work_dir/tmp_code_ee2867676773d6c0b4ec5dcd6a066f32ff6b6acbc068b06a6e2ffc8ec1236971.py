code = """import json, re, os
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

print('Total patents:', len(all_patents))
print('First patent sample:')
print(json.dumps(all_patents[0], indent=2)[:500])

# Step 1: Find UNIV CALIFORNIA patents and extract their publication numbers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        # Extract publication number
        match = re.search(r'(?:pub\. number|publication number|pub\. no\.|with pub\. number)\s+([A-Z]{2}-[^\s,]+)', patents_info)
        if match:
            uc_pub_numbers.add(match.group(1))

print(f'\nFound {len(uc_patents)} UNIV CALIFORNIA patents')
print(f'Extracted {len(uc_pub_numbers)} publication numbers')
print('Sample UC pub numbers:', list(uc_pub_numbers)[:10])

# Step 2: Find patents that cite UNIV CALIFORNIA patents
citing_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    citation_data = patent.get('citation', '[]')
    
    # Skip UNIV CALIFORNIA patents themselves
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        for citation in citations:
            pub_num = citation.get('publication_number', '')
            if pub_num in uc_pub_numbers:
                citing_patents.append(patent)
                break
    except:
        continue

print(f'\nFound {len(citing_patents)} patents that cite UNIV CALIFORNIA')

# Step 3: Extract assignees and CPC codes from citing patents
assignee_cpc_map = defaultdict(set)

for patent in citing_patents:
    patents_info = patent.get('Patents_info', '')
    
    # Extract assignee
    assignee_match = re.search(r'(?:is owned by|is assigned to|is belonging to|belongs to|holds the)\s+([^,.(]+)', patents_info)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
        if 'UNIV CALIFORNIA' not in assignee.upper():
            # Get CPC codes
            cpc_data = patent.get('cpc', '[]')
            try:
                cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                # Get primary (inventive) CPC codes
                for cpc in cpc_list:
                    if cpc.get('inventive', False):
                        code = cpc.get('code', '')
                        if code:
                            assignee_cpc_map[assignee].add(code)
            except:
                continue

print(f'\nFound {len(assignee_cpc_map)} unique citing assignees')
print('Sample assignees:', list(assignee_cpc_map.keys())[:10])

# Step 4: Get CPC titles from CPCDefinition_database
all_cpc_codes = set()
for codes in assignee_cpc_map.values():
    all_cpc_codes.update(codes)

print(f'\nNeed to look up {len(all_cpc_codes)} CPC codes')

result = {
    'uc_patents_count': len(uc_patents),
    'citing_patents_count': len(citing_patents),
    'citing_assignees_count': len(assignee_cpc_map),
    'cpc_codes_to_lookup': list(all_cpc_codes)[:50]  # Limit for now
}

print('\n__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
