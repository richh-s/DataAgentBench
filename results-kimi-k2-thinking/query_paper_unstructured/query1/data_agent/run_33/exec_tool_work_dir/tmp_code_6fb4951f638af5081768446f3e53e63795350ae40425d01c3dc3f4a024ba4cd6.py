code = """import json

# Access papers data - it's stored in a JSON file
papers_data = json.load(open('.storage/query_db_40.json', 'r'))
citations_data = json.load(open('.storage/query_db_41.json', 'r'))

print('Papers loaded:', len(papers_data))
print('Citations loaded:', len(citations_data))

# Find food papers
food_papers = []
for paper in papers_data:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        # Check if text mentions food
        text = paper.get('text', '').lower()
        if 'food' in text or 'diet' in text or 'nutrition' in text or 'eating' in text or 'meal' in text or 'calorie' in text:
            food_papers.append(title)

print('Food papers identified:', len(food_papers))

# Calculate total citations
total_citations = 0
for citation in citations_data:
    if citation.get('title') in food_papers:
        total_citations += int(citation.get('citation_count', 0))

print('Total citation count for food domain:', total_citations)
print('__RESULT__:')
print(json.dumps({"total_food_citations": total_citations}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
