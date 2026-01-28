code = """import json
import os

# Access the stored results
citations_data = locals()['var_functions.query_db:2']
paper_docs_data = locals()['var_functions.query_db:3']

result = {
    'citations_type': str(type(citations_data)),
    'paper_docs_type': str(type(paper_docs_data)),
    'citations_is_str': isinstance(citations_data, str),
    'paper_docs_is_str': isinstance(paper_docs_data, str)
}

# If they are file paths, check if files exist
if isinstance(citations_data, str):
    result['citations_file_exists'] = os.path.exists(citations_data)
if isinstance(paper_docs_data, str):
    result['paper_docs_file_exists'] = os.path.exists(paper_docs_data)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 1, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 2, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 3, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 4, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 5, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 6, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 7, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 8, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}, {'index': 9, 'filename': '', 'years_found': [], 'venues_found': [], 'has_physical_activity': False, 'text_preview': ''}]}

exec(code, env_args)
