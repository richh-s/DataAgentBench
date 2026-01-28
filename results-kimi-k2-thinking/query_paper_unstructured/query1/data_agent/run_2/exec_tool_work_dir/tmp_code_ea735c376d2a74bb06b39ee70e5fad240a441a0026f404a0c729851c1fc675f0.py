code = """import json
import os
import re

# Load all data
papers_path = locals().get('var_functions.query_db:2', '')
citations_path = locals().get('var_functions.query_db:9', '')

with open(papers_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(papers)}")
print(f"Total citation records: {len(citations)}")

# Analyze each paper more carefully
food_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # More sophisticated domain detection
    # Look for domain indicators in the text
    domain_indicators = []
    
    # Check if paper is specifically about food (not just mentioning it)
    # Look for food-related terms in key sections or with high frequency
    text_lower = text.lower()
    
    # Count food-related terms
    food_terms = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    food_count = sum(text_lower.count(term) for term in food_terms)
    
    # Check for food focus in title
    title_lower = title.lower()
    title_has_food = any(term in title_lower for term in food_terms)
    
    # Also check for other domains for context
    other_domains = []
    if 'physical activity' in text_lower or 'exercise' in text_lower:
        other_domains.append('physical activity')
    if 'sleep' in text_lower:
        other_domains.append('sleep')
    if 'mental' in text_lower:
        other_domains.append('mental')
    if 'finance' in text_lower or 'financial' in text_lower:
        other_domains.append('finances')
    
    # Classify as food domain if:
    # - Food terms appear frequently (more than just passing mentions)
    # OR - Title indicates food focus
    # OR - Food is the only/primary domain mentioned
    is_food_domain = False
    if title_has_food:
        is_food_domain = True
    elif food_count > 10:  # More than just casual mentions
        is_food_domain = True
    elif food_count > 0 and len(other_domains) == 0:
        is_food_domain = True  # Only domain mentioned
    
    if is_food_domain:
        food_papers.append({
            'title': title,
            'food_count': food_count,
            'other_domains': other_domains,
            'title_has_food': title_has_food
        })
    
    print(f"\nPaper: {title}")
    print(f"  Food term occurrences: {food_count}")
    print(f"  Title mentions food: {title_has_food}")
    print(f"  Other domains: {other_domains}")
    print(f"  Classified as food domain: {is_food_domain}")

print(f"\n{'='*50}")
print(f"Papers classified in food domain: {len(food_papers)}")
for p in food_papers:
    print(f"  - {p['title']}")

# Get citations for these papers
food_titles = [p['title'] for p in food_papers]
print(f"\nFood domain titles: {food_titles}")

# Calculate total citations for food domain papers
food_citations = []
for citation in citations:
    cit_title = citation.get('title', '')
    if cit_title in food_titles:
        food_citations.append({
            'title': cit_title,
            'citation_count': int(citation.get('citation_count', 0)),
            'citation_year': citation.get('citation_year')
        })

print(f"\nFound {len(food_citations)} citation records for food domain papers")
if food_citations:
    total_citations = sum(c['citation_count'] for c in food_citations)
    print(f"Total citations: {total_citations}")
    # Group by paper
    by_paper = {}
    for c in food_citations:
        title = c['title']
        if title not in by_paper:
            by_paper[title] = 0
        by_paper[title] += c['citation_count']
    
    print("\nCitations by paper:")
    for title, count in by_paper.items():
        print(f"  {title}: {count}")
else:
    total_citations = 0

print('__RESULT__:')
print(json.dumps({
    "food_papers_count": len(food_papers),
    "food_paper_titles": food_titles,
    "total_citation_records": len(food_citations),
    "total_citation_count": total_citations
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'papers': 5, 'citations': 1405}, 'var_functions.execute_python:14': {'total_papers': 5, 'food_papers': 5, 'food_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
