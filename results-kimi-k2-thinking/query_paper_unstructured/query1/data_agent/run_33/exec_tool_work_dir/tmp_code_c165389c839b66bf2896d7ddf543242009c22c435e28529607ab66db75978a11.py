code = """import json

# Access the stored result variables directly
# papers_data_file contains the path to the papers JSON file
papers_data_file = var_functions.query_db_40

# citations_data contains the actual citations list
citations_data = var_functions.query_db_5

print('Papers file path:', papers_data_file)
print('Citations data type:', type(citations_data))
print('Number of citations:', len(citations_data))

# Load papers from file
with open(papers_data_file, 'r') as f:
    papers = json.load(f)

print('Number of papers loaded:', len(papers))

# Find food-related papers
food_paper_titles = set()
for paper in papers:
    filename = paper.get('filename', '')
    if filename and filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
        # Check if the paper text contains food-related keywords
        text_lower = paper.get('text', '').lower()
        if 'food' in text_lower or 'diet' in text_lower or 'nutrition' in text_lower or 'eating' in text_lower:
            food_paper_titles.add(title)

print('Food papers found:', len(food_paper_titles))

# Calculate total citations for food papers
total_food_citations = 0
food_citation_count = 0
for citation in citations_data:
    cit_title = citation.get('title', '')
    if cit_title in food_paper_titles:
        total_food_citations += int(citation.get('citation_count', 0))
        food_citation_count += 1

print('Citations matching food papers:', food_citation_count)
print('Total citation count for food domain:', total_food_citations)

# Output result in required JSON format
result = {"total_food_citations": total_food_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:38': ['paper_docs'], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json'}

exec(code, env_args)
