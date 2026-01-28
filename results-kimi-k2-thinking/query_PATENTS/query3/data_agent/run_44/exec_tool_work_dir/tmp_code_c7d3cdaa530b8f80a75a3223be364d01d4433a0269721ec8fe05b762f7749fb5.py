code = """import json
import re

# Load UNIV CALIFORNIA patent info file
uc_file = locals().get('var_functions.query_db:30')
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Debug the structure and content
print('__RESULT__:')
print(json.dumps({
    'total_uc_records': len(uc_data),
    'first_record': uc_data[0] if uc_data else None,
    'sample_info': uc_data[0].get('Patents_info', '')[:200] if uc_data else ''
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}, 'var_functions.execute_python:26': {'uc_patents_count': 169, 'uc_pub_numbers_count': 322, 'nonuc_patents_checked': 1000, 'citing_patents_found': 0}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_patents': 169, 'uc_pub_numbers': 322, 'sample_numbers': ['US-6980295-B2', 'US-201515329526-A', 'CN-200380105631-A', 'US-37750473-A', 'US-58729205-A', 'US-11607427-B2', 'US-2017031596-W', 'US-6750960-B2', 'KR-20087016723-A', 'IL-236725-A']}, 'var_functions.execute_python:38': {'uc_patents_count': 169, 'uc_pub_numbers_count': 0, 'nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_citations': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
