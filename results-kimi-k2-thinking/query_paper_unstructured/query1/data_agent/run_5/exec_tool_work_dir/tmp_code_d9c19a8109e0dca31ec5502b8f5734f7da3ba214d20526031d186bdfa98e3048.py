code = """import json
import re

# Read the paper documents from the file
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citations from the file  
with open('file_storage/functions.query_db:8.json', 'r') as f:
    citations = json.load(f)

# More sophisticated food domain detection
food_papers = []
paper_domain_scores = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Score-based approach to identify food papers
    score = 0
    
    # Check if this is explicitly a food paper
    food_indicators = [
        'food tracking', 'food journal', 'diet tracking', 'nutrition tracking',
        'calorie counting', 'meal logging', 'eating habits'
    ]
    
    for indicator in food_indicators:
        if indicator in lower_text:
            score += 5  # High weight for explicit food tracking terms
    
    # Count raw mentions of food (but penalize if only in references)
    food_mentions = len(re.findall(r'\bfood\b', lower_text))
    
    # Check if food appears in context (not just citations)
    # Look for food in sentences
    sentences = re.split(r'[.!?]+', text.lower())
    contextual_food = sum(1 for s in sentences if 'food' in s and 'citation' not in s and '[' not in s)
    
    score += food_mentions
    score += contextual_food * 2
    
    # If score is high enough, classify as food paper
    if score >= 5:
        food_papers.append(title)
        paper_domain_scores[title] = score

# Also check paper titles for obvious food-related terms
food_title_keywords = ['food', 'diet', 'nutrition', 'calorie', 'meal', 'eating']
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    lower_title = title.lower()
    
    if any(keyword in lower_title for keyword in food_title_keywords):
        if title not in food_papers:
            food_papers.append(title)
            paper_domain_scores[title] = 10  # High score for title match

# Create a set for faster lookup
food_papers_set = set(food_papers)

# Sum citations for food domain papers
total_citations = 0
matched_citations = []

for citation in citations:
    citation_title = citation.get('title', '')
    if citation_title in food_papers_set:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        matched_citations.append({
            'title': citation_title,
            'count': count,
            'year': citation.get('citation_year')
        })

result = {
    'total_food_papers': len(food_papers),
    'food_papers_with_scores': {title: paper_domain_scores.get(title, 0) for title in sorted(food_papers)},
    'total_citation_records': len(matched_citations),
    'total_citation_count': total_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'total_citation_records': 26, 'total_citation_count': 1328, 'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_citations': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16, 'year': '2020'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 49, 'year': '2021'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 11, 'year': '2022'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 71, 'year': '2023'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 38, 'year': '2024'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 81, 'year': '2025'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 77, 'year': '2016'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 9, 'year': '2017'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50, 'year': '2018'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'count': 49, 'year': '2019'}]}}

exec(code, env_args)
