code = """import json
import re

# Load UC patents data
uc_patents_file = locals()['var_functions.query_db:37']
with open(uc_patents_file, 'r') as f:
    uc_patents = json.load(f)

# Extract all UC publication numbers
uc_pub_numbers = set()
for record in uc_patents:
    patents_info = record.get('Patents_info', '')
    # Find publication numbers in various formats
    pub_matches = re.findall(r'[A-Z]{2}-\d+-[A-Z]\d+', patents_info)
    for pub in pub_matches:
        uc_pub_numbers.add(pub)

result_info = {
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_uc_pub_numbers': list(uc_pub_numbers)[:10]
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': {'status': 'no_valid_data', 'summary': {}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:18': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:24': [{'cid': '0', 'name': 'Patents_info', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'kind_code', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'application_kind', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'pct_number', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'family_id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'title_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '6', 'name': 'abstract_localized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '7', 'name': 'claims_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '8', 'name': 'description_localized_html', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '9', 'name': 'publication_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '10', 'name': 'filing_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '11', 'name': 'grant_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '12', 'name': 'priority_date', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '13', 'name': 'priority_claim', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '14', 'name': 'inventor_harmonized', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '15', 'name': 'examiner', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '16', 'name': 'uspc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '17', 'name': 'ipc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '18', 'name': 'cpc', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '19', 'name': 'citation', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '20', 'name': 'parent', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '21', 'name': 'child', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '22', 'name': 'entity_status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '23', 'name': 'art_unit', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': {'type': "<class 'str'>", 'is_list': True, 'record_count': 169}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:37': 'file_storage/functions.query_db:37.json', 'var_functions.execute_python:38': {'total_uc_patents': 169, 'uc_publication_numbers': ['US-6750960-B2', 'US-11667770-B2', 'US-10744347-B2', 'US-11607427-B2', 'EP-4284234-A1', 'US-2020283856-A1', 'US-10900049-B2', 'US-2017087258-A1', 'AU-2007297661-A1', 'US-11014955-B2', 'WO-2024050335-A2', 'WO-2018152537-A1', 'AU-2001296493-B2', 'US-7052856-B2', 'US-6767662-B2', 'WO-2024044766-A3', 'WO-2020096950-A1', 'CA-3161617-A1', 'US-2023171142-A1', 'US-2021282642-A1'], 'total_unique_pub_numbers': 124}}

exec(code, env_args)
