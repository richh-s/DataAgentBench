code = """import json

# Load papers
papers_path = 'var_functions.query_db:2.json'
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
citations = var_functions.query_db_5

print('Papers loaded:', len(papers))
print('Citations loaded:', len(citations))

# Extract titles from papers
paper_titles = set()
food_papers = set()

for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        paper_titles.add(title)
        
        # Check if food related
        text = paper.get('text', '').lower()
        if 'food' in text or 'diet' in text or 'nutrition' in text or 'eating' in text:
            food_papers.add(title)

print('Total papers:', len(paper_titles))
print('Food papers:', len(food_papers))

# Match citations with food papers
total_citations = 0
matched_citations = 0

for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_papers:
        cit_count = int(citation.get('citation_count', 0))
        total_citations += cit_count
        matched_citations += 1

print('Matched citations:', matched_citations)
print('Total citation count for food domain:', total_citations)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
