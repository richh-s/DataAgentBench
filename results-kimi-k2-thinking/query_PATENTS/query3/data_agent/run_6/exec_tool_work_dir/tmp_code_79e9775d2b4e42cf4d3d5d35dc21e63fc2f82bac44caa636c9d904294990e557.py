code = """import json
import re

# Load UNIV CALIFORNIA data
file_path = locals()['var_functions.query_db:30']

with open(file_path, 'r') as f:
    univ_calif_data = json.load(f)

# Extract all cited publication numbers and map back to UNIV CALIFORNIA patents
cited_pub_map = {}  # cited_pub -> list of univ_calif patents that cite it
all_cited_pubs = set()

for rec in univ_calif_data:
    # Parse citations
    citations_str = rec['citation']
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for cite in citations:
                if cite.get('publication_number'):
                    cited_pub = cite['publication_number']
                    all_cited_pubs.add(cited_pub)
                    
                    # Map back to this UNIV CALIFORNIA patent
                    if cited_pub not in cited_pub_map:
                        cited_pub_map[cited_pub] = []
                    cited_pub_map[cited_pub].append(rec)
        except:
            pass

result = {
    'total_univ_calif_patents': len(univ_calif_data),
    'unique_cited_publications': len(all_cited_pubs),
    'citations_with_pub_numbers': len(cited_pub_map)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'total_univ_calif_patents': 169, 'total_extracted_pubs': 114, 'sample_pubs': ['US-2006292670-A1.', 'WO-2020055916-A9.', 'WO-2010045542-A3.', 'WO-2017214343-A1.', 'US-6980295-B2.', 'KR-20160119166-A.', 'CA-3161617-A1.', 'AU-2015364602-B2.', 'IL-274176-A.', 'US-2004115131-A1.']}}

exec(code, env_args)
