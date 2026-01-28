code = """import json

# Get the file paths from the stored variables
# The tool results are stored with these specific keys
papers_key = [k for k in locals().keys() if 'query_db_40' in k][0]
citations_key = [k for k in locals().keys() if 'query_db_56' in k][0]

papers_file_path = locals()[papers_key]
citations_file_path = locals()[citations_key]

print('Papers file:', papers_file_path)
print('Citations file:', citations_file_path)

# Load papers data
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Load citations data
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

print('Loaded', len(papers), 'papers')
print('Loaded', len(citations), 'citation records')

# Extract food paper titles
food_titles = set()
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt
        # Check if paper discusses food
        text = paper.get('text', '').lower()
        food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
        if any(keyword in text for keyword in food_keywords):
            food_titles.add(title)

print('Food papers found:', len(food_titles))

# Calculate total citations
from collections import defaultdict
paper_citations = defaultdict(int)
for citation in citations:
    title = citation.get('title', '')
    if title in food_titles:
        paper_citations[title] += int(citation.get('citation_count', 0))

total_food_citations = sum(paper_citations.values())
print('Total citations for food domain:', total_food_citations)

# Format and print result
result = {"total_food_citations": total_food_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
