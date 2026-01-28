code = """import json

# Load papers data from the file path stored in var_functions.query_db_40
papers_file_path = var_functions.query_db_40
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Load citations data from var_functions.query_db_5
citations = var_functions.query_db_5

print('Number of papers loaded:', len(papers))
print('Number of citations loaded:', len(citations))

# Create a set of food paper titles
food_titles = set()
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        # Check if paper is about food (search in text)
        text = paper.get('text', '').lower()
        if 'food' in text or 'diet' in text or 'nutrition' in text or 'eating' in text:
            food_titles.add(title)

print('Food papers found:', len(food_titles))

# Calculate total citations for food papers
total_citations = 0
food_citation_count = 0
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_titles:
        total_citations += int(citation.get('citation_count', 0))
        food_citation_count += 1

print('Citations matched to food papers:', food_citation_count)
print('Total citation count for food domain:', total_citations)

# Output result in required format
result = {"total_food_citations": total_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
