code = """import json
import re

# Get the file paths from stored results
paper_docs_path = locals()['var_functions.query_db:22']
citation_titles_path = locals()['var_functions.query_db:5']

# Read the paper documents
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read the citation titles
with open(citation_titles_path, 'r') as f:
    citation_titles = json.load(f)

# Extract titles from citation records
citation_title_set = set([item['title'] for item in citation_titles])

print('Total paper documents: ' + str(len(paper_docs)))
print('Total unique citation titles: ' + str(len(citation_title_set)))

# Search for food-related papers more effectively
food_paper_titles = []
food_count = 0

for doc in paper_docs:
    filename = doc['filename']
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check if this paper has citations
    has_citations = title in citation_title_set
    
    # Look for food-related terms in the text
    # Use more comprehensive pattern matching
    food_terms = [
        r'\bfood\b', r'\bfoods\b', r'\bdiet\b', r'\bdietary\b', 
        r'\bnutrition\b', r'\bnutritional\b', r'\beating\b',
        r'\bmeal\b', r'\bmeals\b', r'\bcooking\b',
        r'\bfood journal\b', r'\bfood logging\b', r'\bfood tracking\b',
        r'\bdiet tracking\b', r'\bnutrition tracking\b'
    ]
    
    # Check if any food-related terms appear in the text
    has_food_domain = False
    for term in food_terms:
        if re.search(term, text, re.IGNORECASE):
            has_food_domain = True
            break
    
    # Also check the title specifically for food terms
    if not has_food_domain:
        title_lower = title.lower()
        if any(term in title_lower for term in ['food', 'diet', 'nutrition', 'eating']):
            has_food_domain = True
    
    if has_food_domain:
        food_count += 1
        if has_citations:
            food_paper_titles.append(title)
            print('Found food paper with citations: ' + title)

print('Total food-related papers: ' + str(food_count))
print('Food papers with citations: ' + str(len(food_paper_titles)))

# Print the result
print("__RESULT__:")
print(json.dumps(food_paper_titles))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_functions.query_db:20': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
