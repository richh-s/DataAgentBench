code = """import json
import re
from collections import defaultdict

# Load California patents data
file_path = 'file_storage/functions.query_db:10.json'
with open(file_path, 'r') as f:
    cal_pats = json.load(f)

# Step 1: Extract cited publication numbers from California patents
cited_pubs = set()
for patent in cal_pats:
    citation_str = patent.get('citation', '[]')
    if citation_str and citation_str != '[]':
        try:
            citations = json.loads(citation_str)
            for cite in citations:
                pub_num = cite.get('publication_number')
                if pub_num:
                    cited_pubs.add(pub_num)
        except:
            # If parsing fails, skip
            pass

print('__RESULT__:')
print(json.dumps({
    'num_cal_pats': len(cal_pats),
    'num_cited_pubs': len(cited_pubs),
    'sample_cited': list(cited_pubs)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'type': "<class 'str'>", 'is_str': True, 'length': 39, 'preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'num_records': 169, 'sample_record': {'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'citation': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}}}

exec(code, env_args)
