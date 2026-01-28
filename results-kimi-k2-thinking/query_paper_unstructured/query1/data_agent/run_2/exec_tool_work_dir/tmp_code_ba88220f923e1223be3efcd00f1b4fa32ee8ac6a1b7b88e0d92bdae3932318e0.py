code = """import json
import os

# Load papers data
papers_path = locals().get('var_functions.query_db:2', '')
citations_path = locals().get('var_functions.query_db:9', '')

with open(papers_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Find food domain papers
food_titles = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '').lower()
    
    # Check for food domain indicators
    food_terms = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    title_lower = title.lower()
    
    # Check if paper is food domain
    is_food = False
    if any(term in title_lower for term in food_terms):
        is_food = True
    else:
        # Count occurrences in text
        food_count = sum(text.count(term) for term in food_terms)
        if food_count > 10:
            is_food = True
        elif food_count > 0:
            # Check if other domains are mentioned
            other_domains = 0
            if 'physical activity' in text or 'exercise' in text:
                other_domains += 1
            if 'sleep' in text:
                other_domains += 1
            if 'finance' in text or 'financial' in text:
                other_domains += 1
            if food_count > other_domains * 2:  # Primary focus on food
                is_food = True
    
    if is_food:
        food_titles.append(title)

# Calculate citations for food domain papers
total_citations = 0
citation_counts_by_paper = {}

for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_titles:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        citation_counts_by_paper[cit_title] = citation_counts_by_paper.get(cit_title, 0) + count

result = {
    'food_papers_found': len(food_titles),
    'food_paper_titles': food_titles,
    'total_citation_count': total_citations,
    'citations_by_paper': citation_counts_by_paper
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'papers': 5, 'citations': 1405}, 'var_functions.execute_python:14': {'total_papers': 5, 'food_papers': 5, 'food_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
