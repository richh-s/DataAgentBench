code = """import json
import re
import sqlite3
import pandas as pd

# Get the file path for university of california patents
file_path = locals()['var_functions.query_db:20']

# Read all patents assigned to UNIV CALIFORNIA
with open(file_path, 'r') as f:
    uc_patents = json.load(f)

print('Total UC patents found:', len(uc_patents))

# Let's look at the structure of citations and how to extract cited patent numbers
citations_data = []
for patent in uc_patents:
    citations_str = patent.get('citation', '[]')
    if citations_str and citations_str != '[]':
        try:
            citations = json.loads(citations_str)
            for citation in citations:
                if citation.get('publication_number'):
                    citations_data.append({
                        'uc_patent_info': patent['Patents_info'],
                        'cited_pub_num': citation['publication_number'],
                        'uc_cpc_codes': patent.get('cpc', '[]')
                    })
        except:
            continue

print('Total citations from UC patents:', len(citations_data))

# Show sample
if citations_data:
    print('Sample citation data:')
    for i, item in enumerate(citations_data[:3]):
        print(f"  {i+1}. UC: {item['uc_patent_info'][:80]}...")
        print(f"     Cited: {item['cited_pub_num']}")

print('__RESULT__:')
print(json.dumps({'total_uc_patents': len(uc_patents), 'total_citations': len(citations_data)}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:10': ['cpc_definition'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'sample_patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'sample_citation_type': "<class 'str'>", 'sample_citation_length': 653}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
