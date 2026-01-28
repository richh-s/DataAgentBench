code = """import json
import re

# Read the California patents data
california_data_path = locals()['var_functions.query_db:5']
with open(california_data_path, 'r') as f:
    california_patents = json.load(f)

# Process to extract patent publication numbers from citations
all_cited_pubs = set()
citations_by_california_patent = []

for patent in california_patents:
    patent_info = patent['Patents_info']
    citations = patent.get('citation', '[]')
    
    # Parse citation JSON if it's a string
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    
    cited_pubs_for_this_patent = []
    for citation in citations:
        pub_num = citation.get('publication_number')
        npl_text = citation.get('npl_text', '')
        # Only include citations with publication numbers (patents, not NPL)
        if pub_num and 'US-' in pub_num.upper() and not npl_text:
            all_cited_pubs.add(pub_num)
            cited_pubs_for_this_patent.append(pub_num)
    
    citations_by_california_patent.append({
        'california_patent_info': patent_info,
        'cited_publication_numbers': cited_pubs_for_this_patent
    })

print('__RESULT__:')
print(json.dumps({
    "total_california_patents": len(california_patents),
    "total_cited_publications": len(all_cited_pubs),
    "sample_cited_publications": list(all_cited_pubs)[:10],
    "citations_by_patent": citations_by_california_patent
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json', 're'], 'var_functions.execute_python:12': {'california_patents_path': 'file_storage/functions.query_db:5.json', 'table_list_path': ['publicationinfo']}, 'var_functions.execute_python:14': {'num_california_patents': 5, 'sample_patent_citations': '[\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-4599677-A",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-2015129765-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "FR-3105380-A1",\n    "type": ""\n  },\n  {\n    "application_number": "",\n    "category": "SEA",\n    "filing_date": 0,\n    "npl_text": "",\n    "publication_number": "US-11466906-B2",\n    "type": ""\n  }\n]'}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
