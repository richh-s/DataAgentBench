code = """import json
# Get the file path from storage
file_path = locals()['var_functions.query_db:26']
print(f"File path: {file_path}")

# Read the data
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

# Find papers from 2016 in physical activity domain
papers_2016_pa = []
for paper in papers:
    text = paper['text']
    # Check if it contains both 2016 and physical activity
    if '2016' in text and 'physical activity' in text.lower():
        title = paper['filename'].replace('.txt', '')
        papers_2016_pa.append(title)

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")
print(f"Sample titles: {papers_2016_pa[:5]}")

result = {
    'count': len(papers_2016_pa),
    'titles': papers_2016_pa
}

----BEGIN PRINT FORMAT----
print('__RESULT__:')
print(json.dumps(result))
----END PRINT FORMAT----"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
