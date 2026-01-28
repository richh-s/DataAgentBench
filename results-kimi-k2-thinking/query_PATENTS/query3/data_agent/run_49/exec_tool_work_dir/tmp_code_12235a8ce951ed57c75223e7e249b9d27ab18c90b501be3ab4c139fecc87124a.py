code = """import json
import re

# Load UC publication numbers and CPC mappings
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
        
        # Extract CPC subclasses
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
                            cpc_subclasses.add(subclass_match.group(1))
            cpc_codes_by_pubnum[pub_num] = list(cpc_subclasses)
        except:
            cpc_codes_by_pubnum[pub_num] = []

# Load citation data
citation_file_path = locals()['var_functions.query_db:26']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

print(f"Debug: Processing {len(citation_data)} citation records")
print(f"Debug: UC patents: {len(uc_pub_numbers_set)}")

# Find citations
assignee_cpc_mapping = {}  # assignee -> {cpc_subclass: count}
total_citations_found = 0
processed = 0

for entry in citation_data:
    processed += 1
    if processed % 5000 == 0:
        print(f"Debug: Processed {processed}/{len(citation_data)}")
    
    patents_info = entry.get('Patents_info', '')
    
    # Skip UC patents in the citing position
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee - try multiple approaches
    assignee = None
    
    # Method 1: Look for pattern before action verbs
    match = re.search(r'^([^,\.]+?)\s+(holds|hold|owns|is owned by|is assigned to|assigned to|is belonging to|belonging to|from|application from)', patents_info)
    if match:
        potential = match.group(1).strip()
        # Don't include known action phrases
        if potential not in ['is', 'is assigned', 'patent filing', 'application', 'the application']:
            assignee = potential
    
    # Method 2: More patterns
    if not assignee:
        match = re.search(r'^(In [A-Z]{2},\s*)?([^,.]+?)\s+(holds|hold|owns|application|patent filing)', patents_info)
        if match:
            assignee = match.group(2).strip()
    
    # Method 3: Simple split by common keywords
    if not assignee or len(assignee) > 200:  # Sanity check - if too long, it's probably wrong
        parts = re.split(r'\s+(holds|hold|owns|application|patent|is|from)\b', patents_info, maxsplit=1)
        if len(parts) >= 1:
            assignee = parts[0].strip()
    
    # Final cleanup
    if assignee:
        assignee = re.sub(r'^(In [A-Z]{2},\s*|The |Application |Patent filing \(|Application \(|\(app\. number\s*[A-Z0-9-]+\)\s*)', '', assignee)
        assignee = assignee.strip()
        
        # Skip if it still contains UC or is too short/long
        if 'UNIV CALIFORNIA' in assignee.upper() or len(assignee) < 3 or len(assignee) > 200:
            assignee = None
    
    if not assignee:
        continue
    
    # Parse citations to find UC patents
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        if isinstance(citations, list):
            for citation in citations:
                if isinstance(citation, dict):
                    cited_pub_num = citation.get('publication_number', '')
                    if cited_pub_num:
                        # Normalize
                        cited_pub_num_norm = re.sub(r'\s*-\s*', '-', str(cited_pub_num))
                        # Check if cites UC patent
                        if cited_pub_num_norm in uc_pub_numbers_set:
                            total_citations_found += 1
                            cpc_codes = cpc_codes_by_pubnum.get(cited_pub_num_norm, [])
                            
                            # Update mapping
                            if assignee not in assignee_cpc_mapping:
                                assignee_cpc_mapping[assignee] = {}
                            
                            for cpc_code in cpc_codes:
                                if cpc_code not in assignee_cpc_mapping[assignee]:
                                    assignee_cpc_mapping[assignee][cpc_code] = 0
                                assignee_cpc_mapping[assignee][cpc_code] += 1
    except:
        pass

# Summarize results
print(f"\nDebug: Total citations of UC patents found: {total_citations_found}")
print(f"Debug: Unique citing assignees: {len(assignee_cpc_mapping)}")

# Show results
if assignee_cpc_mapping:
    print(f"Debug: Top assignees:")
    for assignee in list(assignee_cpc_mapping.keys())[:10]:
        print(f"  {assignee}: {len(assignee_cpc_mapping[assignee])} CPC subclasses")

print('__RESULT__:')
print(json.dumps({
    'total_citations': total_citations_found,
    'unique_assignees': len(assignee_cpc_mapping),
    'assignee_sample': list(assignee_cpc_mapping.keys())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}}

exec(code, env_args)
