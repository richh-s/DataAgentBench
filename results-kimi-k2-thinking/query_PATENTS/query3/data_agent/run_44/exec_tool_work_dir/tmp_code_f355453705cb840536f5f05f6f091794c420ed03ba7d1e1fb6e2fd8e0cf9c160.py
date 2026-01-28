code = """import json
import re

# Load UNIV CALIFORNIA patent data to extract their publication numbers
uc_file = locals().get('var_functions.query_db:30')
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Extract UNIV CALIFORNIA publication numbers using multiple patterns
uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    
    # Pattern 1: "pub. number XXXXX"
    matches1 = re.findall(r'pub\.\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 2: "publication number XXXXX"
    matches2 = re.findall(r'publication\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 3: "has pub. number XXXXX"
    matches3 = re.findall(r'has\s+pub\.\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 4: "with pub. number XXXXX"
    matches4 = re.findall(r'with\s+pub\.\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 5: "with publication number XXXXX"
    matches5 = re.findall(r'with\s+publication\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 6: "has publication number XXXXX"
    matches6 = re.findall(r'has\s+publication\s*number\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    # Pattern 7: "with publication no. XXXXX"
    matches7 = re.findall(r'with\s+publication\s+no\.\s+([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info, re.IGNORECASE)
    
    all_matches = matches1 + matches2 + matches3 + matches4 + matches5 + matches6 + matches7
    uc_pub_numbers.update(all_matches)

print('__RESULT__:')
print(json.dumps({
    'uc_patents_analyzed': len(uc_data),
    'uc_publication_numbers': len(uc_pub_numbers),
    'uc_sample': list(uc_pub_numbers)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}, 'var_functions.execute_python:26': {'uc_patents_count': 169, 'uc_pub_numbers_count': 322, 'nonuc_patents_checked': 1000, 'citing_patents_found': 0}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_patents': 169, 'uc_pub_numbers': 322, 'sample_numbers': ['US-6980295-B2', 'US-201515329526-A', 'CN-200380105631-A', 'US-37750473-A', 'US-58729205-A', 'US-11607427-B2', 'US-2017031596-W', 'US-6750960-B2', 'KR-20087016723-A', 'IL-236725-A']}, 'var_functions.execute_python:38': {'uc_patents_count': 169, 'uc_pub_numbers_count': 0, 'nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_citations': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_uc_records': 169, 'first_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'sample_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.query_db:44': [{'total_patents': '277813'}], 'var_functions.execute_python:46': {'total_uc_patents': 169, 'total_uc_pub_numbers': 56, 'total_nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_uc_numbers': ['AU-2007297661-A1', 'US-2006051790-A1', 'AU-6535890-A', 'US-2022018060-A1', 'TW-201925402-A', 'CN-103189548-A', 'AU-2003297741-A1', 'AU-2010214112-B2', 'US-2023155090-A1', 'KR-20200041324-A'], 'sample_citing': []}, 'var_functions.execute_python:48': {'uc_patents_count': 169, 'uc_pub_numbers_count': 134, 'sample_uc_pub_numbers': ['EP-2029921-A4', 'AU-7724398-A', 'US-9061071-B2', 'JP-2009260386-A', 'CN-102584712-A', 'US-2022018060-A1', 'KR-20160119166-A', 'CN-100339724-C', 'US-2006292670-A1', 'US-11376346-B2', 'CA-2550552-A1', 'US-2021181673-A1', 'WO-2024044766-A3', 'US-11421276-B2', 'JP-2005104983-A']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
