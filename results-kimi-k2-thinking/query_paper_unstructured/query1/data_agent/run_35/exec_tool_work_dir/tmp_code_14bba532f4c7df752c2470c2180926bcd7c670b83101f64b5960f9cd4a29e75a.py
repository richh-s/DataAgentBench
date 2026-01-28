code = """import json
import re

# Load paper documents data
paper_docs_path = locals()['var_functions.query_db:5']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract information from each paper
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Title is filename without .txt
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    year_patterns = [
        r'UBICOMP\s*\'?(\d{2})',
        r'CHI\s*\'?(\d{2})',
        r'CSCW\s*\'?(\d{2})',
        r'DIS\s*\'?(\d{2})',
        r'(\d{4})',
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
            else:
                year = int(year_str)
            break
    
    # Check if paper is about food
    text_lower = text.lower()
    is_food = False
    food_keywords = ['food', 'eating', 'diet', 'nutrition', 'meal', 'calorie', 'dietary', 'meal planning']
    for keyword in food_keywords:
        if keyword in text_lower:
            is_food = True
            break
    
    papers_info.append({
        'title': title,
        'year': year,
        'is_food': is_food
    })

# Filter food papers
food_papers = [p for p in papers_info if p['is_food']]

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for quick lookup
citations_dict = {}
for citation in citations_data:
    citations_dict.setdefault(citation['title'], []).append(citation)

# Calculate total citations for food papers
total_citations = 0
food_papers_with_citations = []

for paper in food_papers:
    title = paper['title']
    if title in citations_dict:
        paper_citations = citations_dict[title]
        total_for_paper = sum(int(c['citation_count']) for c in paper_citations)
        total_citations += total_for_paper
        food_papers_with_citations.append({
            'title': title,
            'year': paper['year'],
            'total_citations': total_for_paper
        })

print('__RESULT__:')
print(json.dumps({
    'food_papers': food_papers_with_citations,
    'total_citations': total_citations
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_papers': 5}, 'var_functions.execute_python:12': {'citations_count': 1405, 'papers_count': 5}}

exec(code, env_args)
