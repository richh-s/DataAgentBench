code = """import json
import re

# Step 1: Extract all UNIV CALIFORNIA publication numbers
uc_file = locals().get('var_functions.query_db:30')
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Extract UC publication numbers using regex patterns
uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    # Match patterns like "pub. number US-2022074631-A1" or "with publication number US-11081687-B2"
    matches = re.findall(r'(?:pub\. number|publication number|with pub\. number|has pub\. number|has publication number|with publication number|with publication no\.)\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    uc_pub_numbers.update(matches)

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_data),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'sample_uc_pub_numbers': list(uc_pub_numbers)[:15]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}, 'var_functions.execute_python:26': {'uc_patents_count': 169, 'uc_pub_numbers_count': 322, 'nonuc_patents_checked': 1000, 'citing_patents_found': 0}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_patents': 169, 'uc_pub_numbers': 322, 'sample_numbers': ['US-6980295-B2', 'US-201515329526-A', 'CN-200380105631-A', 'US-37750473-A', 'US-58729205-A', 'US-11607427-B2', 'US-2017031596-W', 'US-6750960-B2', 'KR-20087016723-A', 'IL-236725-A']}, 'var_functions.execute_python:38': {'uc_patents_count': 169, 'uc_pub_numbers_count': 0, 'nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_citations': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_uc_records': 169, 'first_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'sample_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.query_db:44': [{'total_patents': '277813'}], 'var_functions.execute_python:46': {'total_uc_patents': 169, 'total_uc_pub_numbers': 56, 'total_nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_uc_numbers': ['AU-2007297661-A1', 'US-2006051790-A1', 'AU-6535890-A', 'US-2022018060-A1', 'TW-201925402-A', 'CN-103189548-A', 'AU-2003297741-A1', 'AU-2010214112-B2', 'US-2023155090-A1', 'KR-20200041324-A'], 'sample_citing': []}}

exec(code, env_args)
