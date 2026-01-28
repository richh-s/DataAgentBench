code = """import json
import re

# Load UC data
cpc_codes_by_pubnum = {}
uc_file_path = locals()['var_functions.query_db:14']
with open(uc_file_path, 'r') as f:
    uc_data = json.load(f)

uc_pub_numbers = set()
pubnum_pattern = r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(pubnum_pattern, patents_info)
    if match:
        pub_num = match.group(1).strip()
        pub_num = re.sub(r'\s*-\s*', '-', pub_num)
        uc_pub_numbers.add(pub_num)
        
        # Extract CPC subclasses
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
            cpc_codes_by_pubnum[pub_num] = list(subclasses)
        except:
            cpc_codes_by_pubnum[pub_num] = []

print(f"UC patents: {len(uc_pub_numbers)}")

# Load citation data
citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

# Find citations
assignee_cpc_subclasses = {}  # assignee -> set of cpc subclasses
total_citations = 0

for entry in citation_data:
    patents_info = entry.get('Patents_info', '')
    
    if 'UNIV CALIFORNIA' in patents_info.upper():
        continue
    
    # Simple assignee extraction - find first comma-separated element
    assignee = None
    parts = re.split(r'[,.]', patents_info, maxsplit=1)
    if len(parts) >= 1:
        candidate = parts[0].strip()
        # Remove common prefixes
        candidate = re.sub(r'^(In [A-Z]{2},\s*|The |Application |Patent filing \(|Application \()', '', candidate)
        if candidate and len(candidate) < 150 and 'UNIV CALIFORNIA' not in candidate.upper():
            # Remove trailing "holds" or similar
            assignee = re.sub(r'\s+(holds|hold|owns|is owned by|is assigned to|application|patent filing)$', '', candidate)
    
    if not assignee:
        continue
    
    # Check citations
    citation_field = entry.get('citation', '[]')
    try:
        citations = json.loads(citation_field)
        if isinstance(citations, list):
            for citation in citations:
                if isinstance(citation, dict):
                    cited_pub = citation.get('publication_number', '')
                    if cited_pub:
                        cited_norm = re.sub(r'\s*-\s*', '-', str(cited_pub))
                        if cited_norm in uc_pub_numbers:
                            total_citations += 1
                            cpc_codes = cpc_codes_by_pubnum.get(cited_norm, [])
                            
                            if assignee not in assignee_cpc_subclasses:
                                assignee_cpc_subclasses[assignee] = set()
                            
                            for cpc in cpc_codes:
                                assignee_cpc_subclasses[assignee].add(cpc)
    except:
        pass

# Get CPC titles for the subclasses we found
all_subclasses = set()
for cpc_set in assignee_cpc_subclasses.values():
    all_subclasses.update(cpc_set)

print(f"Found {len(assignee_cpc_subclasses)} assignees")
print(f"Found {len(all_subclasses)} unique CPC subclasses")
print(f"Total citations: {total_citations}")

# Query CPC titles
cpc_titles = {}
if all_subclasses:
    subclasses_list = [f"'{s}'" for s in all_subclasses]
    # Due to possible size, query in chunks
    chunk_size = 100
    for i in range(0, len(subclasses_list), chunk_size):
        chunk = subclasses_list[i:i+chunk_size]
        # We'll do this in the next step with query_db
        pass

# Prepare results as list
results_list = []
for assignee, cpc_set in assignee_cpc_subclasses.items():
    for cpc_subclass in sorted(cpc_set):
        results_list.append({
            'assignee': assignee,
            'cpc_subclass': cpc_subclass,
            'cpc_title': None  # Will fill in later
        })

print('__RESULT__:')
print(json.dumps({
    'total_citations': total_citations,
    'unique_assignees': len(assignee_cpc_subclasses),
    'unique_subclasses': len(all_subclasses),
    'assignees_list': list(assignee_cpc_subclasses.keys())[:20],
    'subclasses_list': list(all_subclasses)[:20],
    'total_rows_needed': len(results_list)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}, 'var_functions.execute_python:44': {'uc_patents': 59, 'citations_found': 0, 'sample': []}, 'var_functions.query_db:46': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}]}

exec(code, env_args)
