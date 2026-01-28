code = """import json, re

# Load UC data and extract application numbers
uc_path = locals()['var_functions.query_db:14']
with open(uc_path, 'r') as f:
    uc_data = json.load(f)

uc_app_numbers = set()
appnum_pattern = r'(?:application|app\.? number)\s*\(?\s*([A-Z]{2}-[0-9A-Z-]+)\s*\)?'

for entry in uc_data:
    patents_info = entry.get('Patents_info', '')
    match = re.search(appnum_pattern, patents_info, re.IGNORECASE)
    if match:
        app_num = match.group(1).strip()
        app_num = re.sub(r'\s*-\s*', '-', app_num)
        uc_app_numbers.add(app_num)

print('UC application numbers:')
for i, app_num in enumerate(list(uc_app_numbers)[:10]):
    print(str(i+1) + '. ' + app_num)

print('\nTotal UC app numbers: ' + str(len(uc_app_numbers)))

result = {
    'uc_app_count': len(uc_app_numbers),
    'uc_apps_sample': list(uc_app_numbers)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['cpc_definition'], 'var_functions.execute_python:22': 'Loaded 169 UNIV CALIFORNIA patents', 'var_functions.execute_python:24': {'count': 59, 'sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'US-9061071-B2', 'EP-0826155-A4', 'RO-70061-A', 'WO-2021102420-A1', 'WO-2012162563-A2']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': 'Proceed to loading citation data', 'var_functions.execute_python:30': 'UC data loaded successfully', 'var_functions.execute_python:32': 'Citation data loaded, 277813 records', 'var_functions.execute_python:34': {'citing_assignee_count': 0, 'top_assignees': []}, 'var_functions.execute_python:36': {'citing_assignees_count': 1, 'matches_found': 1, 'top_assignees': ['US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.']}, 'var_functions.execute_python:40': {'total_citations': 1, 'unique_assignees': 1, 'assignees': ['The US patent']}, 'var_functions.execute_python:42': {'total_records': 277813, 'samples': [{'index': 0, 'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-H01209663-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 1, 'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "DE-3533193-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 2, 'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "JP-S53139639-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n '}, {'index': 3, 'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "EP-0126544-A2",\n    "type": ""\n  },\n  {\n    "application_number": "",\n  '}, {'index': 4, 'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.', 'citation_preview': '[\n  {\n    "application_number": "",\n    "category": "APP",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4051340-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n   '}]}, 'var_functions.execute_python:44': {'uc_patents': 59, 'citations_found': 0, 'sample': []}, 'var_functions.query_db:46': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}, {'symbol': 'A01K2227/106', 'titleFull': 'Primate'}, {'symbol': 'A01K2227/706', 'titleFull': 'Insects, e.g. Drosophila melanogaster, medfly'}, {'symbol': 'A01K2227/703', 'titleFull': 'Worms, e.g. Caenorhabdities elegans'}, {'symbol': 'A01K2267/025', 'titleFull': 'Animal producing cells or organs for transplantation'}, {'symbol': 'A01K2267/0393', 'titleFull': 'Animal model comprising a reporter system for screening tests'}], 'var_functions.execute_python:50': {'total_citations': 1, 'unique_assignees': 1, 'unique_subclasses': 0, 'assignees_list': ['US patent application (no'], 'subclasses_list': [], 'total_rows_needed': 0}, 'var_functions.execute_python:52': {'uc_patent_count': 59, 'matches_found': 0, 'sample_matches': []}, 'var_functions.execute_python:60': {'cited_count': 103, 'uc_count': 59, 'overlap': 0, 'cited_sample': ['JP-H01209663-A', 'JP-H0737617-A', 'WO-9744842-A1', 'JP-H09330720-A', 'JP-H10294100-A'], 'uc_sample': ['US-2022074631-A1', 'TW-201925402-A', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1']}}

exec(code, env_args)
