code = """import json
import re
import sqlite3

# Load UC publication numbers and CPC mapping
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

uc_pub_numbers = set()
uc_cpc_mapping = {}
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers.add(pub_num)
        
        # Extract CPC codes
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            primary_cpc_codes = []
            for cpc_item in cpc_data:
                if isinstance(cpc_item, dict):
                    code = cpc_item.get('code', '')
                    if code:
                        # Extract subclass (e.g., H01M from H01M8/04)
                        subclass_match = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                        if subclass_match:
                            subclass = subclass_match.group(1)
                            if subclass not in primary_cpc_codes:
                                primary_cpc_codes.append(subclass)
            uc_cpc_mapping[pub_num] = primary_cpc_codes
        except:
            uc_cpc_mapping[pub_num] = []

print(f"Debug: UC patents: {len(uc_pub_numbers)}")

# Load citation data
citation_file_path = locals()['var_functions.query_db:26']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

# Find citations of UC patents and extract citing assignees
citations_by_assignee = {}

for entry in citation_data:
    patents_info = entry.get('Patents_info', '')
    
    # Skip if this patent is itself a UC patent
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract citing assignee
    assignee_match = re.search(r'^([^0-9]+?)\s+(holds|hold|owns|is owned by|is assigned to|assigned to|is belonging to|belonging to|from|application from)\b', patents_info)
    if assignee_match:
        citing_assignee = assignee_match.group(1).strip()
        # Skip if it's UC
        if 'UNIV CALIFORNIA' in citing_assignee.upper():
            continue
    else:
        # Extract first organization name
        parts = patents_info.split(' holds')
        if len(parts) > 1:
            citing_assignee = parts[0].strip()
            if 'UNIV CALIFORNIA' in citing_assignee.upper():
                continue
        else:
            continue
    
    # Clean assignee name
    citing_assignee = re.sub(r'^(In |The |Application |Patent filing \(|Application \()([^,]+).*', r'\2', citing_assignee).strip()
    
    # Parse citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        if isinstance(citations, list):
            for citation in citations:
                if isinstance(citation, dict):
                    cited_pub_num = citation.get('publication_number', '')
                    if cited_pub_num and cited_pub_num in uc_pub_numbers:
                        # Found a citation of a UC patent
                        if citing_assignee not in citations_by_assignee:
                            citations_by_assignee[citing_assignee] = []
                        
                        # Get CPC codes for this cited UC patent
                        cpc_codes = uc_cpc_mapping.get(cited_pub_num, [])
                        for cpc_code in cpc_codes:
                            citations_by_assignee[citing_assignee].append({
                                'cited_uc_patent': cited_pub_num,
                                'cpc_subclass': cpc_code
                            })
    except:
        pass

print(f"Debug: Found {len(citations_by_assignee)} citing assignees (excluding UC)")
print('__RESULT__:')
print(json.dumps({
    'citing_assignee_count': len(citations_by_assignee),
    'top_assignees': list(citations_by_assignee.keys())[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records'}

exec(code, env_args)
