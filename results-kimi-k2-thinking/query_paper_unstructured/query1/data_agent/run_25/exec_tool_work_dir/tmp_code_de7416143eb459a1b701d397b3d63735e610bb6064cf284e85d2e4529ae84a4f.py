code = """import json

# Get the data from storage
citations_data = locals()['var_functions.query_db:26']
food_papers_data = locals()['var_functions.query_db:22']

# Parse citations data
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

# Parse food papers data
if isinstance(food_papers_data, str):
    with open(food_papers_data, 'r') as f:
        food_papers = json.load(f)
else:
    food_papers = food_papers_data

# Extract food paper titles
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        food_titles.append(title)

print("Food domain paper titles:")
for i, title in enumerate(food_titles, 1):
    print(f"{i}. {title}")

# Create a dictionary of citations by title
citations_dict = {item['title']: int(item['total_citations']) for item in citations}

# Get citation counts for food papers
food_citations = []
total_citations = 0

for title in food_titles:
    if title in citations_dict:
        count = citations_dict[title]
        food_citations.append((title, count))
        total_citations += count
    else:
        food_citations.append((title, 0))

print("\nCitation counts for food domain papers:")
for title, count in food_citations:
    print(f"{title}: {count}")

print(f"\nTotal citation count: {total_citations}")

result = {"total_citations": total_citations, "papers": food_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.list_db:20': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
