code = """import json
import os

# Load papers data
papers_path = 'var_functions.query_db:2.json'
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations data from variable
citations = var_functions.query_db_5

print('Papers count:', len(papers))
print('Citations count:', len(citations))

# Create a map of paper titles from papers (extract from filename)
paper_titles_map = {}
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]
        paper_titles_map[title.lower()] = title

print('Unique paper titles:', len(paper_titles_map))

# Join papers with citations to find food domain papers
citations_with_titles = []
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title:
        # Match case-insensitively
        lower_title = cit_title.lower()
        if lower_title in paper_titles_map:
            paper_title = paper_titles_map[lower_title]
            citations_with_titles.append({
                'title': paper_title,
                'citation_count': int(citation.get('citation_count', 0)),
                'citation_year': citation.get('citation_year')
            })

print('Matched citations to papers:', len(citations_with_titles))

# Now check which papers are in food domain
food_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    # Check for food-related terms
    food_terms = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    has_food = any(term in text for term in food_terms)
    if has_food:
        filename = paper.get('filename', '')
        if filename and filename.endswith('.txt'):
            title = filename[:-4]
            food_papers.append(title)

print('Food papers identified:', len(food_papers))

# Filter citations to only food papers
food_citations = []
for cit in citations_with_titles:
    if cit['title'] in food_papers:
        food_citations.append(cit)

print('Food citations:', len(food_citations))

# Calculate total citation count for food papers
total_citations = sum(cit['citation_count'] for cit in food_citations)
print('Total food citations count:', total_citations)

# Display sample of food papers
if food_papers:
    print('\nSample food papers:')
    for i, title in enumerate(food_papers[:10]):
        print(f'{i+1}. {title}')"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
