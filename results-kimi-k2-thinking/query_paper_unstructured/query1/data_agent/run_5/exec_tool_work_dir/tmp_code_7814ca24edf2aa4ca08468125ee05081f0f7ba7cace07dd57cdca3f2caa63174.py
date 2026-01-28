code = """import json
import re

# Read the paper documents from the file
with open('file_storage/functions.query_db:14.json', 'r') as f:
    paper_docs = json.load(f)

# Read the citations from the file  
with open('file_storage/functions.query_db:8.json', 'r') as f:
    citations = json.load(f)

# Extract paper titles and identify food domain papers
food_papers = []
all_paper_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '').lower()
    
    # Check if paper is in food domain by searching for domain mentions
    # Look for explicit domain indicators
    has_food_domain = 'food' in text
    
    # Also check for food-related keywords in context
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']
    food_keyword_count = sum(1 for keyword in food_keywords if keyword in text)
    
    if has_food_domain or food_keyword_count >= 3:  # At least 3 food mentions suggests food domain
        food_papers.append(title)
    
    all_paper_info.append({
        'title': title,
        'has_food': has_food_domain,
        'food_keywords': food_keyword_count
    })

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
    'total_citation_records': len(matched_citations),
    'total_citation_count': total_citations,
    'food_papers': sorted(food_papers)[:20],  # Show first 20
    'sample_citations': matched_citations[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'paper_docs_file': 'file_storage/functions.query_db:6.json', 'citations_file': 'file_storage/functions.query_db:8.json'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
