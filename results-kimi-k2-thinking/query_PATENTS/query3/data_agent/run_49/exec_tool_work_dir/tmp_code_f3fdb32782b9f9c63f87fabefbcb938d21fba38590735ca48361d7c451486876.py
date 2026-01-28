code = """import json
import re

# Load UC publication numbers
cpc_codes_by_pubnum = {}  # Map pubnum to CPC codes
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

# Build UC set and CPC mapping
uc_pub_numbers_set = set()
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers_set.add(pub_num)
        
        # Extract all unique CPC codes (subclasses) for this UC patent
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            cpc_subclasses = set()
            for cpc_item in cpc_data:
                if isinstance(cpc_item, dict):
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract subclass (e.g., H01M from H01M8/04)
                        subclass_match = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                        if subclass_match:
                            subclass = subclass_match.group(1)
                            cpc_subclasses.add(subclass)
            cpc_codes_by_pubnum[pub_num] = list(cpc_subclasses)
        except:
            cpc_codes_by_pubnum[pub_num] = []

print(f"Debug: UC publication numbers: {len(uc_pub_numbers_set)}")
print(f"Debug: CPC mappings: {len(cpc_codes_by_pubnum)}")

# Load citation data
citation_file_path = locals()['var_functions.query_db:26']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

print(f"Debug: Total records with citations: {len(citation_data)}")

# Find all citations of UC patents by non-UC assignees
citations_by_assignee = {}
successful_matches = 0
processed = 0

for entry in citation_data:
    processed += 1
    if processed % 10000 == 0:
        print(f"Debug: Processed {processed}/{len(citation_data)} records")
    
    patents_info = entry.get('Patents_info', '')
    
    # Extract assignee (handle multiple formats)
    assignee = None
    
    # Try different patterns to extract assignee
    patterns = [
        r'^([^,]+?)\s+(holds|hold|owns|is owned by|is assigned to|assigned to|is belonging to|belonging to|from|application from)\b',
        r'^(In [A-Z]{2}, the [^,]+, |In [A-Z]{2}, |The )?([^.,]+?)\s+(holds|hold|owns|is owned by|is assigned to|assigned to|is belonging to|belonging to)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, patents_info)
        if match:
            # Find the group that has the assignee name
            for group_num in range(1, len(match.groups()) + 1):
                potential = match.group(group_num)
                if potential and potential not in ['holds', 'hold', 'owns', 'is owned by', 'is assigned to', 'assigned to', 'is belonging to', 'belonging to', 'from', 'application from', 'In', 'The', 'In US,', 'In EP,']:
                    assignee = potential.strip()
                    break
            if assignee:
                break
    
    if not assignee:
        # Fallback: extract first part before common verbs
        parts = re.split(r'\s+(holds|hold|owns|application|patent filing)\b', patents_info)
        if len(parts) > 0:
            assignee = parts[0].strip()
    
    # Skip UC assignees
    if not assignee or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Clean up assignee name
    assignee = re.sub(r'^(In [A-Z]{2},\s*|The |Application |Patent filing \(|Application \()', '', assignee)
    assignee = assignee.strip()
    
    # Parse citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        if isinstance(citations, list):
            for citation in citations:
                if isinstance(citation, dict):
                    cited_pub_num = citation.get('publication_number', '')
                    if cited_pub_num:
                        # Normalize cited_pub_num format
                        cited_pub_num_norm = re.sub(r'\s*-\s*', '-', str(cited_pub_num))
                        # Check if this cites a UC patent
                        if cited_pub_num_norm in uc_pub_numbers_set:
                            successful_matches += 1
                            if assignee not in citations_by_assignee:
                                citations_by_assignee[assignee] = []
                            
                            # Get CPC codes for this UC patent
                            cpc_codes = cpc_codes_by_pubnum.get(cited_pub_num_norm, [])
                            for cpc_code in cpc_codes:
                                citations_by_assignee[assignee].append({
                                    'cited_uc_patent': cited_pub_num_norm,
                                    'cpc_subclass': cpc_code
                                })
    except Exception as e:
        pass
        
print(f"Debug: Matches found: {successful_matches}")
print(f"Debug: Citing assignees (non-UC): {len(citations_by_assignee)}")
print('__RESULT__:')
print(json.dumps({
    'citing_assignees_count': len(citations_by_assignee),
    'matches_found': successful_matches,
    'top_assignees': list(citations_by_assignee.keys())[:20] if citations_by_assignee else []
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}}

exec(code, env_args)
