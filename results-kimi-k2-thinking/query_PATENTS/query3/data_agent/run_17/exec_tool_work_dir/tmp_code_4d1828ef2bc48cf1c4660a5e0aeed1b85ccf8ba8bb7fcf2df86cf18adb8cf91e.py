code = """import json
import re
from collections import defaultdict

# Load all patent data
patent_file = locals()['var_functions.query_db:62']
with open(patent_file, 'r') as f:
    all_patents = json.load(f)

print('Total patents loaded: ' + str(len(all_patents)))

# Step 1: Extract UNIV CALIFORNIA identifiers
uc_pub_numbers = set()
uc_patents = []

for patent in all_patents:
    patents_info = patent.get('Patents_info', '')
    if 'UNIV CALIFORNIA' in patents_info.upper():
        uc_patents.append(patent)
        # Extract publication number
        pub_match = re.search(r'(?:pub\. number|publication number|pub\. no\.)\s+([A-Z]{2}-[^\s,\)]+)', patents_info, re.IGNORECASE)
        if pub_match:
            uc_pub_numbers.add(pub_match.group(1))

print('UNIV CALIFORNIA patents: ' + str(len(uc_patents)))
print('UNIV CALIFORNIA publication numbers: ' + str(len(uc_pub_numbers)))
print('Sample: ' + str(list(uc_pub_numbers)[:10]))

# Step 2: Find patents that cite UC patents and extract assignees/CPCs
assignee_cpc_codes = defaultdict(set)
assignee_citation_counts = defaultdict(int)
citing_patents = []

# Process patents in batches to avoid memory issues
batch_size = 10000
for batch_start in range(0, min(len(all_patents), 50000), batch_size):
    batch_end = min(batch_start + batch_size, len(all_patents))
    
    for i in range(batch_start, batch_end):
        patent = all_patents[i]
        patents_info = patent.get('Patents_info', '')
        
        # Skip UNIV CALIFORNIA patents
        if 'UNIV CALIFORNIA' in patents_info.upper():
            continue
        
        # Check citations
        citation_data = patent.get('citation', '[]')
        if citation_data == '[]' or not citation_data:
            continue
        
        try:
            citations = json.loads(citation_data) if isinstance(citation_data, str) else citation_data
            
            # Check if any citation matches UC publication numbers
            cites_uc = False
            for citation in citations:
                if not isinstance(citation, dict):
                    continue
                pub_num = citation.get('publication_number', '')
                if pub_num and pub_num in uc_pub_numbers:
                    cites_uc = True
                    break
            
            if cites_uc:
                citing_patents.append(patent)
                
                # Extract assignee
                assignee_match = re.search(r'(?:is (?:owned by|assigned to|belonging to)|holds the|belongs to)\s+([^,.(]+)', patents_info, re.IGNORECASE)
                if assignee_match:
                    assignee = assignee_match.group(1).strip()
                else:
                    # Alternative pattern
                    assignee_match = re.search(r'^([A-Z][A-Z\s&\-]+?)\s+(?:holds|is|has)', patents_info)
                    if assignee_match:
                        assignee = assignee_match.group(1).strip()
                    else:
                        assignee = 'Unknown'
                
                # Skip if it's still UNIV CALIFORNIA
                if 'UNIV CALIFORNIA' in assignee.upper():
                    continue
                
                # Extract primary CPC codes (inventive=True)
                cpc_data = patent.get('cpc', '[]')
                try:
                    cpc_list = json.loads(cpc_data) if isinstance(cpc_data, str) else cpc_data
                    primary_cpcs = []
                    for cpc in cpc_list:
                        if isinstance(cpc, dict) and cpc.get('inventive', False):
                            code = cpc.get('code', '')
                            if code:
                                primary_cpcs.append(code)
                                assignee_cpc_codes[assignee].add(code)
                    
                    if primary_cpcs:
                        assignee_citation_counts[assignee] += 1
                        
                except:
                    continue
        except:
            continue

print('Patents citing UC patents: ' + str(len(citing_patents)))
print('Unique assignees: ' + str(len(assignee_cpc_codes)))
print('Top assignees:')
for assignee, count in sorted(assignee_citation_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    cpc_count = len(assignee_cpc_codes[assignee])
    print('  ' + assignee + ': ' + str(count) + ' citations, ' + str(cpc_count) + ' CPC codes')

# Step 3: Collect all CPC codes for database lookup
all_cpc_codes = set()
for codes in assignee_cpc_codes.values():
    all_cpc_codes.update(codes)

print('Total unique CPC codes to look up: ' + str(len(all_cpc_codes)))

# Save results
results = {
    'uc_patent_count': len(uc_patents),
    'citing_patent_count': len(citing_patents),
    'assignee_count': len(assignee_cpc_codes),
    'cpc_code_count': len(all_cpc_codes),
    'assignee_citation_counts': dict(assignee_citation_counts),
    'assignee_cpc_map': {k: list(v) for k, v in assignee_cpc_codes.items()}
}

with open('citation_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)

final_result = {
    'status': 'completed',
    'citing_assignees': len(assignee_cpc_codes),
    'total_cpc_codes': len(all_cpc_codes)
}
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:8': ['publicationinfo'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': {'uc_patents': 169, 'citing_patents': 0, 'citing_assignees': 0}, 'var_functions.execute_python:46': {'citation_count': 0, 'assignee_count': 0, 'assignees': {}}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'uc_patent_count': 169, 'uc_pub_numbers': 114}, 'var_functions.execute_python:52': {'citing_assignees': 0, 'total_cpc_codes': 0, 'sample_assignees': {}}, 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:60': {'uc_patents': 169, 'uc_pub_numbers': 114}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
