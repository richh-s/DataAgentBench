code = """import json

# Read the paper documents
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citations
with open('file_storage/functions.query_db:8.json', 'r') as f:
    citations = json.load(f)

# Identify papers in food domain
food_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Count food-related words
    food_count = text_lower.count('food')
    diet_count = text_lower.count('diet')
    nutrition_count = text_lower.count('nutrition')
    eating_count = text_lower.count('eating')
    
    total = food_count + diet_count + nutrition_count + eating_count
    
    # If found at least 5 food-related terms, classify as food paper
    if total >= 5:
        food_papers.append(title)

# Create set for lookup
food_set = set(food_papers)

# Calculate total citations for food papers
total_citations = 0
citation_count = 0

for citation in citations:
    title = citation.get('title', '')
    if title in food_set:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        citation_count += 1

result = {
    'food_papers_count': len(food_papers),
    'citation_records_count': citation_count,
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'total_citation_records': 26, 'total_citation_count': 1328, 'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_citations': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16, 'year': '2020'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 49, 'year': '2021'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 11, 'year': '2022'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 71, 'year': '2023'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 38, 'year': '2024'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 81, 'year': '2025'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 77, 'year': '2016'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 9, 'year': '2017'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50, 'year': '2018'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 49, 'year': '2019'}]}, 'var_functions.execute_python:20': {'total_food_papers': 2, 'food_papers_with_scores': {'A Lived Informatics Model of Personal Informatics': 27, 'A Stage-based Model of Personal Informatics Systems': 27}, 'total_citation_records': 11, 'total_citation_count': 610}}

exec(code, env_args)
