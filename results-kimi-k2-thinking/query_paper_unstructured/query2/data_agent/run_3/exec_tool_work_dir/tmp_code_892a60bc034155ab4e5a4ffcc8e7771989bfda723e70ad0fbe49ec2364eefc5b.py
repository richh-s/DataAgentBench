code = """import json

# Read the citation data from the file
citation_file = 'file_storage/functions.query_db:24.json'
with open(citation_file, 'r') as f:
    citations_2018 = json.load(f)

print('Number of citation records in 2018:', len(citations_2018))
print('First record:', citations_2018[0] if citations_2018 else 'None')

# Now let's get paper documents to find which ones were published by ACM
paper_key = 'var_functions.query_db:20'
paper_file = 'file_storage/functions.query_db:20.json'

try:
    with open(paper_file, 'r') as f:
        paper_docs = json.load(f)
    print('Number of paper documents:', len(paper_docs))
    print('First paper doc keys:', list(paper_docs[0].keys()) if paper_docs else 'None')
except:
    print('Could not load paper documents')
    paper_docs = []

result = {
    'citations_count': len(citations_2018),
    'paper_count': len(paper_docs),
    'has_citations': len(citations_2018) > 0,
    'has_papers': len(paper_docs) > 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': "<class 'str'>", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'count': 39, 'has_data': True}, 'var_functions.execute_python:28': {'type': "<class 'str'>", 'is_list': False, 'is_string': True}, 'var_functions.execute_python:30': {'source': 'file_path_or_other', 'data_type': "<class 'str'>", 'count': 0}, 'var_functions.execute_python:32': {'file_path': 'file_storage/functions.query_db:24.json', 'path_exists': True}}

exec(code, env_args)
