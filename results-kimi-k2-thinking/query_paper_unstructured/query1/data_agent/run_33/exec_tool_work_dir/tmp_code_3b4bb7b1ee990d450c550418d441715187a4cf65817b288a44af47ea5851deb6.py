code = """import json

# The query_db:2 result is stored as a file path since it's too large
papers_file = var_functions.query_db_2
citations = var_functions.query_db_5

print('Papers file path:', papers_file)
print('Citations count:', len(citations))

# Read papers data from file
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Total papers:', len(papers))

# Find all unique paper titles from filenames
all_paper_titles = set()
food_paper_titles = set()

for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt
        all_paper_titles.add(title)
        
        # Check if paper mentions food in its text
        text = paper.get('text', '').lower()
        if 'food' in text:
            food_paper_titles.add(title)

print('All papers:', len(all_paper_titles))
print('Food papers:', len(food_paper_titles))

# Sum citations for food domain papers
total_citation_count = 0
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_paper_titles:
        total_citation_count += int(citation.get('citation_count', 0))

print('Total citations for food papers:', total_citation_count)

# Print result in required format
result_json = json.dumps({"total_food_citations": total_citation_count})
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
