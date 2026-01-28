code = """import json
# Access the file path from storage
file_path = locals()['var_functions.query_db:16']
print(f"File path: {file_path}")
# Read the paper data
with open(file_path, 'r') as f:
    papers = json.load(f)
print(f"Total papers mentioning 2016: {len(papers)}")
# Filter for physical activity domain
physical_activity_papers = []
for paper in papers:
    if 'physical activity' in paper['text'].lower():
        physical_activity_papers.append(paper)
print(f"Papers in physical activity domain: {len(physical_activity_papers)}")
# Extract titles
titles = [p['filename'].replace('.txt', '') for p in physical_activity_papers]
print(f"Sample titles: {titles[:3]}")
----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers),
    "pa_papers": len(physical_activity_papers),
    "titles": titles
}))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
