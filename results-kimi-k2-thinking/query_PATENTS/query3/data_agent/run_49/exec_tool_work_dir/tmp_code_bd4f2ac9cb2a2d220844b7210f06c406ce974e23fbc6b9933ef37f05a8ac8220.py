code = """import json, re, os

# Load data efficiently
print('Loading data...')
uc_path = locals()['var_functions.query_db:14']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

citation_path = locals()['var_functions.query_db:26']
with open(citation_path, 'r') as f:
    citation_data = json.load(f)

print(f'UC patents: {len(uc_data)}')
print(f'Citation records: {len(citation_data)}')

# Build UC index (all possible identifiers)
uc_pub_numbers = set()
uc_cpc_map = {}

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    # Extract publication number
    match = re.search(r'pub\.? number\s*([A-Z]{2}-[A-Z0-9-]+)', patents_info)
    if match:
        pub = match.group(1).strip()
        pub_norm = re.sub(r'\s*-\s*', '-', pub)
        uc_pub_numbers.add(pub_norm)
        
        # Extract CPC subclasses
        cpc_field = entry.get('cpc', '[]')
        try:
            cpc_data = json.loads(cpc_field)
            subclasses = set()
            for item in cpc_data:
                code = item.get('code', '') if isinstance(item, dict) else ''
                if code:
                    m = re.match(r'([A-Z][0-9]{2}[A-Z]?)', code)
                    if m:
                        subclasses.add(m.group(1))
            uc_cpc_map[pub_norm] = list(subclasses)
        except:
            uc_cpc_map[pub_norm] = []

print(f'UC publication numbers: {len(uc_pub_numbers)}')
print(f'Sample: {list(uc_pub_numbers)[:5]}')

# Use SQLite to do efficient matching - we're hitting memory/time limits with Python
print('\nSwitching to SQL-based matching...')

result = {
    'uc_patents': len(uc_data),
    'uc_pub_numbers': len(uc_pub_numbers),
    'citation_records': len(citation_data),
    'ready_for_sql': True
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}, 'var_functions.execute_python:44': {'uc_patents': 59, 'citations_found': 0, 'sample': []}, 'var_functions.query_db:46': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_functions.execute_python:50': {'total_citations': 1, 'unique_assignees': 1, 'unique_subclasses': 0, 'assignees_list': ['US patent application (no'], 'subclasses_list': [], 'total_rows_needed': 0}, 'var_functions.execute_python:52': {'uc_patent_count': 59, 'matches_found': 0, 'sample_matches': []}, 'var_functions.execute_python:60': {'cited_count': 103, 'uc_count': 59, 'overlap': 0, 'cited_sample': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'uc_sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}, 'var_functions.execute_python:66': {'uc_app_count': 0, 'sample': []}, 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.execute_python:70': {'total_matches': 0, 'uc_patents_cited': 0, 'sample_matches': []}, 'var_functions.execute_python:72': {'found_matches': 2, 'sample': [{'assignee': '[] and has pub. number RU-183879-U1.', 'cited_pub': 'US-6-A', 'matching_uc': 'US-2021000566-A1', 'uc_cpc': []}, {'assignee': 'PERSONAL PRODUCTS CO', 'cited_pub': 'US-4044766-A', 'matching_uc': 'WO-2024044766-A3', 'uc_cpc': []}]}, 'var_functions.execute_python:74': {'assignee_count': 1, 'total_rows': 0, 'top_assignees': ['The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.'], 'cpc_subclasses_found': 0}, 'var_functions.execute_python:76': {'assignee_count': 0, 'total_cpc_assignments': 0, 'sample_assignees': []}}

exec(code, env_args)
