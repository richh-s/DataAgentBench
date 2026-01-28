code = """import json
import re

# Read the paper documents
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

print("Total papers in collection: %d" % len(paper_docs))

# Identify food domain papers
food_papers = []
all_scores = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Score based on food-related terms
    score = 0
    
    # Check for explicit food domain terms
    food_terms = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'cuisine']
    for term in food_terms:
        score += len(re.findall(r'\b' + term + r'\b', lower_text))
    
    # If score >= 3, consider it a food paper
    if score >= 3:
        food_papers.append(title)
    
    all_scores.append({'title': title, 'score': score})

# Sort by score descending
all_scores.sort(key=lambda x: x['score'], reverse=True)

print("Top 10 papers by food-related terms:")
for i, item in enumerate(all_scores[:10]):
    print("  %d. %s: score %d" % (i+1, item['title'][:60], item['score']))

print("\nFood papers identified:")
for i, title in enumerate(sorted(food_papers)):
    print("  %d. %s" % (i+1, title))

print("\nTotal food papers: %d" % len(food_papers))

# Create result
result = {
    'total_food_papers': len(food_papers),
    'food_papers': sorted(food_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'total_citation_records': 26, 'total_citation_count': 1328, 'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_citations': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16, 'year': '2020'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 49, 'year': '2021'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 11, 'year': '2022'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 71, 'year': '2023'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 38, 'year': '2024'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 81, 'year': '2025'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 77, 'year': '2016'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 9, 'year': '2017'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50, 'year': '2018'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 49, 'year': '2019'}]}, 'var_functions.execute_python:20': {'total_food_papers': 2, 'food_papers_with_scores': {'A Lived Informatics Model of Personal Informatics': 27, 'A Stage-based Model of Personal Informatics Systems': 27}, 'total_citation_records': 11, 'total_citation_count': 610}}

exec(code, env_args)
