code = """import json

# Load the cited publication map from previous step
file_path = locals()['var_functions.query_db:30']

with open(file_path, 'r') as f:
    univ_calif_data = json.load(f)

# Build a set of all cited publication numbers
all_cited_pubs = set()
for rec in univ_calif_data:
    citations_str = rec['citation']
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for cite in citations:
                if cite.get('publication_number'):
                    all_cited_pubs.add(cite['publication_number'])
        except:
            pass

# For the next step, we need to query which of these cited patents cite UNIV CALIFORNIA
# Actually, we need to find patents that cite UNIV CALIFORNIA patents
# Let me reframe: We need to find patents that cite UNIV CALIFORNIA patents, then get their assignees and CPC

# First, let's extract UNIV CALIFORNIA publication numbers
import re

univ_calif_pubs = set()
for rec in univ_calif_data:
    patents_info = rec['Patents_info']
    match = re.search(r'pub\. number\s+([A-Z]{2}-[^,\s]+)', patents_info)
    if match:
        pub_num = match.group(1)
        univ_calif_pubs.add(pub_num)
    else:
        match2 = re.search(r'publication number\s+([A-Z]{2}-[^,\s]+)', patents_info, re.IGNORECASE)
        if match2:
            pub_num = match2.group(1)
            univ_calif_pubs.add(pub_num)

result = {
    'total_cited_by_univ_calif': len(all_cited_pubs),
    'total_univ_calif_publications': len(univ_calif_pubs),
    'sample_univ_calif_pubs': list(univ_calif_pubs)[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}, 'var_functions.execute_python:36': {'total_univ_calif_patents': 169, 'unique_cited_publications': 1112, 'citations_with_pub_numbers': 1112}}

exec(code, env_args)
