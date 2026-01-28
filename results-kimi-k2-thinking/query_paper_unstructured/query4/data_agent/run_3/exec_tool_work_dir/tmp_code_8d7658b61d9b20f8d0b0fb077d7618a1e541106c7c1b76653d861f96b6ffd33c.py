code = """import json
# Read the JSON file
file_path = var_functions.query_db:16
with open(file_path, 'r') as f:
    papers = json.load(f)
# Filter for physical activity papers published in 2016
results = []
for p in papers:
    text = p['text'].lower()
    if 'physical activity' in text:
        title = p['filename'].replace('.txt', '')
        results.append(title)
# Show summary
summary = {
    'total_papers_checked': len(papers),
    'physical_activity_papers': len(results),
    'sample_titles': results[:10]
}
print(json.dumps(summary))
----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps(summary))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
