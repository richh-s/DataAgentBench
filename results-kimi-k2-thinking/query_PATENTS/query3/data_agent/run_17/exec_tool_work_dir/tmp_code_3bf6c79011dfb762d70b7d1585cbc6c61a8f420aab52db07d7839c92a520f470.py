code = """import json
import re
from collections import defaultdict

# Load all patents data
all_patents_path = locals()['var_functions.query_db:24']
with open(all_patents_path, 'r') as f:
    all_patents = json.load(f)

# Step 1: Extract all UNIV CALIFORNIA patents and their identifiers
uc_patents = []
uc_identifiers = defaultdict(set)  # Store multiple types of identifiers

for patent in all_patents[:10000]:  # Process first 10,000 patents
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-[^\s,\)]+)', patents_info, re.IGNORECASE)
        if pub_match:
            uc_identifiers['publication'].add(pub_match.group(1))
        
        # Extract application number  
        app_match = re.search(r'(?:application|app\. number|patent application)\s+\(?([A-Z]{2}-[0-9]+-[A-Z])\)?', patents_info, re.IGNORECASE)
        if app_match:
            uc_identifiers['application'].add(app_match.group(1))

print('UNIV CALIFORNIA patents found: %d' % len(uc_patents))
print('UC publication numbers: %d' % len(uc_identifiers['publication']))
print('UC application numbers: %d' % len(uc_identifiers['application']))

# Show sample identifiers
print('\nSample UC publication numbers:')
for pub in list(uc_identifiers['publication'])[:10]:
    print('  ' + pub)

# Step 2: More flexible citation checking
print('\n=== Testing citation patterns ===')
citation_stats = defaultdict(int)
uc_citing_patents = []

# Process a subset of patents that have citations
test_patents = [p for p in all_patents[:20000] if p.get('citation', '') != '[]' and 'UNIV CALIFORNIA' not in p.get('Patents_info', '').upper()]

print('Testing %d patents with citations...' % len(test_patents))

for patent in test_patents:
    patents_info = patent.get('Patents_info', '')
    citation_data = patent.get('citation', '[]')
    
    try:
        citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
        cited_uc = False
        
        for citation in citations:
            if not isinstance(citation, dict):
                continue
                
            # Check publication number
            pub_num = citation.get('publication_number', '')
            if pub_num and pub_num in uc_identifiers['publication']:
                cited_uc = True
                citation_stats['publication_match'] += 1
                break
            
            # Check if citation mentions UNIV CALIFORNIA in any field
            citation_str = json.dumps(citation).upper()
            if 'UNIV CALIFORNIA' in citation_str:
                cited_uc = True
                citation_stats['text_match'] += 1
                break
        
        if cited_uc:
            uc_citing_patents.append(patent)
            
    except Exception as e:
        continue

print('\nCitation statistics:')
for key, value in citation_stats.items():
    print('  %s: %d' % (key, value))

print('\nPatents citing UC patents found: %d' % len(uc_citing_patents))

# Step 3: Extract assignees and CPC codes
assignee_cpc_codes = defaultdict(set)
assignee_citation_count = defaultdict(int)

for patent in uc_citing_patents[:500]:  # Process first 500
    patents_info = patent.get('Patents_info', '')
    
    # Extract assignee
    assignee = 'Unknown'
    assignee_match = re.search(r'is (?:owned by|assigned to|belonging to)\s+([^,.(]+)', patents_info, re.IGNORECASE)
    if assignee_match:
        assignee = assignee_match.group(1).strip()
    else:
        # Try alternative pattern
        assignee_match = re.search(r'holds the (?:US|TW|AU|EP) (?:patent|application)[^,]+(?:for|by)\s+([^,.(]+)', patents_info, re.IGNORECASE)
        if assignee_match:
            assignee = assignee_match.group(1).strip()
    
    # Skip UNIV CALIFORNIA itself
    if 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Get CPC codes
    cpc_data = patent.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
        for cpc in cpc_list:
            if isinstance(cpc, dict) and cpc.get('inventive', False):
                code = cpc.get('code', '')
                if code:
                    assignee_cpc_codes[assignee].add(code)
    except:
        pass
    
    assignee_citation_count[assignee] += 1

print('\nAssignees that cite UC patents: %d' % len(assignee_cpc_codes))
print('Top assignees by citation count:')
sorted_assignees = sorted(assignee_citation_count.items(), key=lambda x: x[1], reverse=True)
for assignee, count in sorted_assignees[:10]:
    cpc_count = len(assignee_cpc_codes[assignee])
    print('  %s: %d citations, %d CPC codes' % (assignee, count, cpc_count))

# Collect all CPC codes for database lookup
all_cpc_codes = set()
for codes in assignee_cpc_codes.values():
    all_cpc_codes.update(codes)

print('\nTotal unique CPC codes to look up: %d' % len(all_cpc_codes))

# Save results for next step
results = {
    'uc_patent_count': len(uc_patents),
    'citing_patent_count': len(uc_citing_patents),
    'assignee_count': len(assignee_cpc_codes),
    'cpc_code_count': len(all_cpc_codes),
    'assignee_cpc_map': {k: list(v) for k, v in list(assignee_cpc_codes.items())[:50]},
    'assignee_counts': dict(sorted_assignees[:20])
}

with open('citation_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print('\n__RESULT__:')
print(json.dumps({'status': 'completed', 'assignee_count': len(assignee_cpc_codes), 'cpc_codes': len(all_cpc_codes)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}}

exec(code, env_args)
