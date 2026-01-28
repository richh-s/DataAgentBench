code = """import json
import re

# Read the paper documents from the file
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

# Count total papers
print(f"Total papers in collection: {len(paper_docs)}")

# Check for food domain papers with more flexible criteria
food_papers = []
paper_checks = []

for i, doc in enumerate(paper_docs):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check multiple criteria
    has_food_word = 'food' in lower_text
    has_diet_word = 'diet' in lower_text
    has_nutrition_word = 'nutrition' in lower_text
    has_eating_word = 'eating' in lower_text
    
    # Count occurrences
    food_count = len(re.findall(r'\bfood\b', lower_text))
    diet_count = len(re.findall(r'\bdiet\b', lower_text))
    nutrition_count = len(re.findall(r'\bnutrition\b', lower_text))
    eating_count = len(re.findall(r'\beating\b', lower_text))
    
    total_food_refs = food_count + diet_count + nutrition_count + eating_count
    
    # If paper mentions food-related terms frequently, include it
    if total_food_refs >= 3:
        food_papers.append(title)
    
    paper_checks.append({
        'title': title,
        'food_mentions': total_food_refs,
        'has_food': has_food_word or has_diet_word or has_nutrition_word or has_eating_word
    })

# Sort by food mentions to see top papers
paper_checks.sort(key=lambda x: x['food_mentions'], reverse=True)

print(f"Top papers by food mentions:")
for i, check in enumerate(paper_checks[:10]):
    print(f"  {i+1}. {check['title']}: {check['food_mentions']} food mentions")

print(f"\nTotal food papers identified: {len(food_papers)}")
print(f"Food papers: {sorted(food_papers)}")

# Calculate statistics
food_mention_counts = [p['food_mentions'] for p in paper_checks]
papers_with_any_food = sum(1 for p in paper_checks if p['has_food'])

print(f"\nStatistics:")
print(f"  Papers with any food mention: {papers_with_any_food}")
print(f"  Average food mentions per paper: {sum(food_mention_counts)/len(food_mention_counts):.1f}")
print(f"  Max food mentions in a paper: {max(food_mention_counts)}")

result = {
    'total_food_papers': len(food_papers),
    'food_papers': sorted(food_papers),
    'papers_with_any_food': papers_with_any_food
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'total_citation_records': 26, 'total_citation_count': 1328, 'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_citations': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16, 'year': '2020'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 49, 'year': '2021'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 11, 'year': '2022'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 71, 'year': '2023'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 38, 'year': '2024'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 81, 'year': '2025'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 77, 'year': '2016'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 9, 'year': '2017'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50, 'year': '2018'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 49, 'year': '2019'}]}, 'var_functions.execute_python:20': {'total_food_papers': 2, 'food_papers_with_scores': {'A Lived Informatics Model of Personal Informatics': 27, 'A Stage-based Model of Personal Informatics Systems': 27}, 'total_citation_records': 11, 'total_citation_count': 610}}

exec(code, env_args)
