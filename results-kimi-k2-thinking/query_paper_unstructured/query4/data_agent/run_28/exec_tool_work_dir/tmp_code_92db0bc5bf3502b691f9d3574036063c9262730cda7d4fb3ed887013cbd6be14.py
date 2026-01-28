code = """import json

# Access the raw results directly
citations_raw = locals()['var_functions.query_db:2']
paper_docs_raw = locals()['var_functions.query_db:3']

print('Type of citations_raw:', type(citations_raw))
print('Type of paper_docs_raw:', type(paper_docs_raw))

# Load the data properly
citations = citations_raw if isinstance(citations_raw, list) else json.load(open(citations_raw)) if isinstance(citations_raw, str) else []
paper_docs = paper_docs_raw if isinstance(paper_docs_raw, list) else json.load(open(paper_docs_raw)) if isinstance(paper_docs_raw, str) else []

print('Citations loaded:', len(citations))
print('Paper docs loaded:', len(paper_docs))

# Check if data is actually there
if citations:
    print('First citation:', citations[0])
    
if paper_docs:
    print('First paper doc:', paper_docs[0])
    # Check what's actually in the paper docs
    for key, value in paper_docs[0].items():
        print(f'  {key}: {type(value)}, length: {len(str(value)) if value else 0}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 1, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 2, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 3, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 4, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 5, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 6, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 7, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 8, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 9, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}]}

exec(code, env_args)
