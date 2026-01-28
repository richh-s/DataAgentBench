code = """import json, re

# Load citation data and search for any California-related citations
citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

# Also load UC data to get CPC codes
uc_path = locals()['var_functions.query_db:14']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

# Build UC pub -> CPC mapping
uc_pub_to_cpc = {}
for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        
        # Extract CPC codes
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
            uc_pub_to_cpc[pub_num] = list(subclasses)
        except:
            uc_pub_to_cpc[pub_num] = []

# Strategy: Look for patents from California assignees (not UC) that cite UC patents
# Since direct matching failed, let's try a different approach:
# 1. First, identify all citations in the dataset
# 2. Check if any contain publication numbers matching UC format with US, EP, WO, etc.
# 3. Create a mapping to try different matching approaches

# Let's be more lenient and try to extract all possible identifiers
all_citation_ids = set()
uc_related_citations = []

print('Processing citations...')

for entry in citation_data[:100000]:  # Process subset for speed
    patents_info = entry.get('Patents_info', '')
    
    # Skip patents that are themselves from UC
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Extract assignee (more robust)
    assignee = None
    if ' holds ' in patents_info:
        parts = patents_info.split(' holds ', 1)
        if len(parts) > 0:
            assignee = parts[0].strip()
    elif ' owned by ' in patents_info:
        parts = patents_info.split(' owned by ', 1)
        if len(parts) > 1:
            assignee = parts[1].split(',')[0].strip()
    elif ' assigned to ' in patents_info:
        parts = patents_info.split(' assigned to ', 1)
        if len(parts) > 1:
            assignee = parts[1].split(',')[0].strip()
    
    if not assignee or len(assignee) > 200 or 'UNIV CALIFORNIA' in assignee.upper():
        continue
    
    # Parse citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        for citation in citations:
            if isinstance(citation, dict):
                cited_pub = citation.get('publication_number', '')
                cited_app = citation.get('application_number', '')
                
                # Try to normalize various formats
                if cited_pub:
                    # Remove extra spaces and normalize
                    cited_norm = re.sub(r'\s*-\s*', '-', str(cited_pub))
                    # Try partial matches - just extract the core identifier
                    
                    # Check if it looks like a US patent (US-.....-...)
                    if re.match(r'US-[0-9A-Z]+-[A-Z0-9]+', cited_norm):
                        # For US patents, try matching by application number pattern
                        core_id = re.sub(r'US-', '', cited_norm)
                        # Check if any UC patent has this in its pub number
                        for uc_pub in uc_pub_to_cpc.keys():
                            if core_id in uc_pub or uc_pub in cited_norm:
                                uc_related_citations.append({
                                    'assignee': assignee,
                                    'cited_pub': cited_norm,
                                    'matching_uc': uc_pub,
                                    'uc_cpc': uc_pub_to_cpc.get(uc_pub, [])
                                })
                                break
    except Exception as e:
        pass

print('UC-related citations found:', len(uc_related_citations))
if uc_related_citations:
    print('Sample:')
    for i, item in enumerate(uc_related_citations[:10]):
        print(' ' , item['assignee'], 'cites', item['cited_pub'], '(matches UC:', item['matching_uc'], ')')

result = {
    'found_matches': len(uc_related_citations),
    'sample': uc_related_citations[:10]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}, 'var_functions.execute_python:44': {'uc_patents': 59, 'citations_found': 0, 'sample': []}, 'var_functions.query_db:46': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_functions.execute_python:50': {'total_citations': 1, 'unique_assignees': 1, 'unique_subclasses': 0, 'assignees_list': ['US patent application (no'], 'subclasses_list': [], 'total_rows_needed': 0}, 'var_functions.execute_python:52': {'uc_patent_count': 59, 'matches_found': 0, 'sample_matches': []}, 'var_functions.execute_python:60': {'cited_count': 103, 'uc_count': 59, 'overlap': 0, 'cited_sample': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'uc_sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}, 'var_functions.execute_python:66': {'uc_app_count': 0, 'sample': []}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.execute_python:70': {'total_matches': 0, 'uc_patents_cited': 0, 'sample_matches': []}}

exec(code, env_args)
