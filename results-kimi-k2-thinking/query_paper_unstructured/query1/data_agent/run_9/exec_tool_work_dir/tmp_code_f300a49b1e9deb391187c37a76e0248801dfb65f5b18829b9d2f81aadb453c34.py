code = """import json

# Load the paper documents - food domain papers
with open('var_functions.query_db:20', 'r') as f:
    food_papers = json.load(f)

# Load all citations
with open('var_functions.query_db:8', 'r') as f:
    citations = json.load(f)

print("Found", len(food_papers), "potential food-related papers")
print("Found", len(citations), "total citation records")

# Extract titles from food papers (remove .txt extension)
food_titles = []
for paper in food_papers:
    filename = paper['filename']
    # Remove .txt extension to get the title
    title = filename.replace('.txt', '')
    food_titles.append(title)

print("Food paper titles sample:", food_titles[:3])

# Create a set for easy lookup
food_titles_set = set(food_titles)

# Filter citations for food papers
food_citations = []
total_citations = 0

for citation in citations:
    cit_title = citation['title']
    if cit_title in food_titles_set:
        count = int(citation['total_citations'])
        food_citations.append({
            'title': cit_title,
            'citations': count
        })
        total_citations += count

print("Found", len(food_citations), "food papers with citations")
print("Total citations for food domain:", total_citations)

# Print result in required format
result = str(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
