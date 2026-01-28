code = """import json
import re

# List available variables
print("Available variables:", list(locals().keys()))

# Check if we have the data
papers_key = 'var_functions.query_db:38'
citations_key = 'var_functions.query_db:36'

if papers_key in locals():
    papers_data = locals()[papers_key]
    print(f"Type of papers_data: {type(papers_data)}")
    if isinstance(papers_data, str) and papers_data.endswith('.json'):
        # It's a file path
        with open(papers_data, 'r') as f:
            papers_data = json.load(f)
    print(f"Loaded {len(papers_data)} papers")
else:
    print(f"Papers data not found in {papers_key}")

if citations_key in locals():
    citations_data = locals()[citations_key]
    print(f"Type of citations_data: {type(citations_data)}")
    if isinstance(citations_data, str) and citations_data.endswith('.json'):
        # It's a file path
        with open(citations_data, 'r') as f:
            citations_data = json.load(f)
    print(f"Loaded {len(citations_data)} citation records")
else:
    print(f"Citations data not found in {citations_key}")

# Try to find the data in other variables
for var_name in locals().keys():
    if 'query_db' in var_name:
        print(f"Found potential data in {var_name}")
        data = locals()[var_name]
        print(f"  Type: {type(data)}, Sample: {str(data)[:100] if data else 'None'}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
