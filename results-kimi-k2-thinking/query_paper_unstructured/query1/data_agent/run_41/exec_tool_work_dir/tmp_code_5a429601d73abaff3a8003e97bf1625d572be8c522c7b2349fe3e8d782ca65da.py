code = """import json
import re

# Get the citations data file path
citations_file_path = locals()['var_functions.query_db:14']

# Load citations data
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print(f"Total citation records: {len(citations_data)}")
print("Sample citations:", citations_data[:3])

# Calculate total citations across all papers
total_citations_all = sum(int(record['citation_count']) for record in citations_data)
print(f"Total citations across all papers: {total_citations_all}")

# Save result
result = {
    'total_citation_records': len(citations_data),
    'sample_records': citations_data[:3],
    'total_citations_all': total_citations_all
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': [{'total_citations': '1405'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
