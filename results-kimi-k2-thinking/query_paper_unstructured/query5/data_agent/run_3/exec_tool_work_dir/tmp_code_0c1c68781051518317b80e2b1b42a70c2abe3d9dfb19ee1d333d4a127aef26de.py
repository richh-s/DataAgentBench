code = """import json
import re

# Read the first file path
citations_path = '/tmp/tmp2z8w3o6p.json'
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Read the second file path
papers_path = '/tmp/tmp6d_j7p0h.json'
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

print('Number of citations records:', len(citations_data))
print('Number of paper documents:', len(papers_data))
print('\nSample citation record:', citations_data[0])
print('\nSample paper document keys:', list(papers_data[0].keys()) if papers_data else 'No data')
print('\nSample paper document filename:', papers_data[0].get('filename', 'N/A'))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
