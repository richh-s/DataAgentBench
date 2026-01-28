code = """import json
import re

# Access the result from storage using locals()
result_var = locals()['var_functions.query_db:12']

# Read the full result from the previous query
if isinstance(result_var, str) and result_var.endswith('.json'):
    with open(result_var, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_var

# Extract all UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Look for patterns like "pub. number XXXXX" or "publication number XXXXX"
    match = re.search(r'pub\. number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if not match:
        match = re.search(r'publication number\s+([A-Z0-9\-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)

# Also try to extract from citation field patterns which might include publication numbers
for patent in uc_patents:
    citation = patent.get('citation', '')
    if citation and citation != '[]':
        try:
            citations = json.loads(citation) if isinstance(citation, str) else citation
            if isinstance(citations, list):
                for cite in citations:
                    pub_num = cite.get('publication_number')
                    if pub_num:
                        uc_pub_numbers.add(pub_num)
        except:
            pass

print('__RESULT__:')
print(json.dumps({
    'uc_patents_count': len(uc_patents),
    'total_unique_uc_pub_numbers': len(uc_pub_numbers),
    'uc_pub_numbers': list(uc_pub_numbers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'uc_patents_count': 169, 'uc_pub_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2'], 'total_uc_pub_numbers': 114}}

exec(code, env_args)
