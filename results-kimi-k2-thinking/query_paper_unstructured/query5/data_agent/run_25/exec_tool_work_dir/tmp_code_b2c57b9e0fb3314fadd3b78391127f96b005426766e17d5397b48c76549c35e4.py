code = """import json, os
# Load the citations for 2020
citations_2020 = locals().get('var_functions.query_db:2')
print('Citations 2020 sample:')
print(citations_2020[:5])
# Also load the paper docs file path
paper_docs_file = locals().get('var_functions.query_db:5')
print('Paper docs file path:', paper_docs_file)
# Read the file
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)
print('Number of paper docs:', len(paper_docs))
# Show a sample doc
print(paper_docs[0]['filename'])
print(paper_docs[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
