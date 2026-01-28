code = """import json

# Access the stored results
citations_file = locals()['var_functions.query_db:12']
food_papers = locals()['var_functions.execute_python:10']

# Load citations data
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Extract food paper titles from the previous result
food_titles = food_papers['food_paper_titles']

# Create a dictionary for quick lookup of citation counts by title
citation_dict = {}
for record in citations_data:
    title = record['title']
    total_citations = int(record['total_citations'])
    citation_dict[title] = total_citations

# Find citations for food domain papers
food_citations = []
total_citation_count = 0

for title in food_titles:
    if title in citation_dict:
        citations = citation_dict[title]
        food_citations.append({
            'title': title,
            'citations': citations
        })
        total_citation_count += citations
        
print(f"Found {len(food_citations)} food papers with citation data")
print(f"Total citation count: {total_citation_count}")

result = {
    'total_food_papers': len(food_titles),
    'food_papers_with_citations': len(food_citations),
    'total_citation_count': total_citation_count,
    'food_citation_details': food_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'food_papers_count': 5, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
