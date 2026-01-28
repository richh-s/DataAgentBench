code = """import json
import re
from collections import defaultdict

# Load full patent dataset
full_data_path = locals()['var_functions.query_db:20']
with open(full_data_path, 'r') as f:
    all_patents = json.load(f)

# Load UC cited pubs
uc_cited_pubs = set(json.loads(locals()['var_functions.execute_python:20']).get('sample_uc_cited', []))

# For real processing, we need to use the full uc_cited_pubs set
# Let's recalculate it from the UC data
with open(locals()['var_functions.query_db:16'], 'r') as f:
    uc_patents = json.load(f)

uc_cited_pubs_full = set()
for row in uc_patents:
    citation_str = row['citation']
    if citation_str:
        try:
            citations = json.loads(citation_str)
            for citation in citations:
                pub_num = citation.get('publication_number', '')
                if pub_num:
                    uc_cited_pubs_full.add(pub_num)
        except:
            continue

print('__RESULT__:')
print(json.dumps({
    'total_uc_cited_pubs': len(uc_cited_pubs_full),
    'sample': list(uc_cited_pubs_full)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_records': 169, 'total_citations': 1308, 'sample': [{'publication_number': 'US-4599677-A', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2015129765-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'FR-3105380-A1', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-11466906-B2', 'source_patent': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'publication_number': 'US-2001053519-A1', 'source_patent': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}, 'var_functions.execute_python:10': {'total_cited_publications': 1112, 'sample_pubs': ['WO-2013025632-A1', 'US-2020023209-A1', 'US-6200265-B1', 'EP-2694154-A1', 'US-9974593-B2', 'US-5366770-A', 'US-8865406-B2', 'US-2006105322-A1', 'US-7757565-B2', 'US-2014356956-A1', 'JP-H11261169-A', 'US-2016242650-A1', 'US-2014356867-A1', 'WO-2014093712-A1', 'US-8080523-B2', 'WO-2013169802-A1', 'WO-2010144578-A2', 'EP-2515996-A2', 'US-2011281288-A1', 'US-2012065087-A1']}, 'var_functions.execute_python:12': {'message': 'Created cited_pubs.json with all cited publication numbers', 'count': 1112}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_patents': 277813, 'total_uc_cited_pubs': 1112, 'sample_uc_cited': ['US-2014170753-A1', 'US-2003222263-A1', 'FR-1447611-A', 'US-5710621-A', 'US-5019504-A', 'US-5125736-A', 'US-4911920-A', 'US-6303344-B1', 'US-9057109-B2', 'US-5532071-A']}}

exec(code, env_args)
