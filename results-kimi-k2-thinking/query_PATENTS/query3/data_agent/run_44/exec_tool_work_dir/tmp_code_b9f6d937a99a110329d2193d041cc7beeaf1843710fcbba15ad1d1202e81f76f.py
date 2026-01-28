code = """import json
import re

# Load UNIV CALIFORNIA patents
uc_file = locals().get('var_functions.query_db:30')
with open(uc_file, 'r') as f:
    uc_data = json.load(f)

# Extract UC publication numbers
uc_pub_numbers = set()
for record in uc_data:
    info = record.get('Patents_info', '')
    # Look for publication number patterns like US-2022074631-A1
    matches = re.findall(r'pub\. number ([A-Z]{2}-\d{6,12}-[A-Z]\d?)', info)
    uc_pub_numbers.update(matches)

# Load non-UC patents with citations
nonuc_file = locals().get('var_functions.query_db:28')
with open(nonuc_file, 'r') as f:
    nonuc_data = json.load(f)

# Find patents that cite UC patents and extract assignees and CPCs
citing_info = []
for record in nonuc_data:
    # Extract assignee (first listed entity before "holds" or similar)
    info = record.get('Patents_info', '')
    assignee_match = re.search(r'^([^,]+?)(?: holds| is| from|,)', info)
    assignee = assignee_match.group(1).strip() if assignee_match else 'Unknown'
    
    # Skip UC patents
    if 'UNIV CALIFORNIA' in assignee.upper() or 'UNIVERSITY OF CALIFORNIA' in assignee.upper():
        continue
    
    # Check citations
    citations = record.get('citation', '[]')
    try:
        citation_list = json.loads(citations) if citations else []
    except:
        citation_list = []
    
    # Check if this patent cites any UC patent
    cites_uc = False
    for citation in citation_list:
        pub_num = citation.get('publication_number')
        if pub_num and pub_num in uc_pub_numbers:
            cites_uc = True
            break
    
    if cites_uc:
        cpc_data = record.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_data) if cpc_data else []
        except:
            cpc_list = []
        
        # Extract primary CPC subclasses (first 4 characters after section)
        cpc_subclasses = []
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict):
                code = cpc_item.get('code', '')
            else:
                code = str(cpc_item)
            
            # CPC format: Section (1 char), Class (2 digits), Subclass (1 letter), Group (1-3 digits), Subgroup (2-6 digits)
            # We want the subclass level: e.g., from "H01L21/02" we want "H01L"
            if len(code) >= 4:
                subclass = code[:4]
                cpc_subclasses.append(subclass)
        
        citing_info.append({
            'assignee': assignee,
            'cpc_subclasses': list(set(cpc_subclasses))  # Remove duplicates
        })

print('__RESULT__:')
print(json.dumps({
    'total_uc_patents': len(uc_data),
    'total_uc_pub_numbers': len(uc_pub_numbers),
    'total_nonuc_patents_checked': len(nonuc_data),
    'citing_patents_found': len(citing_info),
    'sample_uc_numbers': list(uc_pub_numbers)[:10],
    'sample_citing': citing_info[:5]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'count': 169, 'first_keys': ['Patents_info', 'citation'], 'first_patent_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'first_citation_len': 653}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'message': 'Loaded UNIV CALIFORNIA patents', 'count': 169}, 'var_functions.execute_python:22': {'uc_patents_count': 169}, 'var_functions.execute_python:24': {'uc_patents': 169, 'nonuc_patents': 1000, 'uc_pub_numbers_found': 322, 'sample_uc_numbers': ['US-202318169681-A', 'CN-96195210-A', 'AU-2005269556-A', 'AU-5711401-A', 'US-201313787160-A', 'US-201514981715-A', 'US-202218054917-A', 'US-2019021660-W', 'CA-3027364-A1', 'US-2023321419-A1']}, 'var_functions.execute_python:26': {'uc_patents_count': 169, 'uc_pub_numbers_count': 322, 'nonuc_patents_checked': 1000, 'citing_patents_found': 0}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'uc_patents': 169, 'uc_pub_numbers': 322, 'sample_numbers': ['US-6980295-B2', 'US-201515329526-A', 'CN-200380105631-A', 'US-37750473-A', 'US-58729205-A', 'US-11607427-B2', 'US-2017031596-W', 'US-6750960-B2', 'KR-20087016723-A', 'IL-236725-A']}, 'var_functions.execute_python:38': {'uc_patents_count': 169, 'uc_pub_numbers_count': 0, 'nonuc_patents_checked': 2000, 'citing_patents_found': 0, 'sample_citations': []}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_uc_records': 169, 'first_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'sample_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, 'var_functions.query_db:44': [{'total_patents': '277813'}]}

exec(code, env_args)
