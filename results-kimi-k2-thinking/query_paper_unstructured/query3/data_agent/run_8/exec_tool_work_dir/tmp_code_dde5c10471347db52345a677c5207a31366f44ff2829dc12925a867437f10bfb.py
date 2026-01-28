code = """import json
import re

# Access the result from the previous query
# The result is stored under key var_functions.query_db:14
result_key = var_functions.query_db:14

# If it's a file path, read it; if it's the actual data, use it
if isinstance(result_key, str) and (result_key.endswith('.json') or '/mnt/data/' in result_key):
    with open(result_key, 'r') as f:
        papers = json.load(f)
else:
    papers = result_key

print(f"__RESULT__:")
print(json.dumps({
    "total_papers_loaded": len(papers),
    "first_paper_preview": {
        "title": papers[0].get('filename', '').replace('.txt', '') if papers else None,
        "has_text": bool(papers[0].get('text', '')) if papers else False
    }
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
