code = """import json
import re

# Get the file paths
paper_docs_path = locals()['var_functions.query_db:22']
citation_titles_path = locals()['var_functions.query_db:5']

# Load all paper documents
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load all citation titles
with open(citation_titles_path, 'r') as f:
    citation_titles = json.load(f)

citation_title_set = set([item['title'] for item in citation_titles])

# Food-related keywords to search for
food_keywords = [
    'food', 'diet', 'nutrition', 'dietary', 'eating', 'meal', 'meals',
    'food tracking', 'food journaling', 'diet tracking', 'nutrition tracking',
    'food journal', 'dietary tracking', 'eating behavior', 'eating habits'
]

# Find all papers in the food domain
food_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract year
    year_match = re.search(r"(19|20)\d{2}", text)
    year = year_match.group() if year_match else None
    
    # Extract venue
    venue_patterns = [r"CHI", r"Ubicomp", r"UbiComp", r"CSCW", r"DIS", r"PervasiveHealth", r"WWW", r"IUI", r"OzCHI", r"TEI", r"AH", r"UBICOMP"]
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern.upper()
            break
    
    # Extract source
    source_patterns = [r"ACM", r"IEEE", r"PubMed"]
    source = None
    for pattern in source_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            source = pattern
            break
    
    # Check if paper is in food domain
    text_lower = text.lower()
    title_lower = title.lower()
    
    has_food_domain = False
    for keyword in food_keywords:
        if re.search(r'\b' + keyword + r'\b', text_lower, re.IGNORECASE):
            has_food_domain = True
            break
        elif keyword in title_lower:
            has_food_domain = True
            break
    
    if has_food_domain:
        paper_info = {
            'title': title,
            'year': year,
            'venue': venue,
            'source': source,
            'has_citations': title in citation_title_set,
            'filename': filename
        }
        food_papers.append(paper_info)

print('Total food domain papers found: ' + str(len(food_papers)))
print('Food papers with citation data: ' + str(len([p for p in food_papers if p['has_citations']])))

# Show sample food papers
print('\nSample food papers:')
for p in food_papers[:10]:
    citations_str = 'Yes' if p['has_citations'] else 'No'
    print('- ' + p['title'] + ' (Citations: ' + citations_str + ')')

# Return the titles of food papers with citations
food_paper_titles = [p['title'] for p in food_papers if p['has_citations']]

print('__RESULT__:')
print(json.dumps(food_paper_titles))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'var_functions.query_db:20': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': '220'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
