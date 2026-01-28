code = """import json

# Load papers from the file (var_functions.query_db:2 contains the file path)
papers_file_path = var_functions.query_db_2
citations = var_functions.query_db_5

print('Papers file path:', papers_file_path)
print('Citations count:', len(citations))

# Read and parse papers
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

print('Papers count:', len(papers))

# Find food papers (using filename and text content)
food_paper_titles = set()

for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        
        # Check if paper is about food (case-insensitive search in text)
        text = paper.get('text', '').lower()
        if 'food' in text or 'diet' in text or 'nutrition' in text:
            food_paper_titles.add(title)

print('Food papers found:', len(food_paper_titles))

# Calculate total citations for food papers
total_citations = 0
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_paper_titles:
        total_citations += int(citation.get('citation_count', 0))

result = {'total_food_citations': total_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
