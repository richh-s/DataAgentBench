code = """import json
import re

# Get the file paths from storage variables
paper_docs_file = locals()['var_functions.query_db:5']
citations_file = locals()['var_functions.query_db:10']

# Load paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract title and check for food domain from each document
food_papers = []

# Define food-related keywords (broader than just "food")
food_keywords = [
    'food', 'nutrition', 'diet', 'dietary', 'eating', 'meal', 'meals', 'calorie', 
    'calories', 'nutrient', 'nutrients', 'beverage', 'beverages', 'snack', 
    'snacks', 'dining', 'recipe', 'recipes', 'cooking', 'restaurant', 'restaurants',
    'weight', 'weight loss', 'obesity', 'hunger', 'satiety', 'dieting'
]

# Process each paper
food_titles = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Search for food-related keywords in text (case-insensitive)
    text_lower = text.lower()
    is_food_paper = False
    
    for keyword in food_keywords:
        # Look for keyword as a whole word
        if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', text_lower):
            is_food_paper = True
            break
    
    if is_food_paper:
        food_papers.append({
            'title': title,
            'is_food': True
        })
        food_titles.append(title)

# Load citations data
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Convert citation_count to int for each citation
for citation in citations:
    citation['citation_count'] = int(citation['citation_count'])

# Filter citations for food papers
citations_by_title = {}
for citation in citations:
    title = citation['title']
    if title not in citations_by_title:
        citations_by_title[title] = []
    citations_by_title[title].append(citation)

# Calculate total citation count for food papers
food_citations_total = 0
food_citations_list = []

for title in food_titles:
    if title in citations_by_title:
        for citation in citations_by_title[title]:
            food_citations_total += citation['citation_count']
            food_citations_list.append({
                'title': title,
                'citation_year': citation['citation_year'],
                'citation_count': citation['citation_count']
            })

result = {
    'total_papers': len(paper_docs),
    'food_papers_count': len(food_papers),
    'food_papers': food_titles,
    'food_citations_total': food_citations_total,
    'total_citation_records_for_food': len(food_citations_list),
    'food_citations': food_citations_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'paper_info_count': 5, 'citations_count': 1405, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': []}]}, 'var_functions.execute_python:16': {'total_papers': 5, 'food_papers_count': 0, 'food_papers': [], 'total_citations': 1405}}

exec(code, env_args)
