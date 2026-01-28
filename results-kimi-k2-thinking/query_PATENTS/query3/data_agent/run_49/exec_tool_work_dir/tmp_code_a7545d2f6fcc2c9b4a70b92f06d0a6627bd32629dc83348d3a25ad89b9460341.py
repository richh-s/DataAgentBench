code = """import json, re

# Load all data
uc_path = locals()['var_functions.query_db:14']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

# Build UC map
uc_identifiers = set()
uc_cpc_mapping = {}

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_identifiers.add(pub_num)
        
        # Get CPC codes
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            subclasses = set()
            for item in cpc_data:
                if isinstance(item, dict) and 'code' in item:
                    code = item['code']
                    m = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                    if m:
                        subclasses.add(m.group(1))
            uc_cpc_mapping[pub_num] = list(subclasses)
        except:
            uc_cpc_mapping[pub_num] = []

print('UC patents:', len(uc_identifiers))

# Find citations with better assignee extraction
assignee_citations = {}  # assignee -> list of (uc_patent, cpc_list)

for idx, entry in enumerate(citation_data):
    if idx % 5000 == 0:
        print(f'Processing {idx}/{len(citation_data)}')
    
    patents_info = entry.get('Patents_info', '')
    
    # Skip UC
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee - try multiple patterns
    assignee = None
    
    # Pattern 1: "ORG holds"
    match = re.search(r'^([A-Z][A-Z0-9\s\&\-\.]+?)\s+holds\b', patents_info)
    if match:
        assignee = match.group(1).strip()
    else:
        # Pattern 2: "owned by ORG"
        match = re.search(r'\bowned by\s+([A-Z][A-Z0-9\s\&\-\.]+?)(?:\s+and\s+has|\s*,|\s+and\b)', patents_info)
        if match:
            assignee = match.group(1).strip()
        else:
            # Pattern 3: "assigned to ORG"  
            match = re.search(r'\bassigned to\s+([A-Z][A-Z0-9\s\&\-\.]+?)(?:\s+and\s+has|\s*,|\s+and\b)', patents_info)
            if match:
                assignee = match.group(1).strip()
    
    if not assignee or len(assignee) > 100 or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Clean up
    assignee = re.sub(r'\s+(and|from|application|patent|filing|with).*$', '', assignee, flags=re.IGNORECASE).strip()
    
    # Check citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        for citation in citations:
            cited_pub = citation.get('publication_number', '') if isinstance(citation, dict) else ''
            if cited_pub:
                cited_norm = re.sub(r'\s*-\s*', '-', str(cited_pub))
                if cited_norm in uc_identifiers:
                    if assignee not in assignee_citations:
                        assignee_citations[assignee] = []
                    assignee_citations[assignee].append((cited_norm, uc_cpc_mapping.get(cited_norm, [])))
    except:
        pass

print('Found', len(assignee_citations), 'assignees citing UC patents')

# Show results
if assignee_citations:
    # Sort by number of citations
    sorted_assignees = sorted(assignee_citations.items(), key=lambda x: len(x[1]), reverse=True)
    
    print('Top assignees:')
    for assignee, citations in sorted_assignees[:20]:
        print(f'  {assignee}: {len(citations)} citations')
        # Show CPC breakdown
        cpc_set = set()
        for uc_patent, cpc_list in citations:
            cpc_set.update(cpc_list)
        if cpc_set:
            print(f'    CPC subclasses: {sorted(cpc_set)}')

# Build final structured results
final_results = []
for assignee, citations in assignee_citations.items():
    # Get unique CPC subclasses for this assignee
    cpc_subclasses = set()
    for uc_patent, cpc_list in citations:
        cpc_subclasses.update(cpc_list)
    
    for cpc_subclass in sorted(cpc_subclasses):
        final_results.append({
            'assignee': assignee,
            'cpc_subclass': cpc_subclass
        })

result = {
    'assignee_count': len(assignee_citations),
    'total_cpc_assignments': len(final_results),
    'sample_assignees': list(assignee_citations.keys())[:10]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}, 'var_functions.execute_python:44': {'uc_patents': 59, 'citations_found': 0, 'sample': []}, 'var_functions.query_db:46': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_functions.execute_python:50': {'total_citations': 1, 'unique_assignees': 1, 'unique_subclasses': 0, 'assignees_list': ['US patent application (no'], 'subclasses_list': [], 'total_rows_needed': 0}, 'var_functions.execute_python:52': {'uc_patent_count': 59, 'matches_found': 0, 'sample_matches': []}, 'var_functions.execute_python:60': {'cited_count': 103, 'uc_count': 59, 'overlap': 0, 'cited_sample': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'uc_sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}, 'var_functions.execute_python:66': {'uc_app_count': 0, 'sample': []}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.execute_python:70': {'total_matches': 0, 'uc_patents_cited': 0, 'sample_matches': []}, 'var_functions.execute_python:72': {'found_matches': 2, 'sample': [{'assignee': '[] and has pub. number RU-183879-U1.', 'cited_pub': 'US-6-A', 'matching_uc': 'US-2021000566-A1', 'uc_cpc': []}, {'assignee': 'PERSONAL PRODUCTS CO', 'cited_pub': 'US-4044766-A', 'matching_uc': 'WO-2024044766-A3', 'uc_cpc': []}]}, 'var_functions.execute_python:74': {'assignee_count': 1, 'total_rows': 0, 'top_assignees': ['The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'cpc_subclasses_found': 0}}

exec(code, env_args)
